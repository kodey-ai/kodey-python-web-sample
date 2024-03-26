from flask import Flask, request, jsonify
from models import db, Student

app = Flask(__name__)

@app.route('/student', methods=['POST'])
def add_student():
    user = request.json['user']
    full_name = request.json['full_name']
    roll_no = request.json['roll_no']
    semester = request.json['semester']
    new_student = Student(user=user, full_name=full_name, roll_no=roll_no, semester=semester)
    db.session.add(new_student)
    db.session.commit()
    return jsonify({"message": "Student added successfully"}), 201

@app.route('/student', methods=['GET'])
def get_students():
    students = Student.query.all()
    return jsonify([{"user": student.user, "full_name": student.full_name, "roll_no": student.roll_no, "semester": student.semester} for student in students])

@app.route('/student/<user>', methods=['PUT'])
def update_student(user):
    student = Student.query.filter_by(user=user).first()
    if student:
        student.full_name = request.json['full_name']
        student.roll_no = request.json['roll_no']
        student.semester = request.json['semester']
        db.session.commit()
        return jsonify({"message": "Student updated successfully"}), 200
    else:
        return jsonify({"message": "Student not found"}), 404