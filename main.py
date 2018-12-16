import os
import random
import time
from time import gmtime, strftime

import pyautogui


def lookForActions(upgradeBuildingAndResearch=False):
    numberOfRewardClaims = 0
    numberOfPeopleHelped = 0
    numberOfResourcesCollected = 0
    buildingsUpgraded = 0
    researchDone = 0
    startTime = time.perf_counter()
    while True:

        print("Running time: " + str((time.perf_counter() - startTime) // 60) + " minutes")
        print("Number of rewards claimed: " + str(numberOfRewardClaims))
        print("Number of people helped: " + str(numberOfPeopleHelped))
        print("Number of resources gathered: " + str(numberOfResourcesCollected))
        print("Number of buildings upgraded: " + str(buildingsUpgraded))
        print("Number of research project started: " + str(researchDone))

        print("=============================================\n")
        time.sleep(3)
        rewardAvailable_ImagePath = 'images/rewardAvailable5.PNG'
        rewardAvailable2_ImagePath='images/rewardAvailable6.PNG'
        dilithium_ImagePath = 'images/resource_dilithium.PNG'
        parsteel_ImagePath = 'images/resource_parsteel.PNG'
        tritanium_ImagePath = 'images/resource_tritanium.PNG'
        helpAvailable_ImagePath = 'images/helpAvailable2.PNG'
        goButton_ImagePath = 'images/goButton.PNG'
        askForHelpButton='images/askForHelpButton.PNG'
        topLevelImages = [dilithium_ImagePath, parsteel_ImagePath, helpAvailable_ImagePath,
                          rewardAvailable_ImagePath, tritanium_ImagePath, goButton_ImagePath, rewardAvailable2_ImagePath, askForHelpButton]
        chance = random.randint(0, 10)
        if chance > 3:  # Insurance in case it gets stuck in a screen
            clickBackButton()

        for filePath in topLevelImages:
            time.sleep(1)
            print("Looking for " + filePath + "...")
            actionFound = pyautogui.locateCenterOnScreen(filePath, confidence=0.85)
            if actionFound is not None:
                print("-----------------------------------")
                print(str(filePath) + " found at " + strftime("%H:%M:%S\t", gmtime()))
                if 'rewardAvailable' in filePath:
                    clickOnCoordinates(actionFound)
                    if claimReward():
                        numberOfRewardClaims += 1
                        continue

                elif 'help' in filePath:
                    clickOnCoordinates(actionFound)
                    if helpAll():
                        numberOfPeopleHelped += 1


                elif 'resource_' in filePath:
                    print("Clicking on " + str(actionFound))
                    pyautogui.click(actionFound[0], actionFound[1])
                    numberOfResourcesCollected += 1
                    time.sleep(1)
                elif 'goButton' in filePath:
                    clickOnCoordinates(actionFound)
                    print("Go button found")
                    if not upgradeBuildingAndResearch:
                        print("Skipping upgrading buildings and doing research")
                        continue
                    for n in range(2):
                        buildingUpgradeButton = pyautogui.locateCenterOnScreen("images/upgradeButton.PNG")
                        if clickOnCoordinates(buildingUpgradeButton):
                            print("Upgrading building")
                            buildingsUpgraded += 1
                            continue
                        researchAvailable = pyautogui.locateCenterOnScreen("images/researchAvailable.PNG")
                        clickOnCoordinates(researchAvailable)
                        startButton=pyautogui.locateCenterOnScreen("images/researchStartButton.PNG")
                        clickOnCoordinates(startButton)
                        time.sleep(1)
                        crossButton=pyautogui.locateCenterOnScreen("images/crossButton.PNG")
                        if clickOnCoordinates(crossButton):
                            print("Researching next thing")
                            researchDone += 1
                        clickBackButton()
                elif "askForHelp" in filePath:
                    clickOnCoordinates(actionFound)
                    print("Asked for help")
            else:
                print(strftime("%H:%M:%S\t", gmtime()) + "No action found\n")


def helpAll():
    print("Helping all...")
    time.sleep(1)
    helpAllButton = pyautogui.locateCenterOnScreen('images/helpAllButton.PNG', confidence=0.85)
    if clickOnCoordinates(helpAllButton):
        if clickBackButton():
            print("Help All success")
            return True
    else:
        return False


def clickOnCoordinates(coordinateTuple):
    if coordinateTuple is not None:
        print("Clicking on " + str(coordinateTuple))
        pyautogui.click(coordinateTuple[0], coordinateTuple[1])
        time.sleep(4)
        return True
    else:
        print("No coordinates found")
        return False


def clickBackButton():
    backButton = pyautogui.locateCenterOnScreen("images/backButton.PNG", confidence=0.85)
    if backButton:
        pyautogui.click(backButton[0], backButton[1])
        time.sleep(2)
        print("Clicked on back button")
        return True
    else:
        return False


def claimReward():
    time.sleep(3)
    claimButton = pyautogui.locateCenterOnScreen("images/claimButton2.PNG", confidence=0.85)
    if clickOnCoordinates(claimButton):
        doneButton = pyautogui.locateCenterOnScreen("images/doneButton.PNG", confidence=0.85)
        if clickOnCoordinates(doneButton):
            if clickBackButton():
                return True
    print("Could not claim reward")
    return False


actionFound = lookForActions()
