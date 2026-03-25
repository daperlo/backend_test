def test_generate_slots(client):
    room = client.post("/rooms", json={
        "name": "Room B",
        "capacity": 5
    }).json()

    room_id = room["id"]

    response = client.post(f"/rooms/{room_id}/generate-slots", params={
        "interval_minutes": 30
    })

    assert response.status_code == 200
    assert response.json()["created_slots"] > 0

    
def test_no_duplicate_slots(client):
    room = client.post("/rooms", json={
        "name": "Room C",
        "capacity": 5
    }).json()

    room_id = room["id"]

    client.post(f"/rooms/{room_id}/generate-slots", params={
        "interval_minutes": 30
    })

    response = client.post(f"/rooms/{room_id}/generate-slots", params={
        "interval_minutes": 30
    })

    data = response.json()

    # второй раз почти ничего не должно создать
    assert data["created_slots"] == 0