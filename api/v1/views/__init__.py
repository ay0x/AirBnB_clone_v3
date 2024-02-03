#!/usr/bin/python3
"""This module creates an instance of a
Blueprint.
"""
from flask import Blueprint


app_views = Blueprint('app_views', __name__, url_prefix="/api/v1")
