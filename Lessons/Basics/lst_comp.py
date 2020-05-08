# list comprehensions
#temps = [221, 234, 348, 238]
#new_temps = [temp / 10 for temp in temps]
#print(new_temps)

# list comps with if statements
#temps = [221, 234, 348, -9999, 230]
#new_temps = [temp/10 for temp in temps if temp != -9999]
#print(new_temps)

# list comps with if-else
temps = [221, 234, 348, -9999, 230]
new_temps = [temp/10 if temp != -9999 else 0 for temp in temps]
print(new_temps)
