from flask import Blueprint, render_template, abort
from services.reader import read_csv

dashboard_bp = Blueprint('dashboard', __name__, template_folder='src/templates')

@dashboard_bp.route("/")
def index():
    return render_template('base.html')
