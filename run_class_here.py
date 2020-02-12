
from monster_class import Monster_inc
from student_monster_class import student_monster_inc

print(student_monster_inc.eat("yikes"))

boz = Monster_inc('Boz', 4, 1000)
james_p_sullivan = student_monster_inc("spooky_s", "ID: 413123")

mike_wazowski = student_monster_inc('spooky_subject', "ID: 1241231" )
print(mike_wazowski)

print(Monster_inc.shout_strength(boz))




