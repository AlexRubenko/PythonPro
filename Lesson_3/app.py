import csv

import requests

from flask import Flask, request
from faker import Faker
from webargs import fields, validate
from webargs.flaskparser import use_args
from forex_python.converter import CurrencyCodes


app = Flask(__name__)

fake = Faker()


count_args = {
    'count': fields.Int(
        validate=validate.Range(min=1, max=1000)
    )
}


@app.route('/generate_students')
@use_args(count_args, location='query')
def generate_students(args):
    count = args["count"]
    students = []
    for _ in range(count):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        password = fake.password()
        birthday = fake.date_of_birth(minimum_age=18, maximum_age=60)
        student = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'password': password,
            'birthday': birthday.strftime('%Y-%m-%d')
        }
        students.append(student)

    with open('students.csv', 'w', newline='') as csvfile:
        fieldnames = ['first_name', 'last_name', 'email', 'password', 'birthday']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students)

    output = '<br>'.join([str(dictionary) for dictionary in students])
    return output  # best way to use render_template but Im not good in HTML :-(


def get_currency_symbol(currency_code):
    currency_codes = CurrencyCodes()
    currency_symbol = currency_codes.get_symbol(currency_code)
    return currency_symbol


@app.route('/get_bitcoin_value')
def get_bitcoin_value():
    currency_code = request.args.get('currency', 'USD')
    convert = int(request.args.get('convert', '100'))

    api_url = f"https://bitpay.com/rates/BTC/{currency_code}"

    response = requests.get(api_url)
    data_json = response.json()  # {"data" : {"code":"USD", "name":"US Dollar", "rate":41154.05}}
    data = data_json['data']  # {"code":"USD", "name":"US Dollar", "rate":41154.05}

    code = data['code']
    rate = data['rate']

    value = float(convert) * rate

    currency_symbol = get_currency_symbol(code)

    return f'The value of Bitcoin in {code} ({currency_symbol}) is {value} {code}({currency_symbol})'


if __name__ == '__main__':
    app.run(debug=True)
