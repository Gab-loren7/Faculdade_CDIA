emoji = input("Escreva um emoji(Ex: :) ou :( ):\n")

if emoji[0] == ':':
    if emoji[1] == ')':
        print('😊')
    elif emoji[1] == '(':
        print('☹️')
    else:
        ...
else:
    ...