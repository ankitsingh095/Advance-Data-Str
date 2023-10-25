
def fibonacci_recursion(n):

    if n == 0:
        return 1

    if n == 1:
        return 1

    return fibonacci_recursion(n-1) + fibonacci_recursion(n-2)
# print(fibonacci_recursion(40))



################  TOP DOWN APPROACH

def fibonacci_memoization(n, table):

    if n not in table:
        #we call this as memoization becase we store results of
        # previously solved sequence
        table[n] = fibonacci_memoization(n-1, table) + fibonacci_memoization(n-2, table)

    #o(1) running time
    return table[n]

t = {0:1, 1:1}
# print(fibonacci_memoization(5, t))



###############  Bottom up approach

def fibonacci_tabulation(n, table):

    for i in range(2, n+1):
        #this is bottom up because we start with 1,1,2,3,5,8.. because
        #we start with least value and goes up.
        table[i] = table[i-1] + table[i-2]
    return table[n]

# t= {0:1, 1:1}
# print(fibonacci_tabulation(8, t))





###############################  KNAPSACK problem using recursion

# m - capacity of the knapsack, w - weights list,
# v - values list, n - number of items we consider

def solve_recursion(m, w, v, n):
    # base cases
    if n == 0 or m == 0:
        return 0

    # the given item can NOT fit into the knapsack
    if w[n - 1] > m:
        return solve_recursion(m, w, v, n - 1)
    else:
        # given item can fit into the knapsack so we have 2 options (include, exclude)
        n_included = v[n - 1] + solve_recursion(m - w[n - 1], w, v, n - 1)
        n_excluded = solve_recursion(m, w, v, n - 1)

        return max(n_included, n_excluded)





class KnapsackProblem:


# O(n*m) time complexity

    def __init__(self, n, M, w, v):
        self.n = n
        self.M = M
        self.w = w
        self.v = v
        self.S = [[0 for _ in range(M+1)] for _ in range(n+1)]
    #this is a list comprehension, creating a 2D list (a list of lists)
    # and initializing it with zeros
    # n + 1 is the number of rows in the 2D list, and M + 1 is the number of columns.

    def solve(self):
        #construct the S dynamic programming table
        for i in range(self.n+1):
            for w in range(self.M+1):
                #here w is weights, not a single weight!
                # print('')
                not_taking_item = self.S[i-1][w]
                taking_item = 0

                if self.w[i] <= w:
                    taking_item = self.v[i] + self.S[i-1][w- self.w[i]]

                #memoization - we store the sub-results to avoid recalculating
                # the same values
                self.S[i][w] = max(not_taking_item, taking_item)

    def show_result(self):
        print("Total Benefit: %d" % self.S[self.n][self.M])
        # middle % is string formatting operator
        # self.S[self.n][self.M]: This expression retrieves a  value from a
        # 2D list(presumably a dynamic programming table)
        # When the % operator is used with a string and a value, it formats the string by
        # replacing the % d placeholder with the value provided.
        w = self.M
        for n in range(self.n, 0, -1):
            if self.S[n][w] != 0 and self.S[n][w] != self.S[n-1][w]:
                print("We take item # %d" % n)
                w = w- self.w[n]


# if __name__ == "__main__":
    # knapsack = KnapsackProblem(3, 4, None, None)
    # print(knapsack.S)

    #here .S is called because S is not in the arguments and if included then
    # details of table will be fixed, and according to problem it is not fixed
    # tables column and rows change with n+1, M+1.
    # there it is called separately to show the table


    # num_of_items = 4
    # knapsack_capacity = 7
    # weights = [0, 1, 3, 4, 5]
    # profits = [0, 1, 4, 5, 7]
    # knapsack = KnapsackProblem(num_of_items, knapsack_capacity, weights, profits)
    # knapsack.solve()
    # knapsack.show_result()






# just a hackerrank problem solution
# class Solution:
#     def rearrange(self, arr):


        # arry = []
        # n = len(arr)
        # i = 0

        # while i % 2 == 0:
        #     if arr[i] < 0:
        #         arry.append
        #         i += 1
        #
        # while i % 2 != 0:
        #     if arr[i] > 0:
        #         arr.append(arr[i])
        #         i += 1


#
#         return arry
#
# pexx = [2,6,-4,-6,2,7,0,-5]
# myobject = Solution
# myobject.rearrange(pexx)




###########################        ROD CUTTING PROBLEM     ##################


class RodCutting:
    def __init__(self, n, p):
        self.n = n
        self.p = p
        self.S = [[0]*(n+1) for _ in range(len(p))]

    def solve(self):

        for i in range(1, len(self.p)):
            #since p, n are instance variable so self is used here in arguments
            for j in range(self.n+1):
                if i<=j:
                    self.S[i][j] = max(self.S[i-1][j], self.p[i] + self.S[i][j-i])
                else:
                    self.S[i][j] = self.S[i-1][j]

    def show_result(self):

        print('Max profit : %d' % self.S[len(self.p) - 1][self.n])

        col_index = self.n
        row_index = len(self.p) - 1

        while col_index > 0 or row_index > 0:
            #we hvet to compare the items right above each other
            # if they are the same values then the given row(piece) is not in the solution
            if self.S[row_index][col_index] == self.S[row_index - 1][col_index]:
                row_index = row_index - 1
            else:
                print("We make cut: ", row_index, "m")
                col_index = col_index -  row_index


# if __name__ == '__main__':
    # problem = RodCutting(5, [0,2,5,7,3,9])
    # problem.solve()
    # problem.show_result()





#################  This is incomplete, will do it later with better understanding
    # def show_result(self):

        # print('Max profit: %d' %([len(self.p)-1][self.n]))

        # col_index = self.n
        # row_index = len(self.p) - 1

        # while col_index > 0 or row_index > 0:











################################################       Subset Sum Problem  ##########


class SubsetSumproblem:

    def __init__(self, nums, m):
        self.nums = nums
        self.m = m
        self.S = [[False  for _ in range(m+1)] for _ in range(len(nums) + 1)]

    def solve(self):

        #initialize the first row and first column
        for i in range(len(self.nums)+1):
            self.S[i][0] = True

        # we have to construct the table with the cells one by one
        #   rowIndex can be replaced I
        # col_index can be replaced as J
        for rowIndex in range(1, len(self.nums)+1):
            for colIndex in range(1, self.m +1):
                if colIndex < self.nums[rowIndex-1]:
                    self.S[rowIndex][colIndex] = self.S[rowIndex-1][colIndex]
                else:
                    if self.S[rowIndex - 1][colIndex]:
                        # this is when we do not include the given item rowIndex
                        self.S[rowIndex][colIndex] = self.S[rowIndex-1][colIndex]
                    else:
                        # do include the item i
                        self.S[rowIndex][colIndex] = self.S[rowIndex-1][colIndex - self.nums[rowIndex-1]]


    def show_result(self):
        print("The problem is feasible: %s" % self.S[len(self.nums)][self.m])

        if not self.S[len(self.nums)][self.m]:
            return

        #print out the items in the subset
        col_index = self.m
        row_index = len(self.nums)

        while col_index > 0 or row_index > 0:
            if self.S[row_index][col_index] == self.S[row_index-1][col_index]:
                row_index = row_index-1
            else:
                print("We take item: %d" % self.nums[row_index - 1])
                col_index = col_index - self.nums[row_index-1]
                row_index = row_index-1

if __name__ == '__main__':

    M = 11
    n = [1, 2, 5, 3]
    problem  = SubsetSumproblem(n, M)
    problem.solve()
    problem.show_result()
