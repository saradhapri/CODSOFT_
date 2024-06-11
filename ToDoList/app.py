from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
tasks = []
@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)
@app.route('/add', methods=['POST'])
def add_task():
    task_content = request.form.get('task')
    if task_content:
        tasks.append({"task": task_content, "done": False})
    return redirect(url_for('index'))
@app.route('/update/<int:task_id>', methods=['POST'])
def update_task(task_id):
    new_task_content = request.form.get('task')
    if 0 <= task_id < len(tasks):
        tasks[task_id]['task'] = new_task_content
    return redirect(url_for('index'))
@app.route('/done/<int:task_id>')
def mark_task_done(task_id):
    if 0 <= task_id < len(tasks):
        tasks[task_id]['done'] = True
    return redirect(url_for('index'))
@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect(url_for('index'))
if __name__ == '__main__':
    app.run(debug=True)

