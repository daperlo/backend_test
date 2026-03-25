def test_booking_slot(client):
    room = client.post("/rooms", json={
        "name": "Room D",
        "capacity": 5
    }).json()

    room_id = room["id"]

    client.post(f"/rooms/{room_id}/generate-slots", params={
        "interval_minutes": 30
    })

    slots = client.get(f"/rooms/{room_id}/slots").json()["slots"]

    assert len(slots) > 0   # фикс: не падаем на пустом

    slot_id = slots[0]["slot_id"]

    response = client.post("/booking", json={
        "slot_id": slot_id,
        "user_id": "test-user",
        "people_count": 2
    })

    assert response.status_code == 200

    data = response.json()

    assert "id" in data
    assert data["slot_id"] == slot_id
    assert data["user_id"] == "test-user"
    assert data["people_count"] == 2