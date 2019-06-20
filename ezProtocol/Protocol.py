# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 15:06:03 2019

@author: pengs
"""
import frontmatter
import pandas as pd
from ezProtocol import Deck
#import Deck
from sys import exit
import regex, yaml

#pd.set_option('display.max_columns', 15)

# Things to add
# Mix at the end of divided transfer



class Pipette():
    def _identifyPipette(self):
        # Code for pipettes:
        pipettes = {'P10_single':1,
                    'P10_Single':1,
                    'P50_single':2,
                    'P50_Single':2,
                    'P300_single':3,
                    'P300_Single':3,
                    'P1000_single':4,
                    'P1000_Single':4
                }
        return pipettes[self.name] if self.name in pipettes.keys() else None
    
    def _standardizeName(self):
        pipettes = {1: 'P10_Single',
                    2: 'P50_Single',
                    3: 'P300_Single',
                    4: 'P1000_Single'
                }
        return(pipettes[self.id])
    
    def _getMaxVolume(self):
        max_volume = {1: 10, 2: 50, 3: 300, 4: 1000}
        return max_volume[self.id]
    
    def _getMinVolume(self):
        min_volume = {1: 0.1, 2: 5, 3: 30, 4: 100}
        return min_volume[self.id]
    
    def _attachTipRack(self, tipracks):
        pipette_tip = {1: 10,
                   2: 300,
                   3: 300,
                   4: 1000    
                   }
        tiprack=None
        for i in tipracks:
            if 'volume' in i.keys():
                if i['volume']==str(pipette_tip[self.id]):
                    tiprack = i
                    break
            else:
                volume = regex.match(r".+?(\d+)ul",i['type'])[1]
                if not volume:
                    print("Can't recognize tiprack type: {}. Check spelling or provide tip volume for custome tiprack".format(i['type']))
                    exit(1)
                elif volume==str(pipette_tip[self.id]):
                    tiprack = i
                    break
        if not tiprack:
            print("Can't find tips for pipette: {}.".format(self.name))
            exit(1)
        return tiprack
            
    def __init__(self, name, tipracks):
        self.name, self.mount = name.split(':')
        self.id = self._identifyPipette()
        if not self.id:
            print("Fatal error: Unkown pipette specified!")
            exit(1)
        self.name = self._standardizeName()
        self.max_volume, self.min_volume = self._getMaxVolume(), self._getMinVolume()  
        self.tiprack = self._attachTipRack(tipracks)

class Operation():
    def __init__(self, source, target, volume, touch_tips=False, air_gap=False, blow_out=False, 
                 mix_before_aspirate=0, mix_after_dispense=0, aspirate_speed=0, dispense_speed=0, 
                 pause_after_aspirate=0, pause_after_dispense=0, mix_before_rate=1, mix_after_rate=1, mix_volume=0):
        (self.source, self.target, self.volume) = (source, target, volume)
        (self.touch_tips, self.air_gap, self.blow_out, 
         self.mix_before_aspirate, self.mix_after_dispense) = (touch_tips, air_gap, blow_out, 
                                                          mix_before_aspirate, mix_after_dispense)
        (self.mix_before_rate, self.mix_after_rate, self.mix_volume) = (mix_before_rate, mix_after_rate, mix_volume)
        (self.aspirate_speed, self.dispense_speed, 
                 self.pause_after_aspirate, self.pause_after_dispense) = (aspirate_speed, dispense_speed, 
                 pause_after_aspirate, pause_after_dispense)
    
    def _printOperation(self, in_script):
        if in_script:
            comment = '#'
        else:
            comment=''
        to_print = comment + 'transfer {}ul from:\n #source(s)\tTo\ttarget(s)\n'.format(self.volume)
        for i in range(max(len(self.source), len(self.target))):
            to_print += comment + '{}\t\t{}\n'.format(self.source[i] if i<len(self.source) else None, self.target[i] if i<len(self.target) else None)
        if not in_script:
            print(to_print)
        return to_print
    
    def _choosePipette(self, pipettes):
        # This method chooses a pipette that's best suited for operation based on volumes
        # When more than one available, always choose the one with bigger max volume in case of distribution
        use=None
        max_volume=0
        for pipette in pipettes:    
            if self.volume>pipette.min_volume and pipette.max_volume>max_volume:
                use = pipette
                max_volume = pipette.max_volume
        if not use:
            print('Error! Volume {}ul to small for any available pipette!'.format(self.volume))
            exit(1)
        return use
    
    def _singleTransfer(self, aspirate_volume, dispense_volume, pipette, source, target, labwares, droptips=True, tipattached=False):
        # Single source only
        # Multi targets okay
        command = ''
        # Get info regarding source well
        source_well = labwares[source[0]].wells[source[1]]
        
        if source_well.volume==None:
            command += '# No volume info available in source well, assuming enough volume...\n'
            well_name = "(\'"+source[1]+"\')"
        elif source_well.volume<aspirate_volume:
            print("Not enough volume left to aspirate in slot {} well {}".format(source[0], source[1]))
            exit(1)
        else:
            well_name = "(\'"+source[1]+"\')"+".bottom({})".format(source_well.getLocation(aspirate_volume))
            #print(well_name)
        
        # If aspirate and dispense speeds are specified, change them
        if self.aspirate_speed>0:
            command += '# Save default aspirate speed setting\n'
            command += 'default_aspirate = pipettes[{}].speeds["aspirate"]\n'.format(pipette.id)
            command += '# Set aspirate flow rate to {} uL/second\n'.format(self.aspirate_speed)
            command += 'pipettes[{}].set_flow_rate(aspirate={})\n'.format(self.aspirate_speed)
        if self.dispense_speed>0:
            command += '# Save default dispense speed setting\n'
            command += 'default_dispense = pipettes[{}].speeds["dispense"]\n'.format(pipette.id)
            command += '# Set aspirate flow rate to {} uL/second\n'.format(self.dispense_speed)
            command += 'pipettes[{}].set_flow_rate(dispense={})\n'.format(self.dispense_speed)
        # Prepare aspiration    
        if not tipattached:
            command += '# Picking up tips\n'
            command += 'pipettes[{}].pick_up_tip()\n'.format(pipette.id)
        if self.mix_before_aspirate>0:
            command += '# Mixing {} times before aspirating\n'.format(self.mix_before_aspirate)
            mix_volume = self.mix_volume if self.mix_volume>0 else aspirate_volume/2
            command += 'pipettes[{}].mix({},{}, labwares[{}].wells{}, rate={})\n'.format(pipette.id, self.mix_before_aspirate, mix_volume, source[0], well_name, self.mix_before_rate)
        # Aspirate
        command += '# Aspirating {}ul from slot {} well {}\n'.format(aspirate_volume, source[0], source[1])
        command += 'pipettes[{}].aspirate({},labwares[{}].wells{})\n'.format(pipette.id, aspirate_volume, source[0], well_name)
        # Post-aspiration process
        if self.pause_after_aspirate>0:
            command += '# Pausing {} seconds\n'.format(self.pause_after_aspirate)
            command += 'pipettes[{}].delay(seconds={})\n'.format(pipette.id, self.pause_after_aspirate)
        if self.air_gap:
            command += '# Air gapping 2ul\n'
            command += 'pipettes[{}].air_gap(2)\n'.format(pipette.id)
        # Dispense
        for i in target:
            target_well = labwares[i[0]].wells[i[1]]
        
            if target_well.volume==None:
                command += '# No volume info available in target well, assuming enough room for dispensing...\n'
                well_name = "(\'"+i[1]+"\')"
            elif target_well.volume+dispense_volume>target_well.max_volume:
                print("Not enough room left to dispense in slot {} well {}".format(i[0], i[1]))
                exit(1)
            else:
                well_name = "(\'"+i[1]+"\')"+".top()"
            
            command += '# Dispensing {}ul to slot {} well {}\n'.format(dispense_volume, i[0], well_name)
            command += 'pipettes[{}].dispense({}, labwares[{}].wells{})\n'.format(pipette.id, dispense_volume, i[0], well_name)
            command += '# Performing a blow out\npipettes[{}].blow_out()\n'.format(pipette.id) if self.blow_out else ''
            mix_volume = self.mix_volume if self.mix_volume>0 else dispense_volume/2
            command += '# Mixing\npipettes[{}].mix({},{}, labwares[{}].wells{}, rate={})\n'.format(pipette.id, self.mix_after_dispense, mix_volume, i[0], well_name ,self.mix_after_rate) if self.mix_after_dispense>0 else ''

            command += '# Pausing {0} seconds\npipettes[{1}].delay(seconds={0})\n'.format( self.pause_after_dispense, pipette.id) if self.pause_after_dispense>0 else ''
            command += '# Touch tip\npipettes[{}].touch_tip()\n'.format(pipette.id) if self.touch_tips else ''
        
        # Drop tips
        if droptips:
            command += '# Drop tips\n'
            command += 'pipettes[{}].drop_tip()\n'.format(pipette.id)
        
        # Reset default pipette rates if changed
        if self.aspirate_speed>0:
            command += '# Reset default aspirate speed \n'
            command += 'pipettes[{}].set_flow_rate(aspirate=default_aspirate)\n'.format(pipette.id)
        if self.dispense_speed>0:
            command += '# Reset default dispense speed \n'
            command += 'pipettes[{}].set_flow_rate(dispense=default_dispense)\n'.format(pipette.id)
        
        return command    
        
    def _divideTransfers(self, volume, max_volume, min_volume):
        volumes=[]
        n = int(volume/max_volume) 
        for i in range(n):
            volumes += [max_volume]
        remain = volume - sum(volumes)
        if remain < min_volume:
            to_add = (volumes.pop() + remain)/2
            volumes += [to_add, to_add]
        else:
            volumes += [remain]
        return volumes
    
    def makeCommands(self, pipettes, labwares):
        pipette = self._choosePipette(pipettes)
        command=self._printOperation(True)
        if len(self.source)==0 or len(self.target)==0:
            print('Error occured in operation:\n')
            self._printOperation()
            print('No source or target wells found!\n')
            exit(1)
        if self.volume>pipette.max_volume:
            command += '# Transfer volume exceeds pipette max volume, automatically divide into multiple transfers\n'
            volume_list = self._divideTransfers(self.volume, pipette.max_volume, pipette.min_volume)
        else:
            volume_list = [self.volume]
        if len(self.source)>1 and len(self.target)==1:
            #Consolidate
            for i in self.source:
                for volume in volume_list:
                    command += self._singleTransfer(volume, volume, pipette, i, self.target, labwares)
        elif len(self.source)==1 and len(self.target)>1:
            #Distribute
            # get max volume the pipette can hold
            max_volume = pipette.max_volume
            if self.volume>max_volume:
                # A single transfer exceeds max volume the pipette can hold. Can't distribute. Do simple transfer instead
                for i in self.target:
                    for volume in volume_list:
                        command += self._singleTransfer(volume, volume, pipette, self.source[0], [i], labwares)
            elif self.volume*len(self.target) > max_volume:
                # total volume to distribute exceeds max volume the pipette can hold. Divide operation
                n = int(max_volume/self.volume)
                for i in range((len(self.target) + n - 1) // n ):
                    volume = pipette.min_volume if self.volume*n<pipette.min_volume else self.volume*n
                    command += self._singleTransfer(volume, self.volume, pipette, self.source[0], self.target[i * n:(i + 1) * n], labwares)
            else:
                # Can be distributed in a single transfer:
                command += self._singleTransfer(self.volume*len(self.target), self.volume, pipette, self.source[0], self.target, labwares)
        elif len(self.target)==len(self.source):
            #Transfer
            for source, target in zip(self.source, self.target):
                for volume in volume_list:
                    command += self._singleTransfer(volume, volume, pipette, source, [target], labwares)
        else:
            print('Error! Opeartion has unequal target/source well numbers. Offending operations:\n')
            self._printOperation(False)
            exit(1)
        return command
            

class Protocol:
    # This is a class to parse and store protocol
    # More functionality needs to be added for sanity check
    #operators = ['+']
    
    def _readProtocolFile(self,file):
        try:
            file_content = frontmatter.load(file)
        except FileNotFoundError:
            print("Error! Can't find file: ", file)
            exit()
        except Exception as e:
            print(e)
            exit()
        return file_content
    
   

    def _parseFormula(self, formula):
        (source, target) = regex.split(r"=", formula)
        sources = regex.split(r"\s*\+\s*", source)
        formula_table = pd.DataFrame({'Feature':[], 'Reagent':[], 'Volume':[], 'Wildcard':[], 'Specifics':[]})
        for item in sources:
            match = regex.match(r"(?(DEFINE)(?P<volume>[0-9]+\.*[0-9]*)(?P<wildcard>\(\w+\))(?P<source>\w+)(?P<specifics>[a-zA-Z0-9\.,=_:\s]+))(?&volume)\s*\*\s*(?&wildcard)?\s*\*?\s*(?&source)\s*\|?\s*(?&specifics)?", item)
            formula_table = formula_table.append(pd.DataFrame({'Feature':['source'],
                                              'Reagent':[match.captures('source')[0]],
                                              'Volume':[match.captures('volume')[0]],
                                              'Wildcard':[match.captures('wildcard')[0]] 
                                              if len(match.captures('wildcard'))>0 else None,
                                              'Specifics':[match.captures('specifics')[0]] 
                                              if len(match.captures('specifics'))>0 else None}, index=['source']))
        match = regex.match(r"(?(DEFINE)(?P<target>\w+)(?P<specifics>[a-zA-Z0-9\.,=_:\s]+))\s*(?&target)\s*\|?\s*(?&specifics)?", target)
        total_volume = formula_table.Volume.astype(float).sum()
        formula_table = formula_table.append(pd.DataFrame({'Feature':['target'],
                                              'Reagent':[match.captures('target')[0]],
                                              'Volume':[total_volume],
                                              'Wildcard':[None],
                                              'Specifics':[match.captures('specifics')[0]]
                                              if len(match.captures('specifics'))>0 else None}, index=['target']))
        return formula_table
    
    def _parseProtocol(self, protocol):
        formulas = []
        for line in protocol.content.split('\n'):
            formula = self._parseFormula(line)
            formulas.append(formula)
        return formulas
    
    def _getReagents(self):
        #This method returns a list of reagents
        reagents = []
        for formula in self.formulas:
        # For each line of formula:
            reagents = reagents + formula.Reagent.tolist()
        return reagents

    def _reagentsOnDeck(self, deck):
        # Check if all reagents specified in protocol can be located on deck
        reagents = self._getReagents()
        passed = True
        for reagent in reagents:
            if not reagent in deck.reagents.keys():
                print("Error: Detected reagent name:", reagent, "missing in sample file!")
                passed = False
        return passed

    def _is_number(self, string):
        try:
            float(string)
        except ValueError:
            return False
        else:
            return True

    def _parseWildcard(self, string):
        if not string==None:
            string = regex.match(r"\((.+)\)",string).group(1)
            match = regex.split(r"\+", string)
            new = []
            for item in match:
                if self._is_number(item):
                    new.append(float(item))
                elif item in self.deck.reagents.keys():
                    new.append(len(self.deck.reagents[item]))
                else:
                    print("Error! Unrecognized wildcard: ", item)
                    exit(1)
            return sum(new)

    def _expandWildcard(self):
        for formula in self.formulas:
            formula['wildcard_expanded'] = formula.Wildcard.apply(self._parseWildcard)
                
    def _updateVolume(self):
        self._expandWildcard()
        for formula in self.formulas:
            formula['Volume'] = formula['Volume'].astype(float)
            formula['wildcard_expanded'] = formula['wildcard_expanded'].fillna(1)
            formula['updated_volume'] = formula['Volume'] * formula['wildcard_expanded']
            formula.loc['target','updated_volume']= formula.loc['source','updated_volume'].sum()

# =============================================================================
# If a reagent in 'source' has multiple samples (with different names),
# product should also have same number of samples with same names
# =============================================================================
    
    def _fetchSampleByReagent(self, string):
        return self.deck.sampleNames[string]
    
    def _countUniqueSamples(self, string):
        return len(self.deck.sampleNames[string])
    
    def _linkSampleToReagent(self):
        for formula in self.formulas:
            formula['sample_list'] = formula.Reagent.apply(self._fetchSampleByReagent)
            formula['unique_sample_count'] = formula.Reagent.apply(self._countUniqueSamples)
            

    def _formulaIsExpandable(self):
        for formula in self.formulas:
            product = formula.groupby('Feature')['unique_sample_count'].apply(lambda x: x.product())
            if not product['source']==product['target']:
                print(formula)
                return False
        return True

    def _getSampleWell(self, sample_list, reagent_name):
        #return a 2D list with [Slot, WellID] for each well
        df = self.deck.reagents[reagent_name]
        well_list=[]
        for item in sample_list:
            extract = df.query('Name=="%s"' %item)
            extract = extract.loc[:,'Slot':'WellID']
            for i in range(extract.shape[0]):
                well_list.append(extract.iloc[i,:].tolist())
        return well_list
    
    def _matchByName(self, source, target_list):
        matched=[]
        for i in target_list:
            matched.append(i) if i==source else None
        return matched

    def _convertFormulaToOperation(self):
        # We need to first identify if target reagent relates to multiple samples (aliquoating)
        # In that case we can first aliquoat single-sample reagents into targets
        operations = []
        for formula in self.formulas:
            source_sliced = formula.loc['source']
            if isinstance(source_sliced, pd.Series):
                source_sliced = source_sliced.to_frame().transpose()
            for source_reagent in source_sliced.itertuples():
                specifics = yaml.load("".join(source_reagent.Specifics.split()).replace(":",": ").replace(",","\n")) if source_reagent.Specifics else None
                keys = specifics.keys() if specifics else [None]
                mix_before_rate = specifics['mix_before_rate'] if 'mix_before_rate' in keys else 1
                mix_after_rate = specifics['mix_after_rate'] if 'mix_after_rate' in keys else 1
                touch_tips = specifics['touch_tips'] if 'touch_tips' in keys else False
                air_gap = specifics['air_gap']  if 'air_gap' in keys else False
                blow_out = specifics['blow_out'] if 'blow_out' in keys else False
                mix_before_aspirate = specifics['mix_before_aspirate'] if 'mix_before_aspirate' in keys else 0
                mix_after_dispense = specifics['mix_after_dispense'] if 'mix_after_dispense' in keys else 0
                aspirate_speed = specifics['aspirate_speed'] if 'aspirate_speed' in keys else 0
                dispense_speed = specifics['dispense_speed'] if 'dispense_speed' in keys else 0
                mix_volume = specifics['mix_volume'] if 'mix_volume' in keys else 0 
                pause_after_aspirate = specifics['pause_after_aspirate']if 'pause_after_aspirate' in keys else 0
                pause_after_dispense = specifics['pause_after_dispense'] if 'pause_after_dispense' in keys else 0
                source = self._getSampleWell(source_reagent.sample_list, source_reagent.Reagent)
                target = self._getSampleWell(formula.loc['target'].sample_list, formula.loc['target'].Reagent)
                volume = source_reagent.updated_volume
                if len(source)>1 and len(target)>1 and len(source)!=len(target):
                    print("Unequal target and source well numbers, attempt to divide by sample names")
                    for item in source_reagent.sample_list:
                        # Match by name
                        target_list = self._matchByName(item, formula.loc['target'].sample_list)
                        subset_source = self._getSampleWell([item], source_reagent.Reagent)
                        subset_target = self._getSampleWell([item], formula.loc['target'].Reagent)
                        #print("appending operation:")
                        #print(subset_source)
                        #print(subset_target)
                        operations.append(Operation(source=subset_source, target=subset_target, volume=volume, touch_tips=touch_tips, air_gap=air_gap, blow_out=blow_out, mix_before_aspirate=mix_before_aspirate, mix_after_dispense=mix_after_dispense, aspirate_speed=aspirate_speed, mix_before_rate=mix_before_rate, mix_after_rate=mix_after_rate, dispense_speed=dispense_speed, pause_after_dispense=pause_after_dispense, pause_after_aspirate = pause_after_aspirate, mix_volume = mix_volume))
                else:
                    operations.append(Operation(source=source, target=target, volume=volume, touch_tips=touch_tips, air_gap=air_gap, blow_out=blow_out, mix_before_aspirate=mix_before_aspirate, mix_after_dispense=mix_after_dispense, aspirate_speed=aspirate_speed, mix_before_rate=mix_before_rate, mix_after_rate=mix_after_rate, dispense_speed=dispense_speed, pause_after_dispense=pause_after_dispense, pause_after_aspirate = pause_after_aspirate, mix_volume = mix_volume))
        return operations

    def _writeProtocol(self):
        # Write support information
        opentron_protocol = ['# This script is generated by ezProtocol writer.\n# Author: Sichong Peng \n# Contact: scpeng@ucdavis.edu']
        # Import libraries
        opentron_protocol.append("# import libraries\nfrom opentrons import labware, instruments, robot")
        # Initiate labwares
        opentron_protocol.append('#Initiate labwares\nlabwares={}')
        for i in self.deck.labwareTypes.keys():
            opentron_protocol.append('labwares[{1}] = labware.load(\'{0}\', {1})'.format(self.deck.labwareTypes[i], i))
        # Initiate tip racks and pipettes
        # A dict object for each, with pipette id as keys for both
        opentron_protocol.append('#Initiate tipracks and pipettes\ntipracks={}\npipettes={}')
        for i in self.pipettes:
            opentron_protocol.append('tipracks[{0}] = labware.load(\'{1}\', {2})'.format(i.id, i.tiprack['type'], i.tiprack['slot']))
            opentron_protocol.append('pipettes[{0}] = instruments.{1}(mount=\'{2}\',tip_racks=[tipracks[{0}]])'.format(i.id, i.name, i.mount))
        # Generate command for each operation
        for operation in self.operations:
            #print('Try this operation:\n')
            #operation._printOperation(False)
            opentron_protocol.append(operation.makeCommands(self.pipettes, self.deck.labwares))
        return opentron_protocol
    
    def saveScript(self, path):
        try:
            with open(path,'w') as f:
                f.write('\n'.join(self.script))
        except Exception as e:
            print(e)
            return False
        return True
        
    
    def _parseHeader(self):
        # Collect tipracks
        if 'tiprack' in self.protocol.keys():
            self.tipracks = self.protocol.metadata['tiprack']
        else:
            print('Error: No tipracks detected!')
            exit(1)
        # Collect pipettes
        if 'pipette' in self.protocol.keys():
            pp = self.protocol.metadata['pipette'].replace(" ","").split(',')
            self.pipettes = []
            for item in pp:
                self.pipettes.append(Pipette(item, self.tipracks))
        else:
            print('Error: No pipettes specified!')
            exit(1)
            
    def __init__(self, protocol_file, deck_file=None):
        # Read in file
        self.protocol = self._readProtocolFile(protocol_file)
        
        # Parse header for pipettes and tipracks
        self._parseHeader()
        
        # Parse content 
        self.formulas = self._parseProtocol(self.protocol)
        
        # Use test file if none provided. Change this later
        if not deck_file:
            deck_file = '../test/TestInputPlate.csv'
        # Read deck file
        self.deck = Deck.Deck(deck_file)
        
        # Check conflictions between labwares and tipracks
        fail = False
        for i in self.tipracks:
            if i['slot'] in self.deck.labwareTypes.keys():
                print('Error: slot {} contains both {} and {}'.format(i['slot'], i['type'], self.deck.labwareTypes[i['slot']]))
                fail = True
        if fail:
            exit(1)
                
        # Check if all reagents listed in protocol can be found on deck
        if not self._reagentsOnDeck(self.deck):
            print("Missing samples. Exiting now...")
            exit(1)
            
        # Expand wildcard to get total volumes
        self._updateVolume()
        
        # Find samples for each reagent name and check if a formula is expandable
        self._linkSampleToReagent()
        #if not self._formulaIsExpandable():
            #print("Can't expand formulas. Do you have enough target wells?")
            #exit(1)
                                                                                                                                                                                                                                                                                                                                                                            
        # Convert protocol table to operation object per transfer
        self.operations = self._convertFormulaToOperation()
        
        # Generate script from operations
        self.script = self._writeProtocol()
            
if __name__ == "__main__":
    protocol = Protocol('../testProtocol.txt')
    import pprint
    print('Printing script to test.py')
    protocol.saveScript('./test.py')

