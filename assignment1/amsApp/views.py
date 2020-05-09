from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import User, Role, Activity, Child
from django.db import IntegrityError
from datetime import datetime,timedelta
from datetime import time
from amsApp import forms




# Create your views here.
def home(request):
   return render(request,'home.html',{'includeNav':True})


   

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

def logout_view(request):
    if (request.user.is_authenticated):
        logout(request)
    return redirect('login')

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

    return render(request, 'register.html', {'includeNav': False})
    
def my_profile(request):
    try:
        userrole = request.user.roles.first().id
    except:
        userrole = '3'
    cf = forms.ChildForm()
    if request.method == 'POST':
        cf = forms.ChildForm(request.POST)
        if cf.is_valid():
            child = cf.save()
            request.user.myChildren.add(child)
            messages.add_message(request, messages.SUCCESS, "Child Added Successfully")
        else:
            messages.add_message(request, messages.INFO, "Child Add Failed")
    myChildren = request.user.myChildren.all()
    context= {'userrole':userrole,'includeNav': True, 'myChildren': myChildren,'form':cf}
    return render(request, 'my-profile.html', context)

def child_profile(request,newContext={}):
    context ={'includeNav':True}
    if request.method == 'POST':
        child = request.user.myChildren.all().filter(id=request.POST.get('childId')).first()
        context = {'includeNav':True,'child':child }
    
    return render(request,'child-profile.html',context)

def updateChild(request):
    if (not request.user.is_authenticated):
        return redirect('home')
    
    if request.method == 'POST':
        childId = request.POST.get('childId')
        child = request.user.myChildren.filter(id=childId).first()
        cf = forms.ChildForm(request.POST, instance=child)
        if  cf.is_valid():       
            cf.save()
            messages.add_message(request,messages.SUCCESS, f'{child.name}\'s details have been Updated Successfully!')
            return redirect('my-profile')
    else:
        cf = forms.ChildForm()
        messages.add_message(request,messages.INFO, 'Failed to update child details.')
    
    
    context = {'form': cf}

    return render(request, 'my-profile.html', context)
    
def calendar(request):
    # set sratrdate should be from request params but for now chill
    start_date = datetime.today()

    # set variable to start at start_date
    day = start_date 
    
    # row wise data
    rwd = []

    five_week_days = []
    five_week_days_strings =[]

       # populating the 5 days
    for number in range(0,5):
        five_week_days.append(day)
        day_str = day.strftime('%d-%m-%Y')
        five_week_days_strings.append(day_str)
        day += timedelta(days=1)
    
    for hour in range(8,22):
        
        time_str = f'{hour}:00 - {hour+1}:00'
        if hour <10:
            hour =f'0{hour}'
        else:
            hour = f'{hour}'
        start_time_being_checked = time.fromisoformat(hour+':00:00')
        row = {'time':time_str}
        count = 1
        for aday in five_week_days:
            allActivitiesOnThisDay = Activity.objects.filter(date=aday)
            for activity in allActivitiesOnThisDay:
                if activity.start_time.hour == start_time_being_checked.hour:
                    row[f'a{count}']=activity
            count +=1
        rwd.append(row)
    dates_for_nav={'start_date':start_date}
    end_date = start_date+timedelta(days=4)
    dates_for_nav['end_date'] = end_date

    context = {'row_wise_data':rwd,'next_five_week_days':five_week_days_strings,'includeNav':True,'dates':dates_for_nav}
    return render(request, 'calendar.html', context)
    

