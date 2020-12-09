from selenium import webdriver
driver = webdriver.Chrome('chromedriver.exe')
driver.get("https://www.baseball-reference.com/players/j/jeterde01.shtml")

player = {

    "WAR": {"xpath": '//*[@id="info"]/div[4]/div[2]/div[1]/p', "value" : "" },
    "AB" : {"xpath": '//*[@id="info"]/div[4]/div[2]/div[2]/p', "value" : "" },
    "H" : {"xpath": '//*[@id="info"]/div[4]/div[2]/div[3]/p', "value" : "" },
    "HR" : {"xpath": '//*[@id="info"]/div[4]/div[2]/div[4]/p', "value" : "" },
    "BA" : {"xpath": '//*[@id="info"]/div[4]/div[2]/div[5]/p', "value" : "" },
    "R" : {"xpath": '//*[@id="info"]/div[4]/div[3]/div[1]/p', "value" : "" },
    "RBI" : {"xpath": '//*[@id="info"]/div[4]/div[3]/div[2]/p', "value" : "" },
    "SB" : {"xpath": '//*[@id="info"]/div[4]/div[3]/div[3]/p', "value" : "" },
    "OBP" : {"xpath": '//*[@id="info"]/div[4]/div[4]/div[1]/p', "value" : "" },
    "SLG" : {"xpath": '//*[@id="info"]/div[4]/div[4]/div[2]/p', "value" : "" },
    "OPS" : {"xpath": '//*[@id="info"]/div[4]/div[4]/div[3]/p', "value" : "" },
}

for stat in player.keys():
    player[stat]["value"] = driver.find_element_by_xpath(player[stat]["xpath"]).text

driver.close()

while True:
    print("\nSelect Derek Jeter Career Stat:\n")

    for stat in player.keys():
        print(stat)

    print('\n"WAR" = Wins Above Replacement,"AB" = At Bats, "H" = Hits, "HR" = Home Runs, "BA" = Batting Average,')
    print('"R" = Runs Scored, "RBI" = Runs Batted In, "SB" = Stolen Bases "OBP" = On Base %, "SLG" = Slugging %, "OPS" = On Base + Slugging %')
    print('\n"Quit" to exit\n')

    mychoice = input('Choice: ')

    if mychoice in player.keys():
        print(mychoice,':',player[mychoice]["value"])
    elif mychoice == "Quit":
        break
    else:
        print("Stat Not Found, Try Again")
    print()
