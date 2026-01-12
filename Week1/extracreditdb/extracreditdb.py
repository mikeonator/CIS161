#Michael Audi - Database Extra Credit Assignment

course = {}

##course[""] = {"name":"", "cred":#, "dept":"", "desc":""}
course["CIS 161"] = {"name":"Computer Science 1", "cred":4, "dept":"CIS", "desc":"Algorithms, Algorithms, Algorithms!"}
course["CIS 120"] = {"name":"Computer Concepts", "cred":4, "dept":"CIS", "desc":"Computer Fundamentals, Key Applications, and Living Online"}
course["MUS 118"] = {"name":"Music Technology MIDI/Audio", "cred":3, "dept":"MUS", "desc":"Use various music production tools in live sound engineering and mixing"}
course["MUS 194"] = {"name":"Big Band Jazz", "cred":1, "dept":"MUS", "desc":"Study and performance of music for large jazz band. One major concert presented each term"}
course["CUL 101"] = {"name":"Introduction to Culinary Arts", "cred":4, "dept":"CUL", "desc":"Experience the basic theory and skill sets used throughout the field of culinary arts"}
course["CUL 242"] = {"name":"Charcuterie", "cred":4, "dept":"CUL", "desc":"Learn professional skills in variations of hors d'oeuvres and savories"}
course["ANTH 103"] = {"name":"Cultural Anthropology", "cred":4, "dept":"ANT", "desc":"Provides an introduction to the diversity of human beliefs and behaviors around the world"}
course["ANTH 254"] = {"name":"Magic, Witchcraft, Religion", "cred":4, "dept":"ANT", "desc":"Introduces students to the subject of religion in the broad anthropological context"}
course["AUT 101"] = {"name":"Basic Electricity-Automotive", "cred":2, "dept":"AUT", "desc":"A self paced course that provides understanding of fundamental principles of electricity"}
course["AUT 281"] = {"name":"Hybrid Electric Vehicles II", "cred":4, "dept":"AUT", "desc":"A study of HEV (hybrid electric vehicles) and EV (electric vehicles) part 2"}

def print_course_info(inDict):
    entries = len(inDict)

    print(f"| {'Course Number':^13} | {'Course Name':^30} | {'Credits':^7} | {'Department':^10} | {'Description'}\n" + f"|-{'':-^13}-|-{'':-^30}-|-{'':-^7}-|-{'':-^10}-|-{'':-^12}")

    for key, value in inDict.items():
        print(f"| {key:^13} | {value['name']:^30} | {value['cred']:^7} | {value['dept']:^10} | {value['desc']:.100}")
