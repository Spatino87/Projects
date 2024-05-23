
####Make sure that input.csv is titled as passed in line 11 and it resides in the same directory as project.py####
####To run the program: python project.py####


import csv
from operator import itemgetter


with open('input.csv') as csvfile:
    readCSV = csv.reader(csvfile)
    data=list(readCSV)


data = data[5:]
m_matrix = zip(*data) 

m_matrix = [list(elem) for elem in m_matrix]



def clenseResult2(allData):
    '''This method takes the data collected from the xlsx (excel) file and formats the messy data
    so that we can comprehend the data better '''
    for i in range(len(allData)): 
        
        for j in range(len(allData[i])): 

            if allData[i][j][0].isdigit(): 
                allData[i][j] = float(allData[i][j])
            elif allData[i][j] == '--':
                allData[i][j] = 0.0; 

               


clenseResult2(m_matrix)


listOfDictionary =[]
def createDictionary(allData,listOfDictionary):
    '''This method converts our list of lists to a list of dictionaries so that we can easily sort it later according to key'''
    for i in range(1, 54):
        
        dictionary = {}; 
        dictionary["state"] = allData[0][i] 
        listOfDictionary.append(dictionary)

    for i in range(0, 53): #53 total districts
        
        for j in range(len(allData)): # 13 metrics
            
            listOfDictionary[i][j] = allData[j][i+1]



createDictionary(m_matrix, listOfDictionary)


def displayMenu():
    '''this method is to print the menu of metrics out to the user'''
    print("1. Adult Smoking")
    print("2. Youth Smoking")
    print("3. Adult Physical Activity")
    print("4. Youth Physical Activity")
    print("5. Adult Nutrition")
    print("6. Youth Nutrition")
    print("7. Adult Binge Drinking")
    print("8. Youth Binge Drinking")
    print("9. Observed Seat Belt Use")
    print("10. Youth Seat Belt Use")
    print("11. Youth Marijuana Use")


def fetchTopResults(metric, numberOfResults):
    '''this method displays top results for a specified numberOfResults and metric '''
    print("Top " + str(numberOfResults) + " Results")
    res = sorted(listOfDictionary, key=itemgetter(metric), reverse = True) #operator library's sorted method 
    
    for i in range (0, numberOfResults):
        
        print(res[i]["state"], res[i][metric])


def fetchBottomResults(metric, numberOfResults):
    '''this method displays bottom results for a specified numberOfResults and metric '''
    print("Bottom " + str(numberOfResults) + " Results")
    res = sorted(listOfDictionary, key=itemgetter(metric), reverse = False) #operator library's sorted method 
    
    for i in range (0, numberOfResults):
        
        print(res[i]["state"], res[i][metric])



#prompt the user to input a metric and number of results until he/she wants to end the program
while True:
    displayMenu();
    metric = input("Please enter the corresponding metric number to be summarized, (enter 0 to quit): ")
    
    if metric < 0 or metric > 11:
        print("Please enter a valid number")
   
    elif metric == 0:
        break
   
    else:
        numberOfResults = input("Please enter how many results you would like to see: ")
        print('\n')
        fetchTopResults(metric, numberOfResults)
        print('\n')
        fetchBottomResults(metric, numberOfResults)
        print('\n')





