#!/usr/bin/env python3
import glob
from opentrons import labware, instruments, modules, robot
from opentrons.legacy_api.modules import tempdeck
#Find out the serial number for two modules

#Then replace the below serial number with their corresponding numbers

cold_deck_ID = "TDV04P20190129B13"
hot_deck_ID = "TDV04P20190129B19"
mag_deck_ID = "MDV01P20181127A24"

module_dict = dict()

# Scan /dev/attyACM* for all dev paths:
devs = glob.glob("/dev/ttyACM*")

# Scan all ACM dev paths and attempt to connect temp modules
temp_decks = []
for dev in devs:
    deck = tempdeck.TempDeck()
    deck._port = dev
    # I did not test this try block. Depending on how the code is written, it may not throw an error when you attempt to connect to a mag deck. If that's the case, you may consider calling sys command `udevadm info` to get name of module and only connect when name is tempdeck
    try:
        deck.connect()
    except:
        continue
    temp_decks.append(deck)

# If you have more than one mag deck, you need to do the same here as well

# If modules not found. Give error and exit
if len(temp_decks) == 0:
    print("Failed to find given modules. Are they plugged in?")
    exit(1)

# Match temp deck with serial number:
# Only two provided serial number are checked, update if more temp modules need to be loaded
for deck in temp_decks:
    if deck.device_info == cold_deck_ID:
        cold_deck = deck
    elif deck.device_info == hot_deck_ID:
        hot_deck = deck
    else:
        print("Fatal error: Unknown serial number. Terminating...")
        exit(1)

# Disconnect temp decks if simulating. Otherwise decks will start running when the opentrons app runs simulation to check script integrity 
if robot.is_simulating():
    cold_deck.disconnect()
    hot_deck.disconnect()

# Now you can use hot_deck and cold_deck to control temprature of your deck
# However, you still need to load modules using their standard api:
# This is because the objects constructed by `modules.load('tempdeck')` and 'tempdeck.TempDeck()' belong to two different classes and they each support different part of functions required in this kind of scenario. You have to use hot_deck for any functions related to temp (set, wait, etc) and load hotDeck so that the robot knows there is a module loaded at this position (it will presumably adjust how deep pipettes go down at these locations as plates are elevated by modules)

hotDeck = modules.load('tempdeck',4)
coldDeck = modules.load('tempdeck',7) # Or the positions they are in respectively on the deck

# Use cold_deck and hot_deck to set temp:
cold_deck.set_temprature(10)
hot_deck.set_temprature(60)

cold_deck.wait_for_temp()
hot_deck.wait_for_temp()


