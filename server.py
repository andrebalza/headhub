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


@app.route('/register-email/', methods=['POST'])
def register_email():
    email = validate_email(request.form['email'])
    if email:
        with open('data/emails.txt', 'a') as f:
            f.write(email + '\n')
    return 'ok'

if __name__ == '__main__':
    app.run(debug=True)
