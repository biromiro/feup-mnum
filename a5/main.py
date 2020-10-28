# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def gaussMethod(matrix):
    for i in range(len(matrix)):
        divFactor = matrix[i][i]
        for k in range(i, len(matrix[0])):
            matrix[i][k] /= divFactor
        for j in range(i+1,len(matrix)):
            subFactor = matrix[j][i]
            for k in range(i, len(matrix[0])):
                matrix[j][k] -= subFactor*matrix[i][k]

    return matrix

def rotateMatrix(matrix):
    newMatrix = [];
    innerMatrix = [];
    for i in reversed(range(len(matrix))):
        for j in reversed(range(len(matrix[i])-1)):
            innerMatrix.append(matrix[i][j])
        innerMatrix.append(matrix[i][-1])
        newMatrix.append(innerMatrix)
        innerMatrix = [];
    return newMatrix

def getSolutionsAfterGaussJordan(matrix):
    solMatrix = []
    for i in range(len(matrix)):
        solMatrix.append(matrix[i][-1])
    return solMatrix
    #for i in reversed(range(len(matrix)-1)):>



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    matrix = [[3,-1,2,-1],[1,1,1,8],[2,0,1,5]]
    print(getSolutionsAfterGaussJordan(rotateMatrix(gaussMethod(rotateMatrix(gaussMethod(matrix))))))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
