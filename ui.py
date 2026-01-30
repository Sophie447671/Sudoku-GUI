from tkinter import * #importation du module tkinter

from grid import grid
from generator import generate_grid


class Launch():
    
    #Titre, grille et menu
    def __init__(self, gui, nb_missing_values):
        

        #Titre et paramètres
        self.gui = gui
        gui.geometry('300x300')
        gui.title("Sudoku Solver")

       
    
        #initialisation des valeurs de la grille de l'interface graphique
        for y in range(len(grid)): #parcourt les lignes
            for x in range(len(grid)): #parcourt les colonnes
                grid[y][x] = StringVar(gui) 

        self.nb_missing_values = nb_missing_values
        self.solved_grid = [[]]
        self.newGrid()
        self.solve_mode = False

        
        #configuration du menu
        menu = Menu(gui)
        gui.config(menu = menu)

        file = Menu(menu)
        menu.add_cascade(label = 'Fichier', menu = file)
        file.add_command(label = 'Nouvelle grille', command = self.newGrid)
        file.add_command(label = 'Résoudre la grille', command = self.solveGrid)
        file.add_command(label = 'Quitter', command = gui.quit)


                

    def solveGrid(self):
        has_error = False
        self.solve_mode = True
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j].get() != '' and self.__table[i][j].winfo_class() == "Entry":
                    if not grid[i][j].get() == self.solved_grid[i][j]:
                        has_error = True
                        self.__table[i][j].config(fg='red')
                    else:
                        self.__table[i][j].config(fg='green')
        if not has_error:
            for i in range(len(grid)):
                for j in range(len(grid)):
                    grid[i][j].set(self.solved_grid[i][j])
    

    #Vérifie si la grille est correcte
    def checkGrid(self, event):
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j].get() == '':
                    continue
                if len(grid[i][j].get()) > 1 or grid[i][j].get() not in ['1','2','3','4','5','6','7','8','9']:
                    grid[i][j].set('')
                else:
                    if self.__table[i][j].winfo_class() == "Entry":
                        if self.solve_mode:
                            if not grid[i][j].get() == self.solved_grid[i][j]:
                                self.__table[i][j].config(fg='red')
                            else:
                                self.__table[i][j].config(fg='green')
                        else:
                            self.__table[i][j].config(fg='blue')
        
      
    #supprime des valeurs
    def newGrid(self):

        self.solved_grid = generate_grid(self.nb_missing_values)
        self.solve_mode = False

        #Grille front-end
        font = ('Arial', 18)
        self.__table = []
        for i in range(len(grid)):
            self.__table += [len(grid)*[0]]

        for i in range(len(grid)):
            for j in range(len(grid)):

                if (i < 3 or i > 5) and (j < 3 or j > 5):
                    color = 'gray'
                elif i in [3,4,5] and j in [3,4,5]:
                    color = 'gray'
                else:
                    color = 'lightgray'

                if grid[i][j].get() == '':
                    self.__table[i][j] = Entry(gui, width = 2, font = font, bg = color, fg='blue', cursor = 'arrow', borderwidth = 0,
                                          highlightcolor = 'yellow', highlightthickness = 1, highlightbackground = 'white',
                                          textvar = grid[i][j]) #permet à l'utilisateur d'entrer des valeurs
                    self.__table[i][j].bind('<Motion>', self.checkGrid)
                    self.__table[i][j].bind('<FocusIn>', self.checkGrid)
                    self.__table[i][j].bind('<Button-1>', self.checkGrid)
                else:
                    self.__table[i][j] = Label(gui, width = 2, font = font, bg = color, borderwidth = 0,
                                         highlightthickness = 1, highlightbackground = 'white',
                                          textvar = grid[i][j])

                self.__table[i][j].grid(row=i, column=j)


gui = Tk() #création de la fenêtre