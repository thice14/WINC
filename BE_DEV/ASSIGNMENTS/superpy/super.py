# Imports
import argparse
import csv
import datetime
import os

#import timing
#import time_advancer


# from datetime import datetime

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.
def main():
    pass

wd = os.getcwd()
bought_path = os.path.join(wd, 'bought.csv')
sold_path = os.path.join(wd, 'sold.csv')

parser = argparse.ArgumentParser(
    prog='SuperPy',
    description="A command-line tool to register, track, and report your purchases, sales and inventory.",
    epilog='Thank you for using %(prog)s!'
)

sub_parser = parser.add_subparsers(dest="action", help="Buy, Sell, or Report")

buy_parser = sub_parser.add_parser("buy", help="Register a purchase")
buy_parser.add_argument("product_name", type=str, help="Enter the name of the product")
buy_parser.add_argument("quantity", type=int, help="Enter the quantity of the product bought")
buy_parser.add_argument("buy_price_pu", type=float, help="Enter the purchase price per unit")
buy_parser.add_argument(
    "buy_date",
    type=lambda s: datetime.datetime.strptime(s, '%Y-%m-%d').date(),
    help="Enter the date of the purchase. YYYY-MM-DD (e.g. 2022-12-19)")
buy_parser.add_argument(
    "expiration_date",
    type=lambda s: datetime.datetime.strptime(s, '%Y-%m-%d').date(),
    help="Enter the expiration date of the product. YYYY-MM-DD (e.g. 2023-02-19)")

sell_parser = sub_parser.add_parser("sell", help="Register a sale")
sell_parser.add_argument("product_name", type=str, help="Enter the name of the product")
sell_parser.add_argument("quantity", type=int, help="Enter the quantity of the product sold")
sell_parser.add_argument("sell_price_pu", type=float, help="Enter the selling price per unit")
sell_parser.add_argument(
    "sell_date",
    type=lambda s: datetime.datetime.strptime(s, '%Y-%m-%d').date(),
    help="Enter the date of the sale. YYYY-MM-DD (e.g. 2022-12-19)")

report_parser = sub_parser.add_parser("report", help="Create a report")

args = parser.parse_args()

if args.action == "buy":
    if os.path.exists(bought_path):
        pass
    else:
        with open('bought.csv', 'w+') as file:
            bought_file = csv.DictWriter(
                file, 
                fieldnames = ["Buy_ID","Product_Name","Quantity","Unit_Price",
                "Total_Price","Buy_Date","Expiration_Date"], 
                delimiter = ';')
            bought_file.writeheader()

    with open('bought.csv', 'a') as file:
        bought_file = csv.writer(file, delimiter = ";")
        bought_rowcount = 0
        for row in open("bought.csv"):
            bought_rowcount += 1
        buy_id = "B" + str(bought_rowcount)
        buy_product_name = args.product_name
        buy_quantity = args.quantity
        buy_price_pu = args.buy_price_pu
        buy_price_total = args.quantity * args.buy_price_pu
        buy_date = args.buy_date
        expiration_date = args.expiration_date
        bought_file.writerow([buy_id, buy_product_name, buy_quantity, buy_price_pu, buy_price_total, buy_date, expiration_date])
    print("Purchase successfully registered!")

if args.action == "sell":
    if os.path.exists(sold_path):
        pass
    else:
        with open('sold.csv', 'w+') as file:
            sold_file = csv.DictWriter(file, fieldnames = ["Sell_ID", "Product_Name","Quantity","Unit_Price","Total_Price","Sell_Date"], delimiter = ';')
            sold_file.writeheader()
    
    with open('sold.csv', 'a') as file:
        sold_file = csv.writer(file)
        sold_rowcount = 0
        for row in open("sold.csv"):
            sold_rowcount += 1
        sell_id = "S" + str(sold_rowcount)
        sell_product_name = args.product_name
        sell_quantity = args.quantity
        sell_price_pu = args.sell_price_pu
        sell_price_total = args.quantity * args.sell_price_pu
        sell_date = args.sell_date
        sold_file.writerow([sell_id, sell_product_name, sell_quantity, sell_price_pu, sell_price_total, sell_date])    
    print("Sale successfully registered!")


if __name__ == "__main__":
    main()
