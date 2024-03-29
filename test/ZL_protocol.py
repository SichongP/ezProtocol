# This script is generated by ezProtocol writer.
# Author: Sichong Peng 
# Contact: scpeng@ucdavis.edu
# import libraries
from opentrons import labware, instruments, robot
#Initiate labwares
labwares={}
labwares[1] = labware.load('3x4_1.5mL_Rack', 1)
labwares[2] = labware.load('96-well-plate-20mm', 2)
#Initiate tipracks and pipettes
tipracks={}
pipettes={}
tipracks[1] = labware.load('tiprack-10ul', 4)
pipettes[1] = instruments.P10_Single(mount='left',tip_racks=[tipracks[1]])
tipracks[3] = labware.load('opentrons-tiprack-300ul', 5)
pipettes[3] = instruments.P300_Single(mount='right',tip_racks=[tipracks[3]])
#transfer 1056.0ul from:
 #source(s)	To	target(s)
#[1, 'A1']		[1, 'D3']
# Transfer volume exceeds pipette max volume, automatically divide into multiple transfers
# No volume info available in source well, assuming enough volume...
# Picking up tips
pipettes[3].pick_up_tip()
# Aspirating 300ul from slot 1 well A1
pipettes[3].aspirate(300,labwares[1].wells('A1'))
# No volume info available in target well, assuming enough room for dispensing...
# Dispensing 300ul to slot 1 well ('D3')
pipettes[3].dispense(300, labwares[1].wells('D3'))
# Drop tips
pipettes[3].drop_tip()
# No volume info available in source well, assuming enough volume...
# Picking up tips
pipettes[3].pick_up_tip()
# Aspirating 300ul from slot 1 well A1
pipettes[3].aspirate(300,labwares[1].wells('A1'))
# No volume info available in target well, assuming enough room for dispensing...
# Dispensing 300ul to slot 1 well ('D3')
pipettes[3].dispense(300, labwares[1].wells('D3'))
# Drop tips
pipettes[3].drop_tip()
# No volume info available in source well, assuming enough volume...
# Picking up tips
pipettes[3].pick_up_tip()
# Aspirating 300ul from slot 1 well A1
pipettes[3].aspirate(300,labwares[1].wells('A1'))
# No volume info available in target well, assuming enough room for dispensing...
# Dispensing 300ul to slot 1 well ('D3')
pipettes[3].dispense(300, labwares[1].wells('D3'))
# Drop tips
pipettes[3].drop_tip()
# No volume info available in source well, assuming enough volume...
# Picking up tips
pipettes[3].pick_up_tip()
# Aspirating 156.0ul from slot 1 well A1
pipettes[3].aspirate(156.0,labwares[1].wells('A1'))
# No volume info available in target well, assuming enough room for dispensing...
# Dispensing 156.0ul to slot 1 well ('D3')
pipettes[3].dispense(156.0, labwares[1].wells('D3'))
# Drop tips
pipettes[3].drop_tip()

#transfer 422.4ul from:
 #source(s)	To	target(s)
#[1, 'A2']		[1, 'D3']
# Transfer volume exceeds pipette max volume, automatically divide into multiple transfers
# No volume info available in source well, assuming enough volume...
# Picking up tips
pipettes[3].pick_up_tip()
# Aspirating 300ul from slot 1 well A2
pipettes[3].aspirate(300,labwares[1].wells('A2'))
# Pausing 1 seconds
pipettes[3].delay(seconds=1)
# No volume info available in target well, assuming enough room for dispensing...
# Dispensing 300ul to slot 1 well ('D3')
pipettes[3].dispense(300, labwares[1].wells('D3'))
# Mixing
pipettes[3].mix(10,150.0, labwares[1].wells('D3'), rate=2)
# Pausing 1 seconds
pipettes[3].delay(seconds=1)
# Drop tips
pipettes[3].drop_tip()
# No volume info available in source well, assuming enough volume...
# Picking up tips
pipettes[3].pick_up_tip()
# Aspirating 122.39999999999998ul from slot 1 well A2
pipettes[3].aspirate(122.39999999999998,labwares[1].wells('A2'))
# Pausing 1 seconds
pipettes[3].delay(seconds=1)
# No volume info available in target well, assuming enough room for dispensing...
# Dispensing 122.39999999999998ul to slot 1 well ('D3')
pipettes[3].dispense(122.39999999999998, labwares[1].wells('D3'))
# Mixing
pipettes[3].mix(10,61.19999999999999, labwares[1].wells('D3'), rate=2)
# Pausing 1 seconds
pipettes[3].delay(seconds=1)
# Drop tips
pipettes[3].drop_tip()

