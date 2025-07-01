# PRINCIPE :
# 1. On génère une clé AES pour chiffrer rapidement les données
# 2. On utilise RSA pour chiffrer cette clé AES (sécurité)
# 3. On envoie les données chiffrées + la clé AES chiffrée
# 4. Pour déchiffrer : on déchiffre d'abord la clé AES avec RSA, puis les données avec AES

from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
import base64

class ChiffrementSimple:
    """Classe simple pour chiffrer avec AES + RSA"""
    
    def __init__(self):
        self.cle_rsa = None
        self.cle_publique = None
        self.cle_privee = None
    
    def generer_cles_rsa(self):
        """Étape 1 : Générer les clés RSA (publique et privée)"""
        print(" Génération des clés RSA...")
        
        # Créer une paire de clés RSA de 2048 bits
        self.cle_rsa = RSA.generate(2048)
        
        # Extraire la clé publique et privée
        self.cle_publique = self.cle_rsa.publickey()
        self.cle_privee = self.cle_rsa
        
        print(" Clés RSA créées !")
        print(f"   - Clé publique : {len(self.cle_publique.export_key())} bytes")
        print(f"   - Clé privée : {len(self.cle_privee.export_key())} bytes")
    
    def chiffrer_message(self, message):
        
        print(f"\n Chiffrement du message : '{message}'")
        
        # Vérifier qu'on a les clés
        if not self.cle_publique:
            raise Exception(" Vous devez d'abord générer les clés RSA !")
        
        # ÉTAPE 2A : Générer une clé AES aléatoire (32 bytes = 256 bits)
        cle_aes = get_random_bytes(32)
        print(f" Clé AES générée : {len(cle_aes)} bytes")
        
        # ÉTAPE 2B : Chiffrer le message avec AES
        cipher_aes = AES.new(cle_aes, AES.MODE_EAX)
        donnees_chiffrees, tag = cipher_aes.encrypt_and_digest(message.encode('utf-8'))
        
        print(f" Message chiffré avec AES : {len(donnees_chiffrees)} bytes")
        
        # ÉTAPE 2C : Chiffrer la clé AES avec RSA
        cipher_rsa = PKCS1_OAEP.new(self.cle_publique)
        cle_aes_chiffree = cipher_rsa.encrypt(cle_aes)
        
        print(f" Clé AES chiffrée avec RSA : {len(cle_aes_chiffree)} bytes")
        
        # RÉSULTAT : Tout ce qu'il faut pour déchiffrer
        resultat = {
            'donnees_chiffrees': base64.b64encode(donnees_chiffrees).decode('utf-8'),
            'cle_aes_chiffree': base64.b64encode(cle_aes_chiffree).decode('utf-8'),
            'nonce': base64.b64encode(cipher_aes.nonce).decode('utf-8'),
            'tag': base64.b64encode(tag).decode('utf-8')
        }
        
        print(" Chiffrement terminé !")
        return resultat
    
    def dechiffrer_message(self, donnees_chiffrement):
        
        print("\n Déchiffrement du message...")
        
        # Vérifier qu'on a la clé privée
        if not self.cle_privee:
            raise Exception(" Vous devez avoir la clé privée pour déchiffrer !")
        
        try:
            # ÉTAPE 3A : Décoder les données depuis base64
            donnees_chiffrees = base64.b64decode(donnees_chiffrement['donnees_chiffrees'])
            cle_aes_chiffree = base64.b64decode(donnees_chiffrement['cle_aes_chiffree'])
            nonce = base64.b64decode(donnees_chiffrement['nonce'])
            tag = base64.b64decode(donnees_chiffrement['tag'])
            
            # ÉTAPE 3B : Déchiffrer la clé AES avec RSA
            cipher_rsa = PKCS1_OAEP.new(self.cle_privee)
            cle_aes = cipher_rsa.decrypt(cle_aes_chiffree)
            print(" Clé AES récupérée avec RSA")
            
            # ÉTAPE 3C : Déchiffrer le message avec AES
            cipher_aes = AES.new(cle_aes, AES.MODE_EAX, nonce)
            message_bytes = cipher_aes.decrypt_and_verify(donnees_chiffrees, tag)
            message = message_bytes.decode('utf-8')
            
            print(" Déchiffrement réussi !")
            return message
            
        except Exception as e:
            print(f" Erreur lors du déchiffrement : {e}")
            return None


# PROGRAMME PRINCIPAL - DÉMONSTRATION

def demonstration():
  
    
    print("🎓 DÉMONSTRATION CHIFFREMENT AES + RSA")
    print("=" * 50)
    
    # Créer notre objet de chiffrement
    chiffrement = ChiffrementSimple()
    
    # ÉTAPE 1 : Générer les clés RSA
    chiffrement.generer_cles_rsa()
    
    # ÉTAPE 2 : Chiffrer un message secret
    message_secret = "Ceci est mon message confidentiel pour le devoir !"
    donnees_chiffrees = chiffrement.chiffrer_message(message_secret)
    
    # Afficher les résultats du chiffrement
    print(f"\n RÉSULTATS DU CHIFFREMENT :")
    print(f"   - Données chiffrées : {donnees_chiffrees['donnees_chiffrees'][:50]}...")
    print(f"   - Clé AES chiffrée : {donnees_chiffrees['cle_aes_chiffree'][:50]}...")
    
    # ÉTAPE 3 : Déchiffrer le message
    message_dechiffre = chiffrement.dechiffrer_message(donnees_chiffrees)
    
    # Vérifier que ça marche
    print(f"\n VÉRIFICATION :")
    print(f"   - Message original : '{message_secret}'")
    print(f"   - Message déchiffré : '{message_dechiffre}'")
    print(f"   - Identiques ? {' OUI' if message_secret == message_dechiffre else ' NON'}")


def test_avec_message_personnalise():
    
    print("\n" + "=" * 50)
    print(" Salut jeune saiyan")
    print("=" * 50)
    
    votre_message = "Salut prof, ce chiffrement fonctionne parfaitement !"
    
    chiffrement = ChiffrementSimple()
    chiffrement.generer_cles_rsa()
    
    # Chiffrer
    resultat = chiffrement.chiffrer_message(votre_message)
    
    # Déchiffrer
    message_recupere = chiffrement.dechiffrer_message(resultat)
    
    print(f"\n RÉSULTAT FINAL :")
    print(f"   Message original : {votre_message}")
    print(f"   Message récupéré : {message_recupere}")
    print(f"   Succès : {'' if votre_message == message_recupere else ''}")


# EXÉCUTION DU PROGRAMME
# installer pycryptodome si pas installé

if __name__ == "__main__":    
    try:
        demonstration()
        
        # Test avec votre message
        test_avec_message_personnalise()
        
        print(f"\n PROGRAMME TERMINÉ AVEC SUCCÈS !")
        print(" Vous pouvez maintenant modifier les messages dans le code")
        
    except ImportError:
        print("ERREUR : Vous devez installer pycryptodome")
        print("Tapez dans votre terminal : pip install pycryptodome")
    except Exception as e:
        print(f"ERREUR : {e}")
