from monster_class import monster_inc

class student_monster_inc(monster_inc):

    def __init__(self, scary_subjects, uni_id):

        self.scary_subjects = scary_subjects
        self.uni_id = uni_id

    def studying(self):
        return "i read a lot of books"

    def caffeine_addition(self):
        return ' i drink too much coffee'

    def no_sleep(self):
        return ' i dont sleep enough'


