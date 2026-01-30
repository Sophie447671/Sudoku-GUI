from random import randint #importation du module random

from grid import grid
from solver import solve_sudoku

def generate_grid(nb_missing_values):
  """
  Génère une nouvelle grille de sudoku.

  Args: 
        nb_missing_values (int) : nombre de cases à vider dans la grille

  Returns:
        list : la solution complètes, sous forme de lsite 9*9
  """
  for y in range(len(grid)): 
    for x in range(len(grid)): 
        grid[y][x].set('') 

  for n in range(1,10):
    while True:
      x=randint(0,len(grid)-1)
      y=randint(0,len(grid)-1)
      if grid[y][x].get() == '':
        grid[y][x].set(str(n))
        break

  solve_sudoku()

  print_grid(grid)

  solved_grid=[[]]
  for y in range(len(grid)): 
        solved_grid += [[]]
        for x in range(len(grid)): 
            solved_grid[y].append(grid[y][x].get())

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
    """Affiche une grille dans la console
    
    Args: 
            grid (list) : list 9*9 d'objets StringVar de Tkinter à afficher
    """
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