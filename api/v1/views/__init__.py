#!/usr/bin/python3
"""This module creates an instance of a
Blueprint.
"""
from flask import Blueprint
from api.v1.views.index import *


app_views = Blueprint(url_prefix="/api/v1")
