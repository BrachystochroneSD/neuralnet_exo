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
                printing+= " " + str(col)
            printing+="|\n"
        return printing

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

    def add(self,m):
        if type(m) is int:
            for i in range(self.rows):
                for j in range(self.columns):
                    self.data[i][j]+=m

        elif type(m) is Matrix:
            if m.rows == self.rows and m.columns == self.columns:
                for i in range(self.rows):
                    for j in range(self.columns):
                        self.data[i][j]+=m.data[i][j]
            else:
                raise Exception("Error: m need to be same row and same columns num")
        else:
            "m is not an int nor a Matrix"

    def map(self,func):
        for i in range(self.rows):
            for j in range(self.columns):
                self.data[i][j]=func(self.data[i][j])

    def scalar_multiply(self,n):
        for i in range(self.rows):
            for j in range(self.columns):
                self.data[i][j]*=n

    @staticmethod
    def multiply(metrix,metrux):
        if type(metrux) is Matrix and type(metrix) is Matrix:
            if metrix.columns == metrux.rows:
                newmat=Matrix(metrix.rows,metrux.columns)
                for i in range(metrix.rows):
                    for j in range(metrux.columns):
                        tempsum=0
                        for b in range(metrix.columns): # or metruc.tows
                            tempsum+=metrix.data[i][b]*metrux.data[b][j]
                        newmat.data[i][j]=tempsum
                return newmat
            else:
                raise "Error"
        else:
            raise "Error"
