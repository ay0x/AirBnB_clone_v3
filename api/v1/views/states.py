#!/usr/bin/python3
"""This module creates a route that returns the
State object of our API.
"""
from api.v1.views import app_views
from flask import jsonify, abort
from models import storage


@app_views.route("/states", methods=["GET"], strict_slashes=False)
def get_state():
    states_list = []
    """Returns the status of our API"""
    for state in storage.all("State").values():
        states_list.append(state.to_dict())
    return jsonify(states_list)

@app_views.route("/states/<string:state_id>", methods=["GET"], strict_slashes=False)
def get_state_id(state_id):
    """Get a state by its ID"""
    state = storage.get("State", state_id)
    if state is None:
        abort(404)
    return jsonify(state.to_dict())

@app_views.route("/states/<string:state_id>", methods=["DELETE"], strict_slashes=False)
def delete_state_id(state_id):
    """Delete a state by its ID"""
    state = storage.get("State", state_id)
    if state is None:
        abort(404)
    else:
        state.delete()
        return jsonify({})
    