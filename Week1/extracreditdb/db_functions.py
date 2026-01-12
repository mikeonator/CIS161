#Michael Audi
""" Database functions for Course Database Utility """

def print_course_info(inDict):
    """
    receives a nested dictionary with course information, and prints it out one key (course) at a time with a header at the top
    
    :param inDict: Nested dictionary with the structure: course[""] = {"name":"", "cred":#, "dept":"", "desc":""}
    :return True: Successful print
    """    
    print(f"| {'Course Number':^13} | {'Course Name':^30} | {'Credits':^7} | {'Department':^10} | {'Description'}")
    print(f"|-{'':-^13}-|-{'':-^30}-|-{'':-^7}-|-{'':-^10}-|-{'':-^12}")

    for key, value in inDict.items():
        print(f"| {key:^13} | {value['name']:^30} | {value['cred']:^7} | {value['dept']:^10} | {value['desc']:.100}")
    return True

def print_single_course(inDict, coursenum):
    """    
    receives a nested dictionary with course information and a course number, then prints that individual course's information

    :param inDict: Nested dictionary with the structure: course[""] = {"name":"", "cred":#, "dept":"", "desc":""}
    :param coursenum: Course Number str with max 8 char (Ex: CIS 161 or ANTH 254).
    :return False: When the nested dictionary does not contain an entry with the provided course number
    :return True: Successful printing of the courses based on provided input.
    """
    if coursenum in inDict:
        print_course_info({coursenum: inDict[coursenum]})
        return True
    else:
        print("Course Number not found in database. Check formatting, and make sure you've capitalized the department.")
        return False

def delete_course(inDict, coursenum):
    """
    receives a nested dictionary with course information and a Course number, then deletes the corresponding course from the provided dictionary
    
    :param inDict: Nested dictionary with the structure: course[""] = {"name":"", "cred":#, "dept":"", "desc":""}
    :param coursenum: Course Number str with max 8 char (Ex: CIS 161 or ANTH 254).
    :return False: When the nested dictionary does not contain an entry with a matching course number, leading to no deletion occurring.
    :return True: When the deletion of the entry with a matching course number from the provided dictionary is successful.
    """
    if coursenum in inDict:
        print(f"Successfully deleted {coursenum} - {inDict[coursenum]['name']}")
        del inDict[coursenum]
        return True
    else:
        print("Deletion failed. Course Number not found in database. Check formatting, and make sure you've capitalized the department.")
        return False

def print_department_courses(inDict, dept):
    """
    receives a nested dictionary with course information and a Course Department identifier, then prints the corresponding courses using print_course_info.
    
    :param inDict: Nested dictionary with the structure: course[""] = {"name":"", "cred":#, "dept":"", "desc":""}
    :param dept: Course Department str with exactly 3 uppercase char (matching the first 3 char of coursenum) (Ex: CIS or ANT).
    :return False: If inDict does not contain a course with a matching dept value
    :return True: Successful printing of the courses based on provided input.
    """
    tempdb = {}
    for key, value in inDict.items():
        if value['dept'] == dept:
            tempdb[key] = value
    
    if not tempdb:
        print("No Courses found with the provided department. Make sure you've trimmed the department to 3 characters.")
        return False
    else:
        print_course_info(tempdb)
        return True

def add_course(inDict, coursenum, coursename, coursecred, coursedept, coursedesc):
    """
    receives individual parameters that make up a course dict entry, then adds it to the provided nested dict
    
    :param inDict: Nested dictionary with an internal dict structure of: course[""] = {"name":"", "cred":#, "dept":"", "desc":""}
    :param coursenum: Course Number str with max 8 char (Ex: CIS 161 or ANTH 254).
    :param coursename: Course Name str with max 30 char (Ex: Computer Science 1).
    :param coursecred: Course Credits int (Ex: 4).
    :param coursedept: Course Department str with exactly 3 uppercase char (matching the first 3 char of coursenum) (Ex: CIS or ANT).
    :param coursedesc: Course Description str with max 100 char (Ex: Algorithms, Algorithms, Algorithms!)
    :return False if provided course info cannot be added
    :return True if provided course info is added successfully
    """
    if  type(coursenum) != str:
        print(f"Course Number must be a string <=8 characters. Type: {type(coursenum)}")
        return False
    elif len(coursenum) > 8:
        print(f"Course Number must be a string <=8 characters. Len: {len(coursenum)}")
        return False
    elif coursenum in inDict:
        print("Course Number already in database, please try again.")
        return False
    elif type(coursename) != str:
        print(f"Course Name must be a string <=30 characters. Type: {type(coursename)}")
        return False
    elif len(coursename) > 30:
        print(f"Course Name must be a string <=30 characters. Len: {len(coursename)}")
        return False
    elif type(coursecred) != int:
        print(f"Course Credits does not match type int. Type: {type(coursecred)}")
        return False
    elif type(coursedept) != str:
        print(f"Course Department must be a string 3 characters in length and all uppercase. Type: {type(coursedept)}")
        return False
    elif len(coursedept) != 3:
        print(f"Course Department must be a string 3 characters in length and all uppercase. Len: {len(coursedept)}")
        return False
    elif coursedept.isupper() != True:
        print(f"Course Department must be a string 3 characters in length and all uppercase. isupper: {coursedept.isupper()}")
        return False
    elif type(coursedesc) != str:
        print(f"Course Description must be a string <=100 characters. Type: {type(coursedesc)}")
        return False
    elif len(coursedesc) > 100:
        print(f"Course Description must be a string <=100 characters. Len: {len(coursedesc)}")
        return False
    elif coursenum[:3] != coursedept:
        print(f"Course Number provided does not match the Course Department provided (when trimmed to first 3 characters)")
        return False
    else:
        inDict[coursenum] = {"name":coursename, "cred":coursecred, "dept":coursedept, "desc":coursedesc}
        return True
