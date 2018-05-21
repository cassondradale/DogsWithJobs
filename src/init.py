

def main():
    puppers = ["Dalmation", "Corgi", "Beagle", "Golden Retriever"]
    puppers.append("Wheaten Terrier")
    print(puppers)

    valid_breed = False
    while not valid_breed:
        choice = input("Please select your pupper: ")
        if choice in puppers:
            print("Congrats! You have a new dog!")
            valid_breed = True
        else:
            print("Please select a valid breed.")


if __name__ == "__main__":
    main()
