import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(from_email='Hello@alexangria.com',
to_emails='alex040892@gmail.com',
subject='Sending with Twilio SendGrid is Fun',
plain_text_content='and easy to do anywhere, even with Python.',
html_content='<strong>and easy to do anyehrre, even with Python</strong>')

try:
    sg = SendGridAPIClient('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')
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.body)