from inventory import Inventory
from models.electronics import Electronics
from models.grocery import Grocery
from models.clothing import Clothing

def menu():
    print("\nInventory Menu:")
    print("1. Add Product")
    print("2. Sell Product")
    print("3. View All Products")
    print("4. Search Product")
    print("5. Restock Product")
    print("6. Remove Expired (Groceries)")
    print("7. Total Inventory Value")
    print("8. Save Inventory")
    print("9. Load Inventory")
    print("0. Exit")

inv = Inventory()

while True:
    menu()
    choice = input("Select: ")

    if choice == '1':
        type_ = input("Type (electronics/grocery/clothing): ").lower()
        pid = input("ID: ")
        name = input("Name: ")
        price = float(input("Price: "))
        qty = int(input("Stock Quantity: "))

        if type_ == "electronics":
            brand = input("Brand: ")
            warranty = int(input("Warranty Years: "))
            p = Electronics(pid, name, price, qty, brand, warranty)
        elif type_ == "grocery":
            expiry = input("Expiry Date (YYYY-MM-DD): ")
            p = Grocery(pid, name, price, qty, expiry)
        elif type_ == "clothing":
            size = input("Size: ")
            material = input("Material: ")
            p = Clothing(pid, name, price, qty, size, material)
        else:
            print("Invalid type.")
            continue

        try:
            inv.add_product(p)
            print("Product added!")
        except Exception as e:
            print("Error:", e)

    elif choice == '2':
        pid = input("Product ID: ")
        qty = int(input("Quantity: "))
        try:
            inv.sell_product(pid, qty)
            print("Product sold.")
        except Exception as e:
            print("Error:", e)

    elif choice == '3':
        for item in inv.list_all_products():
            print(item)

    elif choice == '4':
        keyword = input("Name or Type: ")
        result = inv.search_by_name(keyword) + inv.search_by_type(keyword)
        for r in result:
            print(r)

    elif choice == '5':
        pid = input("Product ID: ")
        qty = int(input("Restock Quantity: "))
        inv.restock_product(pid, qty)
        print("Restocked.")

    elif choice == '6':
        inv.remove_expired_products()
        print("Expired groceries removed.")

    elif choice == '7':
        print("Total Value: $", inv.total_inventory_value())

    elif choice == '8':
        inv.save_to_file("inventory_data.json")
        print("Saved to file.")

    elif choice == '9':
        try:
            inv.load_from_file("inventory_data.json")
            print("Loaded from file.")
        except Exception as e:
            print("Load error:", e)

    elif choice == '0':
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
