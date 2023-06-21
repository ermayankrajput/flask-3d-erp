from flask import Blueprint, request,jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime,date
from database.database_models import Quote,QuoteInfo,UnitQuote,app, db


quote_api_blueprint = Blueprint('quote_api_blueprint', __name__)



@quote_api_blueprint.route('/quote', methods = ['POST'])
def create():

    file = request.files["u_file"]
    uniqueFileName = str(datetime.now().timestamp()).replace(".","")
    fileNameSplit = file.filename.split(".")
    ext = fileNameSplit[len(fileNameSplit)-1]
    file.save(f"uploads/{uniqueFileName}.{ext}")
    quote = Quote(quote_date = str(datetime.now()), validity = 30, shipping_cost = 500, grand_total = 1500, )
    # pet = Pet( user_file = user_file)
    db.session.add(quote)
    db.session.commit()
    # breakpoint()
    return jsonify({"success": True,"response":"Quote added"})
