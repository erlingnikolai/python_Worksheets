# -*- coding: utf-8 -*-
# Created on <add the date here>
# For use in Scientific Python course
# Topic: objects
# @author: <add your name here>
# @organisation: IMPACS, Aberystwyth University

"""
Script for exercises on objects
"""

import university

departmentName = "departmentyes"
x = university.department(departmentName)
print(x.name)
#print(x)


#sam = university.student(4, "sam", "male", 24,199)
#erling = university.student(99, "erling", "male", 24, 129)
#x.students.insert(0,sam)
#x.students.insert(1, erling)
#x.list_students()
def a4():
    pfact = university.PeopleFactory()
    people50 = pfact.generate_random_people(50)
    stat50 = university.PersonalStatistics(people50)
    stat50.report()

def bc4():
    sfact = university.PeopleFactory()
    sfact.age_groups = {'young':95, 'older':5}
    sfact.young_age_lbound = 18
    sfact.young_age_hbound = 22
    people100 = sfact.generate_random_people(100)
    stat100 = university.PersonalStatistics(people100)
    stat100.report()



def d4():
    sfact = university.PeopleFactory()
    sfact.age_groups = {'young':95, 'older':5}
    sfact.young_age_lbound = 18
    sfact.young_age_hbound = 22
    people1000 = sfact.generate_random_people(100, cls=university.student)
    x.students = people1000
    x.list_students()
    
    
    
d4()