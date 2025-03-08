from datetime import datetime

def calculate_discount(subtotal, day_of_week):
    discount = 0
    if day_of_week in [1, 2] and subtotal >= 50:  # Tuesday (1) or Wednesday (2)
        discount = subtotal * 0.10
    return discount

def calculate_sales_tax(subtotal, tax_rate=0.06):
    return subtotal * tax_rate

def main():
    try:
        subtotal = float(input("Please enter the subtotal: "))
        if subtotal < 0:
            print("Subtotal cannot be negative.")
            return
        
        current_date_and_time = datetime.now()
        day_of_week = current_date_and_time.weekday()
        
        discount = calculate_discount(subtotal, day_of_week)
        subtotal_after_discount = subtotal - discount
        sales_tax = calculate_sales_tax(subtotal_after_discount)
        total = subtotal_after_discount + sales_tax
        
        if discount > 0:
            print(f"Discount amount: {discount:.2f}")
        print(f"Sales tax amount: {sales_tax:.2f}")
        print(f"Total: {total:.2f}")
        
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

if __name__ == "__main__":
    main()