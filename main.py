import flask
from fetchScripts.sphinx import sphinxFetch
from flask import Flask
from flask import request
from flask import render_template
import phoneNumbers  # handler for phonenumbers
import phonenumbers  # lib used in phoneNumbers
debug = True
app = Flask(__name__)


@app.route('/api')
def api():
    return request.args.get('number')


@app.route('/')
def main():
    return render_template('base.html', name='Input Phone Number Below!', title='Phone Number Information')


class InvalidPhoneNumber(Exception):
    def __init__(self, message=None):
        self.message = message
        super().__init__(message)


# noinspection PyBroadException
@app.route('/numberInfo', methods=['GET', 'POST'])
def numberInfo():
    try:
        information = phoneNumbers.getinformation(str(list(request.form.values())[0]))
        sphinx_info = sphinxFetch(list(request.form.values())[0])
        for key, value in information.items():
            information[key] = str(value).replace('[', '').replace(']', '').replace("'", '')
        if information['Valid'][0] == 'No':
            raise InvalidPhoneNumber("This is an invalid phone number")
        return render_template('info.html', info=information, sphinx=sphinx_info)

    except BaseException as e:
        return render_template('error.html', error=str(e), prevPage='/')
        # https://stackoverflow.com/questions/27539309/how-do-i-create-a-link-to-another-html-page


if __name__ == '__main__':
    app.run()
