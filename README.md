# 🖤 BlackArch Toolkit 2026.7 — Shadow Protocol

> **Auteur:** hackerstchad  
> **Contact:** hackerstchad@protonmail.com  
> **Repository:** https://github.com/hackerstchad/blackarch-toolkit  
> **Version:** 2026.7 "Shadow Protocol"  
> **Release Year:** 2026-2027  

---

## Table des matières

1. [Introduction](#introduction)
2. [Fonctionnalités](#fonctionnalités)
3. [Installation](#installation)
4. [Utilisation](#utilisation)
5. [Commandes Arch Linux incluses](#commandes-arch-linux-incluses)
6. [Catégories BlackArch](#catégories-blackarch)
7. [Exemples d'utilisation](#exemples-dutilisation)
8. [Structure du projet](#structure-du-projet)
9. [Sécurité et avertissements](#sécurité-et-avertissements)
10. [Ressources & Liens](#ressources--liens)
11. [Livres recommandés](#livres-recommandés)
12. [Licence](#licence)

---

## Introduction

**BlackArch Toolkit** est un script Python avancé conçu pour les utilisateurs de **BlackArch Linux** et d'**Arch Linux**. Il centralise une encyclopédie de commandes Arch, des utilitaires d'installation par catégories d'outils de pentest, des fonctions de maintenance système, d'audit, de réseau, et bien plus.

Ce projet a pour objectif d'accompagner les apprentis et professionnels de la cybersécurité dans leur quotidien sous BlackArch/Arch.

---

## Fonctionnalités

- 🎨 Menu interactif stylisé avec bannière ANSI
- 📦 Installation du dépôt BlackArch via `strap.sh`
- 🧰 Installation d'outils par catégories (recon, webapp, crypto, forensics, reverse, etc.)
- 📚 Encyclopédie de commandes Arch Linux documentées
- 🔍 Recherche dans les commandes
- 📤 Export JSON/Markdown de la documentation
- 🔄 Mise à jour, nettoyage, optimisation des miroirs
- 🛡️ Audit système rapide
- 🌐 Outils réseau intégrés
- 🔐 Générateur de mots de passe + assistant hash
- 💾 Sauvegarde / restauration de la liste des paquets
- 📝 Historique des actions

---

## Installation

### Prérequis

- Arch Linux ou BlackArch Linux (ou dérivée)
- Python >= 3.9
- `pacman` (root requis pour certaines actions)
- `curl` pour l'installation de strap.sh

### Étapes

```bash
git clone https://github.com/hackerstchad/blackarch-toolkit.git
cd blackarch-toolkit
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
chmod +x blackarch_toolkit.py
python3 blackarch_toolkit.py --menu
```

---

## Utilisation

### Menu interactif

```bash
python3 blackarch_toolkit.py --menu
```

### Ligne de commande

```bash
python3 blackarch_toolkit.py --install-category recon
python3 blackarch_toolkit.py --search nmap
python3 blackarch_toolkit.py --command-list
python3 blackarch_toolkit.py --export markdown arch_commands.md
python3 blackarch_toolkit.py --update
python3 blackarch_toolkit.py --audit
python3 blackarch_toolkit.py --gen-pass
python3 blackarch_toolkit.py --ip-info 192.168.1.0/24
```

---

## Commandes Arch Linux incluses

Le script contient des centaines de commandes Arch Linux documentées, avec description, syntaxe et exemples.

### Exemples de catégories couvertes

- Gestion des paquets (`pacman`, `makepkg`, `yay`, `pkgfile`)
- Système & Boot (`systemctl`, `journalctl`, `mkinitcpio`, `grub-mkconfig`)
- Réseau (`ip`, `ss`, `ping`, `nmap`, `curl`, `wget`)
- Disques & Fichiers (`lsblk`, `fdisk`, `mkfs`, `dd`, `rsync`)
- Utilisateurs & Permissions (`useradd`, `passwd`, `chmod`, `chown`)
- Surveillance (`top`, `htop`, `iotop`, `vmstat`, `dmesg`)
- BlackArch Pentest (`nmap`, `metasploit`, `burpsuite`, `sqlmap`, `wireshark`, `aircrack-ng`, `john`, `hashcat`)

---

## Catégories BlackArch

| Catégorie | Description |
|-----------|-------------|
| recon | Reconnaissance et OSINT |
| scanning | Scan de ports et de vulnérabilités |
| webapp | Tests d'intrusion web |
| exploitation | Frameworks d'exploitation |
| postexploitation | Post-exploitation et C2 |
| wireless | Sécurité Wi-Fi |
| forensics | Forensique numérique |
| reverse | Reverse engineering |
| crypto | Cryptographie et cassage de hashes |
| sniffer | Analyse de trafic réseau |
| social | Social engineering |
| automobile | Sécurité automobile / CAN |
| fingerprint | Fingerprinting réseau |
| defensive | Outils défensifs et durcissement |
| misc | Utilitaires divers |

---

## Exemples d'utilisation

### Installer une catégorie complète

```bash
sudo python3 blackarch_toolkit.py --install-category webapp
```

### Rechercher une commande

```bash
python3 blackarch_toolkit.py --search firewall
```

### Exporter la documentation

```bash
python3 blackarch_toolkit.py --export json commands.json
python3 blackarch_toolkit.py --export markdown commands.md
```

### Audit système

```bash
sudo python3 blackarch_toolkit.py --audit
```

---

## Structure du projet

```
blackarch-toolkit/
├── blackarch_toolkit.py   # Script principal (tout-en-un)
├── requirements.txt       # Dépendances Python
├── README.md              # Ce fichier
└── .gitignore
```

---

## Sécurité et avertissements

> ⚠️ **Ce script est fourni à des fins éducatives et professionnelles uniquement.**  
> L'utilisation des outils de pentest inclus doit toujours se faire sur des systèmes pour lesquels vous disposez d'une autorisation explicite.  
> L'auteur (hackerstchad) décline toute responsabilité quant à une utilisation illégale ou malveillante.

### Bonnes pratiques

- Toujours tester dans un environnement isolé ou une VM.
- Garder des snapshots avant les mises à jour majeures.
- Ne jamais exécuter de commandes inconnues en root sans vérification.
- Lire les PKGBUILD avant d'installer depuis l'AUR.

---

## Ressources & Liens

### Officiels

- BlackArch Linux : https://blackarch.org/
- Arch Linux : https://archlinux.org/
- Arch Wiki : https://wiki.archlinux.org/
- Pacman Rosetta : https://wiki.archlinux.org/title/Pacman/Rosetta

### Communautés

- r/archlinux : https://www.reddit.com/r/archlinux/
- r/blackarch : https://www.reddit.com/r/blackarch/
- Offensive Security : https://www.offensive-security.com/
- Hack The Box : https://www.hackthebox.com/
- TryHackMe : https://tryhackme.com/

### Outils référencés

- Nmap : https://nmap.org/
- Metasploit : https://www.metasploit.com/
- Burp Suite : https://portswigger.net/burp
- OWASP ZAP : https://www.zaproxy.org/
- Wireshark : https://www.wireshark.org/
- Aircrack-ng : https://www.aircrack-ng.org/
- Hashcat : https://hashcat.net/hashcat/
- John the Ripper : https://www.openwall.com/john/
- SQLMap : https://sqlmap.org/
- Ghidra : https://ghidra-sre.org/
- Radare2 : https://rada.re/

---

## Livres recommandés

1. **The Linux Command Line** — William Shotts
2. **How Linux Works** — Brian Ward
3. **Linux Bible** — Christopher Negus
4. **The Hacker Playbook 3** — Peter Kim
5. **Penetration Testing: A Hands-On Introduction to Hacking** — Georgia Weidman
6. **The Web Application Hacker's Handbook** — Dafydd Stuttard, Marcus Pinto
7. **Real-World Bug Hunting** — Peter Yaworski
8. **Black Hat Python** — Justin Seitz
9. **Gray Hat Python** — Justin Seitz
10. **Practical Malware Analysis** — Michael Sikorski, Andrew Honig
11. **The IDA Pro Book** — Chris Eagle
12. **Reversing: Secrets of Reverse Engineering** — Eldad Eilam
13. **Hacking: The Art of Exploitation** — Jon Erickson
14. **The Shellcoder's Handbook** — Chris Anley et al.
15. **Network Security Assessment** — Chris McNab
16. **Metasploit: The Penetration Tester's Guide** — David Kennedy et al.
17. **Applied Cryptography** — Bruce Schneier
18. **Serious Cryptography** — Jean-Philippe Aumasson
19. **Rootkits and Bootkits** — Alex Matrosov et al.
20. **The Car Hacker's Handbook** — Craig Smith

---

## Licence

MIT License — Copyright (c) 2026-2027 hackerstchad / TchadSec Community.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
