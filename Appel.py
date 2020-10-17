user_input = input("Prenoms 'xy', 'xy'")

input_list = user_input.split(',')
numbers = [str(x.strip()) for x in input_list]

def database():
	return ["alexiane", "basile", "carine", "clement", "igor", "louis",  "sarah", "cindy", "roxane", "marco", "louis", "jean-baptiste", "ilona", "adrien"]

def filterdatabase(names):
	for name in database():
		if name[:2] not in names:
			yield name
g = list(filterdatabase(numbers))

print(g)