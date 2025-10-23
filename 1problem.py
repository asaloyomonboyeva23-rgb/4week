def calculate_item_total(quantity, unit_price):
     return quantity * unit_price 
def apply_bulk_discount(total, quantity):
     if quantity >= 10:
          return 0.1 *(total)
     elif quantity >= 5:
          return 0.05 *(total)
     else:
          return 0
def  calculate_tax(subtotal, tax_rate):
     return (subtotal * tax_rate /100)
def  is_eligible_for_free_shipping(subtotal):
     return subtotal >=50
def  process_order(item_name, quantity, unit_price, tax_rate):
     print (f"Order Receipt for:{item_name}")
     print (f"Quantity: {quantity}@ ${round(unit_price, 2)} each")


     item_total = calculate_item_total(quantity, unit_price)
     print (f" Item Total: ${item_total}")
     bulk_discount = apply_bulk_discount(item_total, quantity)
     print (f"Bulk Discount: -$ {bulk_discount:.2f}")
     subtotal = item_total -bulk_discount
     print(f" Subtotal: ${subtotal:.2f}")
     tax = calculate_tax(subtotal, tax_rate)
     print(f" Tax ({tax_rate})%: ${tax:.2f}")
     final_total = subtotal +tax
     print(f"Final Total: ${final_total:.2f} ")
     if is_eligible_for_free_shipping(subtotal):
          print("eligible_for_free_shipping")
     else :
          need_for_free_shipping = 50- subtotal
          print(f"need {need_for_free_shipping :.2f} more for free shipping")
print(process_order("notebooks", 12, 3.5 ,8))
s


   