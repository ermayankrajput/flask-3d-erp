from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_migrate import Migrate
from sqlalchemy.sql import func
from app import db

database_models_blueprint = Blueprint('database_models_blueprint', __name__)

class Quote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quote_date = db.Column(db.DateTime(timezone=True),nullable = True)
    validity = db.Column(db.Integer,nullable = True)
    shipping_cost = db.Column(db.Numeric,nullable = True)
    grand_total = db.Column(db.Numeric,nullable = True)
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), default=func.now())
    quote_infos = db.relationship('QuoteInfo', backref = 'Quote', cascade="all, delete")


    def __repr__(self):
        return "<Quote %r>" % self.grand_total
    
    def serialize(self):
        quote_infos = []
        if self.quote_infos:
            quote_infos = [quote_infos.serialize() for quote_infos in self.quote_infos]
        return {"id": self.id,
                "quote_date": self.quote_date,
                "validity": self.validity,
                "shipping_cost":self.shipping_cost,
                "grand_total": self.grand_total,
                "quote_infos": quote_infos
                }

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
    quote_id = db.Column(db.Integer, db.ForeignKey('quote.id', ondelete='CASCADE'))
    unit_quotes = db.relationship('UnitQuote', backref = 'QuoteInfo', cascade="all, delete")

    def __repr__(self):
        return "<QuoteInfo %r>" % self.image_file
    
    def serialize(self):
        unit_quotes = []
        if self.unit_quotes:
            unit_quotes = [unit_quotes.serialize() for unit_quotes in self.unit_quotes]
        return {"id": self.id,
                "image_file": self.image_file,
                "uploded_file" : self.uploded_file,
                "transported_file":self.transported_file,
                "material_search":self.material_search,
                "technique": self.technique,
                "finishing" : self.finishing,
                "x_size" : self.x_size,
                "y_size": self.y_size,
                "z_size":self.z_size,
                "unit_quotes": unit_quotes,
                
            }
    

class UnitQuote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    unit_price = db.Column(db.Numeric,nullable = True)
    quantity = db.Column(db.Integer,nullable = True)
    lead_time = db.Column(db.Integer,nullable = True)
    quote_info_id = db.Column(db.Integer, db.ForeignKey('quote_info.id', ondelete='CASCADE'))

    def __repr__(self):
        return "<UnitQuote %r>" % self.lead_time
    

    def serialize(self):
        return {"id" : self.id,
                "unit_price" : self.unit_price,
                "quantity": self.quantity,
                "lead_time": self.lead_time
            }

# with db.app_context():
#     db.create_all()


    