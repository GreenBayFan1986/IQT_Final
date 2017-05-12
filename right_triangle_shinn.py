import math
# given two sides and calculate the third, a and b less than 20
# Question 2

def main():
    """Calculates the third side of a right triangle given the two smaller sides"""
    try:
        side_a = float(raw_input("Enter a value less than 20 for side A: "))
        side_b = float(raw_input("Enter a value less than 20 for side B: "))

        if (side_a <= 0 or side_b <= 0):
            print("Side A and Side B must both be numbers above 0\n")
        else:
            side_c = math.sqrt((side_a * side_a) + (side_b * side_b))

            print("The hypotenuse is: " + str(side_c))

    except:
        print("Side A and Side B must be numeric values")


if __name__ == "__main__":
    main()