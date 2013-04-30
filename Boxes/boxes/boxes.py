
boxes = []
tam = []
n_boxes = 0

def ind_pos(i, j, k):
    global tam
    return str((i*tam[0]*tam[1]) + (j*tam[1]) + k + 1)

def main():
    f = open('file.txt')
    global tam
    tam = f.readline().split(" ")
    tam[0] = int(tam[0])
    tam[1] = int(tam[1])
    n_boxes = int(f.readline())
    for i in xrange(0,n_boxes):
        a = f.readline().split(" ")
        if ( len(a) == 2 ):
            boxes.append([int(a[0]), int(a[1])])
        else:
            print "ERROR PARSING"
        
    print "p cnf %d %d" % (tam[0]*tam[1]*n_boxes + tam[0]*tam[1]*n_boxes, tam[0]*tam[1])
    #minimo una caja por celda
    #para cada caja i,j -> 0 v 1 v ... v k
    for i in xrange(0,tam[0]):
        for j in xrange(0, tam[1]):
            for k in xrange(0, n_boxes):
                print ind_pos(i,j,k),
            print "0"
    
    #maximo una caja por celda
    for i in xrange(0, tam[0]):
        for j in xrange(0, tam[1]):
            for k in xrange(0, n_boxes):
                print "-" + ind_pos(i,j,k) + " ",
            print "0"
    
    dnfs = []
    for k in xrange(0,n_boxes):
        for i in xrange(0, tam[0]-boxes[k][0]+1):
            for j in xrange(0, tam[1]-boxes[k][1]+1):
                for l in xrange(0, boxes[k][0]):
                    for m in xrange(0, boxes[k][1]):
                        dnfs[k][i+j*tam[0]].append([ind_pos(i+l,j+m,k)])
                print "0"
    f.close()
    return 0


if __name__ == "__main__":
    main()