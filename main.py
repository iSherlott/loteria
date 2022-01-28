from random import sample
import os

arrInput = []
switch = True
arrSort = []

def inputValue(i):
    try:
        switch = True
        digit = (int (input("Digite um número de 0 a 99: ")))

        for x in range(len(arrInput)):
            if(digit == arrInput[x]):
                print("Número Já foi selecionado, favor digite outro número: ")
                switch = False
                inputValue(i)
        if(switch): 
            arrInput.append(digit)
    except:
        print("Número Invalido!!!")
        inputValue(i)

def randonNumer():
    return sample(range(0, 100), 10)

arrSort = randonNumer()

for i in range(0, 15):
    inputValue(i)

success = 0

for x in range(len(arrInput)):
    for y in range(len(arrSort)):
        if(arrInput[x] == arrSort[y]): success += 1

os.system('cls' if os.name == 'nt' else 'clear')

print("Os números sorteados foram:", ", ".join(map(str, arrSort)))
print("Onde você teve um total de ", success, " acertos e ", 15 - success, " erros!")