#transfer 184.8ul from:
 #source(s)	To	target(s)
#[1, 'D3']		[2, 'A1']
#None		[2, 'B1']
#None		[2, 'C1']
#None		[2, 'D1']
#None		[2, 'E1']
#None		[2, 'F1']
#None		[2, 'G1']
#None		[2, 'H1']
# No volume info available in source well, assuming enough volume...
# Picking up tips
pipettes[3].pick_up_tip()
# Aspirating 184.8ul from slot 1 well D3
pipettes[3].aspirate(184.8,labwares[1].wells('D3'))
# No volume info available in target well, assuming enough room for dispensing...
# Dispensing 184.8ul to slot 2 well ('A1')
pipettes[3].dispense(184.8, labwares[2].wells('A1'))
# Drop tips
pipettes[3].drop_tip()
# No volume info available in source well, assuming enough volume...
# Picking up tips
pipettes[3].pick_up_tip()
# Aspirating 184.8ul from slot 1 well D3
pipettes[3].aspirate(184.8,labwares[1].wells('D3'))
# No volume info available in target well, assuming enough room for dispensing...
# Dispensing 184.8ul to slot 2 well ('B1')
pipettes[3].dispense(184.8, labwares[2].wells('B1'))
# Drop tips
pipettes[3].drop_tip()
# No volume info available in source well, assuming enough volume...
# Picking up tips
pipettes[3].pick_up_tip()
# Aspirating 184.8ul from slot 1 well D3
pipettes[3].aspirate(184.8,labwares[1].wells('D3'))
# No volume info available in target well, assuming enough room for dispensing...
# Dispensing 184.8ul to slot 2 well ('C1')
pipettes[3].dispense(184.8, labwares[2].wells('C1'))
# Drop tips
pipettes[3].drop_tip()
# No volume info available in source well, assuming enough volume...
# Picking up tips
pipettes[3].pick_up_tip()
# Aspirating 184.8ul from slot 1 well D3
pipettes[3].aspirate(184.8,labwares[1].wells('D3'))
# No volume info available in target well, assuming enough room for dispensing...
# Dispensing 184.8ul to slot 2 well ('D1')
pipettes[3].dispense(184.8, labwares[2].wells('D1'))
# Drop tips
pipettes[3].drop_tip()
# No volume info available in source well, assuming enough volume...
# Picking up tips
pipettes[3].pick_up_tip()
# Aspirating 184.8ul from slot 1 well D3
pipettes[3].aspirate(184.8,labwares[1].wells('D3'))
# No volume info available in target well, assuming enough room for dispensing...
# Dispensing 184.8ul to slot 2 well ('E1')
pipettes[3].dispense(184.8, labwares[2].wells('E1'))
# Drop tips
pipettes[3].drop_tip()
# No volume info available in source well, assuming enough volume...
# Picking up tips
pipettes[3].pick_up_tip()
# Aspirating 184.8ul from slot 1 well D3
pipettes[3].aspirate(184.8,labwares[1].wells('D3'))
# No volume info available in target well, assuming enough room for dispensing...
# Dispensing 184.8ul to slot 2 well ('F1')
pipettes[3].dispense(184.8, labwares[2].wells('F1'))
# Drop tips
pipettes[3].drop_tip()
# No volume info available in source well, assuming enough volume...
# Picking up tips
pipettes[3].pick_up_tip()
# Aspirating 184.8ul from slot 1 well D3
pipettes[3].aspirate(184.8,labwares[1].wells('D3'))
# No volume info available in target well, assuming enough room for dispensing...
# Dispensing 184.8ul to slot 2 well ('G1')
pipettes[3].dispense(184.8, labwares[2].wells('G1'))
# Drop tips
pipettes[3].drop_tip()
# No volume info available in source well, assuming enough volume...
# Picking up tips
pipettes[3].pick_up_tip()
# Aspirating 184.8ul from slot 1 well D3
pipettes[3].aspirate(184.8,labwares[1].wells('D3'))
# No volume info available in target well, assuming enough room for dispensing...
# Dispensing 184.8ul to slot 2 well ('H1')
pipettes[3].dispense(184.8, labwares[2].wells('H1'))
# Drop tips
pipettes[3].drop_tip()
