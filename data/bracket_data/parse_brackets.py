import json
import os



def read_bracket(year: int):
	filename = f"{year}.json"

	if os.path.exists(filename):
		with open(filename, 'r') as file:
			bracket_data = json.load(file)

		return bracket_data

	else:
		print(f"No data found for {year}")
		return None


def write_brackets(start_year: int, end_year: int):
	brackets = {}

	for year in range(start_year, end_year + 1):
		bracket_data = read_bracket(year)

		if bracket_data:
			brackets[year] = bracket_data

	return brackets


brackets = json.dumps(write_brackets(1985, 2018), indent=4)
with open("../brackets.json", 'w') as out:
	out.write(brackets)

print("Combined brackets JSON saved to brackets.json")

