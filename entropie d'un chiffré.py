import math

def calculer_entropie(texte):
    
    # Compter chaque lettre
    compteur = {}
    for lettre in texte:
        if lettre in compteur:
            compteur[lettre] += 1
        else:
            compteur[lettre] = 1
    print (compteur)
    
    # Calculer l'entropie
    total = len(texte)
    entropie = 0.0
    
    for nb_fois in compteur.values():
        probabilite = nb_fois / total
        entropie = entropie - (probabilite * math.log2(probabilite))
    
    print (compteur.values())
    print (f"Dernière probabilité calculée: {probabilite}")
    
    return entropie

# Test simple
texte_test = "ABCDEF"
resultat = calculer_entropie(texte_test)
print(f"Entropie de '{texte_test}': {resultat:.2f}")

# Comparaison
print("\nComparaison:")
print(f"AAAAAA: {calculer_entropie('AAAAAA'):.2f} (mauvais)") 
print(f"ABCDEF: {calculer_entropie('ABCDEF'):.2f} (bon)")

def calculer_redondance(texte):
    """
    Calcule la redondance d'un texte.
    """
    # Calculer l'entropie du texte
    entropie = calculer_entropie(texte)
    
    # Calculer l'entropie maximale possible
    nb_lettres_differentes = len(set(texte))
    
    # Vérifier qu'on a plus d'une lettre différente
    if nb_lettres_differentes <= 1:
        # Si toutes les lettres sont identiques, redondance = 100%
        return 1.0
    
    entropie_max = math.log2(nb_lettres_differentes)
    
    # Calculer la redondance
    redondance = 1 - (entropie / entropie_max)
    
    return redondance

def analyser_texte(texte):
    """
    Analyse complète d'un texte : entropie et redondance.
    """
    entropie = calculer_entropie(texte)
    redondance = calculer_redondance(texte)
    
    print(f"Texte analysé: '{texte}'")
    print(f"Entropie: {entropie:.2f}")
    print(f"Redondance: {redondance:.2f} ({redondance*100:.1f}%)")
    
    if redondance < 0.2:
        print("→ Très peu de redondance (bon chiffrement)")
    elif redondance < 0.5:
        print("→ Redondance modérée")
    else:
        print("→ Beaucoup de redondance (mauvais chiffrement)")
    
    return entropie, redondance

# Tests simples
print("\n=== TESTS ===")

print("\n1. Texte très répétitif:")
analyser_texte("AAAAAA")

print("\n2. Texte bien mélangé:")
analyser_texte("ABCDEF")

print("\n3. Texte avec quelques répétitions:")
analyser_texte("ABCABC")

print("\n=== TON TEXTE ===")
mon_texte = "Bienvenue chez les uchihas"  # Remplace par ton texte
analyser_texte(mon_texte)
