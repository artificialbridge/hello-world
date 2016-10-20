def tip(bill, percentage):
    total = bill*percentage*0.01
    return total

def total_bill(bill,percentage):
    total = bill+tip(bill, percentage)
    return total

def split_bill(bill,people):
    total = float(bill)/people
    return total

def main():
    choice = raw_input("Enter 1 to calculate tip or 2 to split bill ")
    if choice == "1":
        bill = float(raw_input("original bill amount: "))
        percentage = float(raw_input("tip percentage: "))
        print tip(bill, percentage)
        total = total_bill(bill, percentage)
        print total
        if raw_input("Would you like to split the bill? (yes/no) ")=='yes':
            people = int(raw_input("How many ways would you like to split the bill? "))
            print split_bill(total, people)
    if choice=='2':
        bill = float(raw_input("total bill amount: "))
        people = int(raw_input("How many ways would you like to split the bill? "))
        print split_bill(bill, people)



if __name__ == '__main__':
    main()



