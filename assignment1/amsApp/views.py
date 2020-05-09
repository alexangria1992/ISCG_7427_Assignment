from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import User,Role,Activity,Child



# Create your views here.
def home(request):
    try:
        userrole = request.user.roles.first().id
    except:
        userrole = '3'
    af = forms.ActivityForm()
    allActivities = Activity.objects.all()
    if request.method == 'POST':
        if request.POST.get('form-type') == 'remove-activity' and request.POST.get('form-type') is not None:
            activityId = request.POST.get('activityId')
            activity = Activity.objects.filter(id=activityId).delete()
            if activity is not None:
                messages.add_message(request, messages.SUCCESS, "Activity Delete Successful")
            else:
                messages.add_message(request, messages.INFO, "Activity Delete Unsuccessful")
            return redirect('home')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # A backend authenticated the credentials
            return redirect('home')
        else:
            messages.add_message(request, messages.INFO, "please check your username and/or password")
    


    return render(request, 'login.html', {'includeNav': False})
    
def register_view(request):
    if(request.user.is_authenticated):
        return redirect('home')
    try:
        if (request.method == 'POST'):
            username = request.POST.get("username")
            password = request.POST.get("password")
            email = request.POST.get("email")
            userType = request.POST.get("userType")
            user = User.objects.create_user(username, email, password)
            if user is not None:
               #messages.add_message(request, level, message, extra_tags='', fail_silently=False)
                user.roles.add(Role.objects.get(id=userType))
                messages.add_message(request, messages.INFO, "your account was created successfully please log in now")
                # A backend authenticated the credentials
                return redirect( 'login')
    except IntegrityError:
        messages.add_message(request, messages.INFO, "That Username is taken please try another username")

    return render(request,'register.html',{'includeNav':False})