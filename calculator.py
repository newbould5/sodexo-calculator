import csv
import sys
import export

file = 'export.csv'
id = sys.argv[1]
amount = 0

with open(file) as csvread:
	read = csv.reader(csvread, delimiter=';')
	next(read)
	for row in read:
		description = row[1]
		if "Transactie" in description:
			identifier = description.split("(Transactie ")[1][:-1]
			if id == identifier:
				break
			amt = row[2][2:-4]
			amount += float(amt)
print("Total amount: " + str(amount))  
