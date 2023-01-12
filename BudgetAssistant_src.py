
import time as t
import datetime as dt
import operator

Today = dt.date.today()
  
def budget(pick): # The main budgetting program
    totalcost = {}
    budgetList = {}
    timeSpan = {}
    laterItems = {}
    overallCost = []
    savings = []

    def viewItem_time(): # View items along with their dates before deciding to withraw them
        print("\n\nLIST OF ITEMS",' |   ',"TOTAL COST OF ITEMS",'   |    ',"DATE (year-month-day)",' |   ',"DAYS FROM TODAY")
        for ob in timeSpan:
            # The figures attached to the print elements are to make sure the elements of the table are in line
            print("\n"+" "+ob.ljust(16),"   ","GHC "+str(totalcost[ob]).ljust(15),"     ",str(Today + dt.timedelta(timeSpan[ob])).ljust(23),"      ",str(timeSpan[ob]).ljust(15))
        print("\n\nTOTAL COST :","GHC",sum(overallCost),"             ","BUDGET : GHC",customerBudget)
        

    def prioriT(): # Prioritize items in Budget List
        if sum(overallCost) > customerBudget:
            t.sleep(1)
            print("\nConsider removing the item(s) you do not need immediately")
            while sum(overallCost) > customerBudget:
                notNow = max(timeSpan.items(), key=operator.itemgetter(1))[0]
                t.sleep(1)
                print("\nThe item,",notNow,"seems to be needed at a later time than other items in Budget list")
                t.sleep(1)
                choose = input("\nDo you want to view the purchase dates of the items in Budget list?: ")

                if choose == 'yes' or choose == 'Yes' or choose == 'YES' or choose == 'y' or choose == "Y":
                    t.sleep(1)
                    viewItem_time()
                item = input("\n\nEnter item you wish to purchase at a later date: ")

                if item.lower() in budgetList:
                    laterItems[item.lower()] = totalcost[item.lower()]/budgetList[item.lower()]
                    overallCost.remove(totalcost[item.lower()])
                    del timeSpan[item.lower()]
                    del budgetList[item.lower()]
                    del totalcost[item.lower()]                    

                else:
                    print("\nItem does not exist")
                    t.sleep(1)
                    item = input("\nEnter item you wish to purchase at a later date: ")
                 
            t.sleep(1)
            print("\nYou have successfully prioritized your items")

            Save() # If the expenses are below the budget the user gets an option to save
        else:
            t.sleep(1)
            print("\nThis option can only be used when you create a Budget list")
            
        
    def Save():
        if sum(overallCost) < customerBudget and sum(overallCost) > 0:
            t.sleep(1)
            print("\nYour balance is GHC",customerBudget - sum(overallCost))
            t.sleep(1)
            saveM = input("\nWould you consider placing your balance as savings?: ")
            if saveM == "yes" or saveM == "Yes" or saveM == "YES" or saveM == "y" or saveM == "Y":
                savings.append(sum(overallCost))
                
                t.sleep(1)
                print("\nCongratulations!!   Congratulations!!   Congratulations!!"
                      +"\n\nYour balance of GHC",customerBudget - sum(overallCost),"has been successfully saved")
                
            else:
                t.sleep(1)
                print("\n\n"+menu)
                t.sleep(1)
                pick = int(input("\n\nPick a number from the above options: "))
                budget(pick)
                    
        else:
            t.sleep(1)
            print("\nYou have exhausted your budget hence you can't save. Pick option 4 to prioritize items in Budget list")
                    
 

    while pick != 7:
            
        if pick == 1:
            item = input("\nEnter an item: ")            
            
            if item.lower() in budgetList:
                print("\nThis item exists in your budgetList")
                t.sleep(1)
                x = input('\nDo you want to top up on this item?: ')

                if x == 'yes' or x == 'Yes' or x == 'YES' or x == 'y':
                    overallCost.remove(totalcost[item.lower()])
                    t.sleep(1)
                    print("\nInitial cost entered was GHC",cost)
                    cost = float(input("\nConfirm the price of the item: GHC "))

                    if cost == totalcost[item.lower()]/number:
                        t.sleep(1)
                        print("\nYou chose to purchase", item.lower(), "by", Today + dt.timedelta(timeSpan[item.lower()]),",",timeSpan[item.lower()],"day(s) from now")
                        del timeSpan[item.lower()]
                        days = int(input("\nConfirm when you want to purchase this item. Please enter the number of days from today eg 23: "))
                        timeSpan[item.lower()] = days
                        number = int(input("\nEnter the expected quantity: "))
                        tot =  cost * number
                        budgetList[item.lower()] += number
                        totalcost[item.lower()] += tot
                        overallCost.append(totalcost[item.lower()])
                        
                    else:
                        print("\nCost entered is not equal to initial cost of item")
                        y = input("\nDo you want change the cost of the item?: ")
                        
                        if y == 'yes' or y == 'Yes' or y == 'YES' or y == 'y':
                            t.sleep(1)
                            cost = float(input("\nEnter new price of item: GHC "))
                            print("\nYou chose to purchase", item.lower(), "by", Today + dt.timedelta(timeSpan[item.lower()]),",",timeSpan[item.lower()],"day(s) from now")
                            del timeSpan[item.lower()]
                            days = int(input("\nConfirm when you want to purchase this item. Please enter the number of days from today eg 23: "))
                            timeSpan[item.lower()] = days
                            number = int(input("\nEnter the expected quantity: "))
                            budgetList[item.lower()] += number
                            tot =  cost * budgetList[item.lower()]
                            totalcost[item.lower()] = tot
                            overallCost.append(totalcost[item.lower()])

                        else:
                            number = int(input("\nEnter the expected quantity: "))
                            tot =  cost * number
                            budgetList[item.lower()] += number
                            totalcost[item.lower()] += tot
                            overallCost.append(totalcost[item.lower()])
                            

            else:
                days = int(input("\nWhen do you wish to purchase this item? Please enter the number of days from today eg 23: "))
                timeSpan[item.lower()] = days
                cost = float(input("\nEnter the price of the item: GHC "))
                number = int(input("\nEnter the expected quantity: "))
                budgetList[item.lower()] = number
                tot = cost * number
                totalcost[item.lower()] = tot
                overallCost.append(totalcost[item.lower()])
               
        elif pick == 2:
            item = input("\nEnter the item you wish to remove: ")
            if item.lower() in totalcost:
                overallCost.remove(totalcost[item.lower()])
                del budgetList[item.lower()]
                del totalcost[item.lower()]
            else:
                print("\nThis item is not Budget List")
            
        elif pick == 3:
            print("\nLIST OF ITEMS",'  |  ',"NUMBER OF ITEMS",'   |   ',"COST OF ITEMS",'   |   ',"DATE (year-month-day)")
            for it in budgetList:
                print("\n"+" "+it.ljust(16),"     ",str(budgetList[it]).ljust(15),"  ","GHC "+str(totalcost[it]).ljust(20)," ",Today + dt.timedelta(timeSpan[it]))
            print("\n\nTOTAL COST :","GHC",sum(overallCost),"             ","BUDGET : GHC",customerBudget)
                      
        elif pick == 4:
            prioriT()

        elif pick == 5:
            Save()

        elif pick == 6:
            print("\nLIST OF ITEMS",'  |  ',"COST OF ITEMS")
            for mn in laterItems:
                print("\n"+"   "+mn.ljust(16),"  ","GHC "+str(laterItems[mn]).ljust(2))
                        
        else:
            t.sleep(1)
            print("\nThis option does not exist")            

        t.sleep(1)
        print("\n\n"+menu)

        if sum(overallCost) > customerBudget:
            t.sleep(1)
            print("\n\nYou have exceeded your budget of GHC",customerBudget,"by GHC", str(sum(overallCost) - customerBudget)+". Pick option 4 to prioritize your items")
            t.sleep(1)
            pick = int(input("\n\nPick a number from the above options: "))
        else:
            pick = int(input("\n\nPick a number from the above options: "))
    

# The first part seen by the user
print("Welcome to Budget Assistant")
t.sleep(2)

customerBudget = float(input("\nHow much are you willing to budget: GHC "))

t.sleep(1)
menu = """\nOptions
-------
1. Add an item to Budget list

2. Withdraw item from Budget List

3. View your Budget list

4. Prioritize items

5. Save Money

6. View items to be purchased at later date

7. Quit program
"""
print(menu)

t.sleep(1)
pick = int(input("\nPick a number from the above options to begin: "))

if pick == 1:
    budget(pick)
            
elif pick == 2 or pick == 3 or pick == 4 or pick == 5 or pick == 6:
    print("Choose 1 to create a Budget list")
    pick = int(input("\nPick a number from the above options to begin: "))
    budget(pick)

elif pick == 7:
    t.sleep(1)
    y = str(input("Are you sure you want to quit this program?: "))
    if y == 'no' or y == 'NO' or y == 'No' or y == 'n' or y == "N":
        pick = int(input("\nPick a number from the above options to begin: ")) 
        budget(pick)

else:
    t.sleep(1)
    print("\nInvalid input")
    pick = int(input("Pick a number from the above options to begin: "))
    budget(pick)
