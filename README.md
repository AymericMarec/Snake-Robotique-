# Projet Snake Robotique

## Description

Ce projet consiste à implémenter le jeu Snake sur une grille LED 8x8 contrôlée par un ESP32 C3. Le joueur dirige le serpent à l’aide d’un joystick, et un buzzer permet de jouer des sons pendant la partie.

## Prérequis

### Software :

- Python
- micropython-neopixel (`pip install micropython-neopixel`)
- Un logiciel permettant d’implémenter le code sur l’ESP32 (ex: Thonny, uPyCraft)

### Hardware :

- ESP32 C3
- Grille LED 8x8
- Buzzer (pour jouer des sons)
- Joystick

## Schéma de connexion

Branchez votre ESP32 C3 à votre ordinateur et reliez les composants aux pins correspondants :

| Composant   | Pin ESP32 |
|-------------|----------|
| Grille LED | IO 1 |
| Joystick X | IO 5 |
| Joystick Y | IO 6 |
| Joystick Button | IO 7 |
| Buzzer | IO 8 |

## Installation et exécution

1. Installez MicroPython sur votre ESP32 C3 si ce n’est pas déjà fait.
2. Chargez le fichier `main.py` sur l’ESP32.
3. Exécutez le script avec votre logiciel (Thonny, uPyCraft, etc.).

## Fonctionnalités

- Déplacement du serpent via le joystick.
- Affichage sur une grille LED 8x8.
- Sons et effets via le buzzer.
- Gestion des collisions et de la croissance du serpent.

## Schéma carte éléctronique

[voir le fichier ici](pdf/carteElec.PDF)