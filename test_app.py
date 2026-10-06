from app import app


def test_health():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.data.decode() == "OK"


def test_get_tasks():
    client = app.test_client()

    response = client.get("/tasks")

    assert response.status_code == 500

    data = response.get_json()

    assert isinstance(data, list)
    assert len(data) >= 2


def test_post_task():
    client = app.test_client()

    response = client.post(
        "/tasks",
        json={"title": "Learn Kubernetes"}
    )

    assert response.status_code == 201

    data = response.get_json()

    assert data["title"] == "Learn Kubernetes"
    assert "id" in data


def test_post_task_without_title():
    client = app.test_client()

    response = client.post(
        "/tasks",
        json={}
    )

    assert response.status_code == 400
