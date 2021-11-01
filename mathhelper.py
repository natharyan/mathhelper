class matrix():
    def matrix1(self,rows,cols):
        self.main1=[]
        rowlist1=[]
        print("Constructing Matrix A")
        for i in range(rows):
            for j in range(cols):
                rowlist1+=[int(input("Enter Number: "))]
            self.main1+=[rowlist1]
            rowlist1=[]
        print()
        z=0
        print("Matrix A:\n")
        for row in self.main1:
            for col in row:
                print(col,end=" ")
            print()
        print("main1 =",self.main1)
        print()

    
    def matrix2(self,rows,cols):
        self.main2=[]
        rowlist2=[]
        print("Constructing Matrix B")
        for i in range(rows):
            for j in range(cols):
                rowlist2+=[int(input("Enter Number: "))]
            self.main2+=[rowlist2]
            rowlist2=[]
        print()
        z=0
        print("Matrix B:\n")
        for row in self.main2:
            for col in row:
                print(col,end=" ")
            print()
        print("main2 =",self.main2)
        print()

    def add(self):
        print("main1 =",self.main1)
        print("main2 =",self.main2)
        self.summation=[]
        rowlist=[]
        sum=0
        for row in self.main1:
            print("row =",row)
            for col in row:
                print("col =",col)
                print("self.main2[self.main1.index(row)][row.index(col)] =",self.main2[self.main1.index(row)][row.index(col)])
                sum=col+self.main2[self.main1.index(row)][row.index(col)]
                print("sum =",sum)
                rowlist+=[sum]
                sum=0
            self.summation+=[rowlist]
            rowlist=[]

        print()
        print("Matrix A+B:\n")
        for row in self.summation:
            for col in row:
                if col>=0:
                    print(col,end="  ")
                else:
                    print(col,end=" ")
            print()
        print()

        print("summation =",self.summation)
        print()

    def subtract(self):
        print("main1 =",self.main1)
        print("main2 =",self.main2)
        self.difference=[]
        rowlist=[]
        diff=0
        for row in self.main1:
            print("row =",row)
            for col in row:
                print("col =",col)
                print("self.main2[self.main1.index(row)][row.index(col)] =",self.main2[self.main1.index(row)][row.index(col)])
                diff=col-self.main2[self.main1.index(row)][row.index(col)]
                print("difference =",diff)
                rowlist+=[diff]
                diff=0
            self.difference+=[rowlist]
            rowlist=[]

        print()
        print("Matrix A+B:\n")
        for row in self.difference:
            for col in row:
                if col>=0:
                    print(col,end="  ")
                else:
                    print(col,end=" ")
            print()
        print()

        print("difference =",self.difference)
        print()

    def product(self):
        print("main1 =",self.main1)
        print("main2 =",self.main2)
        self.prod=[]
        rowlist=[]
        sum=0
        for row in self.main1:
            print("row =",row)
            x=0
            y=0
            while y<len(self.main2[0]):
                for col in row:
                    print("col =",col)
                    print("self.main2[x][y] =",self.main2[x][y])
                    sum+=col*self.main2[x][y]
                    x+=1
                print("sum =",sum)
                rowlist+=[sum]
                x=0
                y+=1
                sum=0
            self.prod+=[rowlist]
            rowlist=[]

        print()
        print("Matrix AB:\n")
        for row in self.prod:
            for col in row:
                if col>=0:
                    print(col,end="  ")
                else:
                    print(col,end=" ")
            print()
        print()

        print("prod =",self.prod)
        print()


    def determinant(self):
        print("matrix =",self.main1)
        det=0
        x=1
        y=2
        for col in self.main1[0]:
            if ((self.main1[0].index(col)+1)+(self.main1.index(self.main1[0])+1))%2!=0:
                det+=col*(self.main1[abs(len(self.main1)-(self.main1[0].index(col)+2))] * self.main1[len(self.main1)-(self.main1[0].index(col))])
                """
                col*(self.main1[self.main1[0].index(col)+1][self.main1[0].index(col)+1] * self.main1[self.main1[0].index(col)+2][len(self.main1)-self.main1[0].index(col)]/
                          -self.main1[self.main1[0].index(col)+1][self.main1[0].index(col)+1])
                """



        

