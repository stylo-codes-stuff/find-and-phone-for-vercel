from flask import Flask
from flask import request
from flask import render_template

import phoneNumbers

app = Flask(__name__)


@app.route('/api')
def api():
    return request.args.get('number')


@app.route('/')
def main():
    return render_template('base.html', name='Input Phone Number Below!', title='Phone Number Information')


@app.route('/numberInfo', methods=['GET', 'POST'])
def numberInfo():
    return phoneNumbers.getinformation(str(list(request.form.values())[0]))


if __name__ == '__main__':
    app.run()
