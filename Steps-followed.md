# In the project folder:

### Test locally (no Docker)

python3 --version
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -v

# Manually run the app (optional but nice)

python app.py
Open http://localhost:5000
Quick checks:
Add a workout with the form.
View JSON at http://localhost:5000/api/workouts

# Test with Docker

### Build image

docker build -t aceest-fitness .

### Run tests inside the container

docker run --rm aceest-fitness pytest -q

### (Optional) run the app in Docker

docker run --rm -p 5000:5000 aceest-fitness

### visit http://localhost:5000

# Verify CI on GitHub (Actions)

Create a public GitHub repo (default branch: main).

In the project folder:

git init
git add .
git commit -m "Initial commit: Flask app, tests, Docker, CI"
git branch -M main
git remote add origin https://Dimple-AA@github.com/Dimple-AA/DevOps-Assignment-1.git
git push -u origin main

Open your repo’s Actions tab → you should see the pipeline run:

Installs deps

Runs pytest

Builds Docker image

Runs pytest inside Docker
Green check = all good.
