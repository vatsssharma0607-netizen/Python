fruits = ["Apple", "Banana", "Cherry", "Date"]
print("Original list:",fruits)
first_fruit = fruits[0]
third_fruit = fruits[2]
print("First item:",{first_fruit})
print("Third item:",{third_fruit})
fruits[1] = "Blueberry" 
print("Updated list (Banana changed to Blueberry):",fruits)
fruits.remove("Date")
print("After removing 'Date':",fruits)
del fruits[0]
print("After deleting index 0:",fruits)
del fruits
print("List 'fruits' has been successfully deleted.")
