# What this does
# / → a simple HTML form + list of workouts.
# /add → handles form submissions.
# /api/workouts → returns workouts as JSON (handy for testing & CI).

from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

# In-memory storage (like your Tkinter list)
workouts = []

# Simple HTML template
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>ACEestFitness and Gym</title>
</head>
<body>
    <h1>ACEestFitness and Gym</h1>
    <form method="POST" action="/add">
        <label>Workout: <input type="text" name="workout"></label><br>
        <label>Duration (minutes): <input type="number" name="duration"></label><br>
        <button type="submit">Add Workout</button>
    </form>
    <h2>Logged Workouts</h2>
    <ul>
        {% for w in workouts %}
            <li>{{ loop.index }}. {{ w['workout'] }} - {{ w['duration'] }} minutes</li>
        {% else %}
            <li>No workouts logged yet.</li>
        {% endfor %}
    </ul>
</body>
</html>
"""

@app.route("/", methods=["GET"])
def index():
    return render_template_string(HTML_TEMPLATE, workouts=workouts)

@app.route("/add", methods=["POST"])
def add_workout():
    workout = request.form.get("workout")
    duration = request.form.get("duration")

    if not workout or not duration:
        return "Please provide both workout and duration.", 400

    try:
        duration = int(duration)
        workouts.append({"workout": workout, "duration": duration})
        return render_template_string(HTML_TEMPLATE, workouts=workouts)
    except ValueError:
        return "Duration must be a number.", 400

@app.route("/api/workouts", methods=["GET"])
def get_workouts():
    return jsonify(workouts)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
