import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df1=pd.DataFrame()
#olympicdata.csv

def menu():
    global df1
    ans=True
    while ans:
        print("""

OLYMPICS GAMES ANALYSIS SYSTEM

1- Data Visualisation
2- Data Analysis
3- Read CSV File
4- Exit
""")
        ch=int(input("Enter your choice: "))
        if ch==1:
            datavisual()
        elif ch==2:
            odanalysis(df1)
        elif ch==3:
            df1=read_csv()
        elif ch==4:
            ex=input("Are you sure you want to exit?(y/n)")
            if ex=='y' or ex=='Y':
                print("Exiting now............Done! \nHave A Nice Day!!")
                sys.exit()
        else:
            print("\nInvalid Input Try again")
 

def datavisual():
    ans=True
    while ans:
        print('''

DATA VISUALISATION OF TOP 10 COUNTRIES

1- Line Chart-> COUNTRIES VS TOTAL MEDALS
2- Line Chart-> COUNTRIES VS TOTAL NO. OF TIMES PARTICIPATED (IN SUMMER & WINTER)
3- Bar Chart -> COUNTRIES VS TOTAL NO. OF GOLD MEDALS
4- Bar Chart -> COUNTRIES VS TOTAL NO. OF SILVER MEDALS
5- Bar Chart -> COUNTRIES VS TOTAL NO. OF BRONZE MEDALS.
6- Bar Chart -> COUNTRIES VS TOTAL NO. OF MEDALS (IN SUMMER AND WINTER)
7- Exit to Main Menu

''')
        ans=input("Please enter your choice: ")
        if ans=='1':
            line_chart1(df1)
        elif ans=='2':
            line_chart2(df1)
        elif ans=='3':
            bar_chart1(df1)
        elif ans=='4':
            bar_chart2(df1)
        elif ans=='5':
            bar_chart3(df1)
        elif ans=='6':
            dbargraph(df1)
        elif ans=='7':
            menu()
        else:
            print("\nInvalid choice.Try again")


#TO PLOT LINE CHART--> TOP 10 COUNTRIES VS TOTAL MEDALS
def line_chart1(df1):
    df=df1.sort_values('TotalMedal', ascending=False)
    df=df.loc[:,['Country','TotalMedal']]
    df=df.head(10)
    Countries=df['Country']
    Totalmedals=df['TotalMedal']
    plt.plot(Countries,Totalmedals,linestyle=':',color='green',marker='.')
    x=np.arange(len(Countries))
    plt.xticks(x,Countries,rotation=30)
    plt.xlabel('Country ->',fontsize=12,color='r')
    plt.ylabel('Total Medals ->',fontsize=12,color='r')
    plt.title('TOTAL MEDALS WON BY TOP 10 COUNTRIES\n',color='blue',fontsize=18)
    plt.show()
    

    
#TO PLOT LINE CHART --> TOP 10 COUNTRIES VS TOTAL NO. OF TIMES PARTICIPATED (IN SUMMER & WINTER)
def line_chart2(df1):

    df=df1.sort_values('TotalTimesPart', ascending=False)
    df=df.loc[:,['Country','SummerTimesPart','WinterTimesPart' ]]
    df=df.head(10)
    Countries=df['Country']
    Stotal=df['SummerTimesPart']
    Wtotal=df['WinterTimesPart']
    plt.plot(Countries,Stotal,linestyle='dashed',color='orange',label='Summer',marker='+')
    plt.plot(Countries,Wtotal,linestyle='dashed',color='dimgrey',label='Winter',marker='+')
    x=np.arange(len(Countries))
    plt.xticks(x,Countries,rotation=30)
    plt.xlabel('Country ->',fontsize=12,color='r')
    plt.ylabel('No. of times participated ->',fontsize=12,color='r')
    plt.title('TOTAL NO. OF TIMES PARTICIPATED BY TOP 10 COUNTRIES\n',color='blue',fontsize=18)
    plt.legend()
    plt.show()


#TO PLOT BAR CHART-->TOP 10 COUNTRIES VS TOTAL NO, OF GOLD MEDALS
def bar_chart1(df1):
    
    df=df1.sort_values('Tgoldmedal',ascending=False)
    df=df.head(10)
    x=np.arange(len(df))
    Countries=df['Country']
    totalgold=df['Tgoldmedal']
    plt.bar(x+0.25, totalgold,width=.6, label='Total No. of Gold Medals by Top 10 Countries',color='gold')
    plt.xticks(x,Countries,rotation=30)
    plt.title('Olympics Gold Medal Analysis of Top 10 Countries',color='blue',fontsize= 16)
    plt.xlabel('Countries ->',fontsize=12,color='red')
    plt.ylabel('No. of Gold Medals ->',fontsize=12,color='red')
    plt.grid()
    plt.legend()
    plt.show()


#TO PLOT BAR CHART-->TOP 10 COUNTRIES VS TOTAL NO. OF SILVER MEDALS
def bar_chart2(df1):
    
    df=df1.sort_values('Tsilvermedal',ascending=False)
    df=df.head(10)
    x=np.arange(len(df))
    Countries=df['Country']
    totalsilver=df['Tsilvermedal']
    plt.bar(x,totalsilver,width=.6, label='Total No. of Silver Medals by Top 10 Countries',color='silver')
    plt.xticks(x,Countries,rotation=30)
    plt.title('Olympics Silver Medal Analysis of Top 10 Countries',color='blue',fontsize=16)
    plt.xlabel(' Countries ~ ~ ~~ ~ >',fontsize=12,color='red')
    plt.ylabel('No. of Silver Medals ~~~~~>',fontsize=12,color='red')
    plt.grid()
    plt.legend()
    plt.show()


