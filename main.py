# This is a sample Python script.

# Press âŒƒR to execute it or replace it with your code.
# Press Double â‡§ to search everywhere for classes, files, tool windows, actions, and settings.
numbers = {
	"0": [
		" _ ",
		"| |",
		"|_|"
	],
	"1": [
		"   ",
		"  |",
		"  |"
	],
	"2": [
		" _ ",
		" _|",
		"|_ "
	],
	"3": [
		" _ ",
		" _|",
		" _|"
	],
	"4": [
		"   ",
		"|_|",
		"  |"
	],
	"5": [
		" _ ",
		"|_ ",
		" _|"
	],
	"6": [
		" _ ",
		"|_ ",
		"|_|"
	],
	"7": [
		" _ ",
		"  |",
		"  |"
	],
	"8": [
		" _ ",
		"|_|",
		"|_|"
	],
	"9": [
		" _ ",
		"|_|",
		" _|"
	]
}

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press âŒ˜F8 to toggle the breakpoint.

def parse_entry(number):
    print(number)

def parse_number(entrada, posicion):
    resultado = []
    for linea in entrada.split("\n"):
        posicion_ = linea[posicion * 3:posicion * 3 + 3]
        print(posicion_)
        resultado.append(posicion_)
    return resultado
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


