import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def sendEmailWithSendGrid(customMessage):

    message = Mail(
    from_email='Hello@alexangria.com',
    to_emails=customMessage['to_emails'],
    subject=customMessage['subject'],
    plain_text_content=customMessage['plain_text_content'],
    html_content=customMessage['html_content'])



    try:
        sg = SendGridAPIClient('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')
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
        print('sent')
    except Exception as e:
        print(e)
        print(e.body)
