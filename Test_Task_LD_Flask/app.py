import logging
from flask import Flask

# blueprint import
from src.geocoder import geocoder

def create_app():
    app = Flask(__name__)   
    app.register_blueprint(geocoder)           # register blueprint
    return app

if __name__ == "__main__":
    app = create_app()
    logging.basicConfig(filename='result.log',level=logging.INFO)
    app.run(debug=True, host='0.0.0.0', port=5002)
