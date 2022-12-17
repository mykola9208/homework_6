class Course:
    def __init__(self, name, start_date, number_of_lectures, teacher):
        self.name = name
        self.start_date = start_date
        self.number_of_lectures = number_of_lectures
        self.teacher = teacher
        pass

    def __str__(self):
        return f'{self.name} ({self.start_date})'


class Teacher:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        pass

    def __str__(self):
        return f'Teacher: {self.first_name} {self.last_name}'


if __name__ == '__main__':
    main_teacher = Teacher('Thomas', 'Anderson')
    assert str(main_teacher) == f'Teacher: {main_teacher.first_name} {main_teacher.last_name}'
    python_basic = Course('Python basic', '31.10.2022', 16, main_teacher)
    #assert len(python_basic.lectures) == python_basic.number_of_lectures
    assert str(python_basic) == 'Python basic (31.10.2022)'
    assert python_basic.teacher == main_teacher
    #assert python_basic.enrolled_by() == []
    #assert main_teacher.teaching_lectures() == python_basic.lectures