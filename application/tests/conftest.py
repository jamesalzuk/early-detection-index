from pytest import fixture

@fixture(scope='module')
def client():
	flask_app = create_app(
		config_file = os.environ['APP_SETTINGS']
		)
	test_client = flask_app.test_client()

	context = flask_app.app_context()
	context.push()
	yield test_client

	context.pop()

