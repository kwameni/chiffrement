
def cesar_crypter(message, cle):
    message = message.upper()
    message_crypte = ""

    for l in message:
        if l == ' ':
            message_crypte += ' '
        elif 'A' <= l <= 'Z':
            asc = ord(l) + cle
            if asc > 90:
                asc -= 26
            message_crypte += chr(asc)
        else:
            message_crypte += l

    return message_crypte


messageacrypter = input("Entrez le message à crypter : ")
clef_crypt = int(input("Entrez le nombre de décalage : "))

resultat = cesar_crypter(messageacrypter, clef_crypt)
print("Message chiffré :", resultat)

def cesar_decrypt(messagecrypter, cle):
    message_crypter = messagecrypter.upper()
    message_decrypter = ""
    
    for a in resultat:
        if a == " ":
            message_decrypter += " "
        elif 'A' <= a <= 'Z':
            asc = ord(a) - cle
            if asc < 65:
                asc +=26
            message_decrypter += chr(asc)
        else:
            message_decrypter += a
            
    return message_decrypter
    
    
resultats = cesar_decrypt(resultat, clef_crypt)
    
print ("message déchiffré:", resultats)