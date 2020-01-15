"""Generate sales report showing total melons each salesperson sold."""


salespeople = [] # create an empty list of salespeople
melons_sold = [] # create an empty list of melons sold

f = open('sales-report.txt') # open the sales-report.txt file and save it as f
for line in f: # for each line in the file
    line = line.rstrip() # remove the whitespace
    entries = line.split('|') # create a list of each line split on the pipe

    # print(entries)

    salesperson = entries[0] # create a thing called salesperson and set it to the first word in the entries list
    melons = int(entries[2]) # create a thing called melons and set it to the third word in the entries list, made into an integer

    if salesperson in salespeople: # if salesperson is in the salespeople list
        position = salespeople.index(salesperson) # look up their index in the list and save it as position

        melons_sold[position] += melons # add to the number of melons that salesperson has sold

    else: # if the salesperson is not already in the salespeople list
        salespeople.append(salesperson) # add them to the list of salespeople
        melons_sold.append(melons) # add the number of melons sold to the list of melons sold


for i in range(len(salespeople)): # loop over salespeople list
     print(f'{salespeople[i]} sold {melons_sold[i]} melons') # get salesperson's name from salespeople list and number of melons sold from melons_sold list
