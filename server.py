from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register-email/', methods=['POST'])
def register_email():
    email = request.form['email']
    with open('data/emails.txt', 'a') as f:
        f.write(email + '\n')
    return 'ok'

if __name__ == '__main__':
    app.run(debug=True)
