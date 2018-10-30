print("Cutis Liam Knows Preston")
print("16453897")
print()
print()


def per_week(loan,time):
    weekly = loan / time
    return weekly

loan_amount = int(input("Enter an amount: "))
number_of_weeks = int(input("how many weeks will it take to pay off: "))


per_w = per_week(loan_amount,number_of_weeks)

print("you must repay $", per_w," per week to repay a loan of $",loan_amount," in ",number_of_weeks,"weeks")

