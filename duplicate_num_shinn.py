import random
#question 4

def main():
    """Generates a list of 30 numbers, prints out the duplicate numbers"""
    list = []
    for i in range(0, 30):
        list.append(random.randint(1,30))

    list.sort()
    print(list)

    print("\nDuplicates in the list")
    for int in list:
        if list.count(int) > 1:
            print(int)


if __name__ == "__main__":
    main()