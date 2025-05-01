# python-nmap-scan
Scan réseau et génération de rapport HTML (Réseau/Cyber)

# 🔍 Scanner de Ports avec Rapport HTML

Ce projet est un petit script Python qui utilise **Nmap** (via la bibliothèque `python-nmap`) pour scanner une cible (adresse IP ou domaine) et génère automatiquement un **rapport HTML** lisible.  
Le rapport indique les **ports ouverts**, les **services détectés** ainsi que leurs **versions**.

---

## 🧰 Fonctionnalités

- Scan avec détection de version (`-sV`)
- Rapport HTML lisible
- Nom de fichier basé sur l'heure du scan
- Création automatique du dossier de sortie `output/`

---

## 📦 Prérequis

1. **Python 3**
2. **Nmap** installé sur ton système ([https://nmap.org/download.html](https://nmap.org/download.html))
3. Installer la dépendance Python :
   ```bash
   pip install python-nmap

## 🚀 Utilisation

1. Lancer le script
```bash
python3 scanner.py <IP ou nom de domaine>

2. Exemple
```bash
python3 scanner.py 192.168.5.3

3. Fichier de sortie
Port 80 : http (Apache httpd 2.4.41)
Port 22 : ssh (OpenSSH 7.9)
