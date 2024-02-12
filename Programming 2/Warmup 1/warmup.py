def names_from_file(filename):
    """
    Return a list of strings that are read from __filename__-file.

    PARAMETERS:
    filename (string) : name of the file to read strings from
    """
    file1 = open(filename, "r")
    strings_list = file1.readlines()
    strings_list = [line.rstrip() for line in strings_list]
    file1.close()
    return strings_list


def correct_string(string, symbols):
    """
    Return a new string which is __string__ without characters that are in __symbols__-list.
    You can assume that every item in __symbols__ are one character long.

    PARAMETERS:
    string (string) : a string of characters
    symbols (list) : a list of characters

    EXAMPLE:
    correct_string( "a!b?c%d/ef" , ["%","!","?","/"] )
    returns "abcdef".
    """
    new_list = string
    for character in symbols:
        new_list = new_list.replace(character, "")
    return new_list


def count_weighted_average(courses):
    """
    Return a weighted average* of courses from given 2-dimensional list __courses__.
    Average is zero if there are no courses in __courses__-list.
    *Weighted average is counted: sum of grade*credits from all courses / sum of all credits

    PARAMETERS:
    courses (2-dimensional list) : A list of courses. One course is a 3 item list: [grade, coursename , credits]

    EXAMPLE:
    count_weighted_average( [[5, "Basics in Programming Y1", 5], [2, "Communicating Technology", 3],[3, "Fourier Analysis", 5]] )
    returns 3.5384615384615383
    """
    sum = 0
    sum_of_credits = 0
    if len(courses) == 0:
        return sum
    for i in range(len(courses)):
        sum = sum + (courses[i][0] * courses[i][2])
        sum_of_credits = sum_of_credits + courses[i][2]
    wa = sum/sum_of_credits
    return wa


def find_student(dictionary, info):
    """
    Search __info__ from __dictionary__ values and returns the dictionary key of __info__.
    If __info__ is not in dictionary return False.

    PARAMETERS:
    dictionary (dictionary) : string points to 2-dimentional list
    info (2-dimensional list) : __courses__-list from count_weighted_average

    EXAMPLE:
    dictionary = { "Tiina Teekkari" : info1, "Teemu Teekkari": info2, "Kaisa Kemisti": info3 , "Kalle Kemisti": info4 }

    find_student(dictionary, info2)
    returns "Teemu Teekkari"
    """
    if info not in dictionary.values():
        return False
    for key, value in dictionary.items():
        if info == value:
            found_key = key
    return found_key


def is_on_course(students, participants):
    """
    Return a list of strings that are on both __students__-list and __participants__list, and the lenght of the new list.

    PARAMETERS:
    students (list) : list of strings
    participants (list) : list of strings

    RETURNS:
    a list, a lenght of the list (int)

    EXAMPLE:
    students = ["Tiina Teekkari", "Teemu Teekkari", "Kaisa Kemisti", "Kalle Kemisti"]
    participants = ["Anni Arkkitehti", "Antti Arkkitehti", "Teemu Teekkari", "Kaisa Kemisti"]

    is_on_course(students,participants)
    returns ["Teemu Teekkari", "Kaisa Kemisti"], 2
    """
    on_course = []
    for i in students:
        if i in participants:
            on_course.append(i)
    return on_course, len(on_course)
