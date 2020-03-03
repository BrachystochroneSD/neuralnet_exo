import random

class Matrix:
    def __init__(self,rows,columns):
        self.rows=rows
        self.columns=columns
        self.data=[]
        for i in range(rows):
            temprow=[]
            for j in range(columns):
                temprow.append(0)
            self.data.append(temprow)

    def __str__(self):
        printing=""
        for row in self.data:
            printing+="|"
            for col in row:
                printing+= " " + str(round(col,2))
            printing+="|\n"
        return printing

    def __iadd__ (self,other):
        if type(other) is int or float:
            for i in range(self.rows):
                for j in range(self.columns):
                    self.data[i][j] += other
        elif type(other) is Matrix:
            if other.rows == self.rows and other.columns == self.columns:
                for i in range(self.rows):
                    for j in range(self.columns):
                        self.data[i][j] += other.data[i][j]
            else:
                raise Exception("Error: m need to be same row and same columns num")
        else:
            raise Exception("m is not an int nor a Matrix")

    def __add__ (self,other):
        if type(other) is int or float:
            res = Matrix(self.rows,self.columns)
            for i in range(self.rows):
                for j in range(self.columns):
                    res.data[i][j] = self.data[i][j] + other
            return res
        elif type(other) is Matrix:
            if other.rows == self.rows and other.columns == self.columns:
                res = Matrix(self.rows,self.columns)
                for i in range(self.rows):
                    for j in range(self.columns):
                        res.data[i][j] = self.data[i][j] + other.data[i][j]
                return res
            else:
                raise Exception("Error: m need to be same row and same columns num")
        else:
            raise Exception("m is not an int nor a Matrix")

    def __isub__ (self,other):
        if type(other) is int or float:
            for i in range(self.rows):
                for j in range(self.columns):
                    self.data[i][j] -= other
        elif type(other) is Matrix:
            if other.rows == self.rows and other.columns == self.columns:
                for i in range(self.rows):
                    for j in range(self.columns):
                        self.data[i][j] -= other.data[i][j]
            else:
                raise Exception("Error: m need to be same row and same columns num")
        else:
            raise Exception("m is not an int nor a Matrix")

    def __sub__ (self,other):
        if type(other) is int or float:
            res = Matrix(self.rows,self.columns)
            for i in range(self.rows):
                for j in range(self.columns):
                    res.data[i][j] = self.data[i][j] - other
            return res
        elif type(other) is Matrix:
            if other.rows == self.rows and other.columns == self.columns:
                res = Matrix(self.rows,self.columns)
                for i in range(self.rows):
                    for j in range(self.columns):
                        res.data[i][j] = self.data[i][j] - other.data[i][j]
                return res
            else:
                raise Exception("Error: m need to be same row and same columns num")
        else:
            raise Exception("m is not an int nor a Matrix")

    def __imul__(self,other):
        try:
            newmat = Matrix(self.rows,self.columns)
            for i in range(self.rows):
                for j in range(self.columns):
                    newmat.data[i][j] = self.data[i][j] * other
        except TypeError:
            print("'*=' operation only handle int or float")

    def __mul__(self,other):
        if type(other) is Matrix:
            if self.columns == other.rows:
                newmat=Matrix(self.rows,other.columns)
                for i in range(self.rows):
                    for j in range(other.columns):
                        tempsum=0
                        for b in range(self.columns): # or metruc.tows
                            tempsum+=self.data[i][b]*other.data[b][j]
                        newmat.data[i][j]=tempsum
                return newmat
            else:
                raise ValueError
        elif type(other) is int or float:
            newmat = Matrix(self.rows,self.columns)
            for i in range(self.rows):
                for j in range(self.columns):
                    newmat.data[i][j] = self.data[i][j] * other
        else:
            raise TypeError

    @staticmethod
    def fromArray(inputs):
        m = Matrix(len(inputs),1)
        for i in range(m.rows):
            m.data[i][0]=inputs[i]
        return m

    def toArray(self):
        arr=[]
        for i in range(self.rows):
            for j in range(self.columns):
                arr.append(self.data[i][j])
        return arr


    def randomize(self,n = 1):
        for i in range(self.rows):
            for j in range(self.columns):
                self.data[i][j]+=random.uniform(-n,n)

    def transpose(self):
        tempmatrix=[]
        for j in range(self.columns):
            temprow=[]
            for i in range(self.rows):
                temprow.append(self.data[i][j])
            tempmatrix.append(temprow)
        self.data=tempmatrix
        self.rows,self.columns = self.columns,self.rows

    @staticmethod
    def map(func,matrix):
        if type(matrix) is not Matrix:
            raise Exception(matrix," is not a matrix")
        else:
            m=Matrix(matrix.rows,matrix.columns)
            for i in range(m.rows):
                for j in range(m.columns):
                    m.data[i][j]=func(matrix.data[i][j])
            return m
