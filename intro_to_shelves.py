import shelve

blt = ["bacon", "lettuce", "tomato", "bread"]
beans_on_toast = ["beans", "bread"]
scrambled_eggs = ["eggs", "butter", "milk"]
soup = ["tin of soup"]
pasta = ["pasta", "cheese"]

with shelve.open("recipes") as recipes:
    recipes["blt"] = blt
    recipes["beans on toast"] = beans_on_toast
    recipes["scrambled eggs"] = scrambled_eggs
    recipes["soup"] = soup
    recipes["pasta"] = pasta

    for snack in recipes:
        print(snack, recipes[snack])

print("========== Example 2 ==========")

books = {"recipes": {"blt": ["bacon", "lettuce", "tomato", "bread"],
                     "beans_on_toast": ["beans", "bread"],
                     "scrambled_eggs": ["tin of soup"],
                     "pasta": ["pasta", "cheese"]},
         "maintenance": {"stuck": ["oil"],
                         "loose": ["gaffer tape"]}}
