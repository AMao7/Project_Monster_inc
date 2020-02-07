
from monster_class import monster_inc
from student_monster_class import student_monster_inc

print(student_monster_inc.eat('yikes'))

boz = monster_inc('Boz', 4, 1000)
james_p_sullivan = student_monster_inc("ID: 413123", 10)

print(boz.shout_strength())
print(james_p_sullivan.studying())
print(james_p_sullivan.shout_strength())
