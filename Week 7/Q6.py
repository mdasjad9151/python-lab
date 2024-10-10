
def swap_lines(file1, file2):

    with open(file1, 'r') as f1:
        lines_file1 = f1.readlines()
    
 
    with open(file2, 'r') as f2:
        lines_file2 = f2.readlines()

    
    middle_index_file1 = len(lines_file1) // 2

    
    last_index_file2 = len(lines_file2) - 1

    lines_file1[middle_index_file1], lines_file2[last_index_file2] = lines_file2[last_index_file2], lines_file1[middle_index_file1]

    with open(file1, 'w') as f1:
        f1.writelines(lines_file1)
    
    
    with open(file2, 'w') as f2:
        f2.writelines(lines_file2)


file1 = "Week 7\\file1.txt"
file2 = 'Week 7\\file2.txt'

swap_lines(file1, file2)
