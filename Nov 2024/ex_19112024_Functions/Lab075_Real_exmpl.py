"""
Pizza

toppings - paneer, corn, olive, tomato, onion, capsicum
"""

def make_pizza(*toppings):
    # for i in toppings: # - It will display as list
    #     print(i)
        print(toppings) # - It will display as tuple, will discuss tuple later

User1=make_pizza("onioon", "capsicum", "paneer")
User2=make_pizza("onioon", "capsicum", )
User3=make_pizza("tomato", "olive")
User4=make_pizza("corn")