import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as c:
        yield c


def test_health(client):
    res = client.get("/health")
    assert res.status_code == 200
    assert res.get_json()["status"] == "healthy"


def test_health_has_timestamp(client):
    res = client.get("/health")
    assert "timestamp" in res.get_json()


def test_index(client):
    res = client.get("/")
    assert res.status_code == 200


def test_admin_dashboard(client):
    res = client.get("/admin")
    assert res.status_code == 200


def test_admin_stats(client):
    res = client.get("/admin/stats")
    assert res.status_code == 200
    data = res.get_json()
    assert "total_visits" in data
    assert "unique_visitors" in data
    assert "page_views" in data
    assert "recent_visits" in data


def test_visitor_tracking(client):
    before = client.get("/admin/stats").get_json()["total_visits"]
    client.get("/")
    after = client.get("/admin/stats").get_json()["total_visits"]
    assert after > before


def test_metrics(client):
    res = client.get("/metrics")
    assert res.status_code == 200
