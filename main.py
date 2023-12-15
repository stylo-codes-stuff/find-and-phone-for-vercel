import flask
from flask import Flask
from flask import request
from flask import render_template

import phoneNumbers  # handler for phonenumbers
import phonenumbers  # lib used in phoneNumbers

app = Flask(__name__)


@app.route('/api')
def api():
    return request.args.get('number')


@app.route('/')
def main():
    return render_template('base.html', name='Input Phone Number Below!', title='Phone Number Information')


# noinspection PyBroadException
@app.route('/numberInfo', methods=['GET', 'POST'])
def numberInfo():
    try:
        return phoneNumbers.getinformation(str(list(request.form.values())[0]))

    except Exception as e:
        return f"Unknown error, or the phone number was incorrectly entered. <br> Error: <code>{e}<code> <br> <a href={flask.url_for('main')}>Link To Go Back</a>"
        # https://stackoverflow.com/questions/27539309/how-do-i-create-a-link-to-another-html-page


if __name__ == '__main__':
    app.run()
