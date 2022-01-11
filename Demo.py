value = input('''Welcome to the menu. Options below:
\n\t 1. Roll
\n\t 2. Sweep
\n\t 3. Scroll

Type the number of your choice and Enter. ''')

def roll(val):
    return val**1
def sweep(val):
    return val**2
def scroll(val):
    return val**3

print("The value you input is: ", value)
print(f'it is of type {type(value)}.')

while True:
    if value.isdigit() == True:
        value = int(value)
        if value > 3 or value < 1:
            value = input("Please input a smaller number between 1 and 2")
            continue
        else: break
        '''print("The value you input is converted: ", value)
        print(f'it is of type {type(value)}.')
        break'''
    else:
        input("Invalid. Input: ")

if value == 1:
    print(roll(value))
elif value == 2:
    print(sweep(value))
else:
    print(scroll(value))
