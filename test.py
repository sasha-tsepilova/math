from project import *

if __name__ =='__main__':
    import time
    start = time.time()
    to_read = 'rel_1500_0.45.csv'
    matrix = read_file('task6_data/' + to_read)
    write_file(find_reflexive(matrix), 'after/'+ to_read[:-4] + '/reflexive.csv')
    symmetric = find_symmetric(matrix)
    write_file(symmetric, 'after/'+ to_read[:-4] + '/symmetric.csv')
    transitive = find_transitive(matrix)
    write_file(transitive, 'after/'+ to_read[:-4] + '/transitive.csv')
    equal = find_reflexive(find_transitive(symmetric)) 
    write_file(equal, 'after/'+ to_read[:-4] + '/equal.csv' )
    with open('after/'+ to_read[:-4] + '/analytics.csv', 'w') as to_write:
        to_write.write('transitive: ' + str(check_transitive(transitive)) +'\n' + 'equal classes: ' + str(find_equal(equal)) + '\n')
        to_write.write('time for analys: ' + str(time.time() - start))
