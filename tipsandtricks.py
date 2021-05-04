#Ternary
condition = True

x = 1 if condition else 0

print(x)

#underscores
amount1 = 10_000_000
amount2 = 10_000
total = amount1 + amount2
print(f'{total:,}')

#enumerate
names = ['John', 'Robb', 'Ned', 'Jaime']
for index, name in enumerate(names):
	print(index, name)

#zip
names = ['Tony Stark', 'Peter Parker', 'Steve Rogers', 'Bruce Wayne', 'Clark Kent']
heroes = ['Ironman', 'Spiderman', 'Captain America', 'Batman', 'Superman']
universes = ['Marvel', 'Marvel', 'Marvel', 'DC', 'DC']
for name, hero, universe in zip(names, heroes, universes):
	print(f'{name} is actually {hero} from {universe}')

