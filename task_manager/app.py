from flask import Flask, request, jsonify
import index

app = Flask(__name__)

#Admin Endpoints
@app.route('/user',methods=['POST'])
def add_user():
    data = request.json
    
    index.create_user(
        name=data['name'],s_name=data['s_name'],u_type=data['u_type']
    )
    
    return ("User is successfully created", 201)

@app.route('/task',methods=['POST'])
def add_task():
    data = request.json
    
    index.create_task(
        name=data['name'],heading=data['heading'],
        description=data['description'],
        status=data['status'],
        type=data['type'],creator_id=data['creator_id'],
        worker_id=data['worker_id']
    )
    
    return ("Task is successfully created", 201)

@app.route('/delete/task',methods=['DELETE'])
def remove_task():
    data = request.json
    
    index.delete_task(
        name=data['name'],heading=data['heading'],
        worker_id=data['worker_id']
    )
    
    return ("Task is successfully deleted", 204)

@app.route('/getTask',methods=['GET'])
def get_task():
    
    tasks=index.view_tasks()
    
    return (jsonify(tasks), 200)

@app.route('/editTask',methods=['PUT'])
def update_task():
    data = request.json
    
    index.edit_task(u_id=data['u_id'],heading=data['heading'],description=data['description'])
    
    return ("Task has been successfully edited", 200)

#Worker Endpoints
@app.route('/completeTask',methods=['PUT'])
def finish_task():
    data = request.json
    
    index.complete_task(name=data['name'],worker_id=data['worker_id'])
    
    return ("Task has been successfully completed", 200)

if __name__ == "__main__":
    app.run(debug=True)
