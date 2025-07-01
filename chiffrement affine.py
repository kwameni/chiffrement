def chiffrer_affine(texte_clair, a, b):
    """
    Chiffre un texte avec une fonction affine.
    
    Formule: y = (a * x + b) mod 26
    où x est la position de la lettre (A=0, B=1, ..., Z=25)
    
    Args:
        texte_clair (str): Le texte à chiffrer
        a (int): Premier paramètre (doit être premier avec 26)
        b (int): Décalage (entre 0 et 25)
        
    Returns:
        str: Le texte chiffré
    """
    texte = texte_clair.upper().replace(' ', '')
    texte_chiffre = ""
    
    for lettre in texte:
        if lettre.isalpha():  # Vérifier que c'est une lettre
            # Convertir lettre en nombre (A=0, B=1, ..., Z=25)
            x = ord(lettre) - ord('A')
            
            # Appliquer la fonction affine: y = (a*x + b) mod 26
            y = (a * x + b) % 26
            
            # Reconvertir en lettre
            lettre_chiffree = chr(y + ord('A'))
            texte_chiffre += lettre_chiffree
        else:
            # Garder les caractères non-alphabétiques
            texte_chiffre += lettre
    
    return texte_chiffre

def dechiffrer_affine(texte_chiffre, a, b):
    """
    Déchiffre un texte chiffré avec une fonction affine.
    
    Formule: x = a_inv * (y - b) mod 26
    où a_inv est l'inverse modulaire de a modulo 26
    """
    # Trouver l'inverse modulaire de a
    a_inv = inverse_modulaire(a, 26)
    if a_inv == -1:
        return "Erreur: 'a' n'a pas d'inverse modulaire"
    
    texte = texte_chiffre.upper()
    texte_dechiffre = ""
    
    for lettre in texte:
        if lettre.isalpha():
            # Convertir lettre en nombre
            y = ord(lettre) - ord('A')
            
            # Appliquer la fonction inverse: x = a_inv * (y - b) mod 26
            x = (a_inv * (y - b)) % 26
            
            # Reconvertir en lettre
            lettre_dechiffree = chr(x + ord('A'))
            texte_dechiffre += lettre_dechiffree
        else:
            texte_dechiffre += lettre
    
    return texte_dechiffre

def inverse_modulaire(a, m):
    """
    Trouve l'inverse modulaire de a modulo m.
    Utilise l'algorithme d'Euclide étendu.
    """
    def euclide_etendu(a, b):
        if a == 0:
            return b, 0, 1
        gcd, x1, y1 = euclide_etendu(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y
    
    gcd, x, y = euclide_etendu(a, m)
    if gcd != 1:
        return -1  # Pas d'inverse
    return x % m

def tester_chiffrement():
    """
    Teste le chiffrement affine avec des exemples.
    """
    print("=== TEST DU CHIFFREMENT AFFINE ===")
    
    # Paramètres du chiffrement
    a = 5  # Doit être premier avec 26
    b = 8  # Décalage
    
    print(f"Paramètres: a = {a}, b = {b}")
    print(f"Formule: y = ({a} * x + {b}) mod 26")
    
    # Texte d'exemple
    texte_original = "HELLO WORLD"
    print(f"\nTexte original: {texte_original}")
    
    # Chiffrement
    texte_chiffre = chiffrer_affine(texte_original, a, b)
    print(f"Texte chiffré: {texte_chiffre}")
    
    # Déchiffrement
    texte_dechiffre = dechiffrer_affine(texte_chiffre, a, b)
    print(f"Texte déchiffré: {texte_dechiffre}")
    
    # Vérification
    if texte_original.replace(' ', '') == texte_dechiffre:
        print("✓ Chiffrement/déchiffrement réussi!")
    else:
        print("✗ Erreur dans le processus")

def valeurs_a_valides():
    """
    Affiche les valeurs de 'a' valides (premières avec 26).
    """
    print("\nValeurs de 'a' valides (premières avec 26):")
    valides = []
    for i in range(1, 26):
        # Vérifier si i et 26 sont premiers entre eux
        def pgcd(x, y):
            while y:
                x, y = y, x % y
            return x
        
        if pgcd(i, 26) == 1:
            valides.append(i)
    
    print(f"a peut être: {valides}")
    print(f"Total: {len(valides)} valeurs possibles")

# Tests
tester_chiffrement()
valeurs_a_valides()

print("\n=== TON CHIFFREMENT ===")
# Remplace par tes valeurs
mon_a = 3
mon_b = 7
mon_texte = "BONJOUR"

print(f"Ton texte: {mon_texte}")
print(f"Tes paramètres: a={mon_a}, b={mon_b}")
resultat = chiffrer_affine(mon_texte, mon_a, mon_b)
print(f"Résultat chiffré: {resultat}")