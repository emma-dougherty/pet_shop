# WRITE YOUR FUNCTIONS HERE
#Q1
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

#Q2
def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

#Q3-Q4
# def add_or_remove_cash(amount, cash):
#     get_total_cash(amount)
#     if cash > 0 or cash < 0:
#        amount["admin"]["total_cash"] += cash
#     return amount

def add_or_remove_cash(pet_shop, amount):
    pet_shop["admin"]["total_cash"] += amount

#Q5
def get_pets_sold(pets_sold):
    return pets_sold["admin"]["pets_sold"]

#Q6  
def increase_pets_sold(pet_shop, sale):
    pet_shop["admin"]["pets_sold"] += sale

#Q7
def get_stock_count(total_pets):
    return len(total_pets["pets"])

#Q8 - #Q9
def get_pets_by_breed(pet_shop, breed):
    pets = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            pets.append(pet)
    return pets

#Q10-11
def find_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            return pet
#Q12
def remove_pet_by_name(pet_shop, name):
      for pet in pet_shop["pets"]:
        if pet["name"] == name:
                pet_shop["pets"].remove(pet)

#Q13
def add_pet_to_stock(pet_shop, new_pet):
    # stock = len(pet_shop["pets"])
    pet_shop["pets"].append(new_pet)
    # return stock

#Q14
def get_customer_cash(customer):
    return customer["cash"]

#Q15
def remove_customer_cash (customer, spent_cash):
    customer["cash"] -= spent_cash
    # return customer["cash"]

#Q16
def get_customer_pet_count(customer):
    return len(customer["pets"])

#Q17
def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)
    return len(customer["pets"])

#Q18 - Q19 - Q20
def customer_can_afford_pet(customer, new_pet):
    if new_pet["price"] <= customer["cash"]:
        return True
    else:
        return False

# I realise this is not correct as it does not work for all intgration tests.
#  
# For  Q21 it does not deduct pet price from from customer cash and add it to shop total cash.
#
#It works for Q22 - 23

def sell_pet_to_customer(pet_shop, pet, customer):
   for pet in pet_shop["pets"]:
       if pet["name"] == pet and customer["cash"] >= pet["price"]:
            # pet_shop["admin"]["pets_sold"] += pet
            # pet_shop["admin"]["total_cash"] += pet["price"]
            # customer["cash"] -= pet["price"]
            # customer["pets"].append(pet)


            
            # pet_shop["admin"]["pets_sold"] += pet
            # customer["cash"] -= pet["price"]
            # pet_shop["admin"]["total_cash"] += pet["price"]
            # customer["pets"].append(pet)


            remove_pet_by_name(pet_shop, pet["name"])
            add_or_remove_cash(pet_shop, pet["price"])
            remove_customer_cash (customer, pet["price"])
            add_pet_to_customer(customer, pet["name"])
            increase_pets_sold(pet_shop, 1)