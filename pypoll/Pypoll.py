import os
import csv


csvpath = os.path.join("election_data.csv")

#lists
count = 0
candidates_list = []
totalcandidate = []
uniquecandidate = []
khanvote = 0
correyvote = 0
livote = 0
otooleyvote = 0
votetally = [khanvote, correyvote, livote, otooleyvote]


with open(csvpath) as csvfile:
    csvreader= csv.reader(csvfile, delimiter= ',')

    header= next(csvreader)

#total number of votes cast

    for row in csvreader:
        count +=1

        #candidates

        candidates_list.append(row[2])

    for name in candidates_list:
        if name not in uniquecandidate:
            uniquecandidate.append(name)
        if name == "Khan":
            khanvote += 1
        elif name == "Correy":
            correyvote += 1
        elif name == "Li":
            livote += 1
        else:
            otooleyvote +=1

    print(f'khan : {khanvote}, correy : {correyvote}, li: {livote}, otooley: {otooleyvote}')
    print(count)
    winningvote_count= max(votetally)
    winner = uniquecandidate[votetally.index(winningvote_count)]


    print(winner)

    print(f'Khan: {round ((khanvote / count) * 100, 2 )}% ({khanvote})')
    print(f'Correy: {round ((correyvote / count) * 100, 2 )}% ({correyvote})')
    print(f'Li: {round ((livote / count) * 100, 2 )}% ({livote})')
    print(f'otooley: {round ((otooleyvote / count) * 100, 2 )}% ({otooleyvote})')

    outpath = os.path.join('..', 'pypoll_output.txt')
    with open(outpath, "w") as text:
        text.write("------------------------------------\n")
        text.write(f"Election Results\n")
        text.write("------------------------------------\n")
        text.write(f"Total Votes: " + str(count) + "\n")
        text.write("------------------------------------\n")
        text.write(f"Khan: " + str(round((khanvote/count)*100,2)) + "% " + "(" + str((khanvote)) + ")" + "\n")
        text.write(f"Correy: " + str(round((correyvote/count)*100,2)) + "% " + "(" + str((correyvote)) + ")" + "\n")
        text.write(f"Li: " + str(round((livote/count)*100,2)) + "% " + "(" + str((livote)) + ")" + "\n")
        text.write(f"O'Tooley: " + str(round((otooleyvote/count)*100,2)) + "% " + "(" + str((otooleyvote)) + ")" + "\n")
        text.write("------------------------------------\n")
        text.write(f"Winner: " + str(winner) + "\n")
        text.write("------------------------------------\n")



