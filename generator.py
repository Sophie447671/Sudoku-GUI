from random import randint #importation du module random

from grid import grid
from solver import solve_sudoku


#générer une grille sudoku
def generate_grid(nb_missing_values):
  
  #mise à zero de la grille
  for y in range(len(grid)): #parcourt les lignes
    for x in range(len(grid)): #parcourt les colonnes
        grid[y][x].set('') 

  #initiliaser la grilles avec 9 valeurs de 1 à 9 placées au hasard
  for n in range(1,10):
    while True:
      x=randint(0,len(grid)-1)
      y=randint(0,len(grid)-1)
      if grid[y][x].get() == '':
        grid[y][x].set(str(n))
        break

  #solutionner la grille      
  solve_sudoku()

  print_grid(grid)

  #copier la grille dans matrice solved_grid
  solved_grid=[[]]
  for y in range(len(grid)): #parcourt les lignes
        solved_grid += [[]]
        for x in range(len(grid)): #parcourt les colonnes
            solved_grid[y].append(grid[y][x].get())

  #mettre nb_missing_values à '' dans la grille
  for i in range(nb_missing_values):
    while True:
      x=randint(0,len(grid)-1)
      y=randint(0,len(grid)-1)
      if grid[y][x].get() != '':
        grid[y][x].set('')
        break
  
  return solved_grid


#imprimer une grille
def print_grid(grid):
    for i in range(len(grid)):
      if i % 3 == 0 and i != 0:
         print("- - - - - - - - - - - -")
      for j in range(len(grid)):
        if j % 3 == 0 and j != 0:
          print(" | ", end="")
        if grid[i][j].get() == '':
            print(" ", end = " ")
        else:
            print(grid[i][j].get(), end = " ")
      print()
    print()