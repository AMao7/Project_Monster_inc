class Exam():

    exam_id = 1000

    def __init__(self, topic, time, format):
        self.topic = topic
        self.time = time
        self.format = format
        self.exam_id += 1
        Exam.exam_id += 1


test_1 = Exam('english', '1pm', 'mcq')
test_2 = Exam('maths', '3pm', 'mcq')

print(test_1.exam_id)
print(test_2.exam_id)
