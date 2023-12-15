from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)


@app.route('/api')
def api():
    return request.args.get('number')


@app.route('/')
def main():
    return render_template('base.html', name='Input Phone Number Below!', title='Phone Number Information')


@app.route('/numberInfo')
def numberInfo():
    print(request)
    return request.values


if __name__ == '__main__':
    app.run()
