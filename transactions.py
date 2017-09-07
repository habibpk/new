import csv

def csv_data(path):
    with open(path) as csv_file:
        readCSV = csv.DictReader(csv_file)

        for line in readCSV:
            col_from = line['from']
            col_to = line['to']
            col_ammount = line['amount']
            from_amount = int(float(col_ammount.lstrip('$').replace(',', ''))) - int(
                float(col_ammount.lstrip('$').replace(',', '')))
            to_amount = 0 + int(float(col_ammount.lstrip('$').replace(',', '')))
            print(col_from, '$'+str(from_amount), col_to, '$'+str(to_amount))





