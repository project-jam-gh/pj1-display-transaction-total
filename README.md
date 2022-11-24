# PJ1 - Display transaction total given a list of transactions

![easy](https://badgen.net/badge/Difficulty/Easy/green)

Technologies: Python 3

## Description

Currently we have a program that read a list of transactions from a CSV file, and shows them in a pretty format
within the terminal. We want to add a functionality where we can also display the total for all transactions at the end.

## Get Started

// TODO: Add more clear instructions.

To get started, first fork this repository. After forking the repository, you would want to work within a separate branch.

## Run the Project

To run the project, you can simply use the command:

```
python3 app.py
```

Once the project is running, you can give a `.csv` file containing transactions, by default, the program will use `transactions.csv` file.

Sample output:

```
Please enter a file name (default: transactions.csv) >
2022/11/24 Starbucks Amount: -10.96
2022/11/30 Rent Amount: -2600
2022/12/01 Income Amount: 1211.09
2022/12/01 Grocery Amount: 158.1
```

## Requirements

- After running `app.py` and specifying a CSV file, user should be able to see the transaction total in addition to all transaction details.
- No unit tests required.
