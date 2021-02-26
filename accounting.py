def has_customer_underpaid(melon_cost, path):
    """Calculate whether the customer underpaid
    
    Given the price of melons and a file path, iterate through each line in the 
    path and parse the data to determine if the customer has underpaid."""

    log = open(path) # open file 

    for line in log: # iterate through each line in the file 
        customer_data = line.split("|") # tokenize the data into a list 
        customer_number = customer_data[0] 
        customer_name = customer_data[1]
        customer_melons = customer_data[2]
        customer_paid = float(customer_data[3])
        
        customer_expected = int(customer_melons) * melon_cost
        if customer_expected != customer_paid:
            print(f"{customer_name} paid ${customer_paid:.2f},", # print how much they underpaid if that's the case 
            f"expected ${customer_expected:.2f}"
            )
    
    log.close() # close file 

has_customer_underpaid(melon_cost=1.00, path="customer-orders.txt")