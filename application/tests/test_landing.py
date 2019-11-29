def test_index(client):
	assert client.get('/').status == '200 OK'
