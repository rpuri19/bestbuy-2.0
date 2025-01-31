import products
import store

def menu_display():
    """
    Displays the main menu of the store with various options for the user.
    """
    menu = {
        1: "List all products in store",
        2: "Show total amount",
        3: "Make an Order",
        4: "Quit"
    }
    print("\nStore Menu:")
    print("----------")
    for key, value in menu.items():
        print(f"{key} : {value}")


def start():
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
    ]
    best_buy = store.Store(product_list)  # Initialize store with list of products

    while True:
        menu_display()
        user_input = input("\nPlease choose a number: ")

        if user_input == "1":
            list_all_products(best_buy)
        elif user_input == "2":
            show_total_amount(best_buy)
        elif user_input == "3":
            make_an_order(best_buy)
        elif user_input == "4":
            break
        else:
            print("Invalid Input")


def list_all_products(store_list):
    """
    Fetches and displays all products currently in the store.
    """
    list_of_items = store_list.get_all_products()

    for index, product in enumerate(list_of_items):
        print(f"{index + 1}. {product}")

def show_total_amount(store_list):
    """
    Displays the total quantity of all items available in the store.
    """
    number_of_items_in_store = store_list.get_total_quantity()
    print (f"Total of {number_of_items_in_store} items in store.")


def order_inputs():
    """
    Prompts the user for their product and quantity selections for an order.
    The user can finish entering products by submitting an empty input.
    """
    inputs_from_user = []
    print("When you want to finish order, enter empty text.")
    while True:
        product_id = input("Which product # do you want? ")
        if not product_id:
            break
        if not product_id.isdigit():
            print("Product # should be a number.")
            continue
        number_of_items = input("What amount do you want? ")
        if not number_of_items:
            break
        if not number_of_items.isdigit():
            print("Amount should be a number")
            continue

        inputs_from_user.append((int(product_id), int(number_of_items)))

    return inputs_from_user

def make_an_order(best_buy):
    """
    Processes the order based on user inputs and calculates the total price.
    """
    tuples_for_orderid_and_number = order_inputs()

    try:
        total_price = best_buy.order(tuples_for_orderid_and_number)
        print(f"\nMessage / Total Amount: {total_price}\n")
    except ValueError:
        print("Error accepting order. Please retry.")


if __name__ == "__main__":
    start()
