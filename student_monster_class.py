from monster_class import Monster_inc

class student_monster_inc(Monster_inc):

    def __init__(self, name, strength, scary_subjects, uni_id, scary_skills):
        super().__init__(name, strength, scary_skills)

        self.scary_subjects = scary_subjects
        self.uni_id = uni_id
        self.__debt = 0      # double underscore makes it private


student_monster_1 = student_monster_inc('ringo', 'super strong', 'English', 1000, 'sdas')
student_monster_2 = student_monster_inc('lingo', 'super strong', 'Maths', 1001, 'sdasda')
student_monster_3 = student_monster_inc('dingo', 'super strong', 'Science', 1002, 'sdasda')


    # def eat(self, *args):      # This overrides the monster class method if the subclass object is called - This is polymorphism
    #     super().eat()       # this accesses the parents class's methods/attributes and runs the desired method
    #     return ' i am a student eating'
    #
    # def setter_debt_attribute(self, amount):        # internal methods can have access to encapsulated methods
    #     self.__debt = amount      # has access to debt attribute
    #
    # def get_debt_value(self):
    #     input('What is your login ')
    #     input('What is your password ')
    #     return self.__debt
    #
    #
    # def studying(self):
    #     return "i read a lot of books"
    #
    # def caffeine_addition(self):
    #     return ' i drink too much coffee'
    #
    # def no_sleep(self):
    #     return ' i dont sleep enough'



