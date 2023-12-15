#!/usr/bin/python3
""" Index view
"""
from flask import jsonify

from api.v1.views import app_views

# Creating a Blueprint instance to export the route
app_views = Blueprint('app_views', __name__)

# Status Route
@app_views.route('/api/v1/status', methods=['GET'], strict_slashes=False)
def status():
    """ Status of the web server
    """
    return jsonify({"status": "OK"})
