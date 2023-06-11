import string
import csv

from random import choices

from flask import Flask, request
from webargs.flaskparser import use_kwargs
from webargs import fields, validate


app = Flask(__name__)

@app.route('/generate_password')
@use_kwargs(
    {
        "password_length": fields.Int(
            missing=10,
            validate=[validate.Range(min=10, max=20)]
        )
    },
    location="query"
)
def generate_password(password_length):  # put application's code here

    return ''.join(choices(string.ascii_lowercase + string.ascii_uppercase + string.punctuation + string.digits,
                           k=password_length))


@app.route('/calculate_average')
def calculate_average():
    filename = 'hw.csv'
    with open(filename) as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # пропустить заголовок
        col_1_sum = 0
        col_2_sum = 0
        count = 0
        for row in reader:
            if len(row) >= 3:
                col_1_sum += float(row[1])
                col_2_sum += float(row[2])
                count += 1
        if count > 0:
            average_height = (col_1_sum / count) * 2.54
            average_weight = (col_2_sum / count) * 0.453
        else:
            average_height = 0
            average_weight = 0
    return f'Average height in cm = {average_height:3.2f}, average weight in kg = {average_weight:2.2f}'


if __name__ == '__main__':
    app.run(debug=True)
