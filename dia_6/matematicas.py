import random
def generate_question():
    n1 = random.randint(1,10)
    n2 = random.randint(1,10)
    operador= random.choice(["+","-","*"])

    if operador == "+":
        resultado= n1 + n2
    elif operador == "-":
        resultado=n1 - n2
    elif operador =="*":
        resultado= n1 * n2
    
    return f" {n1} {n2} {operador} " ,resultado


if __name__=="__main__":
    print(generate_question())
    oracion , re = generate_question()
    print(oracion)
    print(re)