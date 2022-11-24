from transaction import read_transactions, pretty_print_transaction

if __name__ == '__main__':
    # Prompt user to enter a CSV fie name
    file_name = input('Please enter a file name (default: transactions.csv) > ')
    if not file_name:
        file_name = 'transactions.csv'

    # Read transactions from the file and pretty print them
    transactions = read_transactions(file_name)
    for transaction in transactions:
        pretty_print_transaction(transaction)