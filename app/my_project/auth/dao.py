from flask import current_app
from models import User, Course, Module, Test, Question

class UserDAO:
    @staticmethod
    def get_all_users():
        cursor = current_app.mysql.connection.cursor()
        cursor.execute("SELECT * FROM Users")
        users = [User(*row).to_dict() for row in cursor.fetchall()]
        cursor.close()
        return users
    
    @staticmethod
    def get_user_by_id(user_id):
        cursor = current_app.mysql.connection.cursor()
        cursor.execute("SELECT * FROM Users WHERE user_id = %s", (user_id,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return User(*row).to_dict()
        return None

    @staticmethod
    def add_user(name, email, phone_number, registration_date):
        cursor = current_app.mysql.connection.cursor()
        cursor.execute(
            "INSERT INTO Users (name, email, phone_number, registration_date) VALUES (%s, %s, %s, %s)",
            (name, email, phone_number, registration_date)
        )
        current_app.mysql.connection.commit()
        cursor.close()

    @staticmethod
    def update_user(user_id, name, email, phone_number, registration_date):
        cursor = current_app.mysql.connection.cursor()
        cursor.execute(
            "UPDATE Users SET name = %s, email = %s, phone_number = %s, registration_date = %s WHERE user_id = %s",
            (name, email, phone_number, registration_date, user_id)
        )
        current_app.mysql.connection.commit()
        cursor.close()

    @staticmethod
    def delete_user(user_id):
        cursor = current_app.mysql.connection.cursor()
        cursor.execute("DELETE FROM Users WHERE user_id = %s", (user_id,))
        current_app.mysql.connection.commit()
        cursor.close()

class CourseDAO:
    @staticmethod
    def get_all_courses():
        cursor = current_app.mysql.connection.cursor()
        cursor.execute("SELECT * FROM Courses")
        courses = [Course(*row).to_dict() for row in cursor.fetchall()]
        cursor.close()
        return courses

    @staticmethod
    def add_course(title_course, description_course, duration_course):
        cursor = current_app.mysql.connection.cursor()
        cursor.execute(
            "INSERT INTO Courses (title_course, description_course, duration_course) VALUES (%s, %s, %s)",
            (title_course, description_course, duration_course)
        )
        current_app.mysql.connection.commit()
        cursor.close()

    @staticmethod
    def update_course(course_id, title_course, description_course, duration_course):
        cursor = current_app.mysql.connection.cursor()
        cursor.execute(
            "UPDATE Courses SET title_course = %s, description_course = %s, duration_course = %s WHERE course_id = %s",
            (title_course, description_course, duration_course, course_id)
        )
        current_app.mysql.connection.commit()
        cursor.close()

    @staticmethod
    def delete_course(course_id):
        cursor = current_app.mysql.connection.cursor()
        cursor.execute("DELETE FROM Courses WHERE course_id = %s", (course_id,))
        current_app.mysql.connection.commit()
        cursor.close()

    @staticmethod
    def get_courses_by_user(user_id):
        cursor = current_app.mysql.connection.cursor()
        cursor.execute("""SELECT Courses.* FROM Courses
                          JOIN Enrollments ON Courses.course_id = Enrollments.course_id
                          WHERE Enrollments.user_id = %s""", (user_id,))
        courses = [Course(*row).to_dict() for row in cursor.fetchall()]
        cursor.close()
        return courses

class TestDAO:
    @staticmethod
    def get_all_tests():
        cursor = current_app.mysql.connection.cursor()
        cursor.execute("SELECT * FROM Tests")
        tests = [Test(*row).to_dict() for row in cursor.fetchall()]
        cursor.close()
        return tests

    @staticmethod
    def add_test(module_id, title_test, description_test, created_date):
        cursor = current_app.mysql.connection.cursor()
        cursor.execute(
            "INSERT INTO Tests (module_id, titel_test, description_test, created_date) VALUES (%s, %s, %s, %s)",
            (module_id, title_test, description_test, created_date)
        )
        current_app.mysql.connection.commit()
        cursor.close()

    @staticmethod
    def update_test(test_id, module_id, title_test, description_test, created_date):
        cursor = current_app.mysql.connection.cursor()
        cursor.execute(
            "UPDATE Tests SET module_id = %s, title_test = %s, description_test = %s, created_date = %s WHERE test_id = %s",
            (module_id, title_test, description_test, created_date, test_id)
        )
        current_app.mysql.connection.commit()
        cursor.close()

    @staticmethod
    def delete_test(test_id):
        cursor = current_app.mysql.connection.cursor()
        cursor.execute("DELETE FROM Tests WHERE test_id = %s", (test_id,))
        current_app.mysql.connection.commit()
        cursor.close()

class ModuleDAO:
    @staticmethod
    def get_all_modules():
        cursor = current_app.mysql.connection.cursor()
        cursor.execute("SELECT * FROM Modules")
        modules = [Module(*row).to_dict() for row in cursor.fetchall()]
        cursor.close()
        return modules

    @staticmethod
    def add_module(course_id, title_module, description_module):
        cursor = current_app.mysql.connection.cursor()
        cursor.execute(
            "INSERT INTO Modules (course_id, title_module, description_module) VALUES (%s, %s, %s)",
            (course_id, title_module, description_module)
        )
        current_app.mysql.connection.commit()
        cursor.close()

    @staticmethod
    def update_module(module_id, course_id, title_module, description_module):
        cursor = current_app.mysql.connection.cursor()
        cursor.execute(
            "UPDATE Modules SET course_id = %s, title_module = %s, description_module = %s WHERE module_id = %s",
            (course_id, title_module, description_module, module_id)
        )
        current_app.mysql.connection.commit()
        cursor.close()

    @staticmethod
    def delete_module(module_id):
        cursor = current_app.mysql.connection.cursor()
        cursor.execute("DELETE FROM Modules WHERE module_id = %s", (module_id,))
        current_app.mysql.connection.commit()
        cursor.close()

class QuestionDAO:
    @staticmethod
    def get_all_questions():
        cursor = current_app.mysql.connection.cursor()
        cursor.execute("SELECT * FROM Questions")
        questions = [Question(*row).to_dict() for row in cursor.fetchall()]
        cursor.close()
        return questions

    @staticmethod
    def add_question(test_id, text, number_points):
        cursor = current_app.mysql.connection.cursor()
        cursor.execute(
            "INSERT INTO Questions (test_id, text, number_points) VALUES (%s, %s, %s)",
            (test_id, text, number_points)
        )
        current_app.mysql.connection.commit()
        cursor.close()

    @staticmethod
    def update_question(question_id, test_id, text, number_points):
        cursor = current_app.mysql.connection.cursor()
        cursor.execute(
            "UPDATE Questions SET test_id = %s, text = %s, number_points = %s WHERE question_id = %s",
            (test_id, text, number_points, question_id)
        )
        current_app.mysql.connection.commit()
        cursor.close()

    @staticmethod
    def delete_question(question_id):
        cursor = current_app.mysql.connection.cursor()
        cursor.execute("DELETE FROM Questions WHERE question_id = %s", (question_id,))
        current_app.mysql.connection.commit()
        cursor.close()

