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

# -----------------------------
# Extra test cases for robustness
# -----------------------------

def test_add_missing_workout(client):
    """Missing workout name should return 400."""
    response = client.post("/add", data={"workout": "", "duration": "20"})
    assert response.status_code == 400
    assert b"Please provide both workout and duration" in response.data

def test_add_missing_duration(client):
    """Missing duration should return 400."""
    response = client.post("/add", data={"workout": "Swimming", "duration": ""})
    assert response.status_code == 400
    assert b"Please provide both workout and duration" in response.data

def test_multiple_workouts(client):
    """Adding multiple workouts should keep track of all of them."""
    client.post("/add", data={"workout": "Pushups", "duration": "10"})
    client.post("/add", data={"workout": "Situps", "duration": "15"})
    response = client.get("/api/workouts")
    data = response.get_json()
    assert len(data) == 2
    assert data[0]["workout"] == "Pushups"
    assert data[1]["workout"] == "Situps"

def test_home_page_after_add(client):
    """Home page should show the workout after it's added."""
    client.post("/add", data={"workout": "Jump Rope", "duration": "5"})
    response = client.get("/")
    assert b"Jump Rope" in response.data
    assert b"5 minutes" in response.data
