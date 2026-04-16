def sao_anagramas(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    return sorted(s1) == sorted(s2)


def cifra_de_cesar(texto, deslocamento):
    resultado = ""
    
    for c in texto:
        if c.isalpha():
            base = ord('a') if c.islower() else ord('A')
            nova = (ord(c) - base + deslocamento) % 26 + base
            resultado += chr(nova)
        else:
            resultado += c
    
    return resultado


def valida_cpf(cpf):
    cpf = cpf.replace(".", "").replace("-", "")
    
    if len(cpf) != 11:
        return False
    
    # 1º dígito
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    d1 = (soma * 10) % 11
    if d1 == 10:
        d1 = 0

    # 2º dígito
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    d2 = (soma * 10) % 11
    if d2 == 10:
        d2 = 0

    return d1 == int(cpf[9]) and d2 == int(cpf[10])