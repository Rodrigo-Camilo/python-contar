import os
os.system('cls' if os.name == 'nt' else 'clear')
os.system('color 2')

escolha = float(input("Devemos contar de quanto em quanto? "))
numberini = float(input("Vamos começar em qual numero? "))
number = float(input("Até qual numero devemos contar? "))
filename = str("{}ate{}.txt".format(int(numberini), int(number)))
with open(filename, 'w') as document:
    contador = numberini 
    document.write('{}\n'.format(str(contador)))
    while contador < number:
        contador = contador + escolha 
        if contador // 1 == contador:
            contador = int(contador)
        contadortxt = str(contador)
        document.write('{}\n'.format(contadortxt))
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Criamos um arquivo {} com o contador.".format(filename))