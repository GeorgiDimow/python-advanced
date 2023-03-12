def shop_from_grocery_list(budget, grocery_list, *products_info):

    for products_name, products_price in products_info:
        if products_name in grocery_list:
            if products_price <= budget:
                grocery_list.remove(products_name)
                budget -= products_price
            else:
                break

    if not grocery_list:
        return f"Shopping is successful. Remaining budget: {'%.2f' % budget}."

    return f"You did not buy all the products. Missing products: {', '.join(grocery_list)}."


print(shop_from_grocery_list(
    100,
    ["tomato", "cola"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("tomato", 20.45),
))


