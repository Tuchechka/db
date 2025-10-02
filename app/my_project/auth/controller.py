from flask import jsonify, request
from dao import UserDAO, CourseDAO, TestDAO, QuestionDAO, ModuleDAO
from datetime import datetime

class UserController:
    @staticmethod
    def get_all_users():
        users = UserDAO.get_all_users()
        user_list = [user for user in users]
        return jsonify(user_list)

    @staticmethod
    def get_user(user_id):
        user = UserDAO.get_user_by_id(user_id)
        if user:
            return jsonify(user)
        return jsonify({'message': 'User not found'}), 404

    @staticmethod
    def add_user(data):
        date_str = data['registration_date']
        registration_date = datetime.strptime(date_str, "%a, %d %b %Y %H:%M:%S %Z").date()
        formatted_date = registration_date.strftime("%Y-%m-%d")
        UserDAO.add_user(data['name'], data['email'], data['phone_number'], formatted_date)
        return jsonify({'message': 'User added successfully!'}), 201

    @staticmethod
    def update_user(user_id, data):
        date_str = data['registration_date']
        registration_date = datetime.strptime(date_str, "%a, %d %b %Y %H:%M:%S %Z").date()
        formatted_date = registration_date.strftime("%Y-%m-%d")
        user = UserDAO.update_user(user_id, data['name'], data['email'], data['phone_number'], formatted_date)
        if user:
            return jsonify({'message': 'User updated successfully!'}), 200

    @staticmethod
    def delete_user(user_id):
        success = UserDAO.delete_user(user_id)
        if success:
            return jsonify({'message': 'User deleted successfully!'}), 200
        return jsonify({'message': 'User not found'}), 404


class CourseController:
    @staticmethod
    def get_all_courses():
        courses = CourseDAO.get_all_courses()
        course_list = [course for course in courses]
        return jsonify(course_list)

    @staticmethod
    def get_course(course_id):
        course = CourseDAO.get_course_by_id(course_id)
        if course:
            return jsonify(course)
        return jsonify({'message': 'Course not found'}), 404
    
    @staticmethod
    def get_courses_by_user(user_id):
        course = CourseDAO.get_courses_by_user(user_id)
        if course:
            return jsonify(course)
        return jsonify({'message': 'Course not found'}), 404

    @staticmethod
    def add_course(data):
        CourseDAO.add_course(data['titel_course'], data['description_course'], data['duration_course'])
        return jsonify({'message': 'Course added successfully!'}), 201

    @staticmethod
    def update_course(course_id, data):
        course = CourseDAO.update_course(course_id, data['titel_course'], data['description_course'], data['duration_course'])
        if course:
            return jsonify({'message': 'Course updated successfully!'}), 200
        return jsonify({'message': 'Course not found'}), 404

    @staticmethod
    def delete_course(course_id):
        success = CourseDAO.delete_course(course_id)
        if success:
            return jsonify({'message': 'Course deleted successfully!'}), 200
        return jsonify({'message': 'Course not found'}), 404


class TestController:
    @staticmethod
    def get_all_tests():
        tests = TestDAO.get_all_tests()
        test_list = [test for test in tests]
        return jsonify(test_list)

    @staticmethod
    def get_test(test_id):
        test = TestDAO.get_test_by_id(test_id)
        if test:
            return jsonify(test)
        return jsonify({'message': 'Test not found'}), 404

    @staticmethod
    def add_test(data):
        date_str = data['created_date']
        created_date = datetime.strptime(date_str, "%a, %d %b %Y %H:%M:%S %Z").date()
        formatted_date = created_date.strftime("%Y-%m-%d")
        TestDAO.add_test(data['module_id'], data['titel'], data['description'], formatted_date)
        return jsonify({'message': 'Test added successfully!'}), 201

    @staticmethod
    def update_test(test_id, data):
        date_str = data['created_date']
        created_date = datetime.strptime(date_str, "%a, %d %b %Y %H:%M:%S %Z").date()
        formatted_date = created_date.strftime("%Y-%m-%d")
        test = TestDAO.update_test(test_id, data['module_id'], data['titel_test'], data['description_test'], formatted_date)
        if test:
            return jsonify({'message': 'Test updated successfully!'}), 200
        return jsonify({'message': 'Test not found'}), 404

    @staticmethod
    def delete_test(test_id):
        success = TestDAO.delete_test(test_id)
        if success:
            return jsonify({'message': 'Test deleted successfully!'}), 200


class QuestionController:
    @staticmethod
    def get_all_questions():
        questions = QuestionDAO.get_all_questions()
        question_list = [question for question in questions]
        return jsonify(question_list)

    @staticmethod
    def get_question(question_id):
        question = QuestionDAO.get_question_by_id(question_id)
        if question:
            return jsonify(question)
        return jsonify({'message': 'Question not found'}), 404

    @staticmethod
    def add_question(data):
        QuestionDAO.add_question(data['test_id'], data['text'], data['number_points'])
        return jsonify({'message': 'Question added successfully!'}), 201

    @staticmethod
    def update_question(question_id, data):
        question = QuestionDAO.update_question(question_id, data['test_id'], data['text'], data['number_points'])
        if question:
            return jsonify({'message': 'Question updated successfully!'}), 200
        return jsonify({'message': 'Question not found'}), 404

    @staticmethod
    def delete_question(question_id):
        success = QuestionDAO.delete_question(question_id)
        if success:
            return jsonify({'message': 'Question deleted successfully!'}), 200


class ModuleController:
    @staticmethod
    def get_all_modules():
        modules = ModuleDAO.get_all_modules()
        module_list = [module for module in modules]
        return jsonify(module_list)

    @staticmethod
    def get_module(module_id):
        module = ModuleDAO.get_module_by_id(module_id)
        if module:
            return jsonify(module)
        return jsonify({'message': 'Module not found'}), 404

    @staticmethod
    def add_module(data):
        ModuleDAO.add_module(data['course_id'], data['titel_module'], data['description_module'])
        return jsonify({'message': 'Module added successfully!'}), 201

    @staticmethod
    def update_module(module_id, data):
        module = ModuleDAO.update_module(module_id, data['course_id'], data['titel_module'], data['description_module'])
        if module:
            return jsonify({'message': 'Module updated successfully!'}), 200
        return jsonify({'message': 'Module not found'}), 404

    @staticmethod
    def delete_module(module_id):
        success = ModuleDAO.delete_module(module_id)
        if success:
            return jsonify({'message': 'Module deleted successfully!'}), 200
        return jsonify({'message': 'Module not found'}), 404