from flask import Blueprint, request
from controller import UserController, CourseController, TestController, QuestionController, ModuleController

api_bp = Blueprint('api', __name__)

@api_bp.route("/users", methods=["GET"])
def get_all_users():
    """
    Get all users
    ---
    tags: [users]
    responses:
      200:
        description: List of users
        schema:
          type: array
          items:
            type: object
            properties:
              id: {type: integer}
              name: {type: string}
              email: {type: string}
              phone_number: {type: string}
              registration_date: {type: string}
    """
    return UserController.get_all_users()


@api_bp.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    """
    Get user by ID
    ---
    tags: [users]
    parameters:
      - in: path
        name: user_id
        type: integer
        required: true
    responses:
      200:
        description: User found
      404:
        description: User not found
    """
    return UserController.get_user(user_id)


@api_bp.route("/users", methods=["POST"])
def add_user():
    """
    Create user
    ---
    tags: [users]
    consumes: [application/json]
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required: [name, email]
          properties:
            name: {type: string, example: "John"}
            email: {type: string, example: "john@example.com"}
            phone_number: {type: string, example: "+380671112233"}
            registration_date: {type: string, example: "Wed, 02 Oct 2024 00:00:00 GMT"}
    responses:
      201:
        description: Created
    """
    data = request.get_json()
    return UserController.add_user(data)


@api_bp.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    """
    Update user
    ---
    tags: [users]
    consumes: [application/json]
    parameters:
      - in: path
        name: user_id
        type: integer
        required: true
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            name: {type: string}
            email: {type: string}
            phone_number: {type: string}
            registration_date: {type: string}
    responses:
      200:
        description: Updated
      404:
        description: User not found
    """
    data = request.get_json()
    return UserController.update_user(user_id, data)


@api_bp.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    """
    Delete user
    ---
    tags: [users]
    parameters:
      - in: path
        name: user_id
        type: integer
        required: true
    responses:
      200:
        description: Deleted
      404:
        description: User not found
    """
    return UserController.delete_user(user_id)


# =========================
# Courses
# =========================
@api_bp.route("/courses", methods=["GET"])
def get_all_courses():
    """
    Get all courses
    ---
    tags: [courses]
    responses:
      200:
        description: Courses list
    """
    return CourseController.get_all_courses()


@api_bp.route("/courses/<int:course_id>", methods=["GET"])
def get_course(course_id):
    """
    Get course by ID
    ---
    tags: [courses]
    parameters:
      - in: path
        name: course_id
        type: integer
        required: true
    responses:
      200:
        description: Course
      404:
        description: Course not found
    """
    return CourseController.get_course(course_id)


@api_bp.route("/courses-users/<int:users_id>", methods=["GET"])
def get_courses_by_user(users_id):
    """
    Get user's courses
    ---
    tags: [courses]
    parameters:
      - in: path
        name: users_id
        type: integer
        required: true
    responses:
      200:
        description: Courses of the user
    """
    return CourseController.get_courses_by_user(users_id)


@api_bp.route("/courses", methods=["POST"])
def add_course():
    """
    Create course
    ---
    tags: [courses]
    consumes: [application/json]
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required: [titel_course]
          properties:
            titel_course: {type: string, example: "SQL Basics"}
            description_course: {type: string, example: "Intro course"}
            duration_course: {type: integer, example: 30}
    responses:
      201:
        description: Created
    """
    data = request.get_json()
    return CourseController.add_course(data)


@api_bp.route("/courses/<int:course_id>", methods=["PUT"])
def update_course(course_id):
    """
    Update course
    ---
    tags: [courses]
    consumes: [application/json]
    parameters:
      - in: path
        name: course_id
        type: integer
        required: true
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            titel_course: {type: string}
            description_course: {type: string}
            duration_course: {type: integer}
    responses:
      200:
        description: Updated
      404:
        description: Course not found
    """
    data = request.get_json()
    return CourseController.update_course(course_id, data)


@api_bp.route("/courses/<int:course_id>", methods=["DELETE"])
def delete_course(course_id):
    """
    Delete course
    ---
    tags: [courses]
    parameters:
      - in: path
        name: course_id
        type: integer
        required: true
    responses:
      200:
        description: Deleted
      404:
        description: Course not found
    """
    return CourseController.delete_course(course_id)


# =========================
# Modules
# =========================
@api_bp.route("/modules", methods=["GET"])
def get_all_modules():
    """
    Get all modules
    ---
    tags: [modules]
    responses:
      200:
        description: Modules list
    """
    return ModuleController.get_all_modules()


@api_bp.route("/modules/<int:module_id>", methods=["GET"])
def get_module(module_id):
    """
    Get module by ID
    ---
    tags: [modules]
    parameters:
      - in: path
        name: module_id
        type: integer
        required: true
    responses:
      200:
        description: Module
      404:
        description: Module not found
    """
    return ModuleController.get_module(module_id)


