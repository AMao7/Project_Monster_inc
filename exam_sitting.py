
class Exam_Sitting:

    exam_id = 1000

    def __init__(self, exam_name, __attendee_list = []):
        self.exam_name = exam_name
        self.attendee_list = __attendee_list
        self.exam_id += 1
        Exam_Sitting.exam_id += 1

    def add_student(self, student_monster_name):
        self.attendee_list.append(student_monster_name)


    # def student_list(self, exam_id, exam_name, attendee_list):
    #     return '{}-{}-{}'.format(exam_id, exam_name, attendee_list)


am = Exam_Sitting('Maths 101', ['Bob', 'Helen', 'Harry', 'Alonso', 'Stephanie'])
pm = Exam_Sitting('Spanish 109', ['Jack', 'Harvey', 'Nicole', 'Erica', 'Fernando'])

print(am.attendee_list)

