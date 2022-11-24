# PJ1 - Display transaction total given a list of transactions

![easy](https://badgen.net/badge/Difficulty/Easy/green)

Technologies: Python 3

## Description

Currently we have a program that read a list of transactions from a CSV file, and shows them in a pretty format
within the terminal. We want to add a functionality where we can also display the total for all transactions at the end.

## Get Started

To get started, first create a new repository in your account using this template.

![](https://i.imgur.com/mO49do2.png)

Then, create a new branch for your solution, you may call this anything, usually, we just call the branch: `solution`.

![](https://i.imgur.com/fbMVtun.png)

Push your solution to this branch, when you are ready, create a new pull request and add `project-jam-admin` as a reviewer.

![](https://i.imgur.com/1xdAjFG.png)

If you don't hear back within 24 hours, ping the admin on Discord channel. Once your PR is approved, your profile will have have this issue marked as fixed!

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
