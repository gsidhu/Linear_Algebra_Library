## Linear Algebra Library
## MIT License, 2014 Gurjot S. Sidhu

class matrix(object):
    def __init__(self, string):
        '''
        Returns a 2-D matrix from a string of data.

        Example:
        >>> A = matrix("1 2 3;4 5 6; 7 8 9")
        >>> A.show()
        [1, 2, 3]
        [4, 5, 6]
        [7, 8, 9]
        
        '''
        self.matrix = []
        test = string.split(';')
        for i in range(0, len(test)):
            test[i] = test[i].strip()
            self.matrix.append(test[i].split(' '))
        for i in self.matrix:
            for j in range(0, len(i)):
                i[j] = float(i[j])

        self.rows = len(test)
        self.cols = len(test[0].split(' '))

## Matrix input
##        for i in range(len(A)):
##            row = A[i]
##            elements = row.split(' ')
##            for j in range(len(elements)):
##                self.matrix.append(int(elements[j]))
##        self.rows = len(A)
##        self.cols = len(A[0].split(' '))
##        
                  
    def length(self):
        return self.rows
                       
    def show(self):
        '''
        Prints a matrix object.
        '''
        for i in self.matrix:
            print(i, sep='\n')

    def shape(self):
        return (self.rows, self.cols)

    def __add__(self, B, print_matrix=True):
        '''
        Adds two matrices.

        This method does not alter the initial matrix.
        '''
        if self.shape() != B.shape():
            raise ValueError("Matrices have different shapes.")
        
        C = zero(self.shape()) 
        for i in range(0, self.rows):
            for j in range(0, self.cols):
                C.matrix[i][j] = self.matrix[i][j] + B.matrix[i][j]
        if print_matrix == True:
            C.show()
        return C

    def __sub__(self, B, print_matrix=True):
        '''
        Subtracts two matrices.
        This method does not alter the initial matrix.
        '''
        if self.shape() != B.shape():
            raise ValueError("Matrices have different shapes.")
        
        C = zero(self.shape())
        for i in range(0, self.rows):
            for j in range(0, self.cols):
                C.matrix[i][j] = self.matrix[i][j] - B.matrix[i][j]
        if print_matrix == True:
            C.show()
        return C

    def __mul__(self, B, print_matrix=True):
        '''
        Multiplies two matrices.
        '''
        if self.cols != B.rows:
            raise ValueError("Matrices have different shapes. Cannot multiply these matrices.")

        temp = B.transpose(print_matrix=False)
        C = zero((self.rows,B.cols))

        for i in range(C.rows):
            for j in range(C.cols):
                C.matrix[i][j] = self.row(i,print_matrix=False).inner(B.column(j,print_matrix=False).transpose(print_matrix=False))
                
        if print_matrix == True:
            C.show()
        return C

    def __pow__(self,n):
        '''
        Raises the matrix to the given power
        '''
        while n > 0:
            C = self.__mul__(self,print_matrix=False)
            n -= 1
        C.show()
        return C

    def __contains__(self,x):
        '''
        Returns boolean if given element lies in the matrix
        '''
        for i in range(self.rows):
            for j in range(self.cols):
                if self.matrix[i][j] == x:
                    return True
        return False

    def transpose(self, print_matrix=True):
        '''
        Transpose a matrix.
        This method does not alter the initial matrix.
        '''
        C = zero((self.cols, self.rows))
        
        for i in range(0, self.rows):
            for j in range(0, self.cols):
                C.matrix[j][i] = self.matrix[i][j]
        if print_matrix == True:
            C.show()
        return C

    
    def is_symmetric(self):
        '''
        Boolean
        '''
        temp = self.subtract(self.transpose())
        for i in range(temp.length()):
            for j in range(temp.length()):
                if temp.matrix[i][j] != 0:
                    return False
        return True

    def is_diagonal(self):
        '''
        Boolean
        '''
        true = 0
        for i in range(self.rows):
            for j in range(self.cols):
                if i != j:
                    if self.matrix[i][j] == 0:
                        true = 1
                    else:
                        true = 0
        if true == 1:
            return True
        return False

    def is_square(self):
        '''
        Boolean
        '''
        if self.rows == self.cols:
            return True
        return False
                
    def row_exchange(self, row, print_matrix=True):
        '''
        Exchange the first row (index 0) with the row with the given index

        Example:
        >>> A = matrix("1 2 3;4 5 6")
        >>> A.row_exchange(1)
        [3, 4, 5]
        [1, 2, 3]
        '''
        temp = self.matrix[0]
        self.matrix[0] = self.matrix[row]
        self.matrix[row] = temp

        if print_matrix == True:
            self.show()
        return self

    def column(self, col, print_matrix=True):
        '''
        Returns the column at the given index
        Index starts at 0

        Example:
        >>> A = matrix("1 2;3 4;5 6")
        >>> A.column(1)
        [2]
        [4]
        [6]
        '''
        string = ''
        for i in range(self.rows):
            string += str(self.matrix[i][col]) + ' '
        string = string.rstrip(' ')

        C = matrix(string).transpose(print_matrix=False)

        if print_matrix == True:
            C.show()
        return C

    def row(self, row, print_matrix=True):
        '''
        Returns the row at the given index
        Index starts at 0

        Example:
        >>> A = matrix("1 2 3;3 4 5;5 6 7")
        >>> A.row(2)
        [5, 6, 7]
        '''
        temp = self.transpose(print_matrix=False)
        C = temp.column(row, print_matrix=False) 
        return C.transpose(print_matrix=False)

    def add_row(self, string, print_matrix=True):
        '''
        Adds the given row string to the self matrix
        '''
        temp = self.matrix_string() + ";"
        temp += string
        
        return matrix(temp)
    
    def matrix_string(self):
        '''
        Returns the input matrix in the string form
        '''
        string = ''
        for i in range(self.rows):
            for j in range(self.cols):
                string += str(self.matrix[i][j]) + ' '
            string = string.rstrip(" ") + ";"
        string = string.rstrip(" ;")
        return string
            
        
    def dot(self,B, print_matrix=True):
        '''
        Return the dot product of the two arrays A and B
        This method does not alter the initial matrices.

        Example:
        >>> A = matrix("1 2 3")
        >>> B = matrix("3 2 1")
        >>> A.dot(B)
        [3 4 3]
        '''
        if self.shape() != B.shape():
            raise ValueError("Matrices have different shapes.")

        
        C = zero(self.shape())
        
        for i in range(self.rows):
            for j in range(B.cols):
                var = self.matrix[i][j] * B.matrix[i][j]
                C.matrix[i][j] = var

        if print_matrix == True:
            C.show()
            
        return C

    def inner(self,B):
        '''
        Returns the dot product of the two arrays A and B
        Valid only for 1-D row vectors
        '''
        product = 0
        temp = self.dot(B, print_matrix=False)
        
        for i in range(temp.rows):
            for j in range(temp.cols):
                product += temp.matrix[i][j]
        return product

    

    def norm(self,roundto=5):
        '''
        Normalises a vector
        '''
        vector = self.transpose(print_matrix=False).matrix[0]
        largest = sorted(vector,reverse=True)[0]
        
        for i in range(len(vector)):
            self.matrix[i][0] = round((self.matrix[i][0]/largest), roundto)
        
        return self
        
        
    def eig_max(self):
        '''
        Return the largest eigenvalue of the given matrix using Power Method
            A^(m+1)X . Y
        e = ------------
             A^(m)X . Y
        '''

        X = matrix("1;0")
        Y = matrix("1;0")
        m = 10
        Am = self.__mul__(X,print_matrix=False)
        while m > 1:
            Am = self.__mul__(Am,print_matrix=False)
            m -= 1
        Am1 = self.__mul__(Am,print_matrix=False)

        num = num.dot(Y,print_matrix=False)
        den = den.dot(Y,print_matrix=False)
        eig = num.matrix[0][0]/den.matrix[0][0]

        
        return round(eig,5)

    
