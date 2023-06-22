from flask import Flask, request, jsonify
import sqlite3

from markupsafe import Markup

app = Flask(__name__)


@app.route('/order_price')
def order_price():
    try:
        conn = sqlite3.connect('chinook.db')
        cursor = conn.cursor()

        cursor.execute("""
            SELECT SUM(UnitPrice * Quantity) AS Sales
            FROM invoice_items
        """)
        sales = cursor.fetchall()

        country = request.args.get('country')
        if country:
            cursor.execute("""
                SELECT BillingCountry, SUM(UnitPrice * Quantity) AS TotalSales
                FROM invoice_items
                INNER JOIN invoices ON invoice_items.InvoiceId = invoices.InvoiceId
                WHERE BillingCountry = ?
            """, (country,))
            sales_by_country = cursor.fetchall()
        else:
            cursor.execute("""
                SELECT BillingCountry, SUM(UnitPrice * Quantity) AS TotalSales
                FROM invoice_items
                INNER JOIN invoices ON invoice_items.InvoiceId = invoices.InvoiceId
                GROUP BY BillingCountry
            """)
            sales_by_country = cursor.fetchall()

        conn.close()

        return jsonify(sales=sales, sales_by_country=sales_by_country)

    except Exception as e:
        error_message = str(e)
        return jsonify(error=error_message), 500


@app.route('/get_all_info_about_track')
def get_all_info_about_track():
    try:
        conn = sqlite3.connect('chinook.db')
        cursor = conn.cursor()

        track_id = request.args.get('track_id')

        cursor.execute("""
            SELECT *
            FROM tracks
            INNER JOIN albums ON tracks.AlbumId = albums.AlbumId
            INNER JOIN artists ON albums.ArtistId = artists.ArtistId
            INNER JOIN playlist_track ON tracks.TrackId = playlist_track.TrackId
            WHERE tracks.TrackId = ?
        """, (track_id,))

        track_info = cursor.fetchall()

        conn.close()

        html = "<h1>Track Info</h1>"

        for row in track_info:
            html += "<p>"
            html += "<br>".join(str(column) for column in row)
            html += "</p>"

        return Markup(html)


    except Exception as e:
        error_message = str(e)
        return jsonify(error=error_message), 500


if __name__ == '__main__':
    app.run(debug=True)

