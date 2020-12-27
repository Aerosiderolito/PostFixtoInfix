#cesarrodriguez_raphaelcaloz

def postfixToInfix(param):
    pile = []
    tabu = param.split(" ")
    lengthParam = len(tabu)

    for i in range(lengthParam):
        # Conditions pour determiner si on a un operateur ou operande
        if len(tabu) > 1 and (not (tabu[i] == "+" or tabu[i] == "-" or tabu[i] == "*" or tabu[i] == "/" or tabu[i] == "<" or
                                   tabu[i] == ">" or tabu[i] == "=" or tabu[i] == "!" or tabu[i] == "√")):
            pile.append(tabu[i])                # stocker dans la pile l'operande
        #Cas de la racine
        elif tabu[i] == "√":
                pile.append(tabu[i]+pile.pop())
                continue
        #Cas du factoriel
        elif tabu[i] == "!":
            pile.append(pile.pop()+tabu[i])
            continue
        else:
        #cas ou on concatenent les valeurs dans l'expression
            localValue = tabu[i]
            temp = pile.pop()
            tmp = pile.pop()
            increment = '('+tmp + localValue +temp+')'
            pile.append(increment)



    return pile[0][1:-1]

if __name__ == '__main__':
    print(postfixToInfix("15 7 1 1 + - / 3 * 2 1 1 + + -"))
    print(postfixToInfix("n ! n 1 + ! <"))
    print(postfixToInfix("9 √ 3 ="))