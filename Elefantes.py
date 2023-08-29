def incomodam(n):
    if n < 1:
        return ''
    elif n == 1:
        return "incomodam "
    return "incomodam " + incomodam(n-1)

def elefantes(n, i=1):
    if n == i or n < 2:
        return ''
    elif i == 1:
        return "Um elefante incomoda muita gente\n" + str(i+1) + " elefantes " + incomodam(i+1) + "muito mais\n" + elefantes(n, i+1)
    else:
        return str(i) + " elefantes incomodam muita gente\n" + str(i+1) + " elefantes " + incomodam(i+1) + "muito mais\n" + elefantes(n, i+1)
