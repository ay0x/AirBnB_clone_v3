#!/usr/bin/python3
"""This module creates a route that returns the
status of our API.
"""
from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {"Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


@app_views.route("/status", methods=["GET"])
def get_status():
    """Returns the status of our API"""
    return jsonify({"status": "OK"})


@app_views.route("/stats", methods=["GET"])
def get_stats():
    """Returns the stat of our API"""
    obj_dict = {}

    for cls in classes:
        obj_dict[cls] = storage.count(classes[cls])

    return jsonify(obj_dict)
