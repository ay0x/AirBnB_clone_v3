#!/usr/bin/python3

from models import storage
import os
from api.v1.views import app_views
from flask import Flask, Blueprint

app = Flask(__name__)

app.register_blueprint(app_views)

@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()

if __name__ == "__main__":
    host = os.getenv("HBNB_API_HOST", "0.0.0.0")
    port = os.getenv("HBNB_API_PORT", 5001)
    app.run(host=host, port=port, threaded=True)
