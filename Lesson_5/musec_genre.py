from flask import Flask
import sqlite3

from webargs import fields
from webargs.flaskparser import use_args


app = Flask(__name__)


@app.route('/stats_by_city')
@use_args({"genre": fields.Str(required=True)}, location="query")
def stats_by_city(args):
    genre = args["genre"]

    if genre:
        conn = sqlite3.connect('chinook.db')
        cursor = conn.cursor()

        cursor.execute("SELECT BillingCity, COUNT(*) as Count FROM Invoices "
                       "INNER JOIN invoice_items ON invoices.InvoiceId = invoice_items.InvoiceId "
                       "INNER JOIN tracks ON invoice_items.TrackId = tracks.TrackId "
                       "INNER JOIN genres ON tracks.GenreId = genres.GenreId "
                       "WHERE genres.Name = ? "
                       "GROUP BY BillingCity "
                       "ORDER BY Count DESC "
                       "LIMIT 1", (genre,))

        result = cursor.fetchone()

        if result:
            city = result[0]
            count = result[1]
            return f"The most popular city for the genre '{genre}' is {city} with a count of {count}."
        else:
            return f"No data available for the genre: {genre}"

        conn.close()
    else:
        return "Error: 'genre' parameter is required."


if __name__ == '__main__':
    app.run(debug=True)
