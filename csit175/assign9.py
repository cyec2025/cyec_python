### Assignment 9 - Working with numbers
### Author: CYeC
### Date: 2022-04-21

tax_rate = 18

def user_input():
    global hours
    global pay_rate
    # user input section
    hours = float(input("Hours Worked: "))
    pay_rate = float(input("Hourly Pay Rate: "))

def gross_pay():
    global gross
    # calculate gross pay
    gross = hours * pay_rate
    
def tax_amount():
    global tax_amount
    # calculate tax amount
    tax_amount = gross * (tax_rate / 100)
    
def take_home_pay():
    global take_home_pay
    # calculate take home pay
    take_home_pay = gross - tax_amount

def main():
    # user input
    user_input()
    
    # calculations
    gross_pay()
    tax_amount()
    take_home_pay()
    
    # document results
    print("Gross Pay:",round(gross,2))
    print("Tax Rate:",str(tax_rate)+"%")
    print("Tax Amount:",round(tax_amount,2))
    print("Take Home Pay:", round(take_home_pay,2))
    
if __name__ == "__main__":
    main()
