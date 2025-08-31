# ACEest Fitness and Gym 🏋️‍♀️

A simple **Flask-based fitness tracker** for managing workouts, built as part of the *Introduction to DevOps Assignment - 1 (2025)*.  
This project demonstrates **Flask development, unit testing with Pytest, Docker containerization, and CI/CD with GitHub Actions**.

---

## 🚀 Features
- Add workouts with duration (minutes).
- View logged workouts on a web page.
- Access workouts as JSON via `/api/workouts`.
- Fully tested with **Pytest**.
- Containerized with **Docker**.
- Automated build + test pipeline via **GitHub Actions**.

---

## 📂 Project Structure
```
.
├── app.py                  # Flask application
├── test_app.py             # Pytest unit tests
├── requirements.txt        # Python dependencies
├── Dockerfile              # Containerization
└── .github/workflows/ci.yml # GitHub Actions CI/CD pipeline
```

---

## 🖥️ Running Locally

### Prerequisites
- Python 3.11+
- pip

### Setup
```bash
# Clone repo
git clone <your-repo-url>
cd <your-repo>

# Install dependencies
pip install -r requirements.txt

# Run Flask app
python app.py
```

App will run at: [http://localhost:5000](http://localhost:5000)

---

## 🧪 Running Tests Locally
```bash
pytest -v
```

---

## 🐳 Running with Docker
```bash
# Build the Docker image
docker build -t aceest-fitness .

# Run the container
docker run -p 5000:5000 aceest-fitness
```

Then visit [http://localhost:5000](http://localhost:5000).

---

## ⚙️ CI/CD with GitHub Actions
Every push to `main` triggers the workflow:
1. Install dependencies
2. Run **Pytest** locally
3. Build Docker image
4. Run **Pytest** inside Docker

You can view runs under **Actions tab** in GitHub.

---

## 📖 Assignment Deliverables Checklist
- [x] Flask application (`app.py`)
- [x] Unit tests (`test_app.py`)
- [x] Dockerfile
- [x] GitHub Actions CI/CD (`ci.yml`)
- [x] Documentation (`README.md`)

---

## 👩‍💻 Author
**ACEest DevOps Student**  
Built for *Introduction to DevOps Assignment - 1 (2025)*
