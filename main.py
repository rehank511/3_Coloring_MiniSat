# To run the program cd to the folder and the output of this program will be copied in the minisat solver.


def main():
    alph = []
    minisat = []
    graph = []
    alpha = 'a'
    for i in range(0, 26):
        alph.append(alpha)
        alpha = chr(ord(alpha) + 1)
    extra = [" ", "\n"]
    name = input("Name of the file: ")
    try:
        file = open(name, 'r')
    except FileNotFoundError:
        print("Wrong file name please re-run the program")
        exit(-1)

    temp1 = file.readlines()
    i = 0
    num = 0
    for x in temp1:
        graph.append([])
        for y in x:
            if y not in extra:
                graph[i].append(y)
                num = num + 1
        i = i + 1

    minisat.append(['p', 'cnf', str(len(graph)*3), str((len(graph)*4) + (num*3))])

    for i in range(len(graph)):
        var = [(i*3)+1, (i*3)+2, (i*3)+3]
        minisat.append([str(var[0]), str(var[1]), str(var[2]), '0'])
        minisat.append([str(var[0]*-1), str(var[1]*-1), '0'])
        minisat.append([str(var[0]*-1), str(var[2]*-1), '0'])
        minisat.append([str(var[1]*-1), str(var[2]*-1), '0'])

    for i in range(len(graph)):
        for y in graph[i]:
            y = alph.index(y)
            var1 = [(i*3)+1, (i*3)+2, (i*3)+3]
            var2 = [(y*3)+1, (y*3)+2, (y*3)+3]
            minisat.append([str(var1[0] * -1), str(var2[0] * -1), '0'])
            minisat.append([str(var1[1] * -1), str(var2[1] * -1), '0'])
            minisat.append([str(var1[2] * -1), str(var2[2] * -1), '0'])

    print("Output needed to be copied to Minisat Solver: \n")
    for x in minisat:
        for y in x:
            print(y, end=" ")
        print("")


if __name__ == '__main__':
    main()
