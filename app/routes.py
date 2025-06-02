from flask import Blueprint, request, jsonify
from app.service import TaskService

task_routes = Blueprint('tasks', __name__)
task_service = TaskService()

@task_routes.route('/tasks', methods=['GET'])
def list_tasks():
    return jsonify(task_service.get_all_tasks()), 200

@task_routes.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    if not data or 'title' not in data:
        return jsonify({'error': 'Missing title'}), 400
    task = task_service.create_task(data['title'])
    return jsonify(task), 201

@task_routes.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    if not data or 'title' not in data:
        return jsonify({'error': 'Missing title'}), 400
    updated = task_service.update_task(task_id, data['title'])
    if not updated:
        return jsonify({'error': 'Task not found'}), 404
    return jsonify(updated), 200

@task_routes.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    deleted = task_service.delete_task(task_id)
    if not deleted:
        return jsonify({'error': 'Task not found'}), 404
    return '', 204
