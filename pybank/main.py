import os
import csv

#Specifying the path to write the output to file 
output_path = os.path.join("..", "PyBank", "Analysis", "output.txt")

# Path to access budget_data.csv file
csvpath = os.path.join('..','PyBank', 'Resources', 'budget_data.csv')
    
counter=0
greatestIncreaseInProfit=0
greatestDecreaseInProfit=0
sumOfNetChangeInProfit=0
firstRow=True
total=0
dots="-----------------------------------------------"



with open(output_path, 'w', newline='') as outputFile:
     
    outputFile.writelines(f'Financial Analysis\n{dots}\n')


    with open(csvpath) as budgetFile:

        csvreader = csv.reader(budgetFile, delimiter=',')

        csv_header = next(csvreader)
        
        for items in csvreader:

            if firstRow==True:
                total=total+int(items[1])

                counter+=1
                
                previousRow=int(items[1])
                
                firstRow=False
            
            else:
                total=total+int(items[1])

                counter+=1
                
                netChange=int(items[1])-previousRow

                previousRow=int(items[1])

                sumOfNetChangeInProfit += netChange
                
                if netChange > greatestIncreaseInProfit:
                    greatestIncreaseInProfit = netChange
                    greatestIncreaseInProfitmonth = items[0]
                
                elif netChange<greatestDecreaseInProfit:
                    greatestDecreaseInProfit=netChange
                    greatestDecreaseInProfitmonth=items[0]
            
        averageChange=sumOfNetChangeInProfit/(counter-1)

        outputFile.writelines(f'Total Months : {counter}\n')
        outputFile.writelines(f"Total : {total}\n")
        outputFile.writelines(f"Average Change : ${round(averageChange,2)}\n")
        outputFile.writelines(f'Greatest Increase In Profits : {greatestIncreaseInProfitmonth} (${greatestIncreaseInProfit})\n')
        outputFile.writelines(f'Greatest Decrease In Profits : {greatestDecreaseInProfitmonth} (${greatestDecreaseInProfit})')
        
        # Printing the values to terminal
        print("Financial Analysis\n",dots)
        print(f'Total Months : {counter}')
        print("Total : ",total)
        print(f"Average Change : ${round(averageChange,2)}")
        print(f'Greatest Increase In Profits : {greatestIncreaseInProfitmonth} (${greatestIncreaseInProfit})')
        print(f'Greatest Decrease In Profits : {greatestDecreaseInProfitmonth} (${greatestDecreaseInProfit})')
       
        
        





