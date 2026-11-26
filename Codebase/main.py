# Mini E-Commerce System Using Python

# Available Products
products = {
    1: {"name": "Laptop", "price": 45000},
    2: {"name": "Mobile", "price": 15000},
    3: {"name": "Headphones", "price": 1500},
    4: {"name": "Keyboard", "price": 800},
    5: {"name": "Mouse", "price": 500}
}

# Shopping Cart
cart = {}

# Main Menu
while True:

    print("\n===== MINI E-COMMERCE SYSTEM =====")
    print("1. View Products")
    print("2. Add to Cart")
    print("3. View Cart")
    print("4. Remove from Cart")
    print("5. Generate Bill")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # View Products
    if choice == "1":

        print("\n----- Available Products -----")

        for key, value in products.items():
            print(key, value["name"], "- Rs.", value["price"])

    # Add Product to Cart
    elif choice == "2":

        product_id = int(input("Enter Product ID: "))

        if product_id in products:

            quantity = int(input("Enter Quantity: "))

            if quantity > 0:
                if product_id in cart:
                    cart[product_id] += quantity
                else:
                    cart[product_id] = quantity

                print("Product added to cart successfully!")

            else:
                print("Quantity must be greater than zero.")

        else:
            print("Invalid Product ID!")

    # View Cart
    elif choice == "3":

        print("\n----- Your Shopping Cart -----")

        if len(cart) == 0:
            print("Your cart is empty.")

        else:
            total = 0

            for product_id, quantity in cart.items():

                name = products[product_id]["name"]
                price = products[product_id]["price"]

                amount = price * quantity
                total += amount

                print(name, "x", quantity, "= Rs.", amount)

            print("Total Amount: Rs.", total)

    # Remove Product
    elif choice == "4":

        product_id = int(input("Enter Product ID to remove: "))

        if product_id in cart:
            del cart[product_id]
            print("Product removed successfully!")

        else:
            print("Product not found in cart.")

    # Generate Bill
    elif choice == "5":

        if len(cart) == 0:
            print("Your cart is empty.")

        else:
            total = 0

            print("\n======= FINAL BILL =======")

            for product_id, quantity in cart.items():

                name = products[product_id]["name"]
                price = products[product_id]["price"]

                amount = price * quantity
                total += amount

                print(name, "x", quantity, "= Rs.", amount)

            print("--------------------------")
            print("Total Bill: Rs.", total)
            print("Thank you for shopping!")
            print("==========================")

            cart.clear()

    # Exit
    elif choice == "6":

        print("Thank you for visiting our store!")
        break

    else:
        print("Invalid choice! Please try again.")
