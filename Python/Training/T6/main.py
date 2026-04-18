def build_inventory_report(inventory, delivered_item, delivered_amount):
    total_item = 0
    report = "Inventory Report\n"
    if delivered_item in inventory:
            inventory[delivered_item] += delivered_amount

    if delivered_item not in inventory:
            inventory[delivered_item]  = delivered_amount
            
    for item in inventory:
        
        test = inventory[item]
        total_item += test
        report += (f"- {item}: {test}\n")


    report += (f"Total items: {total_item}")

    return report














"""
Inventory Report
Complete the build_inventory_report function.

It should:

Take an inventory dictionary where each key is an item name and each value is its quantity
Add the delivered amount to the given item
If the item is already in the dictionary, increase its quantity
If the item is not in the dictionary, add it
Return a multi-line string report
The report must include:

A first line: Inventory Report
One line per item in the dictionary in this format: - item_name: quantity
A last line showing the total of all quantities: Total items: total
Use the dictionary's normal iteration order.

Example:

inventory = {
    "apples": 3,
    "bread": 2,
}

print(build_inventory_report(inventory, "apples", 1))

Output:

Inventory Report
- apples: 4
- bread: 2
Total items: 6

Another example:

inventory = {
    "carrots": 5,
}

print(build_inventory_report(inventory, "milk", 2))

Output:

Inventory Report
- carrots: 5
- milk: 2
Total items: 7

"""