#!/bin/python3

import math
import os
import random
import re
import sys

def my_map(f,lst):
    if lst == []:
        return []
    else:
        return [f(lst[0])] + my_map(f, lst[1:])

def myzip(lst1,lst2):
    if lst1 ==[] or lst2 == []:
        return []
    else:
        return [(lst1[0],lst2[0])] + myzip(lst1[1:],lst2[1:])

def student(sid,fname,lname, crses):
    """Constructor for student"""
    courses = []
    while crses != []:
        courses += [(crses[0],crses[1])]
        crses = crses[2:]
    return [sid,[fname,lname],courses]

def get_id(std):
    """Returns students ID"""
    return std[0]

def get_name(std):
    """Returns students Name"""
    return std[1]

def get_courses(std):
    """Returns a list of tuples of course codes and grade"""
    return std[2]

def get_fname(name):
    """Returns first name"""
    return name[0]

def get_lname(name):
    """Returns last name"""
    return name[1]

def get_ccode(course_det):
    """Returns course code part of the tuple"""
    return course_det[0]

def get_grade(course_det):
    """Returns grade part of the tuple"""
    return course_det[1]

       
## For this function to work you first need to write calc_gpa()
def print_students_gpa(std):
    """Prints the students details and GPA"""
    fptr.write("Student Id: " + get_id(std) + '\n')
    fptr.write("Student name: " + get_fname(get_name(std)) + ' ' + get_lname(get_name(std)) + '\n')
    fptr.write("GPA: %.2f\n" %(calc_gpa(std)))


# Include the 'compute_letter_grade' function (from PROBLEM 1)

# Include the 'compute_letter_grade' function (from PROBLEM 1) below.
def compute_letter_grade(num_grade):
    # Write your code here
    if num_grade > 89:
        g = 'A+'
    elif num_grade >= 80:
        g = 'A'
    elif num_grade >= 75:
        g = 'A-'
    elif num_grade >= 70:
        g = 'B+'
    elif num_grade >= 65:
        g = 'B'
    elif num_grade >= 60:
        g = 'B-'
    elif num_grade >= 55:
        g = 'C+'
    elif num_grade >= 50:
        g = 'C'
    elif num_grade >= 45:
        g = 'F1'
    elif num_grade >= 40:
        g = 'F2'
    elif num_grade >= 0:
        g = 'F3'
    return g




# Complete the 'calc_letter_grade' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY std as parameter.
#

def calc_letter_grade(student):
    # Write your code here
    list_s = get_courses(student)


    num_grades = my_map(get_grade, list_s)
    list_grades = my_map(compute_letter_grade, num_grades)

    list_courses = my_map(get_ccode, list_s)

    result = myzip(list_courses, list_grades)
    return result
    
#
# Complete the 'convert_to_wtqp' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY c_pair as parameter.
#

def convert_to_wtqp(c_pair):
    # Write your code here
      
    list_code = get_ccode(c_pair)
    list_letter = get_grade(c_pair)

    list_credits = credit_list[list_code]
    list_scores = qp_list[list_letter]

    result = (list_credits,list_scores)
    return result

#
# Complete the 'calc_gpa' function below.
#
# The function is expected to return a FLOAT.
# The function accepts STRING_ARRAY std as parameter.
#

def calc_gpa(student):
    # Write your code here
    list_qt = []
    divide = []
    courses = get_courses(student)
    courses_letters = calc_letter_grade(student)

    a = my_map(convert_to_wtqp, courses_letters)
    divide = my_map(get_ccode, a)
    point = my_map(math.prod, a)
    list_result = sum(point) / sum(divide)

    return list_result

if __name__ == '__main__':
    credit_list={'COMP1126':3,'COMP1127':3,'COMP1161':3,'COMP1210':3,'COMP1220':3,'COMP2140':3,\
                 'COMP2111':3,'COCR2003':1}

    qp_list = {"A+":4.3,"A":4.0,"A-":3.7,"B+":3.3,"B":3.0,"B-":2.7,"C+":2.3,"C":2.0,"F1":1.7,"F2":1.3,\
               "F3": 0.0}

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    std = input().split(',')
    sid = std[0]
    fname = std[1]
    lname = std[2]
    no_of_courses = int(std[3])
    courses = []
    for i in range(no_of_courses):
        courses += [std[4+2*i]] + [int(std[4+2*i+1])]
    stud=student(sid,fname,lname,courses)

    print_students_gpa(stud)
    fptr.write('\n')

    fptr.close()