import random
bilhete = ""
for i in range(6):
    num = random.randint(1,60)
    if i == 5:
        bilhete += f"{num}"
    else:
        bilhete += f"{num} - "
    
print(bilhete)
    