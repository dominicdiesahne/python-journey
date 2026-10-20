# Apply Discount Function from FreeCodeCamp.org
def apply_discount(price, discount): 
    if not isinstance(price, (int, float)): 
        return 'The price should be a number'
    if not isinstance(discount, (int, float)):
        return 'The discount should be a number'
    if price <= 0:
        return 'The price should be greater than 0'
    if discount < 0 or discount > 100: 
        return 'The discount should be between 0 and 100'
    if isinstance(price, (int, float)) and isinstance(discount, (int, float)): 
        discount /= 100
        discount = 1 - discount
        return price * discount

print(apply_discount(100, 20))
print(apply_discount(50, 0))
    