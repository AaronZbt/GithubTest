

array1 = [2,1,3,5,8,6,7,9]
array2 = (2,1,3,5,8,6,7,9)
'''
def  sortedSquenceArreay (array):
    newArray = []
    order = 0
    for i in array:
        x = i*i
        newArray.insert(i,x)
        newArray.sort()
        i +=1

    print(newArray)

'''
#第二题
'''
newArray = []
for i in array1:
    x = i*i
    newArray.insert(i,x)
    newArray.sort()
    i+=1

print(newArray)
'''


#第三题

competitions = [["HTML", "C#"],
               ["C#", "Python"],
               ["Python","HTML"]]

results = [0,0,1]


# winners = []
# i = 0
# for y in results:
#
#     if y == 0:
#         winners.append(competitions[i][1])
#     else:
#         winners.append(competitions[i][0])
#     i += 1
#
#     if i <= len(results):
#         continue
#     else:
#         break
#
# finalWinner = {}
#
# for winner in winners:
#     winners.count(winner)
#     if winners.count(winner) >=1:
#         finalWinner[winner] = winners.count(winner)
# z = max(finalWinner.items(),key=lambda x:x[1])[0]
#
# print(z)


# WIN_SCORE = 3
#
# def tournamentWinner(competitions, results):
#     # Write your code here.
#     currentBestteam = ""
#     scores = {currentBestteam:0}
#
#     for match in competitions:
#         homeTeam = match[0]
#         awayTeam = match[1]
#
#         for result in results:
#             if result == 0:
#                 scores[awayTeam] = 3
#             else:
#                 scores[homeTeam] = 3
# print(scores)

# HOME_TEAM_WON = 1
#
# def tournamentWinner (competitions, results):
#     currentBestteam = ""
#     scores = {currentBestteam:0}
#
#     for idx, competiton in enumerate(competitions):
#         result = results[idx]
#         homeTeam, awayTeam = competiton
#
#
#         winningTeam = homeTeam if result == HOME_TEAM_WON else awayTeam
#
#         updateScores(winningTeam, 3, scores)
#
#         if scores[winningTeam] > scores[currentBestteam]:
#             currentBestteam = winningTeam
#
#
#     return currentBestteam
#
#
#
#
# def updateScores (team, points, scores):
#
#     if team not in scores:
#         scores[team] = 0
#
#     scores[team] += points

########################################################## ”Question 4 “ ####################################

coins = [1,1,1,1,1,1]
coins.sort()

currentAmount = 0
cannotMake = 0
for i in coins:

    if i > currentAmount +1:
        cannotMake = currentAmount +1
    else:
        currentAmount = currentAmount + i
        print(currentAmount)

print(cannotMake)


# def nonConstructiblechange(coins):
#     coins.sort()
#
#     currenChangeCreated = 0
#
#     for coin in coins:
#         if coin > currenChangeCreated +1:
#             return  currenChangeCreated +1
#
#         currenChangeCreated += coin
#
#     return currentAmount +1

