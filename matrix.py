class Matrix:
    def __init__(self, mat):
        self.mat = mat
        if isinstance(mat[0], list):
            self.rows = len(mat)
            self.cols = len(mat[0])
        else:
            self.rows = len(mat)
            self.cols = 1
    
    def __str__(self):
        for i in range(self.rows):
            print(self.mat[i])
        return ""

    def __add__(self, other):
        mat = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self.mat[i][j] + other.mat[i][j])
            mat.append(row)
        return Matrix(mat)

    def __sub__(self, other):
        mat = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self.mat[i][j] - other.mat[i][j])
            mat.append(row)
        return Matrix(mat)

    def __mul__(self, other):
        mat = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                if isinstance(other, Matrix):
                    cell = 0
                    for k in range(self.rows):
                        cell += self.mat[i][k] * other.mat[k][j]
                    row.append(cell)
                elif isinstance(other, int):
                    row.append(other*self[i,j])
            mat.append(row)
        return Matrix(mat)

    def __rmul__(self, other):
        return self * other

    def __getitem__(self, index):
        if isinstance(index, int):
            if self.rows == 1:
                return self.mat[0][index]
            elif self.cols == 1:
                return self.mat[index][0]
            else:
                return Matrix([self.mat[index]])
        elif isinstance(index, tuple):
            return self.mat[index[0]][index[1]]
    
    def __setitem__(self, index, value):
        if isinstance(index, tuple):
            self.mat[index[0]][index[1]] = value

    def row(self, m):
        return self[m]

    def col(self, n):
        mat = []
        for i in range(self.rows):
            mat.append(self[i][n])
        return Matrix(mat)

    def zeros(m, n):
        mat = []
        for i in range(m):
            mat.append([0]*n)
        return Matrix(mat)

    def identity(n):
        mat = Matrix.zeros(n,n)
        for i in range(n):
            mat[i,i] = 1
        return mat

    def isSquare(self):
        return self.rows == self.cols

    def transpose(self):
        mat = Matrix.zeros(self.cols, self.rows)
        for i in range(self.cols):
            for j in range(self.rows):
                mat[i,j] = self[j,i]
        return mat

    def subMatrix(self, x, y):
        mat = []
        for i in range(self.rows):
            if i == x:
                continue
            row = []
            for j in range(self.cols):
                if j != y:
                    row.append(self.mat[i][j])
            mat.append(row)
        return Matrix(mat)

    def determinant(self):
        if self.isSquare():
            if self.rows == 1:
                return self[0,0]
            else:
                det = 0
                for j in range(self.cols):
                    det += (-1)**(j) * self[0,j] * self.subMatrix(0,j).determinant()
                return det







m = Matrix([[1,2,3],[4,5,6]])
print(m)
print(m.transpose())
print(2*Matrix.identity(3))
m1 = Matrix([[3,9,27,81],[1,1,1,1],[-2,4,-8,16],[2,4,8,16]])
print(m1)
print(m1.determinant())