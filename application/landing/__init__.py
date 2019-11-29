from flask import current_app, Blueprint 

landing_bp = Blueprint('landing_bp', __name__, 
	template_folder='templates')

from application.landing import routes