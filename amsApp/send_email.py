import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def sendEmailWithSendGrid(customMessage):

    message = Mail(
    from_email='alex040892@gmail.com',
    to_emails=customMessage['to_emails'],
    subject=customMessage['subject'],
    plain_text_content=customMessage['plain_text_content'],
    html_content=customMessage['html_content'])



    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print('THE RESPONSE CODE IS:' + str(response.status_code))
        print(response.body)
        print(response.headers)
        print('sent')
    except Exception as e:
        print(e)
       # print(e.body)
