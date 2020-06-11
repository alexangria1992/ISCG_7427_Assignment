import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
'''from django.core.mail import send_mail as send_mail_with_gmail
from django.conf import settings'''


 
def sendEmailWithSendGrid(customMessage):

    message = Mail(
    from_email='alexangria1992@gmail.com',
    to_emails=customMessage["to_emails"],
    subject=customMessage["subject"],
    plain_text_content=customMessage["plain_text_content"],
    html_content=customMessage["html_content"])



    try:
        sg = SendGridAPIClient ('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')
        response = sg.send(message)
        print('THE RESPONSE CODE IS:' + str(response.status_code))
        print(response.body)
        print(response.headers)
        print('sent')
    except Exception as e:
        print("Exception occured")
        print(e)
        print(e.body)

'''def send_cancellation_email(activity):
    to_emails = []
    html_content = f'<h1> has been cancelled</h1><p>Sorry to inform you that {activity} on {activity.date}, {activity.start_time} has been cancelled due to the rainy weather that has been forecasted</p><h2>From:Activity Management System</h2>'

    for child in activity.child_set.all():
        to_emails.append(child.user_set.first().email)
    customMessage = {}
    customMessage["to_emails"]=  to_emails
    customMessage["subject"] = f'{activity} has been cancelled'
    customMessage["plain_text_content"] = f'Sorry to inform you that {activity} on {activity.date}, {activity.start_time} has been cancelled due tot he rainy weather that has been forecasted'
    customMessage["html_content"] = html_content
    print(f'Sending email to {customMessage["to_emails"]}')

    send_mail_with_gmail(customMessage.get('subject'),
     customMessage.get('plain_text_content'),
     settings.EMAIL_HOST_USER, customMessage.get('to_emails'),
     False, None, None, None, html_content)'''