##        v = matrix("1;1")
##        eig = [0,0]
##        v = self.multiply(v,print_matrix=False)
##        row = v.transpose(print_matrix=False).matrix[0]
##        row = sorted(row,reverse=True)
##        if abs(row[-1]) > abs(row[0]):
##            eig[1] = row[-1]
##        else:
##            eig[1] = row[0]
##        
##        while True:
##            v = self.multiply(v,print_matrix=False)
##            row = v.transpose(print_matrix=False).matrix[0]
##            eig[0] = eig[1]
##            eig[1] = (sorted(row,reverse=True)[0])
##            v.norm()
##            
##            if abs(eig[1] - eig[0]) < 0.00001:
##                break
##        return eig[1]    

            
## Identity Matrix
def identity(size):
      '''
      Returns an identity matrix of given size
      '''
      string = ''
      for i in range(size):
          for j in range(size):
              if i == j:
                  string += '1 '
              else:
                  string += '0 '
          
          string += ';'
      string = string.rstrip(" ;")
      
      C = matrix(string)
      return C
      


def zero(size):
      '''
      Returns a zero matrix of given size tuple (rows, cols)

      Example:
      >>> Z = zero((2,3))
      >>> Z.show()
      [0, 0, 0]
      [0, 0, 0]
      '''
      
      string = '0 '*size[1] + ';'
      string = string*size[0]
      string = string.rstrip(' ;')
      
      A = matrix(string)
      return A
