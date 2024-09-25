def chkItr():
    n1 = eval(input("Enter an object"))
    ob_dir = dir(n1)
    if '__iter__' and '__next__' in ob_dir:
        print("Iteartor")
    elif '__iter__' in ob_dir:
        print("Iterable")
    else:
        print("neither")

chkItr()