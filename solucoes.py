def sao_anagramas(texto1, texto2):
    # Remove espaços e deixa tudo minúsculo
    texto1 = texto1.replace(" ", "").lower()
    texto2 = texto2.replace(" ", "").lower()
    
    # Ordena as letras e compara
    # Se forem iguais, são anagramas
    return sorted(texto1) == sorted(texto2)


def cifra_de_cesar(texto_original, deslocamento):
    resultado = ""
    
    for caractere in texto_original:
        # Verifica se é letra
        if caractere.isalpha():
            # Define a base (A ou a) dependendo se é maiúscula ou minúscula
            base_ascii = ord('a') if caractere.islower() else ord('A')
            
            # Converte a letra para número (0 a 25), aplica o deslocamento
            # e usa % 26 para "voltar" ao início do alfabeto se passar de Z
            novo_codigo = (ord(caractere) - base_ascii + deslocamento) % 26
            
            # Converte de volta para letra
            nova_letra = chr(novo_codigo + base_ascii)
            
            resultado += nova_letra
        else:
            # Mantém caracteres que não são letras (espaços, números, etc)
            resultado += caractere
    
    return resultado


def valida_cpf(cpf_string):
    # Remove pontos e traço do CPF
    cpf_numeros = cpf_string.replace(".", "").replace("-", "")
    
    # Verifica se tem 11 dígitos
    if len(cpf_numeros) != 11:
        return False
    
    # -------------------------
    # CÁLCULO DO 1º DÍGITO
    # -------------------------
    soma = 0
    for i in range(9):
        # Multiplica cada número pelo peso (10 até 2)
        soma += int(cpf_numeros[i]) * (10 - i)
    
    # Fórmula do dígito verificador
    primeiro_digito = (soma * 10) % 11
    
    # Se der 10, vira 0
    if primeiro_digito == 10:
        primeiro_digito = 0

    # -------------------------
    # CÁLCULO DO 2º DÍGITO
    # -------------------------
    soma = 0
    for i in range(10):
        # Multiplica cada número pelo peso (11 até 2)
        soma += int(cpf_numeros[i]) * (11 - i)
    
    segundo_digito = (soma * 10) % 11
    
    if segundo_digito == 10:
        segundo_digito = 0

    # Verifica se os dígitos calculados são iguais aos do CPF
    return (primeiro_digito == int(cpf_numeros[9]) and
            segundo_digito == int(cpf_numeros[10]))