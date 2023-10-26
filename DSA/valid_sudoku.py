       
def check_columns(arr):

    i = 0

    while i < len(arr[0]):

        col_dic = {}

        for j in range(len(arr)):

            if arr[j][i] == ".":

                continue

            elif arr[j][i] in col_dic:

                col_dic[arr[j][i]] += 1
            
            else:

                col_dic[arr[j][i]] = 1
            
        # print(col_dic.values())
        if len(col_dic.values()) == 0:

            i += 1

            continue

        lis = sorted(col_dic.values())

        if lis[-1] != 1:

            return False

        i += 1
    return True

def check_rows(arr):

    i = 0

    while i < len(arr[0]):

        row_dic = {}

        for j in range(len(arr)):

            if arr[i][j] == ".":

                continue

            elif arr[i][j] in row_dic:

                row_dic[arr[i][j]] += 1
            
            else:

                row_dic[arr[i][j]] = 1
            
        # print(col_dic.values())
        lis = sorted(row_dic.values())

        if len(row_dic.values()) == 0:

            i += 1

            continue

        if lis[-1] != 1:

            return False

        i += 1
    return True

def check_block(arr):

    row_len = len(arr)

    column_len = len(arr[0])

    row_itr1 = 0

    column_itr1 = 0

    while column_itr1 < column_len:

        row_itr1 = 0

        while row_itr1 < row_len:

            column_itr2 = column_itr1

            count_ele = {}

            while column_itr2 < column_itr1 + 3:

                row_itr2 = row_itr1

                while row_itr2 < row_itr1 + 3:

                    element = arr[column_itr2][row_itr2]

                    if element == ".":

                        row_itr2 +=1

                        continue
                    
                    elif element in count_ele:

                        count_ele[element] += 1

                    else:

                        count_ele[element] = 1

                    row_itr2 +=1

                column_itr2 +=1
            
            count = sorted(count_ele.values())

            if len(count_ele.values()) == 0:

                row_itr1 += 3

                continue

            if count[-1] != 1:

                return False

            row_itr1 += 3
        
        column_itr1 += 3

    return True


def valid_sudoku(arr):
        
    if check_columns(arr):

        if check_rows(arr):

            if check_block(arr):

                return True


    return False

arr = [["5","3",".",".","7",".",".",".","."],
       ["6",".",".","1","9","5",".",".","."],
       [".","9","8",".",".",".",".","6","."],
       ["8",".",".",".","6",".",".",".","3"],
       ["4",".",".","8",".","3",".",".","1"],
       ["7",".",".",".","2",".",".",".","6"],
       [".","6",".",".",".",".","2","8","."],
       [".",".",".","4","1","9",".",".","5"],
       [".",".",".",".","8",".",".","7","9"]]

print(valid_sudoku(arr))

arr = [["5","3",".",".","7",".","6",".","."],
       ["6",".",".","1","9","5",".",".","."],
       [".","9","8",".",".",".",".","6","."],
       ["8",".",".",".","6",".",".",".","3"],
       ["4",".",".","8",".","3",".",".","1"],
       ["7",".",".",".","2",".",".",".","6"],
       [".","6",".",".",".",".","2","8","."],
       [".",".",".","4","1","9",".",".","5"],
       [".",".",".",".","8",".",".","7","9"]]

print(valid_sudoku(arr))

arr = [["5","3",".",".","7",".",".",".","9"],
       ["6",".",".","1","9","5",".",".","."],
       [".","9","8",".",".",".",".","6","."],
       ["8",".",".",".","6",".",".",".","3"],
       ["4",".",".","8",".","3",".",".","1"],
       ["7",".",".",".","2",".",".",".","6"],
       [".","6",".",".",".",".","2","8","."],
       [".",".",".","4","1","9",".",".","5"],
       [".",".",".",".","8",".",".","7","9"]]

print(valid_sudoku(arr))

arr = [["8","3",".",".","7",".",".",".","."]
      ,["6",".",".","1","9","5",".",".","."]
      ,[".","9","8",".",".",".",".","6","."]
      ,["8",".",".",".","6",".",".",".","3"]
      ,["4",".",".","8",".","3",".",".","1"]
      ,["7",".",".",".","2",".",".",".","6"]
      ,[".","6",".",".",".",".","2","8","."]
      ,[".",".",".","4","1","9",".",".","5"]
      ,[".",".",".",".","8",".",".","7","9"]]

print(valid_sudoku(arr))