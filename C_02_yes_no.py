# check # checks users enter yes (y) or no (n)
def _yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "you chose yes"
        elif response == "no" or response == "n":
            return "you chose no"
        else:
            print("You did not choose a vaid response")


# Main routine
while True:
    want_instructions = _yes_no("Do you want to read the instructions?")
    print(f"you chose {want_instructions}")

    

