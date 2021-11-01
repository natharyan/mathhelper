from mathhelper import matrix,permutecomb,graph


print("Welcome!!")
print("Mathhelper is an efficient module to solve your doubts and homework problems, quickly and always correctly.")

print("""Currently available prompts:
1. Matrices
2. Determinants
2. Permutations
3. Combinations
4. Plot Graph""")
while True:
    cmd=input("What do you need help with today?\n")

    if cmd=='menu':
        print()
        print("""Currently available prompts:
1. Matrices
2. Determinants
2. Permuations
3. Combinations
4. Plot Graph""")
        print()

    elif cmd.lower() == 'matrices':
        print("Currently available operations:","1. Addition","2. Subtraction","3. Multiplication",sep="\n")
        type = input("Enter Operation: ")
        
        if type.lower()=='addition':
            order=input("Enter order of matrices: ")
            rows=int(order.partition('x')[0])
            cols=int(order.partition('x')[2])
            print("rows1, cols1 =",rows, cols)
            print("rows2, cols2 =",rows, cols)
            matrix.matrix1(matrix,rows,cols)
            matrix.matrix2(matrix,rows,cols)
            print()
            t=input("Press Enter to continue: ")
            matrix.add(matrix)
        elif type.lower()=='subtraction':
            order=input("Enter order of matrices: ")
            rows=int(order.partition('x')[0])
            cols=int(order.partition('x')[2])
            print("rows1, cols1 =",rows, cols)
            print("rows2, cols2 =",rows, cols)
            matrix.matrix1(matrix,rows,cols)
            matrix.matrix2(matrix,rows,cols)
            print()
            t=input("Press Enter to continue: ")
            matrix.subtract(matrix)
        elif type.lower()=='multiplication':
            while True:
                order1=input("Enter order of matrix A: ")
                order2=input("Enter order of matrix B: ")
                rows1=int(order1.partition('x')[0])
                cols1=int(order1.partition('x')[2])
                rows2=int(order2.partition('x')[0])
                cols2=int(order2.partition('x')[2])
                if cols1!=rows2:
                    print("Matrix order invalid")
                else:
                    break
            print("rows1, cols1 =",rows1, cols1)
            print("rows2, cols2 =",rows2, cols2)
            matrix.matrix1(matrix,rows1,cols1)
            matrix.matrix2(matrix,rows2,cols2)
            print()
            t=input("Press Enter to continue: ")
            matrix.product(matrix)

    elif cmd.lower()=='determinants':
        order=input("Enter order of matrix: ")
        rows=int(order.partition('x')[0])
        cols=int(order.partition('x')[2])
        print("rows, cols =",rows, cols)
        matrix.matrix1(matrix,rows,cols)
        print()
        t=input("Press Enter to continue: ")
        matrix.determinant(matrix)


    elif cmd.lower() =='permutations':
        quest=input("Question: ")
        quest=quest.split()
        num1=int(quest[quest.index('from')+1])
        num2=int(quest[quest.index('select')+1])
        permutecomb.permutation(permutecomb,num1,num2)
    elif cmd.lower() =='combinations':
        quest=input("Question: ")
        quest=quest.split()
        num1=int(quest[quest.index('from')+1])
        num2=int(quest[quest.index('select')+1])
        permutecomb.combination(permutecomb,num1,num2)
    elif cmd.lower()=='plot graph':
        print("Graphs currently available:","1. sine graph","2. cosine graph","3. tan graph","4. cot graph","5. cosec graph","6. sec graph","7. sine inverse graph","8. cosine inverse graph","9. bar graph","10. line graph",sep="\n")                        
        print()
        type=input("Enter Graph Type: ")
        if type.lower()=='sine graph':
            graph.sine()
        elif type.lower()=='cosine graph':
            graph.cosine()
        elif type.lower()=='tan graph':
            graph.tan()
        elif type.lower()=='cot graph':
            graph.cot()
        elif type.lower()=='cosec graph':
            graph.cosec()
        elif type.lower()=='sec graph':
            graph.sec()
        elif type.lower()=='sine inverse graph':
            graph.sineinvere()
        elif type.lower()=='bar graph':
            graph.bar()
        elif type.lower()=='line graph':
            graph.line()
    else:
        break

