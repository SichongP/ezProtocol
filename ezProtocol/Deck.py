# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 10:04:51 2019

@author: pengs
"""
#import sys
import pandas as pd
from opentrons import labware as lw
from opentrons import robot
from sys import exit

class well:
    
    # Each well should hold its parameters: depth, remaining volume(optional), max volume
    # Calculate volume/height for each well
    
    def _calculateCapacity(self):
        # Assume cylinder shaped tube
        # If well is in fact cube shaped, tip will be moved deeper than it should. So far it doesn't seem to cause a problem for up to 50ml tubes
        pi=3.14
        return pi*(self.diameter**2)/4
    
    def getLocation(self, volume):
        # Return distance from bottom the pipette should go to inorder to pipette given volume (self.volume must be set)
        if self.volume==None:
            print("Can't calculate location without knowing volume left in well!")
            exit(1)
        return round((self.volume-volume)/self.capacity,0)
    
    def addVolume(self, vol):
        self.volume += vol
        if self.volume > self.max_volume:
            self.volume -= vol
            return False
        return True
    
    def removeVolume(self, vol):
        self.volume -= vol
        if self.volume < 0:
            self.volume += vol
            return False
        return True
        
    def volLeft(self):
        return self.volume
    
    def isEmpty(self):
        if self.volume==0:
            return True
        else:
            return False
        
    def isUnset(self):
        if self.volume==None:
            return True
        else:
            return False
    
    def __init__(self, i):
        stats = i.properties
        (self.depth, self.max_volume, self.diameter, 
         self.length, self.width, self.height) = (stats['depth'], i.max_volume(), stats['diameter'],
                                                 stats['length'], stats['width'], stats['height'])
        self.capacity = self._calculateCapacity()
        self.volume = None
        self.name = None
        
        

class labware:
    
    def _getName(self, labwareTable):
        return labwareTable.LabwareType.to_list()[0]

    def _identifyLabware(self):
        try:
            container = lw.load(self.name, 1)
        except ValueError:
            print('Error! Labware \"{}\" not found. Have you created it in opentrons database yet?'.format(self.name))
            exit(1)
        wells = {}
        for i in container.wells():
            wells[i.get_name()] = well(i)
            wells[i.get_name()].name = i.get_name()
        robot.reset()
        return wells
    
    def _fillWells(self, labwareTable):
        for well in labwareTable.itertuples():
            self.wells[well.WellID].volume = well.volume if not pd.isnull(well.volume) else None

            
    def __init__(self, labwareTable):
        self.name = self._getName(labwareTable)
        self.wells = self._identifyLabware()
        self._fillWells(labwareTable)
    
class Deck:

    def _readTestFile(self, file):
        try:
            deck_input = pd.read_csv(file)
        except Exception as e:
            print(e)
            exit(1)
        return deck_input

    def labwareTypeIsConsistent(self):
        labwareTypes = dict()
        for sample in self._deckInput.itertuples():
            if not sample.Slot in labwareTypes.keys():
                labwareTypes[sample.Slot] = sample.LabwareType
            elif not labwareTypes[sample.Slot] == sample.LabwareType:
                print("Error: Different plate type specifications for slot ", sample.Slot, ". Exiting now...")
                exit(1)
        return labwareTypes

    def _multiSampleReagent(self):
        multiSampleReagents = {}
        for reagent in self.reagents:
            if len(self.reagents[reagent]['Name'].unique())>1:
                multiSampleReagents[reagent] = self.reagents[reagent]['Name'].unique().tolist()
        return multiSampleReagents
# Below function gets unique samples (unique names)    
#    def _sampleNamePerReagent(self):
#        sampleNames = {}
#        for reagent in self.reagents:
#            sampleNames[reagent] = self.reagents[reagent]['Name'].unique().tolist()
#            sampleNames[reagent].sort()
#        return sampleNames
 
# Below function gets all samples regardless of names    
    def _sampleNamePerReagent(self):
        sampleNames = {}
        for reagent in self.reagents:
            sampleNames[reagent] = self.reagents[reagent]['Name'].tolist()
            sampleNames[reagent].sort()
        return sampleNames
    
    def _subsetTableByLabware(self):
        labwares = {}
        for slotID in self._deckInput.Slot.unique():
            labwares[slotID] = self._deckInput[self._deckInput.Slot==slotID]
        return labwares
    
    def __init__(self, sample_file):
        
        robot.reset()
        
        self._deckInput = self._readTestFile(sample_file)
        #self._plateInput = self._readTestFile(plate_file)
        self.reagents = {reagent: self._deckInput[self._deckInput.Reagent == reagent] 
                        for reagent in self._deckInput.Reagent.unique()}
        self.multiSampleReagent = self._multiSampleReagent()
        self.sampleNames = self._sampleNamePerReagent()
        self.labwareTypes = self.labwareTypeIsConsistent()
        self.labwareTable = self._subsetTableByLabware()
        self.labwares={}
        for i in self.labwareTable.keys():
            self.labwares[i] = labware(self.labwareTable[i])
#       Don't need to initiate labware objects
#        try:
#            self.labwares = {slot: labware.load(self._labwareTypes[slot], slot) for slot in self._deckInput.Slot.unique()}
#        except ValueError as v:
#            print("Unrecognized container:", v)
#            exit()
#        except Exception as e:
#            print(e)
#            exit()
        #self.formulas = formula._intialProtocolFile(protocol_file)

if __name__ == "__main__":
    deck = Deck('../TestInputPlate.csv')
    print(deck.reagents)
    print(deck.labwares)
    #formulas = formula._intialProtocolFile()
    import pprint
    pprint.pprint(deck)

