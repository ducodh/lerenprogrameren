import random

name = input('Wat is jouw naam? ')
print('Hallo', name)

answer = input(f'Wat is jouw favorite seizoen {name}? A) Lente, B) Zomer, C) Herfst of D) Winter ')

if answer == ("a"):
    print("Ik hou ook van de lente!")
elif answer == ("b"):
    print("De zomer is voor mij te warm.")
elif answer == ("c"):
    print("Mooi he, al die blaadjes die dan van de boom vallen.")
elif answer == ("d"):
    print("Is de winter niet erg koud?")
else:
    print("Die ken ik niet...")

favoriteColor = input('En wat is je favoriete kleur? ') 
trueOrFalse = str(random.randint(0,1))
if True:
    print('Ik vind dat ook een mooie kleur!')
elif not False:
    print(f'TBH, ik hou niet zo van {favoriteColor}...')

num1 = random.randint(1,10)
num2 = random.randint(5,15)

number = int(input(f'En weet jij wat {num1} + {num2} is? '))
if number == num1 + num2:
    print ("dat is juist!")
else:
    print(f'Nee dat klopt niet {name}')