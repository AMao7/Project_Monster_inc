# make monster class here
class monster_inc():

    def __init__(self,  name,  strength, scary_skills):
        self.name = name
        self.strength = strength
        self.scary_skills = scary_skills

    def eat(self):
        return 'i like to eat!'

    def sleep(self):
        return 'zzzz'

    def pay_taxes(self):
        return 'rip monies'

    def shout_strength(self):
        return 'ARRGHHHHHHHHHHH'
