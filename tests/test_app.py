import json
from app.main import create_app

def test_health():
    app = create_app()
    client = app.test_client()
    resp = client.get("/health")
    assert resp.status_code == 200
    data = json.loads(resp.data.decode("utf-8"))
    assert data["status"] == "ok"

def test_list_orders():
    app = create_app()
    client = app.test_client()
    resp = client.get("/orders")
    assert resp.status_code == 200
    data = json.loads(resp.data.decode("utf-8"))
    assert isinstance(data, list)
    assert len(data) >= 1