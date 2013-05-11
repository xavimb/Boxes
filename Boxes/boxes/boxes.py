import sys

boxes = []
tam = []
n_boxes = 0

def ind_pos(i, j, k):
    global tam
    global n_boxes
    return str((i*n_boxes) + (j*tam[0]*n_boxes) + k + 1)
    #return str(i) + str(j) + str(k)

def main():
    f = open(sys.argv[1])
    global tam
    global n_boxes
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
        
    count = 0;
    
     #todas las cajas tienen alguna posicion ----- minimo ------
    for k in xrange(0,n_boxes):
        count += 1
    
    #maximo una caja esta en un sitio ----- maximo -------
    if (n_boxes >= 2):
        for k in xrange(0, n_boxes):
            for i in xrange(0, tam[0]-boxes[k][0]+1):
                for j in xrange(0, tam[1]-boxes[k][1]+1):
                    for l in xrange(0, tam[0]-boxes[k][0]+1):
                        for m in xrange(0, tam[1]-boxes[k][1]+1):
                            if (not (l == i and m == j)):
                                count += 1
                                
    #maximo una caja por celda
    for i in xrange(0, tam[0]):
        for j in xrange(0,tam[1]):
            for k in xrange(0, n_boxes):
                for l in xrange(0, n_boxes):
                    if (k != l):
                        count += 1
    
    #si una esquina esta en un sitio, no esta en ningun otro sitio 
    for k in xrange(0,n_boxes):
        for i in xrange(0, tam[0]-boxes[k][0]+1):
            for j in xrange(0, tam[1]-boxes[k][1]+1):
                for m in xrange(0,boxes[k][0]):
                    for n in xrange(0,boxes[k][1]):
                        if (not (m == 0 and n == 0)):
                            for l in xrange(0,n_boxes):
                                if (l != k):
                                    count += 1
        
    
    print "p cnf %d %d" % (tam[0]*tam[1]*n_boxes, count)
    
    #todas las cajas tienen alguna posicion ----- minimo ------
    for k in xrange(0,n_boxes):
        for i in xrange(0, tam[0]-boxes[k][0]+1):
            for j in xrange(0,tam[1]-boxes[k][1]+1):
                print ind_pos(i,j,k) + " ",
        print "0"
    
    #maximo una caja esta en un sitio ----- maximo -------
    if (n_boxes >= 2):
        for k in xrange(0, n_boxes):
            for i in xrange(0, tam[0]-boxes[k][0]+1):
                for j in xrange(0, tam[1]-boxes[k][1]+1):
                    for l in xrange(0, tam[0]-boxes[k][0]+1):
                        for m in xrange(0, tam[1]-boxes[k][1]+1):
                            if (not (l == i and m == j)):
                                print "-" + ind_pos(i,j,k) + " -" + ind_pos(l,m,k) + " 0"
                                #print "pos:" + str(i) + str(j) + str(k) + " pos2:" + str(l) + str(m) +str(k)

    #maximo una caja por celda
    for i in xrange(0, tam[0]):
        for j in xrange(0,tam[1]):
            for k in xrange(0, n_boxes):
                for l in xrange(0, n_boxes):
                    if (k != l):
                        print "-" + ind_pos(i,j,k) + " -" + ind_pos(i,j,l) + " 0"
                        #print "pos:" + str(i) + str(j) + str(k) + " pos2:" + str(i) + str(j) +str(l)
    
    #si una esquina esta en un sitio, no esta en ningun otro sitio 
    for k in xrange(0,n_boxes):
        for i in xrange(0, tam[0]-boxes[k][0]+1):
            for j in xrange(0, tam[1]-boxes[k][1]+1):
                for m in xrange(0,boxes[k][0]):
                    for n in xrange(0,boxes[k][1]):
                        if (not (m == 0 and n == 0)):
                            for l in xrange(0,n_boxes):
                                if (l != k):
                                    print "-" + ind_pos(i,j,k) + " -" + ind_pos(i+m,j+n,l) + " 0"
                                    #print "pos:" + str(i) + str(j) + str(k) + " pos2:" + str(m) + str(n) +str(l)
                                    # falta bucle para cada caja, dejar margen
                                    for p in xrange(0,boxes[l][0]):
                                        for q in xrange(0, boxes[l][1]):
                                            if (i+m-p >= 0 and i+m-p < tam[0] and j+n-q >= 0 and j+n-q < tam[1]):
                                                print "-" + ind_pos(i,j,k) + " -" + ind_pos(i+m-p,j+n-q,l) + " 0"
    
    f.close()
    return 0


if __name__ == "__main__":
    main()