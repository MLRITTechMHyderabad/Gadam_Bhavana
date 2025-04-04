
customers = [
    {"name": "Emma", "age": 22, "total_purchase": 150.0},
    {"name": "John", "age": 30, "total_purchase": 200.0},
    {"name": "Grace", "age": 45, "total_purchase": 180.0}
]

# to check if a customer is eligible for a discount
def is_eligible(customer):
    return customer["age"] <= 40  # Only customers aged 40 or below are eligible

# apply the discount based on age
def apply_discount(customer):
    if 18 <= customer["age"] <= 25:
        discount_rate = 0.90  # 10% discount
    elif 26 <= customer["age"] <= 40:
        discount_rate = 0.95  # 5% discount
    else:
        discount_rate = 1.0  # No discount 
    return {
        "name": customer["name"],
        "age": customer["age"],
        "total_purchase": round(customer["total_purchase"] * discount_rate, 2)
    }

# eligible for a discount
eligible_customers = filter(is_eligible, customers)

# using map()
discounted_customers = list(map(apply_discount, eligible_customers))

print(discounted_customers)

