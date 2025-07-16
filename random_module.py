import random 

a=random.randint(2,5)
print(a)

b=random.randrange(1,3)
print(b)

c=random.random()
print(c)

d=random.uniform(2,4)
print(d)

l=[76,89,74,24,65]
f=random.choice(l)
random.shuffle(l)

print(l)
print(f)