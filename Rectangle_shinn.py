import re
# question 5

class rectangle:
    def __init__(self, length, width):
        self.length = float(length)
        self.width = float(width)


    def calculate_perimeter(self):
        perimeter = (self.length * 2) + (self.width * 2)
        print("Perimeter: " + str(perimeter))

    def calculate_area(self):
        area = self.length * self.width
        print("Area:\t   " + str(area))

    def check_square(self):
        if (self.length == self.width):
            print("This rectangle is a square")


def main():
    print("Calculating a Rectangle")
    length = raw_input("Enter length or the coordinates for bottom left corner\n"
                       + "(i.e) (2,2) or just 5: ")
    width = raw_input("Enter width or the coordinates for the top right corner\n"
                       + "(i.e) (6,6) or just 5: ")

    if (re.match("\d+", length)):
        len = length
    elif (re.match("\(\d+,\d+\)", length)):
        print("worked")
        tup_len = tuple(length)
    if (re.match("\d+", width)):
        wid = width
    elif (re.match("\(\d+,\d+\)", width)):
        tup_width = tuple(width)
        len = float(tup_width[1]) - float(tup_len[1])
        wid = float(tup_width[3]) - float(tup_len[3])

    rec = rectangle(len, wid)

    rec.calculate_perimeter()
    rec.calculate_area()
    rec.check_square()

if __name__ == "__main__":
    main()