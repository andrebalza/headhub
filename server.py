import re
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


def validate_email(raw_email):
    email = raw_email.strip()
    regex = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
    if regex.match(email):
        return email
    return None

def send_email(user, pwd, recipient, subject, body):
    import smtplib

    gmail_user = user
    gmail_pwd = pwd
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print 'successfully sent the mail'
    except:
        print "failed to send mail"
    return 'ok'



@app.route('/register-email/', methods=['POST'])
def register_email():
    email = validate_email(request.form['email'])
    if email:
        with open('data/emails.txt', 'a') as f:
            f.write(email + '\n')
	send_email("hiyafinland@gmail.com", 
			"HeadHubCentral", 
			email, 
			"no-reply", 
			"Welcome to Hiya " + '\n'
			"Wait for the launch of this big community " +
			"of hairdressers and haircuts")
    return 'ok'

if __name__ == '__main__':
    app.run(debug=True)
