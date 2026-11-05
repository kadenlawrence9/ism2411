# Exercise 1: Build the list

inventory = ["pen", "notebook", "stapler", "tape", "marker"]

print(inventory)
print(len(inventory))

print(inventory[0])
print(inventory[-1])
print(inventory[len(inventory) // 2])

print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])

inventory.append("envelope")
print(inventory)
inventory.remove("tape")
print(inventory)
inventory.sort()
print(inventory)

coords = (40.7128, -74.0060)
print(coords)

try:
    coords[0] = 99
except TypeError:
    print("Tuples cannot be changed because they are immutable.")

print(coords)

sales = [100, 250, 75, 480, 200]

total = sum(sales)
print("Total:", total)

count = len(sales)
print("Count:", count)

average = total / count
print("Average:", average)

print("Best:", max(sales))
print("Worst:", min(sales))

prices = [9.99, 14.99, 4.99, 24.99, 1.99]

discounted = []

for price in prices:
    new_price = round(price * 0.90, 2)
    discounted.append(new_price)

print("Original:", prices)
print("Discounted:", discounted)

sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]

high_sales = []

for sale in sales:
    if sale > 300:
        high_sales.append(sale)

print("High sales:", high_sales)
print("Count:", len(high_sales))
print("Average:", round(sum(high_sales) / len(high_sales), 2))

# Reflection 1: The most surprising thing about Python lists was how
# easy it is to add, remove, and organize items. I also learned that
# Python starts counting list positions at zero.
#
# Reflection 2: A Python list could save time in a business by organizing
# daily sales numbers and calculating totals and averages automatically.
# This would be faster than entering and calculating everything manually in Excel.