from flask import render_template
from application.landing import landing_bp


@landing_bp.route('/', methods=['GET'])
def index():
	"""Index route"""
	return render_template('index.html')


