


level = [ ['#','#','#','#','#'],
          ['F','T','#','F','#'],
          ['#','#','#','#','#'],
          ['#','F','#','F','#'],
          ['#','#','#','#','#']
        ]

n_trees = []

def check_tent():
    n_tents = []
    for i in range(len(level)):
        for n in range(len(level)):
            if level[i][n] == 'F':
                n_trees.append('F')
                if level[i -1][n] == 'T':
                    n_tents.append((i,n))

                if level[i +1][n] == 'T':
                    n_tents.append((i,n))

                if level[i][n-1] == 'T':
                    n_tents.append((i,n))

                if level[i][n +1] == 'T':
                    n_tents.append((i,n))

    if len(n_tents) == len(n_trees):
        return True


if check_tent() == True:
    print('asd')
