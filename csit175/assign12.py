### Assignment 12 - Rectangle Calculator
### Author - CYeC
### Date: 2022-05-25

class Rectangle:
    def __init__(self,h,w):
        
        self.height = h
        self.width = w


    # method to get perimeter 
    def get_perimeter(self):
        
        perimeter = self.height * 2 + self.width * 2
        print("Perimeter: ", perimeter)

    # method to get area      
    def get_area(self):
        
        area = self.height * self.width
        print("Area: ", area)

    # square drawing
    def get_str(self):
        mystr = ""
        width = "* " * self.width + "\n"
        mystr += width
        for i in range(self.height - 2):
            mystr += "* "
            mystr += "  " * (self.width - 2)
            mystr += "* \n"
        mystr += width
        print(mystr)







def main():
    print("Rectangle Calculator Program")
    while True:
        # input
        height = int(input("\nNew rectangle height: "))
        width = int(input("New rectangle width: "))

        # methods
        my_rectangle = Rectangle(height,width)
        my_rectangle.get_perimeter()
        my_rectangle.get_area()
        my_rectangle.get_str()

        if input("\nContinue? (y/n):").lower() == "n":
            break
    print("Exited Program.")

if __name__ == "__main__":
    main()
