def inverte_string(string):
    string_invertida = ''
    for caractere in range(len(string) -1, -1, -1):
        string_invertida += string[caractere]
    return string_invertida


entrada = input('Digite qualquer coisa: ')
entrada_invertida = inverte_string(entrada)
print(entrada_invertida)
