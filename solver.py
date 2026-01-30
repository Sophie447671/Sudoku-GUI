from grid import grid


#fonction pour résoudre le sudoku
def solve_sudoku():
    """
    Résout la grille en utilisant le backtracking.
    Returns : 
        bool: True si la grille a été résolue, False si aucune solution n'a été trouvée
    """
    for y in range(len(grid)): 
        for x in range(len(grid)): 
            if grid[y][x].get() == '':
                for n in range(1,10): 
                    if is_valid_value(y, x, n):
                        grid[y][x].set(str(n))
                        if solve_sudoku(): 
                            return True
                        else:
                            grid[y][x].set('')  
                else: 
                    return False                
    return True


def is_valid_value(y,x,n):
    """
    Vérifie si une certaine valeur peut être placée dans une case de la grille grille
    Args: 
        y (int) : indice de la ligne de la case, entre 0 et 8
        x (int) : indice de la colonne de la case, entre 0 e t8
        n (int) : valeur à tester (1 à 9)
    
    Returns:
        bool : True si la valeur est valide à cette position, False sinon 
    """
    for x0 in range(len(grid)): 
        if grid[y][x0].get() == str(n):
            return False
    for y0 in range(len(grid)): 
        if grid[y0][x].get() == str(n):
            return False
    x0 = (x//3) * 3
    y0 = (y//3) * 3
    for i in range(3):
        for j in range(3):
            if grid[y0+i][x0+j].get() == str(n):
                return False
    return True