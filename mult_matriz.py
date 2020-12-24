def mult(a, b):
    a  = a
    b = b

    linhasa, colunasa = len(a), len(a[0])
    linhasb, colunasb = len(b), len(b[0])

    if linhasa == colunasb and colunasa == linhasb:
        mult = []
        
        for x in range(linhasa):
            mult.append([])

            for y in range(colunasb):
                mult[x].append(0)

                for k in range(colunasa):
                     mult[x][y] += a[x][k] * b[k][y]
        return mult
                



print(mult([[3, 3], [3, 3], [3, 3]], [[3, 3, 3], [3, 3, 3]]))
