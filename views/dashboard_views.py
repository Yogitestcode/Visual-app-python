from flask import Blueprint, render_template, abort

from services.reader import read_csv

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route("/")
def index():
    return read_csv()
