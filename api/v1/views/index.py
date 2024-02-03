#!/usr/bin/python3
"""This module creates a route that returns the
status of our API.
"""
from app.v1.views import app_views
from flask import jsonify


@app_views.route("/status", methods=["GET"])
def get_status():
    """Returns the status of our API"""
    return jsonify({"status": "OK"})
