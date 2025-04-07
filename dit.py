def piza():
    """Set up pizza and topping data."""
    piza = [
        ["Pepperoni", 10, ["Small", "Medium", "Large"]],
        ["Margherita", 8, ["Small", "Medium", "Large"]],
        ["Veggie Deluxe", 12, ["Small", "Medium", "Large"]],
        ["Hawaiian", 11, ["Small", "Medium", "Large"]],
        ["Meat Lovers", 14, ["Small", "Medium", "Large"]],
        ["BBQ Chicken", 13, ["Small", "Medium", "Large"]],
        ["Mushroom & Onion", 9, ["Small", "Medium", "Large"]],
        ["Spinach & Feta", 12, ["Small", "Medium", "Large"]],
        ["Seafood Special", 15, ["Small", "Medium", "Large"]],
        ["Supreme", 13, ["Small", "Medium", "Large"]],
    ]
    sizes = {"Small": 1, "Medium": 3, "Large": 5}   # Size multipliers
    toppings = [
        ["Mushrooms", 1],
        ["Olives", 1],
        ["Extra Cheese", 2],
        ["Onions", 1],
        ["Capsicum",1.5],
        ["Pineapple", 1],
        ["Bacon", 2],
        ["Chicken", 2.5],
        ["Spinach", 1.5],
        ["Seafood Mix", 3],
    ]
    return piza, sizes, toppings


def display_menu(piza, toppings):   # piza, toppings
    """Display the menus."""
    print("Pizza Menu:")
    print("0. To end")
    for i, pizza in enumerate(piza):   # loops through the pizzas
        print(f"{i + 1}. {pizza[0]} - ${pizza[1]:.2f} (Sizes: {', '.join(pizza[2])})")


    print("\nToppings:")
    for i, topping in enumerate(toppings):
        print(f"{i + 1}. {topping[0]} - ${topping[1]:.2f}")

def get_customer_details():
    """Gets tha custmres details,whether they would like to pick up or get tha food delivered ."""
    name = input("Enter your name: ")
    phone = input("Enter your phone number: ")
    address = ""
    delivery_choice = input("Pickup or Delivery? (p/d): ").lower()
    if delivery_choice == "d":
        address = input("Enter your address: ")
    return name, phone, address, delivery_choice

def get_customer_order(piza, toppings):
    """Gets the customer's pizza order."""
    order = []
    while True:
        try:
            piza_choice = int(input("Enter pizza number  (0 to finish): "))
            
            if piza_choice == 0:
                break

            if piza_choice == 11:
                # Custom pizza option
                custom_name = input("Enter name of your custom pizza: ")
                custom_base_price = float(input("Enter base price of your pizza: "))
                custom_pizza = [custom_name, custom_base_price, ["Small", "Medium", "Large"]]
                piza.append(custom_pizza) 
                pizza_index = len(piza) - 1    # last index of the list
            else:
                pizza_index = piza_choice - 1

            selected_pizza = piza[pizza_index]

            size_choice = input(f"Enter size ({', '.join(selected_pizza[2])}): ").capitalize()
            quantity = int(input("Enter quantity: "))

            selected_toppings = []
            while True:
                topping_choice = input("Enter topping number:")
                if topping_choice == "0":
                 break
                else:
                    topping_choice = int(topping_choice)
                topping_index = int(topping_choice) - 1
                selected_toppings.append(toppings[topping_index])   # get the topping from the list

            order.append([selected_pizza, size_choice, quantity, selected_toppings])

        except (ValueError, IndexError):
            print("Invalid input. Try again.")

    return order

def calculate_total_cost(order, sizes):
    """Calculate tha total cost of tha order."""
    total_cost = 0
    for item in order:
        pizza, size, quantity, toppings_list = item
        pizza_price = pizza[1] * sizes[size] * quantity   # pizza price based on size and quantity
        total_toppings_cost = sum(topping[1] for topping in toppings_list) * quantity
        total_cost += pizza_price + total_toppings_cost
    return total_cost

def display_order_summary(order, sizes, name, phone, address, delivery_choice):
    """Display the order summary witvh  customer detail."""
    print("\n----Order Summary----")
    print(f"Name: {name}")
    print(f"Phone: {phone}")
    if delivery_choice == "d":   # if the customer chose delivery prints the address
        print(f"Address: {address}")
        print("Delivery")
    else:
        print("Pickup")

    for item in order:   # loops through the order list
        pizza, size, quantity, toppings_list = item
        pizza_price = pizza[1] * sizes[size] * quantity
        print(f"{quantity} x {size} {pizza[0]} - ${pizza_price:.2f}")

        for topping in toppings_list:
            print(f" + {quantity} x {topping[0]} - ${topping[1] * quantity:.2f}")

    total_cost = calculate_total_cost(order, sizes)   # calculate the total cost of the order
    print(f"Total Cost: ${total_cost:.2f}")
    print("----Thank you for your order!----")

def main():
    """Main function to run the pizza ordering system."""
    pizzas, size, toppings = piza()

    name, phone, address, delivery_choice = get_customer_details()
    display_menu(pizzas, toppings)
    order = get_customer_order(pizzas, toppings)
    display_order_summary(order, size, name, phone, address, delivery_choice)

main()   # run the main function
