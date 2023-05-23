def CodeText(text,KeyP,KeyK):
    KeyO = KeyP * KeyK
    secret_text = ''
    for i in range(len(text)):
        C = text[i]
        K = ord(C)
        K = K ^ KeyO
        Cc = chr(K)
        secret_text = secret_text + Cc
    return secret_text