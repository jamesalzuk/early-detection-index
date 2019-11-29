def test_landing_page_load(client):
	assert client.get('/').status == '200 OK'

