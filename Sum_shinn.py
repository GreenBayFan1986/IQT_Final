import random
# Question 3

def main():
    """Generates two random numbers, then prompts the user for the sum of those numbers"""
    try:
        is_correct = False
        num_one = random.randint(1, 12)
        num_two = random.randint(1, 12)
        correct_answer = num_one + num_two

        while (is_correct == False):
            answer = int(raw_input("What is the sum of " + str(num_one) + " and " + str(num_two) + ": "))
            if (answer == correct_answer):
                print("Your answer was correct")
                is_correct = True
            else:
                print("That is incorrect try again")

    except:
        print("The answer must be a numeric value")


if __name__ == "__main__":
    main()