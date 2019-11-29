import os
from flask import Flask

def create_app():
	"""
	Create instance of flask application
	
	Returns
	-------
	app : Flask

	"""
	app = Flask(__name__)
	app.config.from_object(os.environ['APP_SETTINGS'])

	return app

def main():
	app = create_app()
	app.run()

if __name__ == '__main__':
	main()