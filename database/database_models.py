from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_migrate import Migrate
from sqlalchemy.sql import func
from app import app
db = SQLAlchemy(app)
migrate = Migrate(app, db, compare_type=True)

database_models_blueprint = Blueprint('database_models_blueprint', __name__)

class Quote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quote_date = db.Column(db.DateTime(timezone=True),nullable = True)
    validity = db.Column(db.Integer,nullable = True)
    shipping_cost = db.Column(db.Numeric,nullable = True)
    grand_total = db.Column(db.Numeric,nullable = True)
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), default=func.now())
    quote_infos = db.relationship('QuoteInfo', backref = 'Quote')

    def __repr__(self):
        return "<Quote %r>" % self.grand_total

class QuoteInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_file = db.Column(db.Text(), nullable = True)
    uploded_file = db.Column(db.Text(), nullable = True)
    transported_file = db.Column(db.Text(), nullable = True)
    material_search = db. Column(db.String(100), nullable = True)
    technique = db. Column(db.String(100), nullable = True)
    finishing = db. Column(db.String(100), nullable = True)
    x_size = db.Column(db.Numeric,nullable = True)
    y_size = db.Column(db.Numeric,nullable = True)
    z_size = db.Column(db.Numeric,nullable = True)
    quote_id = db.Column(db.Integer, db.ForeignKey('quote.id'))
    unit_quote = db.relationship('UnitQuote', backref = 'QuoteInfo')

    def __repr__(self):
        return "<QuoteInfo %r>" % self.image_file
    

class UnitQuote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    unit_price = db.Column(db.Numeric,nullable = False)
    quantity = db.Column(db.Integer,nullable = True)
    lead_time = db.Column(db.Integer,nullable = True)
    quote_info_id = db.Column(db.Integer, db.ForeignKey('quote_info.id'))

    def __repr__(self):
        return "<UnitQuote %r>" % self.lead_time

with app.app_context():
    db.create_all()