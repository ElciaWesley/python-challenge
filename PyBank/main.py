import os
import csv

budget_data_csv = os.path.join(r"C:\Drake State Data Analyst\Challenges\python-challenge\PyBank\Resources\budget_data.csv")

totalmonth = 0
totalnet = 0
previous_profit_loss = 0
netchange_list = []
greatest_decrease = 0
greatest_increase = 0
with open(budget_data_csv) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")

    csv_header = next(csvreader)

    for row in csvreader:
        totalmonth = totalmonth +1
        profitloss = int(row[1])
        totalnet = totalnet + profitloss
        
        if totalmonth>1:
            netchange=profitloss-previous_profit_loss
            netchange_list.append(netchange)
            

        previous_profit_loss=profitloss
   
    most=max(netchange_list)
    least=min(netchange_list)
  
        

    average_netchange=sum(netchange_list)/len(netchange_list)
    


print("Total Month:",totalmonth)
print("Total:",totalnet)
print("Average Change:", average_netchange)
print("Greatest Increase in Profits:",most)
print("Great Decrease in Profits", least)


