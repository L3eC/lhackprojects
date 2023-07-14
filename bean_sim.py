import random

melting_pot = []
potluck = []
cup = []
bean_types = ['lima', 'pinto', 'black', 'red']


for i in range(200):
    melting_pot.append(random.choice(bean_types))
    potluck.append(random.choice(bean_types))

print('Bean cups filled.\n')

print('Type "sample" to get a sample from a specified container ("melting pot" or "potluck") and put the sample into your cup, type "return" to dump your cup\'s contents into a specified container, type "view" to see the beans in your cup, and type "quit" to quit.')
user_input = ''

while True: 
    user_input = input('>').lower()

    if 'sample' in user_input:
        if 'melting' in user_input:
            print("Sampling 10 beans from melting pot")
            for i in range(10):
                cup.append(melting_pot.pop(0))
        elif 'potluck' in user_input:
            print("Sampling 10 beans from potluck")
            for i in range(10):
                cup.append(melting_pot.pop(0))

    elif 'return' in user_input:
        if 'melting' in user_input:
            print("Dumping cup contents into melting pot")
            melting_pot.append(cup)
        elif 'potluck' in user_input:
            print("Dumping cup contents into potluck")
            potluck.append(cup)
        cup = []

    elif 'view' in user_input:
        cup.sort()
        print("Your cup contains: " + ', '.join(cup))

    elif 'quit' in user_input:
        print("Thanks for playing!")
        break

    else:
        print('Invalid input. Please try again.')

