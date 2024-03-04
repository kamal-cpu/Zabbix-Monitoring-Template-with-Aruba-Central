import re
import uuid

# Fonction pour générer un UUID v4
def generateUUIDv4():
    return str(uuid.uuid4()).replace('-', '')

# Lire le contenu du fichier old.yaml
with open('old.yaml', 'r') as file:
    content = file.read()

# Remplacer les UUID dans le contenu
content = re.sub(r"uuid: (.*)\n", lambda match: "uuid: " + generateUUIDv4() + "\n", content)

# Écrire le contenu modifié dans un nouveau fichier new.yaml
with open('new.yaml', 'w') as file:
    file.write(content)
