from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    task = request.form.get('task')
    tasks.append(task)
    return jsonify({'message': 'Task added successfully', 'tasks': tasks})

if __name__ == '__main__':
    app.run(debug=True)
