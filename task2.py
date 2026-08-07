#---------------------------Task 2--------------------------

import csv
sales = {}
try:
    with open("sales.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            product = row["Product"]
            quantity = int(row["Quantity"])
            price = float(row["UnitPrice"])

            total = quantity * price

            if product in sales:
                sales[product] += total
            else:
                sales[product] = total

    print("\n Sales Summary")
    print("-" * 30)

    for product, total in sales.items():
        print(f"{product}: {total}")

    top_product = max(sales, key=sales.get)

    print("\nTop Selling Product:", top_product)
    print("Total Sales:", sales[top_product])

    with open("sales_summary.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["Product", "Total Sales"])

        for product, total in sales.items():
            writer.writerow([product, total])

    print("\nSummary exported to sales_summary.csv")

except FileNotFoundError:
    print("Error: sales.csv file not found.")

except Exception as e:
    print("Something went wrong:", e)

    