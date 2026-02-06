# Michael Audi - CIS161 Week 5 Main Assignment


def divisible_five(numin:int):
    '''
    Checks if the input integer is divisible
    by 5, then returns True or False 
    '''
    if numin % 5 == 0:
        return True
    else:
        return False

def statein21(userinput:str):
    '''
    based on a the input string, compares the string to 6
    possible states and if it finds a match, prints
    the state's capital.
    '''
    statein = userinput.capitalize()
    if statein == "Alabama":
        print("The capital of Alabama is Montgomery.")
    elif statein == "Alaska":
        print("The capital of Alaska is Juneau.")
    elif statein == "Arizona":
        print("The capital of Arizona is Phoenix.")
    elif statein == "Arkansas":
        print("The capital of Arkansas is Little Rock.")
    elif statein == "California":
        print("The capital of California is Sacramento.")
    elif statein == "Colorado":
        print("The capital of Colorado is Denver.")
    else:
        print("I don't know that one!")

def statein22(userinput:str):
    '''
    '''
    statein = userinput.capitalize()
    statedict = {
        "Alabama":"Montgomery",
        "Alaska":"Juneau",
        "Arizona":"Phoenix",
        "Arkansas":"Little Rock",
        "California":"Sacramento",
        "Colorado":"Denver"
    }
    return statedict.get(statein, "[State not in Dict]")

def statein23(userinput:str):
    user23 = userinput.capitalize()
    match user23:
        case "Alabama":
            print(f"The capital of {user23} is Montgomery.")
        case "Alaska":
            print(f"The capital of {user23} is Juneau.")
        case "Arizona":
            print(f"The capital of {user23} is Phoenix.")
        case "Arkansas":
            print(f"The capital of {user23} is Little Rock.")
        case "California":
            print(f"The capital of {user23} is Sacramento.")
        case "Colorado":
            print(f"The capital of {user23} is Denver.")
        case other:
            print(f"The capital of {user23} is not stored in the match case system.")

def main():
    # Step 1
    userfive = int(input("Enter a number: "))
    print(f'The number {userfive} {"is" if divisible_five(userfive) else "isn\'t"} divisible by five.')

    # Step 2.1
    statein21(str(input("Input the name of a State: ")))
    

    # Step 2.2
    user22 = str(input("Input the name of a State: ")).capitalize()
    print(f"The capital of {user22} is {statein22(user22)}")

    # Step 2.3
    statein23(str(input("Input the name of a State: ")).capitalize())
    

    
        
if __name__ == "__main__":
    main()