@api_bp.route("/modules", methods=["POST"])
def add_module():
    """
    Create module
    ---
    tags: [modules]
    consumes: [application/json]
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required: [course_id, titel_module]
          properties:
            course_id: {type: integer, example: 1}
            titel_module: {type: string, example: "Module 1"}
            description_module: {type: string, example: "Basics"}
    responses:
      201:
        description: Created
    """
    data = request.get_json()
    return ModuleController.add_module(data)


@api_bp.route("/modules/<int:module_id>", methods=["PUT"])
def update_module(module_id):
    """
    Update module
    ---
    tags: [modules]
    consumes: [application/json]
    parameters:
      - in: path
        name: module_id
        type: integer
        required: true
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            course_id: {type: integer}
            titel_module: {type: string}
            description_module: {type: string}
    responses:
      200:
        description: Updated
      404:
        description: Module not found
    """
    data = request.get_json()
    return ModuleController.update_module(module_id, data)


@api_bp.route("/modules/<int:module_id>", methods=["DELETE"])
def delete_module(module_id):
    """
    Delete module
    ---
    tags: [modules]
    parameters:
      - in: path
        name: module_id
        type: integer
        required: true
    responses:
      200:
        description: Deleted
      404:
        description: Module not found
    """
    return ModuleController.delete_module(module_id)


# =========================
# Tests
# =========================
@api_bp.route("/tests", methods=["GET"])
def get_all_tests():
    """
    Get all tests
    ---
    tags: [tests]
    responses:
      200:
        description: Tests list
    """
    return TestController.get_all_tests()


@api_bp.route("/tests/<int:test_id>", methods=["GET"])
def get_test(test_id):
    """
    Get test by ID
    ---
    tags: [tests]
    parameters:
      - in: path
        name: test_id
        type: integer
        required: true
    responses:
      200:
        description: Test
      404:
        description: Test not found
    """
    return TestController.get_test(test_id)


@api_bp.route("/tests", methods=["POST"])
def add_test():
    """
    Create test
    ---
    tags: [tests]
    consumes: [application/json]
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required: [module_id, titel]
          properties:
            module_id: {type: integer, example: 1}
            titel: {type: string, example: "Test 1"}
            description: {type: string, example: "Intro test"}
            created_date: {type: string, example: "Wed, 02 Oct 2024 00:00:00 GMT"}
    responses:
      201:
        description: Created
    """
    data = request.get_json()
    return TestController.add_test(data)


@api_bp.route("/tests/<int:test_id>", methods=["PUT"])
def update_test(test_id):
    """
    Update test
    ---
    tags: [tests]
    consumes: [application/json]
    parameters:
      - in: path
        name: test_id
        type: integer
        required: true
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            module_id: {type: integer}
            titel_test: {type: string}
            description_test: {type: string}
            created_date: {type: string}
    responses:
      200:
        description: Updated
      404:
        description: Test not found
    """
    data = request.get_json()
    return TestController.update_test(test_id, data)


@api_bp.route("/tests/<int:test_id>", methods=["DELETE"])
def delete_test(test_id):
    """
    Delete test
    ---
    tags: [tests]
    parameters:
      - in: path
        name: test_id
        type: integer
        required: true
    responses:
      200:
        description: Deleted
      404:
        description: Test not found
    """
    return TestController.delete_test(test_id)


# =========================
# Questions
# =========================
@api_bp.route("/questions", methods=["GET"])
def get_all_questions():
    """
    Get all questions
    ---
    tags: [questions]
    responses:
      200:
        description: Questions list
    """
    return QuestionController.get_all_questions()


@api_bp.route("/questions/<int:question_id>", methods=["GET"])
def get_question(question_id):
    """
    Get question by ID
    ---
    tags: [questions]
    parameters:
      - in: path
        name: question_id
        type: integer
        required: true
    responses:
      200:
        description: Question
      404:
        description: Question not found
    """
    return QuestionController.get_question(question_id)


@api_bp.route("/questions", methods=["POST"])
def add_question():
    """
    Create question
    ---
    tags: [questions]
    consumes: [application/json]
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required: [test_id, text, number_points]
          properties:
            test_id: {type: integer, example: 1}
            text: {type: string, example: "2+2?"}
            number_points: {type: integer, example: 5}
    responses:
      201:
        description: Created
    """
    data = request.get_json()
    return QuestionController.add_question(data)


@api_bp.route("/questions/<int:question_id>", methods=["PUT"])
def update_question(question_id):
    """
    Update question
    ---
    tags: [questions]
    consumes: [application/json]
    parameters:
      - in: path
        name: question_id
        type: integer
        required: true
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            test_id: {type: integer}
            text: {type: string}
            number_points: {type: integer}
    responses:
      200:
        description: Updated
      404:
        description: Question not found
    """
    data = request.get_json()
    return QuestionController.update_question(question_id, data)


@api_bp.route("/questions/<int:question_id>", methods=["DELETE"])
def delete_question(question_id):
    """
    Delete question
    ---
    tags: [questions]
    parameters:
      - in: path
        name: question_id
        type: integer
        required: true
    responses:
      200:
        description: Deleted
      404:
        description: Question not found
    """
    return QuestionController.delete_question(question_id)
