from flask import Blueprint, request
from controller import UserController, CourseController, TestController, QuestionController, ModuleController

api_bp = Blueprint('api', __name__)

@api_bp.route('/users', methods=['GET'])
def get_all_users():
    return UserController.get_all_users()

@api_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    return UserController.get_user(user_id)

@api_bp.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    return UserController.add_user(data)

@api_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    return UserController.update_user(user_id, data)

@api_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    return UserController.delete_user(user_id)

@api_bp.route('/courses', methods=['GET'])
def get_all_courses():
    return CourseController.get_all_courses()

@api_bp.route('/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    return CourseController.get_course(course_id)

@api_bp.route('/courses-users/<int:users_id>', methods=['GET'])
def get_courses_by_user(users_id):
    return CourseController.get_courses_by_user(users_id)

@api_bp.route('/courses', methods=['POST'])
def add_course():
    data = request.get_json()
    return CourseController.add_course(data)

@api_bp.route('/courses/<int:course_id>', methods=['PUT'])
def update_course(course_id):
    data = request.get_json()
    return CourseController.update_course(course_id, data)

@api_bp.route('/courses/<int:course_id>', methods=['DELETE'])
def delete_course(course_id):
    return CourseController.delete_course(course_id)

@api_bp.route('/tests', methods=['GET'])
def get_all_tests():
    return TestController.get_all_tests()

@api_bp.route('/tests/<int:test_id>', methods=['GET'])
def get_test(test_id):
    return TestController.get_test(test_id)

@api_bp.route('/tests', methods=['POST'])
def add_test():
    data = request.get_json()
    return TestController.add_test(data)

@api_bp.route('/tests/<int:test_id>', methods=['PUT'])
def update_test(test_id):
    data = request.get_json()
    return TestController.update_test(test_id, data)

@api_bp.route('/tests/<int:test_id>', methods=['DELETE'])
def delete_test(test_id):
    return TestController.delete_test(test_id)

@api_bp.route('/questions', methods=['GET'])
def get_all_questions():
    return QuestionController.get_all_questions()

@api_bp.route('/questions/<int:question_id>', methods=['GET'])
def get_question(question_id):
    return QuestionController.get_question(question_id)

@api_bp.route('/questions', methods=['POST'])
def add_question():
    data = request.get_json()
    return QuestionController.add_question(data)

@api_bp.route('/questions/<int:question_id>', methods=['PUT'])
def update_question(question_id):
    data = request.get_json()
    return QuestionController.update_question(question_id, data)

@api_bp.route('/questions/<int:question_id>', methods=['DELETE'])
def delete_question(question_id):
    return QuestionController.delete_question(question_id)

@api_bp.route('/modules', methods=['GET'])
def get_all_modules():
    return ModuleController.get_all_modules()

@api_bp.route('/modules/<int:module_id>', methods=['GET'])
def get_module(module_id):
    return ModuleController.get_module(module_id)

@api_bp.route('/modules', methods=['POST'])
def add_module():
    data = request.get_json()
    return ModuleController.add_module(data)

@api_bp.route('/modules/<int:module_id>', methods=['PUT'])
def update_module(module_id):
    data = request.get_json()
    return ModuleController.update_module(module_id, data)

@api_bp.route('/modules/<int:module_id>', methods=['DELETE'])
def delete_module(module_id):
    return ModuleController.delete_module(module_id)
