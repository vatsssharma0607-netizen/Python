my_tuple = ("Apple", "Banana", "Cherry", "Date")
print("Original Tuple:",{my_tuple})
first_item = my_tuple[0]
last_item = my_tuple[-1]
print("First item:",{first_item})
print("Last item:",{last_item})
temp_list = list(my_tuple)        
temp_list[1] = "Blueberry"        
my_tuple = tuple(temp_list)       
print("Updated Tuple:",{my_tuple})
temp_list = list(my_tuple)
temp_list.pop(0)                  
my_tuple = tuple(temp_list)
print("Tuple after removing one item:",{my_tuple})
del my_tuple
print("Tuple successfully deleted from memory.")
