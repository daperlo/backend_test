def test_create_room(client):
    response = client.post("/rooms", json={
        "name": "Room A",
        "capacity": 10
    })

    assert response.status_code == 200
    assert response.json()["name"] == "Room A"