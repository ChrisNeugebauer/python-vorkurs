import time

import numpy as np

class spielDesLebens:

    def __init__(self, rows, columns, generations):
        self.rows = rows
        self.columns = columns
        self.generations = generations

        self.cells = np.random.randint(2, size=(rows, columns))

    def update(self):
        next_gen = self.cells.copy()
        #next_gen = np.zeros(self.cells.shape)

        for row in range(0, self.rows):
            for column in range(0, self.columns): #For each cell:
                neighbor_value = 0
                for i in range(row - 1, row + 2):
                    for j in range(column -1, column + 2):
                        try:
                            neighbor_value += self.cells[i][j]
                        except IndexError:
                            neighbor_value += 0
                #Eigenen Wert von neighbor_value subatrahieren
                neighbor_value -= self.cells[row][column]
                #Game rules
                if self.cells[row][column] == 0 and neighbor_value == 3:
                    next_gen[row][column] = 1
                elif self.cells[row][column] == 1 and neighbor_value < 2:
                    next_gen[row][column] = 0
                elif self.cells[row][column] == 1 and neighbor_value > 3:
                    next_gen[row][column] = 0
                elif self.cells[row][column] == 1 and neighbor_value == 3 or neighbor_value == 2:
                    next_gen[row][column] = 1
                else:
                    next_gen[row][column] = 0

        self.cells = next_gen

    def __str__(self) -> str:
        s = str(self.cells)
        return s

    def run(self):
        #print(self.cells)
        #time.sleep(0.5)
        for x in range(0, self.generations + 1):
            #start = time.thread_time()
            self.update()
            #ende = time.thread_time()
            #laufzeit = ende - start
            #print("Generation (" + str(x) + "/" + str(self.generations) + ") hat " + str(laufzeit) + " Sekunden gedauert")
            #print("\n\n" + "-" *50 + "\n")
            #print(self.cells)
            #time.sleep(0.5)



if __name__ == "__main__":
    testing = True

    if testing is True:
        rows = 5000
        columns = 5000
        generations = 2
    else:
        rows = input("Rows: ")
        columns = input("Columns: ")
        generations = input("Generations: ")

    start = time.thread_time()
    game = spielDesLebens(rows, columns, generations)
    game.run()
    ende = time.thread_time()
    laufzeit = ende - start

    print("-" * 100 + "\n\n" + "Die Simulation hat " + str(laufzeit) + " Sekunden gedauert.\nPro Generation sind das " + str((laufzeit/generations)) + " Sekunden.")
    #game.update()