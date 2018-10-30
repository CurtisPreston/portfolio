import random

print("Curtis Preston")
print("16453897")
print()

main_ingredient = ['chocolate', 'banana', 'salted caramel', 'carrot', 'bran']
baking = ['cake', 'brownie', 'cupcake', 'muffin']
measure =['tbsp', 'tsp', 'cup', 'mls']
ingredient = ['flour', 'baking powder', 'butter', 'milk', 'eggs', 'vanilla', 'sugar']
inRecipe = []
for x in range(0,5):
    inRecipe.append(random.choice(ingredient))
main=random.choice(main_ingredient)
baking_type=random.choice(baking)



print("""*** """+main+""" """+baking_type+""" Recipe ***
Ingredients:""")
print(str(random.randint(1,3))+" "+str(random.choice(measure))+" "+main)

for x in range(0,len(inRecipe)):
    print(str(random.randint(1,3))+" "+str(random.choice(measure))+" "+inRecipe[x])


print("method:")
print("Mix the ", end="")
for x in range(0,len(inRecipe)-1):
    print(inRecipe[x]+" ", end="")
print("and")
print()
print(inRecipe[len(inRecipe)-1]+" together.")
print("Gently fold in the "+main)
print("Place mixture in"+baking_type+"tin and bake at "+str(random.randint(170,220))+" degrees Celsius for")
print("*"*46)