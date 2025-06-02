from prettytable import PrettyTable

table = PrettyTable()


table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmandar", "Bulbasaur", "Togepi", "Chigurita"], 'l')
table.add_column("Type", ["Electric", "Water", "Fire", "Grass", "Special", "Grass"], 'r')
print(table)