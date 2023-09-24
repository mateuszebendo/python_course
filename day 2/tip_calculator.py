print("Welcome to the tip calculator.")
bill = input("What was the total bill ? $")
pctg = input("What percentage tip would you like to give: 10, 12 or 15 ?")
split = input("How many peolple to split the bill ? ")

result = (float(bill) + float(bill)*(float(pctg)/100))/float(split)
total = round(result, 2)

print(f"Each person should pay: ${total}")