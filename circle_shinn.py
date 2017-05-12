import math
# Question 1


def main():
    """Calculates the Diamter, Circumference and Area of a circle given a radius as input\n"""
    try:
        radius = float(raw_input("Please enter the radius of a circle: "))
        diameter = radius * 2
        circumference = (2 * math.pi * radius)
        area = math.pi * (radius * radius)

        print("Diameter:\t\t " + str(diameter))
        print("Circumference:\t " + str(circumference))
        print("Area:\t\t\t " + str(area))


    except:
        print("radius must be a numeric value")


if __name__ == "__main__":
    main()