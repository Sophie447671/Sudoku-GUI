Application de sudoku avec interface graphique réalisée avec Tkinter.
Elle génère une grille aléatoire, permet de la remplir et de vérifier ses réponses ou de la résoudre automatiquement.

## Utilisation 
Le menu *Fichier* propose : 
- *Nouvelle grille* : génère une nouvelle grille à compléter.
- *Résoudre la grille* : vérifie les saisies de l'utilisateur (vert = correct, rouge = erreur). S'il n'y a aucune erreur, la grille est entièrement remplie avec la solution.
- *Quitter* : ferme l'application.

## Fonctionnement 
1. La grille est remplie avec un exemplaire de chaque chiffre de 1à 9 placé au hasard.
2. Elle est ensuite complétée par un algorithme de **backtracking** récursif.
3. La solution complète est sauvegardée, puis 40 cases sont vidés pour créer la grille à résoudre.

## Lancement 
```bash
python main.py
```