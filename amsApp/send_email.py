import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

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
        print(e)
       # print(e.body)
