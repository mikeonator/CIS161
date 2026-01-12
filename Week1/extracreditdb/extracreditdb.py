#Michael Audi - Database Extra Credit Assignment

course_db = {}

##course[""] = {"name":"", "cred":#, "dept":"", "desc":""}
course_db["CIS 161"] = {"name":"Computer Science 1", "cred":4, "dept":"CIS", "desc":"Algorithms, Algorithms, Algorithms!"}
course_db["CIS 120"] = {"name":"Computer Concepts", "cred":4, "dept":"CIS", "desc":"Computer Fundamentals, Key Applications, and Living Online"}
course_db["MUS 118"] = {"name":"Music Technology MIDI/Audio", "cred":3, "dept":"MUS", "desc":"Use various music production tools in live sound engineering and mixing"}
course_db["MUS 194"] = {"name":"Big Band Jazz", "cred":1, "dept":"MUS", "desc":"Study and performance of music for large jazz band. One major concert presented each term"}
course_db["CUL 101"] = {"name":"Introduction to Culinary Arts", "cred":4, "dept":"CUL", "desc":"Experience the basic theory and skill sets used throughout the field of culinary arts"}
course_db["CUL 242"] = {"name":"Charcuterie", "cred":4, "dept":"CUL", "desc":"Learn professional skills in variations of hors d'oeuvres and savories"}
course_db["ANTH 103"] = {"name":"Cultural Anthropology", "cred":4, "dept":"ANT", "desc":"Provides an introduction to the diversity of human beliefs and behaviors around the world"}
course_db["ANTH 254"] = {"name":"Magic, Witchcraft, Religion", "cred":4, "dept":"ANT", "desc":"Introduces students to the subject of religion in the broad anthropological context"}
course_db["AUT 101"] = {"name":"Basic Electricity-Automotive", "cred":2, "dept":"AUT", "desc":"A self paced course that provides understanding of fundamental principles of electricity"}
course_db["AUT 281"] = {"name":"Hybrid Electric Vehicles II", "cred":4, "dept":"AUT", "desc":"A study of HEV (hybrid electric vehicles) and EV (electric vehicles) part 2"}

def print_course_info(inDict):
    print(f"| {'Course Number':^13} | {'Course Name':^30} | {'Credits':^7} | {'Department':^10} | {'Description'}")
    print(f"|-{'':-^13}-|-{'':-^30}-|-{'':-^7}-|-{'':-^10}-|-{'':-^12}")

    for key, value in inDict.items():
        print(f"| {key:^13} | {value['name']:^30} | {value['cred']:^7} | {value['dept']:^10} | {value['desc']:.100}")

def print_single_course(inDict, coursenum):
    if coursenum in inDict:
        print_course_info({coursenum: inDict[coursenum]})
        return True
    else:
        print("Course Number not found in database. Check formatting, and make sure you've capitalized the department.")
        return False

def delete_course(inDict, coursenum):
    if coursenum in inDict:
        print(f"Successfully deleted {coursenum} - {inDict[coursenum]['name']}")
        del inDict[coursenum]
        return True
    else:
        print("Deletion failed. Course Number not found in database. Check formatting, and make sure you've capitalized the department.")
        return False

def print_department_courses(inDict, dept):
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
