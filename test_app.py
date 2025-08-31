# Uses Flask’s built-in test_client for HTTP requests.
# Each test clears the workout list so results don’t bleed across tests.
# Covers:
# Home page render.
# Adding valid workouts.
# Handling invalid duration.
# JSON API response.

import pytest
from app import app, workouts

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        # clear workouts before each test
        workouts.clear()
        yield client

def test_home_page(client):
    """Home page should load and show 'No workouts logged yet' initially."""
    response = client.get("/")
    assert response.status_code == 200
    assert b"No workouts logged yet" in response.data

def test_add_workout(client):
    """Adding a valid workout should update the list."""
    response = client.post("/add", data={"workout": "Running", "duration": "30"})
    assert response.status_code == 200
    assert b"Running" in response.data
    assert b"30 minutes" in response.data
    assert len(workouts) == 1

def test_add_invalid_duration(client):
    """Non-numeric duration should return error 400."""
    response = client.post("/add", data={"workout": "Yoga", "duration": "thirty"})
    assert response.status_code == 400
    assert b"Duration must be a number" in response.data

def test_api_get_workouts(client):
    """API should return workouts as JSON."""
    client.post("/add", data={"workout": "Cycling", "duration": "45"})
    response = client.get("/api/workouts")
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert data[0]["workout"] == "Cycling"
    assert data[0]["duration"] == 45