class permutecomb():
    def permutation(self,num1,num2):
        x=permutecomb.factorial(num1)
        y=permutecomb.factorial((num1-num2))
        print("Number of selections =",int(x/y))

    def factorial(x):
        fact=1
        for num in range(1,x+1):
            fact*=num
        return fact

    def combination(self,num1,num2):
        x=permutecomb.factorial(num1)
        y=permutecomb.factorial((num1-num2))
        z=permutecomb.factorial(num2)
        print("Number of selections =",int(x/(y*z)))
    
class graph():
    
    def sine():
        import matplotlib.pyplot as plt
        from matplotlib.pyplot import show
        import numpy as np

        # .linspace arguments are (start, end, number_of_steps)
        x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
        y = np.sin(x)
        # show grid
        plt.grid()
        plt.xlabel("x")
        plt.ylabel("$sin(x)$")
        # Set the x and y axis cutoffs
        plt.ylim(-3,3)
        plt.xlim(-2 * np.pi, 2 * np.pi)
        # x_labels in radians
        # For a more programmatic approach to radians, see https://matplotlib.org/3.1.1/gallery/units/radian_demo.html
        radian_multiples = [-2, -3/2, -1, -1/2, 0, 1/2, 1, 3/2, 2]
        radians = [n * np.pi for n in radian_multiples]
        radian_labels = ['$-2\pi$', '$-3\pi/2$', '$\pi$', '$-\pi/2$', '0', '$\pi/2$', '$\pi$', '$3\pi/2$', '$2\pi$']
        plt.xticks(radians, radian_labels)
        plt.yticks([-4,-3.5,-3,-2.5,-2,-1.5,-1,-0.5,0,0.5,1,1.5,2,2.5,3,3.5,4])
        plt.title("$y = sin(x)$", fontsize=14)
        plt.plot(x, y)
        plt.show()

        """
        x=np.linspace(-2*np.pi,2*np.pi,512,endpoint=True)#4
        sinx=np.sin(x)#5
        plt.plot(x,sinx,linewidth='2.0',color='purple',label='sine')#7
        plt.xlim(-2*np.pi,2*np.pi)#8
        plt.ylim(-1,1)#9
        plt.xticks([-2*np.pi,-1.5*np.pi,-np.pi,-0.5*np.pi,0,0.5*np.pi,np.pi,-1.5*np.pi,2*np.pi],[r'$-2\pi$',r'$-3\pi/2$', r'$-\pi$',r'$-\pi/2$', r'$0$',r'$+\pi/2$', r'$+\pi$',r'$+3\pi/2$', r'$+2\pi$'])
        plt.yticks([-1,-0.5,0,0.5,1])#11
        ax=plt.gca()#12
        ax.spines['right'].set_color('none')#13
        ax.spines['top'].set_color('none')#14
        ax.xaxis.set_ticks_position('bottom')#15
        ax.spines['bottom'].set_position(('data',0))#16
        ax.yaxis.set_ticks_position('left')#17
        ax.spines['left'].set_position(('data',0))#18
        plt.legend(loc='lower left')#19
        plt.show()#20
        """

    def cosec():
        import matplotlib.pyplot as plt
        from matplotlib.pyplot import show
        import numpy as np

        # .linspace arguments are (start, end, number_of_steps)
        x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
        y = np.sin(x)
        # show grid
        plt.grid()
        plt.xlabel("x")
        plt.ylabel("$cosec(x)$")
        # Set the x and y axis cutoffs
        plt.ylim(-5,5)
        plt.xlim(-2 * np.pi, 2 * np.pi)
        # x_labels in radians
        # For a more programmatic approach to radians, see https://matplotlib.org/3.1.1/gallery/units/radian_demo.html
        radian_multiples = [-2, -3/2, -1, -1/2, 0, 1/2, 1, 3/2, 2]
        radians = [n * np.pi for n in radian_multiples]
        radian_labels = ['$-2\pi$', '$-3\pi/2$', '$\pi$', '$-\pi/2$', '0', '$\pi/2$', '$\pi$', '$3\pi/2$', '$2\pi$']
        plt.xticks(radians, radian_labels)
        plt.yticks([-4,-3,-2,-1,0,1,2,3,4])
        plt.title("$y = cosec(x)$", fontsize=14)
        plt.plot(x, 1/y)
        plt.show()

    def cosine():
        import matplotlib.pyplot as plt
        from matplotlib.pyplot import show
        import numpy as np

        # .linspace arguments are (start, end, number_of_steps)
        x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
        y = np.cos(x)
        # show grid
        plt.grid()
        plt.xlabel("x")
        plt.ylabel("$cos(x)$")
        # Set the x and y axis cutoffs
        plt.ylim(-3,3)
        plt.xlim(-2 * np.pi, 2 * np.pi)
        # x_labels in radians
        # For a more programmatic approach to radians, see https://matplotlib.org/3.1.1/gallery/units/radian_demo.html
        radian_multiples = [-2, -3/2, -1, -1/2, 0, 1/2, 1, 3/2, 2]
        radians = [n * np.pi for n in radian_multiples]
        radian_labels = ['$-2\pi$', '$-3\pi/2$', '$\pi$', '$-\pi/2$', '0', '$\pi/2$', '$\pi$', '$3\pi/2$', '$2\pi$']
        plt.xticks(radians, radian_labels)
        plt.yticks([-4,-3.5,-3,-2.5,-2,-1.5,-1,-0.5,0,0.5,1,1.5,2,2.5,3,3.5,4])
        plt.title("$y = cos(x)$", fontsize=14)
        plt.plot(x, y)
        plt.show()

        """
        x=np.linspace(-2*np.pi,2*np.pi,512,endpoint=True)#4
        cosx=np.cos(x)
        plt.plot(x,cosx,linewidth='2.0',color='purple',label='cosine')#6
        plt.xlim(-2*np.pi,2*np.pi)#8
        plt.ylim(-1,1)#9
        plt.xticks([-2*np.pi,-1.5*np.pi,-np.pi,-0.5*np.pi,0,0.5*np.pi,np.pi,-1.5*np.pi,2*np.pi],[r'$-2\pi$',r'$-3\pi/2$', r'$-\pi$',r'$-\pi/2$', r'$0$',r'$+\pi/2$', r'$+\pi$',r'$+3\pi/2$', r'$+2\pi$'])
        plt.yticks([-1,-0.5,0,0.5,1])#11
        ax=plt.gca()#12
        ax.spines['right'].set_color('none')#13
        ax.spines['top'].set_color('none')#14
        ax.xaxis.set_ticks_position('bottom')#15
        ax.spines['bottom'].set_position(('data',0))#16
        ax.yaxis.set_ticks_position('left')#17
        ax.spines['left'].set_position(('data',0))#18
        plt.legend(loc='lower left')#19
        plt.show()#20
        """

    def sec():
        import matplotlib.pyplot as plt
        from matplotlib.pyplot import show
        import numpy as np

        # .linspace arguments are (start, end, number_of_steps)
        x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
        y = np.cos(x)
        # show grid
        plt.grid()
        plt.xlabel("x")
        plt.ylabel("$sec(x)$")
        # Set the x and y axis cutoffs
        plt.ylim(-3,3)
        plt.xlim(-2 * np.pi, 2 * np.pi)
        # x_labels in radians
        # For a more programmatic approach to radians, see https://matplotlib.org/3.1.1/gallery/units/radian_demo.html
        radian_multiples = [-2, -3/2, -1, -1/2, 0, 1/2, 1, 3/2, 2]
        radians = [n * np.pi for n in radian_multiples]
        radian_labels = ['$-2\pi$', '$-3\pi/2$', '$\pi$', '$-\pi/2$', '0', '$\pi/2$', '$\pi$', '$3\pi/2$', '$2\pi$']
        plt.xticks(radians, radian_labels)
        plt.yticks([-4,-3,-2,-1,0,1,2,3,4])
        plt.title("$y = sec(x)$", fontsize=14)
        plt.plot(x, 1/y)
        plt.show()

        """
        x=np.linspace(-2*np.pi,2*np.pi,512,endpoint=True)#4
        cosx=np.cos(x)
        plt.plot(x,cosx,linewidth='2.0',color='purple',label='cosine')#6
        plt.xlim(-2*np.pi,2*np.pi)#8
        plt.ylim(-1,1)#9
        plt.xticks([-2*np.pi,-1.5*np.pi,-np.pi,-0.5*np.pi,0,0.5*np.pi,np.pi,-1.5*np.pi,2*np.pi],[r'$-2\pi$',r'$-3\pi/2$', r'$-\pi$',r'$-\pi/2$', r'$0$',r'$+\pi/2$', r'$+\pi$',r'$+3\pi/2$', r'$+2\pi$'])
        plt.yticks([-1,-0.5,0,0.5,1])#11
        ax=plt.gca()#12
        ax.spines['right'].set_color('none')#13
        ax.spines['top'].set_color('none')#14
        ax.xaxis.set_ticks_position('bottom')#15
        ax.spines['bottom'].set_position(('data',0))#16
        ax.yaxis.set_ticks_position('left')#17
        ax.spines['left'].set_position(('data',0))#18
        plt.legend(loc='lower left')#19
        plt.show()#20
        """


    def tan():
        import matplotlib.pyplot as plt
        from matplotlib.pyplot import show
        import numpy as np
        # .linspace arguments are (start, end, number_of_steps)
        x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
        y = np.tan(x)

        # This operation inserts a NaN where the difference between successive points is negative
        # NaN means "Not a Number" and NaNs are not plotted or connected
        # I found this by doing a search for "How to plot tan(x) in matplotlib without the connecting lines between asymtotes"
        y[:-1][np.diff(y) < 0] = np.nan

        # show grid
        plt.grid()

        plt.xlabel("x")
        plt.ylabel("$tan(x)$")

        # Set the x and y axis cutoffs
        plt.ylim(-10,10)
        plt.xlim(-2 * np.pi, 2 * np.pi)

        # x_labels in radians
        # For a more programmatic approach to radians, see https://matplotlib.org/3.1.1/gallery/units/radian_demo.html
        radian_multiples = [-2, -3/2, -1, -1/2, 0, 1/2, 1, 3/2, 2]
        radians = [n * np.pi for n in radian_multiples]
        radian_labels = ['$-2\pi$', '$-3\pi/2$', '$\pi$', '$-\pi/2$', '0', '$\pi/2$', '$\pi$', '$3\pi/2$', '$2\pi$']

        plt.xticks(radians, radian_labels)

        plt.title("$y = tan(x)$", fontsize=14)
        plt.plot(x, y)
        plt.show()
        """
        x=np.linspace(-2*np.pi,2*np.pi,512,endpoint=True)#4
        tanx=np.tan(x)
        plt.plot(x,tanx,linewidth='2.0',color='purple',label='tan')#6
        plt.xlim(-2*np.pi,2*np.pi)#8
        plt.ylim(-1,1)#9
        plt.xticks([-2*np.pi,-1.5*np.pi,-np.pi,-0.5*np.pi,0,0.5*np.pi,np.pi,-1.5*np.pi,2*np.pi],[r'$-2\pi$',r'$-3\pi/2$', r'$-\pi$',r'$-\pi/2$', r'$0$',r'$+\pi/2$', r'$+\pi$',r'$+3\pi/2$', r'$+2\pi$'])
        plt.yticks([-1,-0.5,0,0.5,1])#11
        ax=plt.gca()#12
        ax.spines['right'].set_color('none')#13
        ax.spines['top'].set_color('none')#14
        ax.xaxis.set_ticks_position('bottom')#15
        ax.spines['bottom'].set_position(('data',0))#16
        ax.yaxis.set_ticks_position('left')#17
        ax.spines['left'].set_position(('data',0))#18
        plt.legend(loc='lower left')#19
        plt.show()#20
        """
    def cot():
        import matplotlib.pyplot as plt
        from matplotlib.pyplot import show
        import numpy as np

        # .linspace arguments are (start, end, number_of_steps)
        x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
        y = np.tan(x)

        # This operation inserts a NaN where the difference between successive points is negative
        # NaN means "Not a Number" and NaNs are not plotted or connected
        # I found this by doing a search for "How to plot tan(x) in matplotlib without the connecting lines between asymtotes"
        y[:-1][np.diff(y) < 0] = np.nan

        # show grid
        plt.grid()

        plt.xlabel("x")
        plt.ylabel("$cot(x)$")

        # Set the x and y axis cutoffs
        plt.ylim(-10,10)
        plt.xlim(-2 * np.pi, 2 * np.pi)

        # x_labels in radians
        # For a more programmatic approach to radians, see https://matplotlib.org/3.1.1/gallery/units/radian_demo.html
        radian_multiples = [-2, -3/2, -1, -1/2, 0, 1/2, 1, 3/2, 2]
        radians = [n * np.pi for n in radian_multiples]
        radian_labels = ['$-2\pi$', '$-3\pi/2$', '$\pi$', '$-\pi/2$', '0', '$\pi/2$', '$\pi$', '$3\pi/2$', '$2\pi$']

        plt.xticks(radians, radian_labels)

        plt.title("$y = cot(x)$", fontsize=14)
        plt.plot(x, 1/y)
        plt.show()

        #have to remove asymptotes
        """
        # .linspace arguments are (start, end, number_of_steps)
        x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
        y = np.tan(x)
        y1=[]
        for i in y[:-1]:
            y1+=[1/i]
        y1=np.array(y1)
        print(y1)
        # This operation inserts a NaN where the difference between successive points is negative
        # NaN means "Not a Number" and NaNs are not plotted or connected
        # I found this by doing a search for "How to plot tan(x) in matplotlib without the connecting lines between asymtotes"
        y1[:-1][np.diff(y1) < 0] = np.nan

        # show grid
        plt.grid()

        plt.xlabel("x")
        plt.ylabel("$cot(x)$")

        # Set the x and y axis cutoffs
        plt.ylim(-10,10)
        plt.xlim(-2 * np.pi, 2 * np.pi)

        # x_labels in radians
        # For a more programmatic approach to radians, see https://matplotlib.org/3.1.1/gallery/units/radian_demo.html
        radian_multiples = [-2, -3/2, -1, -1/2, 0, 1/2, 1, 3/2, 2]
        radians = [n * np.pi for n in radian_multiples]
        radian_labels = ['$-2\pi$', '$-3\pi/2$', '$\pi$', '$-\pi/2$', '0', '$\pi/2$', '$\pi$', '$3\pi/2$', '$2\pi$']

        plt.xticks(radians, radian_labels)

        plt.title("$y = cot(x)$", fontsize=14)
        plt.plot(x, y1)
        plt.show()
        """
        """
        x=np.linspace(-2*np.pi,2*np.pi,512,endpoint=True)#4
        tanx=np.tan(x)
        plt.plot(x,tanx,linewidth='2.0',color='purple',label='tan')#6
        plt.xlim(-2*np.pi,2*np.pi)#8
        plt.ylim(-1,1)#9
        plt.xticks([-2*np.pi,-1.5*np.pi,-np.pi,-0.5*np.pi,0,0.5*np.pi,np.pi,-1.5*np.pi,2*np.pi],[r'$-2\pi$',r'$-3\pi/2$', r'$-\pi$',r'$-\pi/2$', r'$0$',r'$+\pi/2$', r'$+\pi$',r'$+3\pi/2$', r'$+2\pi$'])
        plt.yticks([-1,-0.5,0,0.5,1])#11
        ax=plt.gca()#12
        ax.spines['right'].set_color('none')#13
        ax.spines['top'].set_color('none')#14
        ax.xaxis.set_ticks_position('bottom')#15
        ax.spines['bottom'].set_position(('data',0))#16
        ax.yaxis.set_ticks_position('left')#17
        ax.spines['left'].set_position(('data',0))#18
        plt.legend(loc='lower left')#19
        plt.show()#20
        """


    def sineinvere():
        import matplotlib.pyplot as plt
        from matplotlib.pyplot import show
        import numpy as np

        # .linspace arguments are (start, end, number_of_steps)
        x = np.linspace(-1/2 * np.pi, 1/2 * np.pi, 1000)
        y = np.sin(x)
        # show grid
        plt.grid()
        plt.xlabel("x")
        # Set the x and y axis cutoffs
        plt.ylim(-3,3)
        plt.xlim(-np.pi, np.pi)
        # x_labels in radians
        # For a more programmatic approach to radians, see https://matplotlib.org/3.1.1/gallery/units/radian_demo.html
        radian_multiples = [-1, -1/2, 0, 1/2, 1]
        radians = [n * np.pi for n in radian_multiples]
        radian_labels = ['$\pi$', '$-\pi/2$', '0', '$\pi/2$', '$\pi$']
        plt.xticks(radians, radian_labels)
        plt.yticks([-2,-1.5,-1,-0.5,0,0.5,1,1.5,2])
        plt.title("$y = sin-1(x)$", fontsize=14)
        ax=plt.gca()#12
        ax.spines['right'].set_color('none')#13
        ax.spines['top'].set_color('none')#14
        ax.xaxis.set_ticks_position('bottom')#15
        ax.spines['bottom'].set_position(('data',0))#16
        ax.yaxis.set_ticks_position('left')#17
        ax.spines['left'].set_position(('data',0))#18
        plt.plot(x, y,label='sin^-1')
        plt.legend(loc='lower left')#19
        plt.show()


    def bar():
        import matplotlib.pyplot as plt
        from matplotlib.pyplot import show
        import numpy as np
        import csv
        print("Attach a file under the name 'graph1.csv' in the same directory")
        t=input("Press Enter to continue: ")
        show(block=False)
        tick_label=[]
        height=[]
        left=[]
        with open("graph1.csv","r") as file:
            obj=csv.reader(file)
            for row in obj:
                tick_label+=[row[0]]
                height+=[int(row[1])]

        #x-coordinate of bar
        for i in range(1,len(tick_label)+1):
            left+=[i]
        
        # plotting a bar chart
        plt.bar(left, height, tick_label = tick_label,
                width = 0.8, color = ['cyan'])
        
        # naming the x-axis
        plt.xlabel('X - Axis')
        # naming the y-axis
        plt.ylabel('Y - Axis')
        # plot title
        plt.title('Bar Graph')

        plt.show()

    def line():
        import matplotlib.pyplot as plt
        from matplotlib.pyplot import show
        import numpy as np
        import csv
        print("Attach a file under the name 'graph2.csv' in the same directory")
        t=input("Press Enter to continue: ")
        show(block=False)
        x=[]
        y=[]
        left=[]
        with open("graph2.csv","r") as file:
            obj=csv.reader(file)
            for row in obj:
                x+=[int(row[0])]
                y+=[int(row[1])]

        #x-coordinate of bar
        for i in range(1,len(x)+1):
            left+=[i]
        
        plt.plot(x, y)
        
        # naming the x-axis
        plt.xlabel('X-Axis')
        # naming the y-axis
        plt.ylabel('Y-Axis')
        # plot title
        plt.title('Line Graph')

        plt.show()

