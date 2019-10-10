import csv
import sys
import export

file = 'export.csv'
id = sys.argv[1]
amount = 0

with open(file) as csvread:
	read = csv.reader(csvread, delimiter=';')
	next(read)
	hasRead = False
	for row in read:
		description = row[1]
		if "Transactie" in description:
			identifier = description.split("(Transactie ")[1][:-1]
			if hasRead == False:
				print("Last transaction is now: " + identifier + ", Remember this!")
			if id == identifier:
				break
			amt = row[2][2:-4]
			amount += float(amt)
		hasRead = True
print("Total amount: " + str(amount))  
