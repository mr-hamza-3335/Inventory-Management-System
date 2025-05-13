# 🛒 Inventory Management System (Python OOP)

A simple yet robust Inventory Management System built using Python and Object-Oriented Programming (OOP) principles.

This project manages different types of products like Electronics, Groceries, and Clothing — each with unique attributes and behaviors. The system supports stock operations, sales, data persistence using JSON, and includes a user-friendly command-line interface (CLI).

---

## 🚀 Features

- Add, Sell, and Restock Products
- Search by product name or type
- List all available products
- Automatically remove expired groceries
- Calculate total inventory value
- Save and Load inventory data (JSON)
- Custom exception handling
- CLI-based user interaction

---

## 🧱 Technologies Used

- Python 3.x
- Object-Oriented Programming (OOP)
- `abc` module for abstract base classes
- `json` for file handling
- Command-line interface

---

## 📂 Project Structure

InventorySystem/
│
├── main.py # CLI interface
├── inventory.py # Inventory management logic
├── custom_exceptions.py # Custom exception classes
│
├── models/
│ ├── product.py # Abstract base class
│ ├── electronics.py # Electronics subclass
│ ├── grocery.py # Grocery subclass
│ └── clothing.py # Clothing subclass

yaml
Copy
Edit

---

## ▶️ How to Run

1. Clone or download the project
2. Make sure you have Python installed
3. Open terminal / command prompt
4. Navigate to the project folder
5. Run the program:

```bash
python main.py
📸 Sample CLI Menu
markdown
Copy
Edit
1. Add Product
2. Sell Product
3. View Products
4. Search Product
5. Restock Product
6. Remove Expired
7. Inventory Value
8. Save to File
9. Load from File
0. Exit
✅ Sample Product Types
🖥 Electronics
ID, Name, Price, Stock

Brand, Warranty Years

🥦 Grocery
ID, Name, Price, Stock

Expiry Date

Checks if product is expired

👕 Clothing
ID, Name, Price, Stock

Size, Material

📌 Notes
Data is saved to inventory_data.json

Expired groceries are removed via menu option

Custom errors for:

Duplicate product IDs

Out-of-stock sales

Invalid product types
