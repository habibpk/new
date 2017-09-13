import csv
import argparse

parser = argparse.ArgumentParser(description='Calculate values from a csv file')
parser.add_argument("path", type=str, help='Transactions amounts')
args = parser.parse_args()

def csv_data(path):

        accounts = {}  

        with open(path) as csv_file:
            readCSV = csv.DictReader(csv_file)

            for line in readCSV:
                account_from = int(line['from'])
                account_to = int(line['to'])
                transaction = line['amount']
                transaction_amount = int(float(transaction.lstrip('$').replace(',', '')))

               
                if account_from in accounts:
                    accounts[account_from] -= transaction_amount
                else:
                    accounts[account_from] = (0-transaction_amount)

                
                if account_to in accounts:
                    accounts[account_to] += transaction_amount
                else:
                    accounts[account_to] = transaction_amount

        for account in accounts:
            print("{}: \t{}".format(account, accounts[account]))

csv_data(args.path)





