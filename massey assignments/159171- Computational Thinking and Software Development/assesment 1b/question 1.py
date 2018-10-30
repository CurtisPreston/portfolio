print("Curtis Preston")
print("16453897")
print()

def profit(price,amount):
    cost=0.20
    prof_per=price-cost
    profit=prof_per*amount

    return profit


def get_list_of_totals_from_sizzles():
    income=[]
    num = int(input("Enter the number of sausage sizzles last year:"))
    for x in range(0,num):
        print()
        print("****Sausage sizzle "+str(x+1)+"****")
        price=int(input("Enter the price per sausage: "))
        number=int(input("Enter the number of sausages to sell: "))
        income.append(int(profit(price,number)))
        print("The profit you would make is $"+str(income[x])+" for a sausage sizzle selling "+str(number))
        print("sausages at $"+str(price)+" per sausage.")
    return income


def total(list):
    y=0
    for x in range(0,len(list)):
        y+=list[x]
    return y


profits = get_list_of_totals_from_sizzles() #call the function
print()
print("Totals: ", profits)
total_profits=total(profits)
print()
print("The total profit made last year was $"+str(total_profits))

