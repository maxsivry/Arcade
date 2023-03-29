#This code was written by Matthew Rieger
#The following code is a working game of mancala. I have attached a text file explaining the rules.
#establish starting list
p1list = [4,4,4,4,4,4,0,4,4,4,4,4,4,0]
#create corresponding list
p2list = p1list+[]
#this function merges the two different lists together to create a complete board
def difflists(p1list,p2list):
        #create empty list for determining the numbers for the top half of the board
        listtooltop = []
        #create range statement, first 6 board slots
        for i in range (0,6):
            #find the difference between the values in the two lists
            topobject = abs(p1list[i]-p2list[i+7])
            #add this value to the list of value differentials for the top row
            listtooltop.append(topobject)
        #repeat this exact process for the bottom row
        listtoolbottom = []
        for i in range(0,6):
            bottomobject = abs(p2list[i]-p1list[i+7])
            listtoolbottom.append(bottomobject)
        #repeat this process for the ends of the board
        endtool = []
        endrighttool = abs(p1list[6]-p2list[13])
        endlefttool = abs(p2list[6]-p1list[13])
        endtool.append(endrighttool)
        endtool.append(endlefttool)
        #create a lsit containing all of these values
        listtool = listtooltop+listtoolbottom+endtool
        return listtool
def p1run(p1input,p1list):
        #the code throws an error when the value of the slot selected exceeds the length of the list, so I've created an try/except statement
        try:
                #establish the range which will be effected by the slot selected
                for i in range ((p1input+1),(p1list[p1input]+p1input+1)):
                    #add a bead for each slot affected
                    p1list[i]+=1
                #the value of the slot selected changes to zero
                p1list[p1input] = 0
        except:
                #find how many more slots need to be filled
                calctool = ((p1list[p1input]+(p1input))-13)
                #fill these remaining slots
                for i in range (0,calctool):
                        p1list[i]+=1
                p1list[p1input] = 0
        return p1list
def p2run(p2input,p2list):
        #repeat the exact process used in p1run in p2run
        try:
                for i in range ((p2input+1),(p2list[p2input]+p2input+1)):
                    p2list[i]+=1
                p2list[p2input] = 0
        except:
                calctool = ((p2list[p2input]+(p2input))-13)
                for i in range (0,calctool):
                        p2list[i]+=1
                p2list[p2input] = 0
        return p2list
def convert2board(listtool,top1,top2,top3,top4,top5,top6,bottom1,bottom2,bottom3,bottom4,bottom5,bottom6,endright,endleft):
    #adjust each variable used in the printboard function with their corresponding listtool adjustment
    top1 +=listtool[0]
    top2 += listtool[1]
    top3 += listtool[2]
    top4 += listtool[3]
    top5 += listtool[4]
    top6 += listtool[5]
    bottom1 += listtool[6]
    bottom2 += listtool[7]
    bottom3 += listtool[8]
    bottom4 += listtool[9]
    bottom5 += listtool[10]
    bottom6 += listtool[11]
    endleft += listtool[12]
    endright += listtool[13]
    return top1,top2,top3,top4,top5,top6,bottom1,bottom2,bottom3,bottom4,bottom5,bottom6,endright,endleft
def printboard(top1,top2,top3,top4,top5,top6,bottom1,bottom2,bottom3,bottom4,bottom5,bottom6,endleft,endright):
    #Use list printing variables to print the game board
    print("""__________________________________________________________________|
{  ____     ____    ____    ____    ____    ____    ____          |
{ |    |   [""",top1,"""_]  [""",top2,"""_]  [""",top3,"""_]  [""",top4,"""_]  [""",top5,"""_]  [""",top6,"""_]   ____  |
{ |""",endright,""" |                                                   |    | |
{ |____|    ____    ____    ____    ____    ____    ____   |""",endleft,""" | |
{          [""",bottom6,"""_]  [""",bottom5,"""_]  [""",bottom4,"""_]  [""",bottom3,"""_]  [""",bottom2,"""_]  [""",bottom1,"""_]  |____| |
{_________________________________________________________________|""")

def main(p1list,p2list):
    #establsh starting variables for the list printing tool
    top1 = 4
    top2 = 4
    top3 = 4
    top4 = 4
    top5 = 4
    top6 = 4
    bottom1 = 4
    bottom2 = 4
    bottom3 = 4
    bottom4 = 4
    bottom5 = 4
    bottom6 = 4
    endright = 0
    endleft = 0
    printboard(top1,top2,top3,top4,top5,top6,bottom1,bottom2,bottom3,bottom4,bottom5,bottom6,endleft,endright)
    #print a greeting message and establish the anotherround variable
    anotherround = input("""Hello and welcome to mancala!
select a number between 1 and 6 to select which of your tiles you would like to empty.
Whoever ends with the greatest value in their endzone wins!
Press any key to begin except for 'q'.""")
    while(anotherround!= 'q'):
        #user inputs which tile they would like to select, subtract 1 to use as list input
        p1input = (int(input('which tile would you like to select?(top)'))-1)
        while (p1input<0 or p1input>5):
                #validate input, ensure between 1 and 6
                print('Please select a number between 1 and 6!')
                p1input = (int(input('which tile would you like to select?(top)'))-1)
        #run input through p1run function to alter p1 list
        p1list = p1run(p1input,p1list)
        #Establish listtool, a list of all changes needed to be made to the gameboard
        listtool = difflists(p1list,p2list)
        #ensure that the emptied slot has a value of zerp
        listtool[p1input] = -listtool[p1input]
        #convert calculation data into board values
        (top1,top2,top3,top4,top5,top6,bottom1,bottom2,bottom3,bottom4,bottom5,bottom6,endright,endleft) = convert2board(listtool,top1,top2,top3,top4,top5,top6,bottom1,bottom2,bottom3,bottom4,bottom5,bottom6,endright,endleft)
        #convert board data back to calculation data
        p1list = [top1,top2,top3,top4,top5,top6,endleft,bottom1,bottom2,bottom3,bottom4,bottom5,bottom6,endright]
        p2list = [bottom1,bottom2,bottom3,bottom4,bottom5,bottom6,endright,top1,top2,top3,top4,top5,top6,endleft]
        #print gameboard
        printboard(top1,top2,top3,top4,top5,top6,bottom1,bottom2,bottom3,bottom4,bottom5,bottom6,endleft,endright)
        #repeat exact same process for player 2's turn
        p2input = (int(input('which tile would you like to select?(bottom)'))-1)
        while (p2input<0 or p2input>5):
                print('Please select a number between 1 and 6!')
                p2input = (int(input('which tile would you like to select?(bottom)'))-1)
        p2list = p2run(p2input,p2list)
        
        listtool = difflists(p1list,p2list)
        listtool[p2input+6] = -listtool[p2input+6]
        (top1,top2,top3,top4,top5,top6,bottom1,bottom2,bottom3,bottom4,bottom5,bottom6,endright,endleft) = convert2board(listtool,top1,top2,top3,top4,top5,top6,bottom1,bottom2,bottom3,bottom4,bottom5,bottom6,endright,endleft)
        p1list = [top1,top2,top3,top4,top5,top6,endleft,bottom1,bottom2,bottom3,bottom4,bottom5,bottom6,endright]
        p2list = [bottom1,bottom2,bottom3,bottom4,bottom5,bottom6,endright,top1,top2,top3,top4,top5,top6,endleft]
        printboard(top1,top2,top3,top4,top5,top6,bottom1,bottom2,bottom3,bottom4,bottom5,bottom6,endleft,endright)
        anotherround = input('another round?(press "q" to quit)')
main(p1list,p2list)
