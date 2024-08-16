from datetime import datetime, timedelta
import jwt
import os

# Clé secrète utilisée pour signer le token JWT
secret_key = os.getenv('SECRET_KEY')

def generate_token(user_id):
    """Generate JWT token for the user"""
    # Définition de la durée de validité du token (1 heure à partir de maintenant)
    expiration_time = datetime.utcnow() + timedelta(hours=1)
    
    # Définition des données à inclure dans le payload du token
    payload = {
        'user_id': user_id,
        'exp': expiration_time,
    }
    
    # Génération du token en utilisant la clé secrète
    token = jwt.encode(payload, secret_key, algorithm='HS256')
    return token

def decode_token(token):
    """Decode JWT token and extract user_id"""
    try:
        # Décodage du token en utilisant la clé secrète
        decoded_token = jwt.decode(token, secret_key, algorithms=['HS256'])
        
        # Extrait de l'identifiant de l'utilisateur à partir du payload décodé
        user_id = decoded_token['user_id']
        return user_id
    except jwt.ExpiredSignatureError:
        # Le token a expiré
        return None
    except jwt.InvalidTokenError:
        # Le token est invalide
        return None

# Exemple d'utilisation
user_id = 25
token = generate_token(user_id)
print("Token:", token)

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoyNiwiZXhwIjoxNzEzNzE4MTI5fQ.BT2NuSAjvUCVmCU3g32jC9vdCPHE3CiDCgfN4p5Wz_4"
token2 = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoyNCwiZXhwIjoxNzEzNzIzNTgzfQ.FI1FolgXGgLf-gkkoUcbpdq__neV-ZCcwGSBOFqCo1s"

decoded_user_id = decode_token(token2)
print("Decoded User ID:", decoded_user_id)

