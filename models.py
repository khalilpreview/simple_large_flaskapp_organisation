# importing from app.py
from app import db




# example class for products tabel.......
class CountriesBase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(50), unique=True)
    product_qt = db.Column(db.String(50))
    product_price = db.Column(db.Integer)