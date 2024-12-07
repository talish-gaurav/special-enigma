bill_tot = float(input("Enter the total cost of your bill  "))
tip_perc = int(input("Enter the percentage of your bill you would like to tip to the waiter  "))

def tc(bill_tot,tip_perc):
    total = bill_tot*(1+0.01*tip_perc)
    total = round(total,2)
    return total

print("The total amount of the bill is: ", tc(bill_tot,tip_perc))