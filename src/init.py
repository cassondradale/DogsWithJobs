

def main():
    puppers = ["Dalmation", "Corgi", "Beagle", "Golden Retriever"]
    puppers.append("Wheaten Terrier")
    print(puppers)

    valid_breed = False
    while not valid_breed:
        breed_choice = input("Please select your pupper: ")
        if breed_choice in puppers:
            print("Congrats! You have a new dog!")
            valid_breed = True
        else:
            print("Please select a valid breed.")

    pupper_name = input("Create a name for your new pupper: ")

    print("Your pupper's name is {0} and the breed is {1}".format(pupper_name, breed_choice))
if __name__ == "__main__":
    main()
