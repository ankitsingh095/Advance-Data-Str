from collections import deque
#this import is for maze problem



class QueensProblems:
    def __init__(self, n):
        self.n = n
        self.chess_table = [[None for i in range(n)] for j in range(n)]
        #list comprehension for 2 dimentional array
    def solve_n_queens(self):

        #we start with the first queen (with index 0)
        if self.solve(0):
            self.print_queens()
        else:
            #when we have considered all the possible configurations without a success
            #then it means there is no solution(3x3 with 3 queens)
            print('There is no solution to the problem...')


    #col_index is the same as the index of the queen
    def solve(self, col_index):

        #we have solved the problem - base case
        if col_index == self.n:
            return True

        #lets try to find a position for queen (col_index) within a given column
        for row_index in range(self.n):
            if self.is_place_valid(row_index, col_index):
                #1 means that there is a queen at the given location
                self.chess_table[row_index][col_index] = 1

                # we call the same function with col_index + 1
                # we try to find the location of the next queen in the next column
                if self.solve(col_index+1):
                    return True

                # BACKTRACKING
                self.chess_table[row_index][col_index] = 0
                #here we backtracked to the begining using 0 or None

        #when we have considered all the rows in a col without
        # finding a valid cell for the queen
        return False

    def is_place_valid(self, row_index, col_index):
        #check the rows (whether given queens can attack each other horizontally)
        #it means that there is already at least 1 queen in that given row
        for i in range(self.n):
            if self.chess_table[row_index][i] ==1:
                return False

        #we do not have to check the same column because we implement the problem
        #such that we assign 1 in queen to every single column

        #we have to check the diagnols
        # from top left to bottom right
        j=col_index
        for i in range(row_index, -1, -1):

            if i<0:
                break
            if self.chess_table[i][j] == 1:
                return False
            j = j-1



        #we have to check the diagnols
        # from top right to bottom left
        j=col_index
        for i in range(row_index, self.n):

            if j<0:
                break
            if self.chess_table[i][j] == 1:
                return False
            j = j-1

        return True

    def print_queens(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.chess_table[i][j] == 1:
                    print('Q', end='')
                else:
                    print(' - ', end='')
            print('\n')

# if __name__=='__main__':
#     queens = QueensProblems(4)
#     queens.solve_n_queens()



##############################   HAMILTONIAN PROBLEM    ####################

class HamiltonianPath:

    def __init__(self, adjacency_matrix):
        self.n = len(adjacency_matrix)
        self.adjacency_matrix = adjacency_matrix
        self.path = [0]

    def hamiltonian_path(self):

        #starting from 1 cuz we already taken 0 in path
        if self.solve(1):
            self.show_hamiltonian_path()
        else:
            print('There is no solution to the problem...')

    def solve(self, position):

        #BASE CASE
        if position == self.n:
            return True

        for vertex_index in range(1, self.n):
            if self.is_feasible(vertex_index, position):
                #we include vertex (with vertex_index)
                self.path.append(vertex_index)

                if self.solve(position+1):
                    return True

                #when we have to backtrack
                #we have to remove vertex_index from the result(path)

                self.path.pop()

        #if we have considered all the vertexes withot a success
        return False


    def is_feasible(self, vertex, actual_position):
    #check whether is there a connection between the nodes
        if self.adjacency_matrix[self.path[actual_position-1]][vertex] == 0:
            return False

        #whether we have already included that given vertex in the result
        for i in range(actual_position):
            if self.path[i] == vertex:
                return False

        return True


    def show_hamiltonian_path(self):
        for v in self.path:
            print(v)


# if __name__ == '__main__':

    m = [[0, 1, 0, 0, 0, 1],
         [1, 0, 1, 0, 0, 0],
         [0, 1, 0, 0, 1, 0],
         [0, 0, 0, 0, 1, 1],
         [0, 0, 1, 1, 0, 1],
         [1 ,0, 0, 1, 1, 0]]


    # hamiltonian_path = HamiltonianPath(m)
    # hamiltonian_path.hamiltonian_path()





    ##################################     COLORING PROBLEM    ##################





class ColoringProblem:

    def __init__(self, adjacency_matrix, num_colors):
        self.n = len(adjacency_matrix)
        self.adjacency_matrix = adjacency_matrix
        self.num_colors = num_colors
        self.colors = [0 for _ in range(self.n)]


    def coloring_problem(self):

        #we call the solve with first vertex (index 0)
        if self.solve(0):
            self.show_result()
        else:
            print("There is no feasible solution")

    def solve(self, node_index):

        if node_index == self.n:
            return True

        #condiser the colors

        for color_index in range(1, self.num_colors + 1):
            if self.is_color_valid(node_index, color_index):
                self.colors[node_index] = color_index

                if self.solve(node_index + 1):
                    return True


                ###########  BACKTRACKING
                #in this case backtracking means doing "nothing"

        return False


    def is_color_valid(self, node_index, color_index):

        #we have to check that the nodes are connected
        #And we have to check that the given color is not shared
       #with these adjacent nodes
        for i in range(self.n):
            if self.adjacency_matrix[node_index][i] == 1 and color_index == self.colors[i]:
                return False

        return True


    def show_result(self):
        for v, c in zip(range(self.n), self.colors):
            print("Node %d has color value %d" %(v,c))


# if __name__ == '__main__':

    m = [[0, 1, 1, 1],
         [1, 0, 1, 0],
         [1, 1, 0, 1],
         [1, 0, 1, 0]]

    # problem = ColoringProblem(m,10)
    # problem.coloring_problem()






#######################################    KNIGHTS TOUR PROBLEM    ####################



class KnightsTour:

    def __init__(self, board_size):
        self.board_size = board_size
        #possible horizontal components of the moves
        self.x_moves = [2, 1, -1, -2, -2, -1, 1, 2]
        self.y_moves = [1, 2, 2, 1, -1, -2, -2, 1]
        self.solution_matrix = [[-1 for _ in range(self.board_size)] for _ in range(self.board_size)]
        #  -1 means the blocks are empty

    def solve_problem(self):
        #we start with the top first cell
        self.solution_matrix[0][0] = 0

        #first parameter is the step counter
        #second and third is the location (0,0) ==> (row --, column |)
        if self.solve(1, 0, 0):
            self.print_solution()
        else:
            print("There is no any feasible solution...")

    def solve(self, step_counter, x, y):

        #base cases (N*N = total no of blocks hence last block)
        if step_counter == self.board_size * self.board_size:
            return True

        #we have to consider all the possible moves and find the valid one
        for move_index in range(len(self.x_moves)):
            #we can use .y_moves as well

            next_x = x + self.x_moves[move_index]
            next_y = y + self.y_moves[move_index]

            if self.is_valid_move(next_x, next_y):
                #it is a valid step so we can update the solution_matrix
                self.solution_matrix[next_x][next_y] = step_counter

                if self.solve(step_counter+1, next_x, next_y):
                    return True

                #BACKTRACK as usual if false, so we have to remove the step and
                #reinitialise the solution_matrix with -1

                self.solution_matrix[next_x][next_y] = -1

        return False

    def is_valid_move(self, x, y):

        #that the knight will not step outside the chessboard
        #the knight leaves the board horizontally
        if x < 0 or x >= self.board_size:
            return False

        #the knight leaves the board vertically
        if x < 0 or x >= self.board_size:
            return False

        #maybe we have already visited that given cell
        #which means that the value is not -1

        if self.solution_matrix[x][y] > -1:
            return False
        return True




    def print_solution(self):
        for i in range(self.board_size):
            for j in range(self.board_size):
                print(self.solution_matrix[i][j], end=' ')
            print('\n')




# if __name__ == '__main__':
#     tour = KnightsTour(8)
#     tour.solve_problem()





###############################3#######   MAZE PROBLEM    ##############


class MazeSolver:

    def __init__(self, matrix):
        self.matrix = matrix
        # D(0,1) U(0,-1) L(-1,0) R(1,0)
        self.move_x = [1, 0, 0, -1]
        self.move_y = [0, -1, 1, 0]
        self.visited = [[False for _ in range(len(matrix))] for _ in range(len(matrix))]
        self.min_distance = float('inf')

    def is_valid(self, row, col):

        # outside the table horizontally
        if row < 0 or row >= len(self.matrix):
            return False

        # outside the table vertically
        if col < 0 or col >= len(self.matrix):
            return False

        # obstacle (wall)
        if self.matrix[row][col] == 0:
            return False

        # already visited the given cell
        if self.visited[row][col]:
            return False

        return True

    def search(self, i, j, destination_x, destination_y):

        self.visited[i][j] = True
        # the queue is implemented with a doubly linked list - O(1)
        queue = deque()
        # i is the x coordinate
        # j is the y coordinate
        # why 0? of course because in the first iteration the min_distance is 0
        queue.append((i, j, 0))

        while queue:

            # we take the first item we have inserted
            (i, j, dist) = queue.popleft()

            # if we have reached the destination - we break out of the while loop becase
            # we have found the destination !!!
            if i == destination_x and j == destination_y:
                self.min_distance = dist
                break

            # we are at the location (i,j) we have to make a given move
            # L, U, R, D
            for move in range(len(self.move_x)):
                # we calculate the position ofter the move
                next_x = i + self.move_x[move]
                next_y = j + self.move_y[move]

                # is it possible to make the move to cell with coordinates (next_x, next_y)?
                if self.is_valid(next_x, next_y):
                    # we make the given move (BFS)
                    self.visited[next_x][next_y] = True
                    # we append the move to the queue
                    queue.append((next_x, next_y, dist + 1))

    def show_result(self):
        if self.min_distance != float('inf'):
            print("The shortest path from source to destination: ", self.min_distance)
        else:
            print("No feasible solution - the destination can not be reached!")




if __name__ == '__main__':

    m = [
        [1, 1, 1, 1, 1],
        [0, 1, 1, 1, 1],
        [0, 0, 0, 0, 1],
        [1, 0, 1, 1, 0],
        [0, 0, 0, 1, 1]
        ]

    maze_solver = MazeSolver(m)
    maze_solver.search(0, 0, 4, 4)
    maze_solver.show_result()