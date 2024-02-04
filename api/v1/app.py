#!/usr/bin/python3
"""This module provides a method tht handles teardown
and runs app.
"""
from models import storage
import os
from api.v1.views import app_views
from flask import Flask, make_response, jsonify


app = Flask(__name__)
app.register_blueprint(app_views)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


@app.errorhandler(404)
def error_handler(error):
    """Handles 404 error and returns a JSON-formatted 404 status code
    response"""
    return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == "__main__":
    host = os.getenv("HBNB_API_HOST", "0.0.0.0")
    port = os.getenv("HBNB_API_PORT", 5000)
    app.run(host=host, port=port, threaded=True)
