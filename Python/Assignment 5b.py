mytuple = (10, 20, 30, 20, 40, 50, 30, 60, 20, 70, 80)
seen = []
repeated = []
for item in mytuple:
    if item in seen and item not in repeated:
        repeated.append(item)
    else:
        seen.append(item)
print("Original Tuple:",mytuple)
print("Repeated Items:",repeated)
