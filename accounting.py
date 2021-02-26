MELON_COST = 1.00 # global variable for melon cost

def paid_correct_amount(melon_cost, path):
    """Calculate whether the customer underpaid
    
    Given the price of melons and a file path, iterate through each line in the 
    path and parse the data to determine if the customer has underpaid."""

    log = open(path) # open file 

    for line in log: # iterate through each line in the file 
        customer_data = line.split("|") # tokenize the data into a list 
        customer_name = customer_data[1]
        customer_melons = int(customer_data[2])
        customer_paid = float(customer_data[3])
        
        customer_expected = customer_melons * melon_cost
        if customer_expected > customer_paid:
            print(f"{customer_name} has underpaid for their melons.") # print whether customer over/underpaid

        elif customer_expected < customer_paid:
            print(f"{customer_name} has overpaid for their melons.") # print whether customer over/underpaid

    
    log.close() # close file 

paid_correct_amount(melon_cost=MELON_COST, path="customer-orders.txt") # call the function