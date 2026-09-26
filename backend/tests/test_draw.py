from fastapi.testclient import TestClient

from app.main import app


def test_health():
    with TestClient(app) as client:
        res = client.get("/health")
        assert res.status_code == 200
        assert res.json()["ok"] is True


def test_draw_flow():
    with TestClient(app) as client:
        sms = client.post("/api/v1/auth/sms", json={"mobile": "13900001111"})
        assert sms.status_code == 200
        code = sms.json()["demo_code"]

        login = client.post("/api/v1/auth/login", json={"mobile": "13900001111", "code": code})
        assert login.status_code == 200
        token = login.json()["access_token"]
        headers = {"Authorization": f"Bearer {token}"}

        boxes = client.get("/api/v1/boxes", headers=headers)
        assert boxes.status_code == 200
        box = boxes.json()[0]
        target = next(p for p in box["prizes"] if p["is_jackpot"])

        draw = client.post(
            f"/api/v1/boxes/{box['id']}/draw",
            headers=headers,
            json={"target_prize_id": target["id"]},
        )
        assert draw.status_code == 200
        body = draw.json()
        assert "prize" in body
        assert body["cost"] == box["price"]

        me = client.get("/api/v1/users/me", headers=headers)
        assert me.status_code == 200
        assert me.json()["balance"] == body["balance"]
