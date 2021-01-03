'''
This module contains functions for analysing relations
'''


def read_file(path: str) -> list:
    """
    Reads the file that follows this path and returns a list of lists from the
    contents of this file.
    If the path is not a string, then the function returns None
    >>> read_file(1)

    """
    if isinstance(path, str):
        with open(path, 'r') as file_to_read:
            result = []
            #read from csv line by line, rstrip helps to remove '\n' at the end of line
            lines = [line.rstrip() for line in file_to_read] #read the content as a list
            for line in lines:
                digits = line.split(' ') #convert the contents of lines list into smaller lists
                for index in range(0, len(digits)):
                    digits[index] = int(digits[index]) #convert each list item to an integer
                result.append(digits) #add the converted lists to the result list
            return result

    return None


def find_reflexive(matrix: list) -> list:
    """
    Returns a reflexive closure for a given matrix.
    If the matrix is not a list, then the function returns None.
    >>> find_reflexive([[0, 0, 0],[0, 0, 0],[0, 0, 0]])
    [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    >>> find_reflexive([[1,1,0,1],[0,0,0,0],[0,1,0,1],[1,0,0,1]])
    [[1, 1, 0, 1], [0, 1, 0, 0], [0, 1, 1, 1], [1, 0, 0, 1]]
    >>> find_reflexive((0, 1, 0, 1, 0, 1, 1, 1, 1))

    """
    if isinstance(matrix, list):
        new_matrix = []
        size = len(matrix)
        for i in range(size):
            new_matrix.append([])
            for j in range(size):
                if i == j:
                    new_matrix[i].append(1) #if the number is on the main diagonal, it changes to 1
                else:
                    new_matrix[i].append(matrix[i][j]) #in other case, elements of list dont change
        return new_matrix #return a new matrix with a reflexive closure.
    return None


def write_file(matrix: list, path: str):
    """
    This function writes the matrix into a file. If path is not str, the \
    function returns None
    >>> write_file([], 'name.csv')

    """
    with open(path, "w") as file:
        for ind, row in enumerate(matrix):
            row = list(map(str, row))
            row = " ".join(row)
            if ind == len(matrix) - 1:
                file.write(row)
            else:
                file.write(row + "\n")


def find_equal(matrix: list) -> list:
    """
    Returns list of lists, that contain elements of equivalence class
    >>> find_equal([[1, 1, 0], [1, 1, 0], [0, 0, 1]])
    [[0, 1], [2]]
    """
    result = {}
    for ind, elem in enumerate(matrix):
        if tuple(elem) in result:
            result[tuple(elem)].append(ind)
        else:
            result[tuple(elem)] = [ind]
    return list(result.values())


def find_symmetric(matrix: list) -> list:
    '''
    Returns a symmetrical closure for a given matrix
    >>> find_symmetric([[0, 0, 1], [1, 0, 0], [0, 0, 1]])
    [[0, 1, 1], [1, 0, 0], [1, 0, 1]]
    >>> find_symmetric([[0, 0, 0, 1],[1, 1, 0, 0],[1, 0, 0, 1],[0, 0, 1, 0]])
    [[0, 1, 1, 1], [1, 1, 0, 0], [1, 0, 0, 1], [1, 0, 1, 0]]
    '''
    symmetric_matrix = []
    for row in matrix:
        symmetric_matrix.append(list(row))

    size = len(matrix)
    for i in range(size):
        for j in range(size):
            if matrix[i][j] == 1:
                symmetric_matrix[j][i] = 1

    return symmetric_matrix


def find_transitive (matrix: list) -> list:
    '''
    Returns matrix, that represents transitive closure of given relation
    >>> find_transitive([[0, 0, 1], [1, 0, 0], [0, 0, 1]])
    [[0, 0, 1], [1, 0, 1], [0, 0, 1]]
    '''
    transitive_matrix = []
    size = len(matrix)
    for i in range(size):
        transitive_matrix.append([])
        for j in range(size):
            transitive_matrix[i].append(matrix[i][j])

    for k in range(size):
        for i in range(size):
            for j in range(size):
                if transitive_matrix[i][j] or (transitive_matrix[i][k] and transitive_matrix[k][j]):
                    transitive_matrix[i][j] = 1

    return transitive_matrix


def check_transitive (matrix: list) -> bool:
    '''
    Returns True if relation is transitive and False in other case
    >>> check_transitive([[0, 0, 1], [1, 0, 0], [0, 0, 1]])
    False
    >>> check_transitive([[0, 0, 1], [0, 0, 0], [0, 0, 1]])
    True
    '''
    size = len(matrix)

    for k in range(size):
        for i in range(size):
            for j in range(size):
                if not matrix[i][j] and (matrix[i][k] and matrix[k][j]):
                    return False

    return True


def  generate_matrix(matrix: list, num: int, size: int) -> list:
    '''
    Generates all transitive matrixes
    '''
    for i in range(2):
        matrix[(num - 1) // size][(num - 1) % size] = i
        transitive = True
        if i == 1:
            for j in range((num - 1) // size):
                if matrix[j][(num - 1) // size] and not matrix[j][(num - 1) % size]:
                    transitive = False
                    break
            if transitive and (num - 1) % size < (num - 1) // size:
                for j in range((num - 1) % size):
                    if matrix[(num - 1) % size][j] and not matrix[(num - 1) // size][j]:
                        transitive = False
                        break
        else:
            for j in range(min((num - 1) % size,(num - 1) // size)):
                if matrix[(num - 1) // size][j] and matrix[j][(num - 1) % size]:
                    transitive = False
                    break

        if transitive:
            if num != size ** 2:
                yield from generate_matrix(matrix, num + 1, size)
            else:
                yield matrix


def count_transitive (num: int) -> int:
    '''
    Returns number if all transitive relations on num elements
    >>> count_transitive(1)
    2
    >>> count_transitive(2)
    13
    '''
    starter_matrix = []

    for index in range(num):
        starter_matrix.append([])
        for _ in range(num):
            starter_matrix[index].append(0)

    all_matrixes = generate_matrix(starter_matrix, 1, num)
    transitive = 0

    for _ in all_matrixes:
        transitive += 1

    return transitive
