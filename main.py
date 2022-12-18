class Course:
    def __init__(self, name, start_date, number_of_lectures, teacher):
        self.name = name
        self.start_date = start_date
        self.teacher = teacher
        self.lectures = []
        self._enrolled_by = []
        self.number_of_lectures = number_of_lectures
        self.homeworks = []
        for i in range(1, number_of_lectures+1):
            lec = Lecture(f'Lecture {i}', i, teacher)
            self.lectures.append(lec)
            teacher.teaching_lectures(lec)
        pass

    def __str__(self):
        return f'{self.name} ({self.start_date})'

    def enrolled_by(self, new_student=None):
        if new_student is not None:
            self._enrolled_by.append(new_student)
        return self._enrolled_by

    def get_lecture(self, num):
        if num <= self.number_of_lectures:
            return self.lectures[num-1]
        else:
            raise AssertionError('Invalid lecture number')

    def get_homeworks(self):
        for lec in self.lectures:
            if lec.get_homework() is not None:
                self.homeworks.append(lec.get_homework())
        return self.homeworks


class Lecture:
    def __init__(self, name, number, teacher):
        self.name = name
        self.number = number
        self.teacher = teacher
        self.homework = None
        pass

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name
        return self._name

    def get_homework(self):
        return self.homework

    def set_homework(self, home_work):
        self.homework = home_work

    def new_teacher(self, subst):
        self.teacher.remove_lecture(self)
        self.teacher = subst
        self.teacher.teaching_lectures(self)


class Homework:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        pass

    def __str__(self):
        return f'{self.name}: {self.description}'


class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.enrolled_courses = []
        self.assigned_works = []
        pass

    def __str__(self):
        return f'Student: {self.first_name} {self.last_name}'

    def enroll(self, course):
        self.enrolled_courses.append(course)
        course.enrolled_by(self)


class Teacher:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self._teaching_lectures = []
        self.homeworks_to_check = []
        pass

    def __str__(self):
        return f'Teacher: {self.first_name} {self.last_name}'

    def remove_lecture(self, lecture):
        self._teaching_lectures.remove(lecture)

    def teaching_lectures(self, lecture=None):
        if lecture is not None:
            self._teaching_lectures.append(lecture)
        return self._teaching_lectures


if __name__ == '__main__':
    main_teacher = Teacher('Thomas', 'Anderson')
    assert str(main_teacher) == f'Teacher: {main_teacher.first_name} {main_teacher.last_name}'

    python_basic = Course('Python basic', '31.10.2022', 16, main_teacher)
    assert len(python_basic.lectures) == python_basic.number_of_lectures
    assert str(python_basic) == 'Python basic (31.10.2022)'
    assert python_basic.teacher == main_teacher
    assert python_basic.enrolled_by() == []
    assert main_teacher.teaching_lectures() == python_basic.lectures
    #
    students = [Student('John', 'Doe'), Student('Jane', 'Doe')]
    for student in students:
        assert str(student) == f'Student: {student.first_name} {student.last_name}'
        student.enroll(python_basic)

    assert python_basic.enrolled_by() == students

    third_lecture = python_basic.get_lecture(3)
    assert third_lecture.name == 'Lecture 3'
    assert third_lecture.number == 3
    assert third_lecture.teacher == main_teacher
    try:
        python_basic.get_lecture(17)
    except AssertionError as error:
        assert error.args == ('Invalid lecture number',)

    third_lecture.name = 'Logic separation. Functions'
    assert third_lecture.name == 'Logic separation. Functions'

    assert python_basic.get_homeworks() == []
    assert third_lecture.get_homework() is None
    functions_homework = Homework('Functions', 'what to do here')
    assert str(functions_homework) == 'Functions: what to do here'
    third_lecture.set_homework(functions_homework)

    assert python_basic.get_homeworks() == [functions_homework]
    assert third_lecture.get_homework() == functions_homework
    # for student in students:
        # assert student.assigned_homeworks == [functions_homework]
    # #
    assert main_teacher.homeworks_to_check == []
    # students[0].do_homework(functions_homework)
    # assert students[0].assigned_homeworks == []
    # assert students[1].assigned_homeworks == [functions_homework]
    #
    # assert functions_homework.done_by() == {students[0]: None}
    # assert main_teacher.homeworks_to_check == [functions_homework]
    #
    # for mark in (-1, 101):
    #     try:
    #         main_teacher.check_homework(functions_homework, students[0], mark)
    #     except AssertionError as error:
    #         assert error.args == ('Invalid mark',)
    #
    # main_teacher.check_homework(functions_homework, students[0], 100)
    # assert main_teacher.homeworks_to_check == []
    # assert functions_homework.done_by() == {students[0]: 100}
    #
    # try:
    #     main_teacher.check_homework(functions_homework, students[0], 100)
    # except ValueError as error:
    #     assert error.args == ('You already checked that homework',)
    #
    # try:
    #     main_teacher.check_homework(functions_homework, students[1], 100)
    # except ValueError as error:
    #     assert error.args == ('Student never did that homework',)
    #
    substitute_teacher = Teacher('Agent', 'Smith')
    fourth_lecture = python_basic.get_lecture(4)
    assert fourth_lecture.teacher == main_teacher

    fourth_lecture.new_teacher(substitute_teacher)
    assert fourth_lecture.teacher == substitute_teacher
    assert len(main_teacher.teaching_lectures()) == python_basic.number_of_lectures - 1
    assert substitute_teacher.teaching_lectures() == [fourth_lecture]
    # assert substitute_teacher.homeworks_to_check == []