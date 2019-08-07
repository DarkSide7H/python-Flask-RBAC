import logging

from flask import Blueprint, render_template

log = logging.getLogger(__name__)

site_blueprint = Blueprint('site', __name__, url_prefix='/', template_folder='templates')


@site_blueprint.route('/')
def index():
    return render_template('layout.html')

