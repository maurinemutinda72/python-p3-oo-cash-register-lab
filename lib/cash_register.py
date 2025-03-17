class CashRegister:
    def __init__(self, discount=0):
        """Initialize the cash register with an optional discount."""
        self.discount = discount  # Discount percentage (e.g., 20 for 20%)
        self.total = 0  # Running total
        self.items = []  # List of item titles
        self.last_transaction = None  # Store (amount, quantity) of last transaction

    def add_item(self, title, price, quantity=1):
        """Add an item to the register with price and optional quantity."""
        transaction_amount = price * quantity
        self.total += transaction_amount
        self.last_transaction = (transaction_amount, quantity)  # Store amount and quantity
        # Add the item title to the list, repeated by quantity
        for _ in range(quantity):
            self.items.append(title)

    def apply_discount(self):
        """Apply the discount to the total and print a message."""
        if self.discount == 0:
            print("There is no discount to apply.")
        else:
            discount_amount = (self.discount / 100) * self.total
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${int(self.total)}.")

    def get_items(self):
        """Return the list of items."""
        return self.items

    def void_last_transaction(self):
        """Remove the last transaction from the total and items."""
        if not self.items or not self.last_transaction:
            self.total = 0  # Reset to 0 if no transactions
            return
        # Subtract last transaction amount from total
        amount, quantity = self.last_transaction
        self.total -= amount
        # Remove the last 'quantity' items from the list
        self.items = self.items[:-quantity]
        self.last_transaction = None  # Clear last transaction