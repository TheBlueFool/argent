def test_root_hello(client):
    response = client.get("/hello")
    json_data = response.get_json()
    assert "Hello, Stranger!" in json_data


def test_welcome_by_name_route(client):
    response = client.get("/hello/jacob")
    json_data = response.get_json()
    assert "jacob" in json_data
