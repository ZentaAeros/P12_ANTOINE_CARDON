from os import environ
from getpass import getpass

print("Bienvenue dans la configuration de la base de données.")
print()

username = input("Nom d'utilisateur de la base de données : ")
password = getpass("Mot de passe de la base de données : ")

with open(".env", "w") as file:
    file.write(f"DB_USERNAME={username}")
    file.write("\n")
    file.write(f"DB_PASSWORD={password}")
    file.close()

print()
print("La base de données est bien configurée.")