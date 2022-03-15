import numpy as np


def wagner_fischer(seq1, seq2):
    # Finding dimensions of matrix to be filled, add 1 since we start from zero
    n = len(seq1) + 1
    m = len(seq2) + 1

    # initialize EDMatrix matrix

    # deleting all characters and inserting all characters
    EDMatrix = np.zeros(shape=(n, m), dtype=np.float)  # fill the matrix with zeros
    EDMatrix[:, 0] = range(n)  # filling first column from 0 till n i.e. deleting all chars
    EDMatrix[0, :] = range(m)  # filling first row from 0 till m i.e. inserting all chars

    # Wagner and Fisher algorithm to calculate edit distance
    for i, l_1 in enumerate(seq1, start=1):
        for j, l_2 in enumerate(seq2, start=1):
            deletion = EDMatrix[i-1, j] + 1  # cost of deletion is 1 + cost of previous cell
            insertion = EDMatrix[i, j-1] + 1  # cost of insertion is 1 + cost of previous cell
            # cost of previous cell + calculated cost (to take ambiguity into consideration)
            update = EDMatrix[i-1, j-1] + (calculate_update_cost(l_1, l_2))
            # minimum distance between three operations
            minimum_op = np.min([deletion, insertion, update])
            # adding cost to the edit distance matrix
            EDMatrix[i, j] = minimum_op
    ED = EDMatrix[n-1][m-1]
    Sim = 1/(1+ED)
    return Sim


def calculate_update_cost(char1, char2):
    ambiguous = ["R", "S", "M", "V", "N"]  # ambiguous characters
    unambiguous = ["A", "C", "T", "G"]  # Unambiguous characters
    if char1 in unambiguous and char2 in unambiguous:  # if both chars are not ambiguous
        # if they are equal, update cost is zero, else cost is 1
        if char1 == char2:
            return 0
        else:
            return 1
    else:  # one of them is ambiguous
        if char2 in ambiguous:
            temp = char1
            char1 = char2
            char2 = temp
        if char1 == "R":
            if char2 in ["A", "R", "G"]:
                return 0.5  # if char2 is one of 'R; possibilities, avg cost is 0.5
            elif char2 in unambiguous:
                return 1
            else:
                if char2 in ["M", "S", "N"]:
                    return 0.75
                elif char2 == "V":
                    return 0.67
        if char1 == "S":
            if char2 in ["C", "S", "G"]:
                return 0.5
            elif char2 in unambiguous:
                return 1
            else:
                if char2 in ["M", "R", "N"]:
                    return 0.75
                elif char2 == "V":
                    return 0.67
        if char1 == "M":
            if char2 in ["C", "M", "A"]:
                return 0.5
            elif char2 in unambiguous:
                return 1
            else:
                if char2 in ["S", "R", "N"]:
                    return 0.75
                elif char2 == "V":
                    return 0.67
        if char1 == "V":
            if char2 in ["G", "C", "V", "A"]:
                return 0.33
            elif char2 in unambiguous:
                return 1
            else:
                if char2 in ["S", "R", "M"]:
                    return 0.67
                elif char2 == "N":
                    return 0.75
        if char1 == "N":
            if char2 in ["G", "C", "N", "A", "U"]:
                return 0.25
            elif char2 in unambiguous:
                return 1
            else:
                return 0.75
    return 0
