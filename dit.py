def pizza_order_system():

    print("Welcome to DOMINGOES!")

    customer_name = input("Name: ")
    phone_number = input("Phone Number: ")
    delivery_type = input("Pick-up(1) or Delivery(2)? (1/2): ").lower()

    if delivery_type == "2":
        address = input("Enter your delivery address: ")
    else:
        address = "Pick-up"

    pizzas= []
    total_cost = 0

    while True:
        print("\nPizza Options:")
        print("1. Small Pizza ($10)")
        print("2. Medium Pizza ($15)")
        print("3. Large Pizza ($20)")
        print("4. Add a side ($5)")
        print("5. Add a drink ($2)")
        print("6. Finish Order")

        choice = input("Enter your choice: ")

        if choice == "1":
            pizzas.append("Small Pizza")
            total_cost += 10
        elif choice == "2":
            pizzas.append("Medium Pizza")
            total_cost += 15
        elif choice == "3":
            pizzas.append("Large Pizza")
            total_cost += 20
        elif choice == "4":
            pizzas.append("Side")
            total_cost += 5
        elif choice == "5":
            pizzas.append("Drink")
            total_cost += 2
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

    print("\n--- Order Summary ---")
    print(f"Name: {customer_name}")
    print(f"Phone: {phone_number}")
    print(f"Address: {address}")
    print("\nPizzas:")
    for pizza in pizzas:
        print(f"- {pizza}")
    print(f"\nTotal Cost: ${total_cost}")

    print("\nThank you for your order!")

pizza_order_system()   
