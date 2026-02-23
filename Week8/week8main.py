# Michael Audi - CIS161 Week 8 Main Assignment


def stop_shouting():
    firstin = input("Enter a phrase: ")
    secondin = input("Enter a phrase: ")
    if firstin.upper() == secondin:
        print("Stop shouting please!")
    return

def main():
    print("\n----- Step 1 -----")
    stop_shouting()
    return

if __name__ == "__main__":
    main()