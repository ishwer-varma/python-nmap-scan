
"""
Ce projet est un petit script Python qui utlise Nmap pour scanner une machine (Ip ou domaine) et génére automatiquement un rapport en HTML
contenant les ports ouverts, services et leurs versions.

"""

import nmap
import sys
import os
from datetime import datetime

# Lance un scan de ports sur une cible donnée, que ce soit une IP ou un nom de domaine, avec détection de version (-sV)
# Retourne l'objet scanner contenant les résultats du scan2. Exemple

def scan_cible(target):
    scanner = nmap.PortScanner()  # Crée un objet scanner Nmap
    print(f"[~] Scan en cours sur {target}...\n")
    scanner.scan(hosts=target, arguments='-sV')  # Lance le scan avec Nmap sur l'IP ou le domaine, avec l'option -sV
                                                 # qui permet de détecter les versions des services en plus des ports ouverts
    return scanner

# Génère un rapport HTML lisible à partir des résultats du scan Nmap
# Crée un fichier horodaté dans le dossier "output"

def genere_html_rapport(scanner, target):
    now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')  # Récupère la date et l'heure pour nommer chaque rapport de manière unique
    filename = f"output/rapport_{now}.html"  # Chemin du fichier HTML à créer
    os.makedirs("output", exist_ok=True)  # Crée le dossier output s'il n'existe pas

    with open(filename, "w") as f:  # Ouvre le fichier HTML en écriture
        f.write(f"<html><head><title>Rapport de scan - {target}</title></head><body>")  # En-tête HTML
        f.write(f"<h2>Rapport de scan pour : {target}</h2>")
        for host in scanner.all_hosts():  # Parcourt chaque hôte trouvé par Nmap
            f.write(f"<h3>Hôte détecté : {host}</h3>")
            f.write("<ul>")
            for proto in scanner[host].all_protocols():  # Parcourt les protocoles détectés
                f.write(f"<li>Protocole : {proto}</li><ul>")
                ports = scanner[host][proto].keys() # Récupère tous les ports associés à ce protocole
                for port in sorted(ports): # Parcourt les ports ouverts
                    service = scanner[host][proto][port]  # Récupère un dictionnaire sur toutes les infos de service trouvé sur ce port
                    f.write(f"<li>Port {port} : {service['name']} ({service.get('product', '')} {service.get('version', '')})</li>")
                    # Affiche dans le rapport : numéro de port, nom du service, logiciel utilisé et sa version
                f.write("</ul>")
            f.write("</ul>")
        f.write("</body></html>")

    print(f"\n[✓] Rapport HTML généré : {filename}")  # Affiche le chemin vers le rapport généré dans le terminal

# Point d'entrée du script : vérifie qu'une cible est fournie en argument
# Lance le scan puis génère automatiquement le rapport HTML correspondant

if __name__ == "__main__":
    if len(sys.argv) < 2:  # Vérifie si l'utilisateur a bien fourni une IP ou un nom de domaine
        print("Utilisation : python3 scanner.py <IP ou domaine>")
        sys.exit(1)  # Arrête le programme

    target = sys.argv[1]  # Récupère la valeur donnée en argument
    scanner = scan_cible(target)  # Lance le scan Nmap
    genere_html_rapport(scanner, target)  # Génère automatiquement le rapport HTML
