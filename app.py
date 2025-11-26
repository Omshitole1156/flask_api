import os
from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)

# In-memory task list
tasks = []

# HTML template (simple)
html_page = """
<!DOCTYPE html>
<html>
<head>
    <title>To-Do App</title>
    <style>
        body { font-family: Arial; margin: 40px; }
        input { padding: 8px; }
        button { padding: 8px; }
        li { margin: 8px 0; }
    </style>
</head>
<body>
    <h2>Simple To-Do App</h2>

    <form action="/add" method="POST">
        <input type="text" name="task" placeholder="Enter task" required>
        <button type="submit">Add</button>
    </form>

    <h3>Your Tasks:</h3>
    <ul>
    {% for t in tasks %}
        <li>{{ t }}  
            <a href="/delete/{{ loop.index0 }}">❌ Delete</a>
        </li>
    {% endfor %}
    </ul>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html_page, tasks=tasks)

@app.route("/add", methods=["POST"])
def add_task():
    task = request.form.get("task")
    tasks.append(task)
    return redirect("/")

@app.route("/delete/<int:index>")
def delete_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
    return redirect("/")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
