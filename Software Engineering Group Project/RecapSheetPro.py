import pymysql
import sys
class RecapSheet:

    def makeSheet(teamPair):
        HOST = "brahe.canisius.edu"
        PORT=3306
        USER="neppallv"
        PASSWORD="snake609"
        DB="neppallv_software"
        
      
        weekNum = int(input("Enter the week number: "))
        
        weekTeamDict = {
            1: ['1-2', '3-4', '5-6', '7-8'],
            2: ['6-8', '5-7', '2-4', '1-3'],
            3: ['5-4', '1-8', '7-3', '2-6'],
            4: ['3-6', '7-2', '1-5', '8-4'],
            5: ['7-1', '4-6', '3-8', '5-2'],
            6: ['2-3', '8-5', '4-1', '6-7'],
            7: ['4-7', '6-1', '8-2', '3-5'],
            8: ['5-6', '7-8', '3-4', '1-2'],
            9: ['2-4', '1-3', '5-7', '6-8'],
            10: ['7-3', '2-6', '1-8', '5-4'],
            11: ['1-5', '8-4', '7-2', '3-6'],
            12: ['3-8', '5-2', '4-6', '7-1'],
            13: ['4-1', '6-7', '8-5', '2-3'],
            14: ['8-2', '3-5', '6-1', '4-7'],
            15: ['4-3', '2-1', '8-7', '6-5'],
            17: ['8-1', '4-5', '6-2', '3-7'],
            18: ['2-7', '6-3', '4-8', '5-1'],
            19: ['6-4', '1-7', '2-5', '8-3'],
            20: ['5-8', '3-2', '7-6', '1-4'],
            21: ['1-6', '7-4', '5-3', '2-8'],
            22: ['8-7', '6-5', '2-1', '4-3'],
            23: ['3-1', '4-2', '8-6', '7-5'],
            24: ['6-2', '3-7', '4-5', '8-1'],
            25: ['4-8', '5-1', '6-3', '2-7'],
            26: ['2-5', '8-3', '1-7', '6-4'],
            27: ['7-6', '1-4', '3-2', '5-8'],
            28: ['5-3', '2-8', '7-4', '1-6'],
            29: ['2-1', '4-3', '6-5', '8-7'],
            30: ['8-6', '7-5', '4-2', '3-1'],
            31: ['4-5', '8-1', '3-7', '6-2'],
            32: ['6-3', '2-7', '5-1', '4-8'],
            33: ['1-7', '6-4', '8-3', '2-5'],
            34: ['3-2', '5-8', '1-4', '7-6'],
            35: ['7-4', '1-6', '2-8', '5-3']}
        teamList = weekTeamDict[weekNum]
        for each_list in teamList:
            print(each_list)
        splitTeams = teamList[teamPair].split("-")
        bowlerList = []
        team1 = splitTeams[0]
        team2 = splitTeams[1]
        lane = []
        lane = RecapSheet.getLanes(teamPair)
        lane1 = lane[0]
        lane2 = lane[1]

#######

        mydb = pymysql.connect(host=HOST,port=PORT,user=USER,passwd=PASSWORD,db=DB)
        cursor = mydb.cursor()
        cursor2 = mydb.cursor()

        query_string1 = "select * from team where tid = '" + team1 + "'"
        print("query_string1="+query_string1)
        numrows = cursor.execute(query_string1)
        if numrows == 0:
            print("This failed!72")
            return
        for row in cursor:
            teamName     = row[0]
            teamAverage  = row[1]
            teamHandicap = row[2]
            query_string2 = "select * from bowler where teamid = '" + team1 + "'"
            print("query_string1="+query_string1)
            print("query_string2="+query_string2)
            numrows2 = cursor2.execute(query_string2)
            if numrows2 == 0:
                print("This failed!83")
                return
            numBowlers = 0
            for row in cursor2:
                numBowlers = numBowlers + 1
                bowlerName       = row[1]
                bowlerAverage    = row[6]
                bowlerHandicap   = row[7]
                bowlerentry = str(bowlerName) + "," + str(bowlerAverage) + "," + str(bowlerHandicap)
                bowlerList.append(bowlerentry)
            teamData  =  str(teamName) + "," + str(teamAverage) + "," + str(teamHandicap) + "," + str(numBowlers)

        sendListP1  = []
        sendListP1.append(teamData)
        sendListP1.append(lane1)
        sendListP1.append(bowlerList)



#######
#Team 2
#######
        bowlerList2 = []
        query_string3 = "select * from team where tid = '" + team2 + "'"
        print("query_string3="+query_string3)
        numrows3 = cursor.execute(query_string3)
        if numrows3 == 0:
            print("This failed!110")
            return
        for row in cursor:
            teamName     = row[0]
            teamAverage  = row[1]
            teamHandicap = row[2]
            query_string4 = "select * from bowler where teamid = '" + team2 + "'"
            print("query_string3="+query_string3)
            print("query_string4="+query_string4)
            numrows4 = cursor2.execute(query_string4)
            if numrows4 == 0:
                print("This failed!121")
                return
            numBowlers = 0
            for row in cursor2:
                numBowlers = numBowlers + 1
                bowlerName = row[1]
                bowlerAverage = row[6]
                bowlerHandicap = row[7]
                bowlerentry2 = str(bowlerName) + "," + str(bowlerAverage) + "," + str(bowlerHandicap)
                bowlerList2.append(bowlerentry2)
            teamData  =  str(teamName) + "," + str(teamAverage) + "," + str(teamHandicap) + "," + str(numBowlers)
        sendListP2  = []
        sendListP2.append(teamData)
        sendListP2.append(lane2)
        sendListP2.append(bowlerList)
        sendList = []
        sendList.append(sendListP1)
        sendList.append(sendListP2)
        cursor.close()
        cursor2.close()
        print(sendList)
        return sendList


       # except:
         #   print("****Failed****")
         #   sys.exit(1)




    def getLanes(iteration):
        laneList = ["1.2", "3.4", "5.6", "7.8"]
        lanePair = laneList[iteration].split(".")
        return lanePair

RecapSheet.makeSheet(0)
