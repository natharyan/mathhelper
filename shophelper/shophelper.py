import matplotlib.pyplot as plt
from matplotlib.pyplot import show, plot
import mysql.connector as dat
import csv
from statistics import mean, median, mode

show(block=False)
print("""Command Prompts:
1. customers - display number of customers at different timings
2. items - display the sale of different items""")
def timings():
    tick_label=[]
    height=[]
    left=[]
    with open("timings.csv","r") as file:
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
    plt.xlabel('Time')
    # naming the y-axis
    plt.ylabel('Customers')
    # plot title
    plt.title('Timings')
    l=[]
    for i in tick_label:
        l+=[float(i[:2])]
    sum=0
    for item in l:
        sum+=item
    mean=sum/len(l)
    print("average customers in store =",mean)
    """
    print("average customers in store =",mean(l))
    """
    
    # function to show the plot
    plt.show()
    

def items():
    tick_label=[]
    height=[]
    left=[]
    with open("items.csv","r") as file:
        obj=csv.reader(file)
        for row in obj:
            tick_label+=[row[0]]
            height+=[int(row[1])]

    #x-coordinate of bar
    for i in range(1,len(tick_label)+1):
        left+=[i]
    
    # plotting a bar chart
    plt.bar(left, height, tick_label = tick_label,
            width = 0.8, color = ['magenta'])
    
    # naming the x-axis
    plt.xlabel('Item Name')
    # naming the y-axis
    plt.ylabel('Amount')
    # plot title
    plt.title('Items purchased')
    
    l=[]
    for i in height:
        l+=[int(i)]
    val=max(l)
    pos=height.index(val)
    print(tick_label[pos],"has maximum frequency of",val)
    # function to show the plot
    plt.show()
    
while True:
    t=input("Prompt: ")
    if t=='customers':
        timings()
    elif t=='items':
        items()
    elif t=='end':
        break
    else:
        pass