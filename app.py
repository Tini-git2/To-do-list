from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory list to store tasks
tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    task = request.form.get('task')
    if task:
        tasks.append(task)
    return redirect(url_for('index'))

@app.route('/delete/<int:index>')
def delete(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
    return redirect(url_for('index'))

if __name__ == "__main__":
    # host='0.0.0.0' allows access from any device in your local network (Linux ready)
    app.run(host='0.0.0.0', port=5000, debug=True)
