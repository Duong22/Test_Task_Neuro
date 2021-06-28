from flask import Blueprint, request, current_app
from decimal import Decimal
from datetime import datetime
import json

from src.yandex_geocoder import YandexGeocoder

API_KEY = "8507fcb7-4e42-4537-80ed-3b77efa71f95"

yandex_geocoder = YandexGeocoder(API_KEY)

geocoder = Blueprint('geocoder', __name__)

@geocoder.route("/finddistance", methods=['POST'])
def find_distance():
    try:
        address = request.get_json()['address']
    except:
        return "Bad request", 400

    try:
        distance = yandex_geocoder.calculate_distance(address=address)
        # print(distance)
        distance = str(distance) + "(miles)"
        current_app.logger.info('[{}] address "{}" get distance {}'.format(datetime.now(), address, distance))
        return json.dumps({"distance": distance})
    except Exception as e:
        return str(e), 500