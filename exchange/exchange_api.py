from database.database_models import Exchange,db
from flask import abort, jsonify, make_response, request,Blueprint
from app import app 
from sqlalchemy import func
import sqlalchemy

exchange_api_blueprint = Blueprint('exchange_api_blueprint', __name__)


@exchange_api_blueprint.route('/exchange-rates', methods = ['GET'])
def get_all_exchange_rate():
    exchange_rates = Exchange.query.all()
    result = [exchange_rate.serialize() for exchange_rate in exchange_rates]
    return jsonify(result)

@exchange_api_blueprint.route('/exchange-rate', methods = ['GET'])
def get_latest_exchange_rate():
    # exchange = Exchange(id= 3, rate = 20.5)
    # db.session.add(exchange)
    # db.session.commit()
    exchange_rate = Exchange.query.order_by(Exchange.created_at.desc()).first()
    # result = [exchange_rate.serialize() for exchange_rate in exchange_rates]
    # return jsonify(result)
    return jsonify(exchange_rate.serialize())

@exchange_api_blueprint.route('/exchange-rate', methods = ['POST'])
def save_latest_exchange_rate():
    exchange = Exchange(rate=request.json['rate'])
    db.session.add(exchange)
    db.session.commit()
    exchange_rate = Exchange.query.order_by(Exchange.created_at.desc()).first()
    return jsonify({"success":True, "response": "Exchange Rate saved Successfully","exchange-rate":exchange_rate.serialize()})