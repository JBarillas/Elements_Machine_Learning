#--------------------------------------Problema 0 --------------------------------------------------------
unidades = {
    1: 'uno',
    2: 'dos',
    3: 'tres',
    4: 'cuatro',
    5: 'cinco',
    6: 'seis',
    7: 'siete',
    8: 'ocho',
    9: 'nueve'
}

decenas = {
    10: 'diez',
    20: 'veinte',
    30: 'treinta',
    40: 'cuarenta',
    50: 'cincuenta',
    60: 'sesenta',
    70: 'setenta',
    80: 'ochenta',
    90: 'noventa'
}

centenas = {
    100: 'ciento',
    200: 'doscientos',
    300: 'trescientos',
    400: 'cuatrocientos',
    500: 'quinientos',
    600: 'seiscientos',
    700: 'setecientos',
    800: 'ochocientos',
    900: 'novecientos'
}

numero_max = 1001
def en_palabras(n):
    if (n < numero_max):
        return None

#--------------------------------Problema 1 --------------------------------
    
    

#--------------------------Problema2--------------------------------------
def invertir(num):
    inver = 0
    while(num>0):
        rem = num%10
        inver = (inver *10) + rem
        num = num //10
    return inver

def palindromo(num):
    temp = num
    inver = 0

    while temp != 0:
        inver = (inver * 10) + (temp % 10)
        temp = temp // 10

    if num == inver:
        return False
    else:
        return True
    
def lychrel_num(num):
    i = 0
    type = str(num) + " es Lychrel"
    while palindromo(num):
        num = num + invertir(num)
        i =i+1
        if i == 50:
            type = str(num) + " no es lychreel"
            break
    return num, type

print(lychrel_num(47))

#----------------------------------------------------Problema 3 -----------------------------