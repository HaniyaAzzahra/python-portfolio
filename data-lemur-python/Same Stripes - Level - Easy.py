
# Author : Haniya Azzahra 
# Questions : https://datalemur.com/questions/python-same-stripes

def is_same_stripes(matrix):
  diagonals = {}
  for i in range(len(matrix)): # to loop for each row
    for j in range(len(matrix[0])): # to loop for each column
      if i - j in diagonals and diagonals[i - j] != matrix[i][j]: # i-j ->as index diagonal, make sure that each i-j , have exact value based on matrix i, j if not have index value then directly resulted in false
        return False
      else :
        diagonals[i-j] = matrix[i][j] # if have same value then replace the value 
  return diagonals



# diagonals output example
# {0: 1, -1: 2, -2: 3, -3: 4, 1: 2, 2: 1, 3: 1}
