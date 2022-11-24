import csv

# Read transactions from a CSV file
def read_transactions(file_name):
    with open(file_name, 'r') as file:
        # Create a csv reader object that reads from the file as dict
        # Dict keys are the first row of the file
        csv_reader = csv.DictReader(file, delimiter=',')
        # Return a list of dicts
        transactions = []
        for row in csv_reader:
            transactions.append(row)
        return transactions

def pretty_print_transaction(transaction):
    print(f'{transaction["date"]} {transaction["vendor"]} Amount: {transaction["amount"]}')