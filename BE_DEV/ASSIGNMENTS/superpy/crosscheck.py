"""import csv
import os"""

"""wd = os.getcwd()
bought_path = os.path.join(wd, 'bought.csv')

# def data_finder(name):
    # csv_reader = csv.reader(bought_path)

with open('bought.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for line in csv_file:
        if line_count == 0:
            # print(f'Column names are {" ".join(line)}')
            print(line)
            line_count += 1
        else:
            print(f'\tOf {line[1]} were {line[2]} units bought for €{line[3]} per unit and €{line[4]} in total, on {line[5]}.')
            print(line)
            line_count += 1
    print(f'Processed {line_count} lines.')"""

"""if name in line:
                print("Product found!")
                pass
            else:
                print('Product not found!')"""

# print(data_finder('apples'))

import csv

"""with open('bought.csv', newline='') as csvfile:
    filereader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in filereader:
        print(', '.join(row))
"""

with open('bought.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=";")
    for row in reader:
        print(row['Product_Name'], row['Quantity'])

"""def main():
    pass

all_objects = []

class Product:
    def __init__(self, product_id, product_name):
        self.id = product_id
        self.name = product_name


with open('bought.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')
    next(reader, None)
    for each in reader:
        product_id = each[0]
        product_name= each[1]
        product = Product(product_id=product_id, product_name=product_name)
        all_objects.append(product)

    for each in all_objects:
        print(each.id, each.name)

if __name__ == "__main__":
    main()"""