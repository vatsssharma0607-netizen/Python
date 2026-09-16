set1 = {"Apple", "Banana", "Cherry"}
print("Initial set:",set1)
print("Is 'Apple' in the set?",'Apple' in set1)
print("Looping through set items:")
for fruit in set1:
    print("-",fruit)
set1.add("Dragonfruit")
set1.update(["Elderberry", "Fig"])
print("Updated set:",set1)
set1.remove("Banana") 
set1.discard("Grapes")
print("Set after deletions:",set1)
set1.clear()
print("Set after clearing:",set1)
