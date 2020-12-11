#Main Menu
while True:
    print('\nWelcome to Stat Central\n')
    print('To Search A Players Stats, Type "Stat"')
    print('To Compare 2 Players Stats, Type "Compare"')
    print('To Exit, Type "Quit"')
    initialize = input('Selection: ')

    #Stat Search Menu
    if initialize == "Stat":
        while True:
            print('\nWelcome to Stat Search\n')
            print('"Hit" to Search Hitter Stats')
            print('"Pitch" to Search Pitcher Stats')
            print('"Quit" to Exit')
            selection = input('\nSelection: ')

            #Run stat search for hitters
            if selection == "Hit":
                fname = input("\nInput Hitter's First Name: ")
                lname = input("Input Hitter's Last Name: ")

                #turn names into lower case strings needed for website search
                fullname = lname[:1] + "/" + lname[:5] + fname[:2]
                fullname = fullname.lower()

                #prepare website url by inserting necesarry string
                website = "https://www.baseball-reference.com/players/" + fullname + "01.shtml"

                #open the webpage and parse for data using Selenium
                from selenium import webdriver
                driver = webdriver.Chrome('chromedriver.exe')
                driver.get(website)

                #create dictionary for stats
                player = {

                    "AB" : {"xpath": '//*[@id="batting_standard"]/tfoot/tr[1]/td[3]', "value" : "" },
                    "H" : {"xpath": '//*[@id="batting_standard"]/tfoot/tr[1]/td[5]', "value" : "" },
                    "HR" : {"xpath": '//*[@id="batting_standard"]/tfoot/tr[1]/td[8]', "value" : "" },
                    "BA" : {"xpath": '//*[@id="batting_standard"]/tfoot/tr[1]/td[14]', "value" : "" },
                    "R" : {"xpath": '//*[@id="batting_standard"]/tfoot/tr[1]/td[4]', "value" : "" },
                    "RBI" : {"xpath": '//*[@id="batting_standard"]/tfoot/tr[1]/td[9]', "value" : "" },
                    "SB" : {"xpath": '//*[@id="batting_standard"]/tfoot/tr[1]/td[10]', "value" : "" },
                    "OBP" : {"xpath": '//*[@id="batting_standard"]/tfoot/tr[1]/td[15]', "value" : "" },
                    "SLG" : {"xpath": '//*[@id="batting_standard"]/tfoot/tr[1]/td[16]', "value" : "" },
                    "OPS" : {"xpath": '//*[@id="batting_standard"]/tfoot/tr[1]/td[17]', "value" : "" },
                }

                #assign value of stat from wepage using the xpath
                for stat in player.keys():
                    player[stat]["value"] = driver.find_element_by_xpath(player[stat]["xpath"]).text

                #close driver and webpage
                driver.close()

                #Stat Selection Menu
                while True:
                    print('\nSelect ' + fname + lname + ' Career Stat: \n')

                    #display list of stats to choose from with their descriptions
                    for stat in player.keys():
                        print(stat)

                    print('\n"AB" = At Bats, "H" = Hits, "HR" = Home Runs, "BA" = Batting Average, "R" = Runs Scored')
                    print('"RBI" = Runs Batted In, "SB" = Stolen Bases "OBP" = On Base %, "SLG" = Slugging %, "OPS" = On Base + Slugging %')
                    print('\n"Quit" For Main Menu\n')

                    #user inputs stat they want to see
                    mychoice = input('Choice: ')

                    #cases for what is returned to user depending on their input
                    if mychoice in player.keys():
                        print(mychoice,':',player[mychoice]["value"])
                    elif mychoice == "Quit":
                        break
                    else:
                        print("Stat Not Found, Try Again\n")

            #Run stat search for pitchers
            elif selection == "Pitch":
                 fname = input("\nInput Pitcher's First Name: ")
                 lname = input("Input Pitcher's Last Name: ")

                 #turn names into lower case strigns needed for website search
                 fullname = lname[:1] + "/" + lname[:5] + fname[:2]
                 fullname = fullname.lower()

                 #prepare website url by inserting necesarry string
                 website = "https://www.baseball-reference.com/players/" + fullname + "01.shtml"

                 #open the webpage and parse for data using Selenium
                 from selenium import webdriver
                 driver = webdriver.Chrome('chromedriver.exe')
                 driver.get(website)

                 #create dictionary for stats
                 player = {

                     "IP": {"xpath": '//*[@id="pitching_standard"]/tfoot/tr[1]/td[11]', "value" : "" },
                     "W" : {"xpath": '//*[@id="pitching_standard"]/tfoot/tr[1]/td[1]', "value" : "" },
                     "L" : {"xpath": '//*[@id="pitching_standard"]/tfoot/tr[1]/td[2]', "value" : "" },
                     "SV" : {"xpath": '//*[@id="pitching_standard"]/tfoot/tr[1]/td[10]', "value" : "" },
                     "ERA" : {"xpath": '//*[@id="pitching_standard"]/tfoot/tr[1]/td[4]', "value" : "" },
                     "BB" : {"xpath": '//*[@id="pitching_standard"]/tfoot/tr[1]/td[16]', "value" : "" },
                     "SO" : {"xpath": '//*[@id="pitching_standard"]/tfoot/tr[1]/td[18]', "value" : "" },
                     "WHIP" : {"xpath": '//*[@id="pitching_standard"]/tfoot/tr[1]/td[25]', "value" : "" },

                 }

                 #assign value of stat from wepage using the xpath
                 for stat in player.keys():
                     player[stat]["value"] = driver.find_element_by_xpath(player[stat]["xpath"]).text

                 #close driver and webpage
                 driver.close()

                 #Stat Selection menu
                 while True:
                     print('\nSelect ' + fname + lname + ' Career Stat: \n')

                     #display list of stats to choose from with their descriptions
                     for stat in player.keys():
                         print(stat)

                     print('\n"IP" = Innings Pitched,"W" = Wins, "L" = Losses, "SV" = Saves, "ERA" = Earned Run Average,')
                     print('"BB" = Walks, "SO" = Strike Outs, "WHIP" = Walks + Hits per Innings Pitched')
                     print('\n"Quit" For Main Menu\n')

                 #user inputs stat
                     mychoice = input('Choice: ')

                 #cases for what is returned to user depending on their input
                     if mychoice in player.keys():
                         print(mychoice,':',player[mychoice]["value"])
                     elif mychoice == "Quit":
                         break
                     else:
                         print("Stat Not Found, Try Again")

            #Quit out of Stat Search
            elif selection == "Quit":
                break

            #Failsafe for none of the above inputs
            else:
                print("Error, Try Again\n")

    #Stat Compare Menu
    elif initialize == "Compare":
        while True:
            print('\nWelcome to Stat Compare')
            print('\n"Hit" To Compare Two Hitters')
            print('"Pitch" To Compare Two Pitchers')
            print('"Quit" For Main Menu')
            selection = input('\nSelection: ')

            #Hitter Compare Menu
            if selection == "Hit":
                print("\nPick Two Hitters to Compare")
                #input player names
                fname1 = input("Input Hitter 1's First Name: ")
                lname1 = input("Input Hitter 1's Last Name: ")
                fname2 = input("Input Hitter 2's First Name: ")
                lname2 = input("Input Hitter 2's Last Name: ")

                #turn names into lower case strigns needed for website search
                fullname1 = lname1[:1] + "/" + lname1[:5] + fname1[:2]
                fullname1 = fullname1.lower()

                fullname2 = lname2[:1] + "/" + lname2[:5] + fname2[:2]
                fullname2 = fullname2.lower()

                #prepare website search strings
                website1 = "https://www.baseball-reference.com/players/" + fullname1 + "01.shtml"

                website2 = "https://www.baseball-reference.com/players/" + fullname2 + "01.shtml"

                #open the first webpage and parse for data using Selenium
                from selenium import webdriver
                driver = webdriver.Chrome('chromedriver.exe')
                driver.get(website1)


                #create first dictionary for stats
                player1 = {

                    "AB" : {"xpath1": '//*[@id="batting_standard"]/tfoot/tr[1]/td[3]', "value1" : "" },
                    "H" : {"xpath1": '//*[@id="batting_standard"]/tfoot/tr[1]/td[5]', "value1" : "" },
                    "HR" : {"xpath1": '//*[@id="batting_standard"]/tfoot/tr[1]/td[8]', "value1" : "" },
                    "BA" : {"xpath1": '//*[@id="batting_standard"]/tfoot/tr[1]/td[14]', "value1" : "" },
                    "R" : {"xpath1": '//*[@id="batting_standard"]/tfoot/tr[1]/td[4]', "value1" : "" },
                    "RBI" : {"xpath1": '//*[@id="batting_standard"]/tfoot/tr[1]/td[9]', "value1" : "" },
                    "SB" : {"xpath1": '//*[@id="batting_standard"]/tfoot/tr[1]/td[10]', "value1" : "" },
                    "OBP" : {"xpath1": '//*[@id="batting_standard"]/tfoot/tr[1]/td[15]', "value1" : "" },
                    "SLG" : {"xpath1": '//*[@id="batting_standard"]/tfoot/tr[1]/td[16]', "value1" : "" },
                    "OPS" : {"xpath1": '//*[@id="batting_standard"]/tfoot/tr[1]/td[17]', "value1" : "" },
                }

                #assign value of stat from wepage using the xpath
                for stat in player1.keys():
                    player1[stat]["value1"] = driver.find_element_by_xpath(player1[stat]["xpath1"]).text

                #close driver and webpage
                driver.close()

                #open the second webpage and parse for data using Selenium
                from selenium import webdriver
                driver = webdriver.Chrome('chromedriver.exe')
                driver.get(website2)

                #create second dictionary for stats
                player2 = {

                    "AB" : {"xpath2": '//*[@id="batting_standard"]/tfoot/tr[1]/td[3]', "value2" : "" },
                    "H" : {"xpath2": '//*[@id="batting_standard"]/tfoot/tr[1]/td[5]', "value2" : "" },
                    "HR" : {"xpath2": '//*[@id="batting_standard"]/tfoot/tr[1]/td[8]', "value2" : "" },
                    "BA" : {"xpath2": '//*[@id="batting_standard"]/tfoot/tr[1]/td[14]', "value2" : "" },
                    "R" : {"xpath2": '//*[@id="batting_standard"]/tfoot/tr[1]/td[4]', "value2" : "" },
                    "RBI" : {"xpath2": '//*[@id="batting_standard"]/tfoot/tr[1]/td[9]', "value2" : "" },
                    "SB" : {"xpath2": '//*[@id="batting_standard"]/tfoot/tr[1]/td[10]', "value2" : "" },
                    "OBP" : {"xpath2": '//*[@id="batting_standard"]/tfoot/tr[1]/td[15]', "value2" : "" },
                    "SLG" : {"xpath2": '//*[@id="batting_standard"]/tfoot/tr[1]/td[16]', "value2" : "" },
                    "OPS" : {"xpath2": '//*[@id="batting_standard"]/tfoot/tr[1]/td[17]', "value2" : "" },
                }

                #assign value of stat from wepage using the xpath
                for stat in player2.keys():
                    player2[stat]["value2"] = driver.find_element_by_xpath(player2[stat]["xpath2"]).text

                #close driver and webpage
                driver.close()

                #Stat compare selection menu
                while True:
                    print('\n' + fname1 + ' ' + lname1 + ' vs ' + fname2 + ' ' + lname2)
                    print('\nSelect Career Stat to Compare: \n')

                    #display list of stats to choose from with their descriptions
                    for stat in player1.keys():
                        print(stat)

                    print('\n"AB" = At Bats, "H" = Hits, "HR" = Home Runs, "BA" = Batting Average, "R" = Runs Scored')
                    print('"RBI" = Runs Batted In, "SB" = Stolen Bases "OBP" = On Base %, "SLG" = Slugging %, "OPS" = On Base + Slugging %')
                    print('\n"Quit" to exit\n')

                    #user inputs stat
                    mychoice1 = input('Choice: ')

                    #cases for what is returned to user depending on their input
                    if mychoice1 in player1.keys() and player2.keys():
                        print(fname1 + ' ' + lname1 + " Career " + mychoice1,':',player1[mychoice1]["value1"])
                        print(fname2 + ' ' + lname2 + " Career " + mychoice1,':',player2[mychoice1]["value2"])

                        if float(player1[mychoice1]["value1"]) > float(player2[mychoice1]["value2"]):
                             difference = float(player1[mychoice1]["value1"]) - float(player2[mychoice1]["value2"])
                             differencestr = str(difference)
                             difference = differencestr[:5]
                             print(fname1 + ' ' + lname1 + ' Has ' + difference + ' More Career ' + mychoice1 + ' Than ' + fname2 + ' ' + lname2)

                        elif float(player1[mychoice1]["value1"]) < float(player2[mychoice1]["value2"]):
                              difference = float(player2[mychoice1]["value2"]) - float(player1[mychoice1]["value1"])
                              differencestr = str(difference)
                              difference = differencestr[:5]
                              print(fname2 + ' ' + lname2 + ' Has ' + difference + ' More Career ' + mychoice1 + ' Than ' + fname1 + ' ' + lname1)

                        elif float(player1[mychoice1]["value1"]) == float(player2[mychoice1]["value2"]):
                              print('They Have the Same Career ' + mychoice1)
                        else:
                            print('Error: Stat not Found. Try Again\n')

                    elif mychoice1 == "Quit":
                        break

                    else:
                        print('Error, Try Again\n')

            #Pitcher Compare Menu
            elif selection == "Pitch":
                print("\nPick Two Pitchers to Compare")

                #input player names
                fname1 = input("Input Pitcher 1's First Name: ")
                lname1 = input("Input Pitcher 1's Last Name: ")
                fname2 = input("Input Pitcher 2's First Name: ")
                lname2 = input("Input Pitcher 2's Last Name: ")

                #turn names into lower case strigns needed for website search
                fullname1 = lname1[:1] + "/" + lname1[:5] + fname1[:2]
                fullname1 = fullname1.lower()

                fullname2 = lname2[:1] + "/" + lname2[:5] + fname2[:2]
                fullname2 = fullname2.lower()

                #prepare website search string
                website1 = "https://www.baseball-reference.com/players/" + fullname1 + "01.shtml"

                website2 = "https://www.baseball-reference.com/players/" + fullname2 + "01.shtml"

                #open the first webpage and parse for data using Selenium
                from selenium import webdriver
                driver = webdriver.Chrome('chromedriver.exe')
                driver.get(website1)


                #create first dictionary for stats
                player1 = {

                    "IP": {"xpath1": '//*[@id="pitching_standard"]/tfoot/tr[1]/td[11]', "value1" : "" },
                    "W" : {"xpath1": '//*[@id="pitching_standard"]/tfoot/tr[1]/td[1]', "value1" : "" },
                    "L" : {"xpath1": '//*[@id="pitching_standard"]/tfoot/tr[1]/td[2]', "value1" : "" },
                    "SV" : {"xpath1": '//*[@id="pitching_standard"]/tfoot/tr[1]/td[10]', "value1" : "" },
                    "ERA" : {"xpath1": '//*[@id="pitching_standard"]/tfoot/tr[1]/td[4]', "value1" : "" },
                    "BB" : {"xpath1": '//*[@id="pitching_standard"]/tfoot/tr[1]/td[16]', "value1" : "" },
                    "SO" : {"xpath1": '//*[@id="pitching_standard"]/tfoot/tr[1]/td[18]', "value1" : "" },
                    "WHIP" : {"xpath1": '//*[@id="pitching_standard"]/tfoot/tr[1]/td[25]', "value1" : "" },

                }

                #assign value of stat from wepage using the xpath
                for stat in player1.keys():
                    player1[stat]["value1"] = driver.find_element_by_xpath(player1[stat]["xpath1"]).text

                #close driver and webpage
                driver.close()

                #open the second webpage and parse for data using Selenium
                from selenium import webdriver
                driver = webdriver.Chrome('chromedriver.exe')
                driver.get(website2)

                #create second dictionary for stats
                player2 = {

                    "IP": {"xpath2": '//*[@id="pitching_standard"]/tfoot/tr[1]/td[11]', "value2" : "" },
                    "W" : {"xpath2": '//*[@id="pitching_standard"]/tfoot/tr[1]/td[1]', "value2" : "" },
                    "L" : {"xpath2": '//*[@id="pitching_standard"]/tfoot/tr[1]/td[2]', "value2" : "" },
                    "SV" : {"xpath2": '//*[@id="pitching_standard"]/tfoot/tr[1]/td[10]', "value2" : "" },
                    "ERA" : {"xpath2": '//*[@id="pitching_standard"]/tfoot/tr[1]/td[4]', "value2" : "" },
                    "BB" : {"xpath2": '//*[@id="pitching_standard"]/tfoot/tr[1]/td[16]', "value2" : "" },
                    "SO" : {"xpath2": '//*[@id="pitching_standard"]/tfoot/tr[1]/td[18]', "value2" : "" },
                    "WHIP" : {"xpath2": '//*[@id="pitching_standard"]/tfoot/tr[1]/td[25]', "value2" : "" },

                }

                #assign value of stat from wepage using the xpath
                for stat in player2.keys():
                    player2[stat]["value2"] = driver.find_element_by_xpath(player2[stat]["xpath2"]).text

                #close driver and webpage
                driver.close()

                #Stat compare selection menu
                while True:
                    print('\n' + fname1 + ' ' + lname1 + ' vs ' + fname2 + ' ' + lname2)
                    print('\nSelect Career Stat to Compare: ')

                    #display list of stats to choose from with their descriptions
                    for stat in player1.keys():
                        print(stat)

                    print('\n"IP" = Innings Pitched,"W" = Wins, "L" = Losses, "SV" = Saves, "ERA" = Earned Run Average,')
                    print('"BB" = Walks, "SO" = Strike Outs, "WHIP" = Walks + Hits per Innings Pitched')
                    print('\n"Quit" For Main Menu\n')

                    #user inputs stat
                    mychoice1 = input('Choice: ')

                    #cases for what is returned to user depending on their input
                    if mychoice1 in player1.keys() and player2.keys():
                        print(fname1 + ' ' + lname1 + " Career " + mychoice1,':',player1[mychoice1]["value1"])
                        print(fname2 + ' ' + lname2 + " Career " + mychoice1,':',player2[mychoice1]["value2"])

                        if float(player1[mychoice1]["value1"]) > float(player2[mychoice1]["value2"]):
                             difference = float(player1[mychoice1]["value1"]) - float(player2[mychoice1]["value2"])
                             differencestr = str(difference)
                             difference = differencestr[:5]
                             print(fname1 + ' ' + lname1 + ' Has ' + difference + ' More Career ' + mychoice1 + ' Than ' + fname2 + ' ' + lname2)

                        elif float(player1[mychoice1]["value1"]) < float(player2[mychoice1]["value2"]):
                              difference = float(player2[mychoice1]["value2"]) - float(player1[mychoice1]["value1"])
                              differencestr = str(difference)
                              difference = differencestr[:5]
                              print(fname2 + ' ' + lname2 + ' Has ' + difference + ' More Career ' + mychoice1 + ' Than ' + fname1 + ' ' + lname1)

                        elif float(player1[mychoice1]["value1"]) == float(player2[mychoice1]["value2"]):
                              print('They Have the Same Career ' + mychoice1)
                        else:
                            print('Error: Stat not Found. Try Again\n')

                    elif mychoice1 == "Quit":
                        break

                    else:
                        print('Error, Try Again\n')

            #Quit to main menu
            elif selection == "Quit":
                break

            else:
                print('Error, Try Again')

    #quit out of program
    elif initialize == "Quit":
        break
    else:
        print("\nTry Again\n")