#TO PLOT BAR CHART-->TOP 10 COUNTRIES VS TOTAL NO. OF BRONZE MEDALS
def bar_chart3(df1):

    df=df1.sort_values('Tbronzemedal',ascending= False)
    df=df.head(10)
    x=np.arange(len(df))
    Countries=df['Country']
    totalbronze=df['Tbronzemedal']
    plt.bar(x+0.25,totalbronze,width=.6,label='Total No. of Bronze Medals by Top 10 Countries',color='peru')
    plt.xticks(x,Countries,rotation=30)
    plt.title('Olympics Bronze Medal Analysis of Top 10 Countries',color='blue',fontsize=16)
    plt.xlabel('Countries~~~~~>',fontsize=12,color='red')
    plt.ylabel('No. of Bronze Medals~~~ ~~>',fontsize=12,color='red')
    plt.grid()
    plt.legend()
    plt.show()


#TO PLOT BAR CHART-->TOP 10 COUNTRIES VS TOTAL NO. OF MEDALS(IN SUMMER & WINTER)
def dbargraph(df1):   
    
    df=df1.sort_values('TotalMedal' ,ascending=False)
    df=df.head(10)
    x=np.arange(len(df))
    Countries=df['Country']
    Summermedal=df['SummerTotal']
    Wintermedal=df ['WinterTotal']
    plt.bar(x-0.2,Summermedal,label='Total No. of Medals by Top 10 Countries IN SUMMER', width=0.4, color='orangered')
    plt.bar(x+0.2,Wintermedal,label="Total No. of Medals Top 10 Countries IN WINTER", width=0.4, color= 'grey')
    plt.xticks(x,Countries,rotation=20)
    plt.title('Olympic Medal Analysis by Top 10 Countries',color='navy' ,fontsize= 16)
    plt.xlabel('Countries ~ ~ ~ ~ >',fontsize=12,color='r')
    plt.ylabel('No. of Medals~ ~ ~~ >',fontsize=12,color='r')
    plt.grid()
    plt.legend()
    plt.show()



#FUNCTION FOR ANALYSIS OF OLYMPICS DATA
def odanalysis(df1):
    while True:
        print("<------------------------->")
        print('Data Frame Analysis')
        print("<------------------------->")
        mn='''1) To print Records of Top Countries in terms of  Total Medals won in Olympics.
2) To print  Records of Top Countries in terms of Total Gold Medals won in Olympics.
3) To print Records of Top Countries in terms of Total Silver Medals won in Olympics.
4) To print Records of Top Countries in terms of Total Bronze Medals won in Olympics.
5) To print Records of Bottom-most Countries in terms of Medal won in Olympics

6) To print the Data of column specified by the User
7) To print Maximum value for each Column in the Dataframe. 
8)To go back to the main menu'''
        print(mn)
        x=int(input("Enter your choice : "))
        print("---------x-------------------x------------------x------------------x")
        if x==1:
            df=df1.sort_values('TotalMedal',ascending=False,ignore_index=True)
            df=df.loc[:,['Country','TotalMedal']]
            nor=int(input("Enter the number of records to be displayed : "))
            print("Top",nor," records from DataFrame")
            print(df.head(nor))
            print("---------x-------------------x------------------x------------------x")
        elif x==2:
            df=df1.sort_values('Tgoldmedal',ascending=False,ignore_index=True)
            df=df.loc[:,['Country','Tgoldmedal']]
            nor=int(input("Enter the number of records to be displayed : "))
            print("Top",nor,"records by total no. of gold medals")
            print(df.head(nor))
            print("---------x-------------------x------------------x------------------x")
        elif x==3:
            df=df1.sort_values('Tsilvermedal',ascending=False,ignore_index=True)
            df=df.loc[:,['Country','Tsilvermedal']]
            nor=int(input("Enter the number of records to be displayed : "))
            print("Top",nor,"records by total no. of silver medals")
            print(df.head(nor))
            print("---------x-------------------x------------------x------------------x")
        elif x==4:
            df=df1.sort_values('Tbronzemedal',ascending=False,ignore_index=True)
            df=df.loc[:,['Country','Tbronzemedal']]
            nor=int(input("Enter the number of records to be displayed : "))
            print("Top",nor,"records by total no. of bronze medals")
            print(df.head(nor))
            print("---------x-------------------x------------------x------------------x")
        elif x==5:
            df=df1.sort_values('TotalMedal',ascending=False,ignore_index=True)
            nor=int(input("Enter the number of records to be displayed : "))
            df=df.loc[:,['Country','TotalMedal']]
            print("Bottom",nor,"records from the dataframe")
            print(df.tail(nor))
            print("---------x-------------------x------------------x------------------x")
        elif x==6:
            print("Name of the columns~~>",df1.columns)
            clm=eval(input("Enter the column names in a list"))
            print(df1[clm])
            print("---------x-------------------x------------------x------------------x")
        elif x==7:
            print("Maximum value for each column")
            print(df1.max())
            print("---------x-------------------x------------------x------------------x")
        elif x==8:
            menu()
            break


def read_csv():
    ans=True
    global df1
    while ans:
        print('''1) Read CSV file\n2) Press 2 for data visualisation and Analysis\n3) Press 3 to exit''')
        ans=int(input('Enter your choice:'))
        if ans==1:
            try:
              fname=input("Enter file name: ")
              df1=pd.read_csv(fname)
              print(df1)
              print("Done!")
              
            except Exception as e:
                print(e)
        elif ans==2:
            if df1.empty:
                print("File not read!")
            else:
                menu()
        elif ans==3:
            sys.exit()
        else:
            print("Invalid Choice!Try again.")




read_csv()




