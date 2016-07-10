# Global variables. Feel free to play around with these
# but please return them to their original values before you submit.
a0_weight = 5
a1_weight = 7
a2_weight = 8
term_tests_weight = 20
exam_weight = 45
exercises_weight = 10
quizzes_weight = 5

a0_max_mark = 25
a1_max_mark = 50
a2_max_mark = 100
term_tests_max_mark = 50
exam_max_mark = 100
exercises_max_mark = 10
quizzes_max_mark = 5

exam_pass_mark = 40
overall_pass_mark = 50


def get_max(component_name):
    '''(str) -> float
    Given the name of a course component (component_name),
    return the maximum mark for that component. This is used to allow the GUI
    to display the "out of" text beside each input field.
    REQ: component_name must be one of: a0,a1,a2,exerises,midterm,exam
    >>> get_max('a0')
    25
    >>> get_max('exam')
    100
    REQ: component_name in {'a0', 'a1', 'a2', 'exercises', 'term tests',
    'quizzes', 'exam'}
    '''
    # DO NOT EDIT THIS FUNCTION. This function exists to allow the GUI access
    # to some of the global variables. You can safely ignore this function
    # for the purposes of E2.
    if(component_name == 'a0'):
        result = a0_max_mark
    elif(component_name == 'a1'):
        result = a1_max_mark
    elif(component_name == 'a2'):
        result = a2_max_mark
    elif(component_name == 'exercises'):
        result = exercises_max_mark
    elif(component_name == 'term tests'):
        result = term_tests_max_mark
    elif(component_name == 'quizzes'):
        result = quizzes_max_mark
    else:
        result = exam_max_mark

    return result


def percentage(raw_mark, max_mark):
    ''' (float, float) -> float
    Return the percentage mark on a piece of work that received a mark of
    raw_mark where the maximum possible mark of max_mark.
    >>> percentage(15, 20)
    75.0
    >>> percentage(4.5, 4.5)
    100.0
    REQ: raw_mark >=0
    REQ: max_mark > 0
    REQ: raw_mark <= max_mark
    '''
   
    return float(raw_mark / max_mark * 100)



def contribution(raw_mark, max_mark, weight):
    ''' (float, float, float) -> float
    Given a piece of work where the student earned raw_mark marks out of a
    maximum of max_marks marks possible, return the number of marks it
    contributes to the final course mark if this piece of work is worth weight
    marks in the course marking scheme.
    >>> raw_contribution(13.5, 15, 10.0)
    9.0
    REQ: raw_mark >=0
    REQ: max_mark > 0
    REQ: weight >= 0
    '''
    percent = percentage(raw_mark, max_mark)

    return float(percent*weight/100)


def term_work_mark(a0,a1,a2,ex,qz,tt):
    ''' (float,float,float,float,float,float) -> float
    Given the marks of assignments 0-2, exercises, quizzes, and term tests
    then returns the total points toward the class grade

    >>> term_work_mark(25,50,100,10,5,50)
    55.0
    REQ: a0 >=0
    REQ: a1 >=0
    REQ: a2 >=0
    REQ: ex >=0
    REQ: qz >=0
    REQ: tt >=0
    '''
    a0 = contribution(a0,a0_max_mark,a0_weight)
    a1 = contribution(a1,a1_max_mark,a1_weight)
    a2 = contribution(a2,a2_max_mark,a2_weight)
    ex = contribution(ex,exercises_max_mark,exercises_weight)
    qz = contribution(qz,quizzes_max_mark,quizzes_weight)
    tt = contribution(tt,term_tests_max_mark,term_tests_weight)

    return a0+a1+a2+ex+qz+tt

def final_mark(a0,a1,a2,ex,qz,tt,fe):
    ''' (float,float,float,float,float,float,float) -> float
    Given all marks applicable in the school year for CSCA08
    (assignments 0-2,exercises,quizzes,term tests, and Final exam)
    calculates total grade

    >>>final_mark(25,50,100,10,5,50,100)
    100.0

    REQ: a0 >=0
    REQ: a1 >=0
    REQ: a2 >=0
    REQ: ex >=0
    REQ: qz >=0
    REQ: tt >=0
    REQ: fe >=0
    '''
    
    term = term_work_mark(a0,a1,a2,ex,qz,tt)
    fe = contribution(fe,exam_max_mark,exam_weight)
    return term + fe

def is_pass(a0,a1,a2,ex,qz,tt,fe):
    ''' (float,float,float,float,float,float,float) -> boolean
    Given all marks applicable in the school year for CSCA08
    (assignments 0-2,exercises,quizzes,term,tests, and Final exam)
    calculates a student's pass or fail
    >>>is_pass(25,50,100,10,5,50,100)
    True
    >>>is_pass(25,50,100,10,5,50,39)
    False
    >>>is_pass(0,0,0,0,0,0,0)
    False
    REQ: a0 >=0
    REQ: a1 >=0
    REQ: a2 >=0
    REQ: ex >=0
    REQ: qz >=0
    REQ: tt >=0
    REQ: fe >=0
    '''
    if(fe >= exam_pass_mark):
        if (final_mark(a0,a1,a2,ex,qz,tt,fe) >= overall_pass_mark):
            return True
        else:
            return False
    else:
        return False
