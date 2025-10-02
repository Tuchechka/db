class User:
    def __init__(self, user_id, name, email, phone_number, registration_date):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.registration_date = registration_date

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'name': self.name,
            'email': self.email,
            'phone_number': self.phone_number,
            'registration_date': self.registration_date
        }


class Course:
    def __init__(self, course_id, title, description, duration_course):
        self.course_id = course_id
        self.title = title
        self.description = description
        self.duration_course = duration_course

    def to_dict(self):
        return {
            'course_id': self.course_id,
            'title': self.title,
            'description': self.description,
            'duration_course': self.duration_course
        }


class Module:
    def __init__(self, module_id, title, course_id, order_number):
        self.module_id = module_id
        self.title = title
        self.course_id = course_id
        self.order_number = order_number

    def to_dict(self):
        return {
            'module_id': self.module_id,
            'title': self.title,
            'course_id': self.course_id,
            'order_number': self.order_number
        }


class Test:
    def __init__(self, test_id, title, module_id, description, created_date):
        self.test_id = test_id
        self.title = title
        self.module_id = module_id
        self.description = description
        self.created_date = created_date

    def to_dict(self):
        return {
            'test_id': self.test_id,
            'title': self.title,
            'module_id': self.module_id,
            'description': self.description,
            'created_date': self.created_date,
        }


class Question:
    def __init__(self, question_id, test_id, question_text, correct_answers):
        self.question_id = question_id
        self.test_id = test_id
        self.question_text = question_text
        self.correct_answers = correct_answers 

    def to_dict(self):
        return {
            'question_id': self.question_id,
            'test_id': self.test_id,
            'question_text': self.question_text,
            'correct_answers': self.correct_answers
        }

