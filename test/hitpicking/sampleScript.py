# This script is generated by ezProtocol writer.
# Author: Sichong Peng 
# Contact: scpeng@ucdavis.edu
# import libraries
from opentrons import labware, instruments, robot
#Initiate labwares
labwares={}
labwares[1] = labware.load('96-PCR-flat', 1)
labwares[2] = labware.load('96-PCR-flat', 2)
#Initiate tipracks and pipettes
tipracks={}
pipettes={}
tipracks[1] = labware.load('tiprack-10ul', 8)
pipettes[1] = instruments.P10_Single(mount='left',tip_racks=[tipracks[1]])
tipracks[3] = labware.load('opentrons-tiprack-300ul', 7)
pipettes[3] = instruments.P300_Single(mount='right',tip_racks=[tipracks[3]])
#transfer 3.0ul from:
 #source(s)	To	target(s)
#[1, 'C3']		[2, 'C3']
#[1, 'C4']		[2, 'C4']
#[1, 'B3']		[2, 'B3']
#[1, 'B4']		[2, 'B4']
#[1, 'B5']		[2, 'B5']
#[1, 'B6']		[2, 'B6']
#[1, 'B7']		[2, 'B7']
#[1, 'B8']		[2, 'B8']
#[1, 'B9']		[2, 'B9']
#[1, 'B10']		[2, 'B10']
#[1, 'B11']		[2, 'B11']
#[1, 'B12']		[2, 'B12']
#[1, 'C1']		[2, 'C1']
#[1, 'C2']		[2, 'C2']
#[1, 'D2']		[2, 'D2']
#[1, 'A2']		[2, 'A2']
#[1, 'A1']		[2, 'A1']
#[1, 'A3']		[2, 'A3']
#[1, 'A4']		[2, 'A4']
#[1, 'A5']		[2, 'A5']
#[1, 'A6']		[2, 'A6']
#[1, 'A7']		[2, 'A7']
#[1, 'A8']		[2, 'A8']
#[1, 'A9']		[2, 'A9']
#[1, 'A10']		[2, 'A10']
#[1, 'A11']		[2, 'A11']
#[1, 'A12']		[2, 'A12']
#[1, 'B1']		[2, 'B1']
#[1, 'C5']		[2, 'C5']
#[1, 'C7']		[2, 'C7']
#[1, 'C9']		[2, 'C9']
#[1, 'C11']		[2, 'C11']
#[1, 'B2']		[2, 'B2']
# No volume info available in source well, assuming enough volume...
# Picking up tips
pipettes[1].pick_up_tip()
# Aspirating 3.0ul from slot 1 well C3
pipettes[1].aspirate(3.0,labwares[1].wells('C3'))
# No volume info available in target well, assuming enough room for dispensing...
# Dispensing 3.0ul to slot 2 well ('C3')
pipettes[1].dispense(3.0, labwares[2].wells('C3'))
# Drop tips
pipettes[1].drop_tip()# No volume info available in source well, assuming enough volume...
# Picking up tips
pipettes[1].pick_up_tip()
# Aspirating 3.0ul from slot 1 well C4
pipettes[1].aspirate(3.0,labwares[1].wells('C4'))
# No volume info available in target well, assuming enough room for dispensing...
# Dispensing 3.0ul to slot 2 well ('C4')
pipettes[1].dispense(3.0, labwares[2].wells('C4'))
# Drop tips
pipettes[1].drop_tip()# No volume info available in source well, assuming enough volume...
# Picking up tips
pipettes[1].pick_up_tip()
# Aspirating 3.0ul from slot 1 well B3
pipettes[1].aspirate(3.0,labwares[1].wells('B3'))
# No volume info available in target well, assuming enough room for dispensing...
# Dispensing 3.0ul to slot 2 well ('B3')
pipettes[1].dispense(3.0, labwares[2].wells('B3'))
# Drop tips
pipettes[1].drop_tip()# No volume info available in source well, assuming enough volume...
# Picking up tips
pipettes[1].pick_up_tip()
# Aspirating 3.0ul from slot 1 well B4
pipettes[1].aspirate(3.0,labwares[1].wells('B4'))
# No volume info available in target well, assuming enough room for dispensing...
# Dispensing 3.0ul to slot 2 well ('B4')
pipettes[1].dispense(3.0, labwares[2].wells('B4'))
# Drop tips
pipettes[1].drop_tip()# No volume info available in source well, assuming enough volume...
# Picking up tips
pipettes[1].pick_up_tip()
# Aspirating 3.0ul from slot 1 well B5
pipettes[1].aspirate(3.0,labwares[1].wells('B5'))
# No volume info available in target well, assuming enough room for dispensing...
# Dispensing 3.0ul to slot 2 well ('B5')
pipettes[1].dispense(3.0, labwares[2].wells('B5'))
# Drop tips
pipettes[1].drop_tip()# No volume info available in source well, assuming enough volume...
# Picking up tips
pipettes[1].pick_up_tip()
# Aspirating 3.0ul from slot 1 well B6
pipettes[1].aspirate(3.0,labwares[1].wells('B6'))
# No volume info available in target well, assuming enough room for dispensing...
# Dispensing 3.0ul to slot 2 well ('B6')
pipettes[1].dispense(3.0, labwares[2].wells('B6'))
# Drop tips
pipettes[1].drop_tip()# No volume info available in source well, assuming enough volume...
# Picking up tips
pipettes[1].pick_up_tip()
# Aspirating 3.0ul from slot 1 well B7
pipettes[1].aspirate(3.0,labwares[1].wells('B7'))
# No volume info available in target well, assuming enough room for dispensing...
# Dispensing 3.0ul to slot 2 well ('B7')
pipettes[1].dispense(3.0, labwares[2].wells('B7'))
# Drop tips
pipettes[1].drop_tip()# No volume info available in source well, assuming enough volume...
# Picking up tips
pipettes[1].pick_up_tip()
# Aspirating 3.0ul from slot 1 well B8
pipettes[1].aspirate(3.0,labwares[1].wells('B8'))
# No volume info available in target well, assuming enough room for dispensing...
# Dispensing 3.0ul to slot 2 well ('B8')
pipettes[1].dispense(3.0, labwares[2].wells('B8'))
# Drop tips
pipettes[1].drop_tip()# No volume info available in source well, assuming enough volume...
# Picking up tips
pipettes[1].pick_up_tip()
# Aspirating 3.0ul from slot 1 well B9
pipettes[1].aspirate(3.0,labwares[1].wells('B9'))
# No volume info available in target well, assuming enough room for dispensing...
# Dispensing 3.0ul to slot 2 well ('B9')
pipettes[1].dispense(3.0, labwares[2].wells('B9'))
# Drop tips
pipettes[1].drop_tip()# No volume info available in source well, assuming enough volume...
# Picking up tips
pipettes[1].pick_up_tip()
# Aspirating 3.0ul from slot 1 well B10
pipettes[1].aspirate(3.0,labwares[1].wells('B10'))
# No volume info available in target well, assuming enough room for dispensing...
# Dispensing 3.0ul to slot 2 well ('B10')
pipettes[1].dispense(3.0, labwares[2].wells('B10'))
# Drop tips
pipettes[1].drop_tip()# No volume info available in source well, assuming enough volume...
# Picking up tips
pipettes[1].pick_up_tip()
# Aspirating 3.0ul from slot 1 well B11
pipettes[1].aspirate(3.0,labwares[1].wells('B11'))
# No volume info available in target well, assuming enough room for dispensing...
# Dispensing 3.0ul to slot 2 well ('B11')
pipettes[1].dispense(3.0, labwares[2].wells('B11'))
# Drop tips
pipettes[1].drop_tip()# No volume info available in source well, assuming enough volume...
# Picking up tips
pipettes[1].pick_up_tip()
# Aspirating 3.0ul from slot 1 well B12
pipettes[1].aspirate(3.0,labwares[1].wells('B12'))
# No volume info available in target well, assuming enough room for dispensing...
# Dispensing 3.0ul to slot 2 well ('B12')
pipettes[1].dispense(3.0, labwares[2].wells('B12'))
# Drop tips
pipettes[1].drop_tip()# No volume info available in source well, assuming enough volume...
# Picking up tips
pipettes[1].pick_up_tip()
# Aspirating 3.0ul from slot 1 well C1
pipettes[1].aspirate(3.0,labwares[1].wells('C1'))
# No volume info available in target well, assuming enough room for dispensing...
# Dispensing 3.0ul to slot 2 well ('C1')
pipettes[1].dispense(3.0, labwares[2].wells('C1'))
# Drop tips
pipettes[1].drop_tip()# No volume info available in source well, assuming enough volume...
# Picking up tips
pipettes[1].pick_up_tip()
# Aspirating 3.0ul from slot 1 well C2
pipettes[1].aspirate(3.0,labwares[1].wells('C2'))
# No volume info available in target well, assuming enough room for dispensing...
# Dispensing 3.0ul to slot 2 well ('C2')
pipettes[1].dispense(3.0, labwares[2].wells('C2'))
# Drop tips
pipettes[1].drop_tip()# No volume info available in source well, assuming enough volume...
# Picking up tips
pipettes[1].pick_up_tip()
# Aspirating 3.0ul from slot 1 well D2
pipettes[1].aspirate(3.0,labwares[1].wells('D2'))
# No volume info available in target well, assuming enough room for dispensing...
# Dispensing 3.0ul to slot 2 well ('D2')
pipettes[1].dispense(3.0, labwares[2].wells('D2'))
# Drop tips
pipettes[1].drop_tip()# No volume info available in source well, assuming enough volume...
# Picking up tips
pipettes[1].pick_up_tip()
# Aspirating 3.0ul from slot 1 well A2
pipettes[1].aspirate(3.0,labwares[1].wells('A2'))
# No volume info available in target well, assuming enough room for dispensing...
# Dispensing 3.0ul to slot 2 well ('A2')
pipettes[1].dispense(3.0, labwares[2].wells('A2'))
# Drop tips
pipettes[1].drop_tip()# No volume info available in source well, assuming enough volume...
# Picking up tips
pipettes[1].pick_up_tip()
# Aspirating 3.0ul from slot 1 well A1
pipettes[1].aspirate(3.0,labwares[1].wells('A1'))
# No volume info available in target well, assuming enough room for dispensing...
# Dispensing 3.0ul to slot 2 well ('A1')
pipettes[1].dispense(3.0, labwares[2].wells('A1'))
# Drop tips
pipettes[1].drop_tip()# No volume info available in source well, assuming enough volume...
# Picking up tips
pipettes[1].pick_up_tip()
# Aspirating 3.0ul from slot 1 well A3
pipettes[1].aspirate(3.0,labwares[1].wells('A3'))
# No volume info available in target well, assuming enough room for dispensing...
# Dispensing 3.0ul to slot 2 well ('A3')
pipettes[1].dispense(3.0, labwares[2].wells('A3'))
# Drop tips
pipettes[1].drop_tip()# No volume info available in source well, assuming enough volume...
# Picking up tips
pipettes[1].pick_up_tip()
# Aspirating 3.0ul from slot 1 well A4
pipettes[1].aspirate(3.0,labwares[1].wells('A4'))
# No volume info available in target well, assuming enough room for dispensing...
# Dispensing 3.0ul to slot 2 well ('A4')
pipettes[1].dispense(3.0, labwares[2].wells('A4'))
# Drop tips
pipettes[1].drop_tip()# No volume info available in source well, assuming enough volume...
# Picking up tips
pipettes[1].pick_up_tip()
# Aspirating 3.0ul from slot 1 well A5
pipettes[1].aspirate(3.0,labwares[1].wells('A5'))
# No volume info available in target well, assuming enough room for dispensing...
# Dispensing 3.0ul to slot 2 well ('A5')
pipettes[1].dispense(3.0, labwares[2].wells('A5'))
# Drop tips
pipettes[1].drop_tip()# No volume info available in source well, assuming enough volume...
# Picking up tips
pipettes[1].pick_up_tip()
# Aspirating 3.0ul from slot 1 well A6
pipettes[1].aspirate(3.0,labwares[1].wells('A6'))
# No volume info available in target well, assuming enough room for dispensing...
# Dispensing 3.0ul to slot 2 well ('A6')
pipettes[1].dispense(3.0, labwares[2].wells('A6'))
# Drop tips
pipettes[1].drop_tip()# No volume info available in source well, assuming enough volume...
# Picking up tips
pipettes[1].pick_up_tip()
# Aspirating 3.0ul from slot 1 well A7
pipettes[1].aspirate(3.0,labwares[1].wells('A7'))
# No volume info available in target well, assuming enough room for dispensing...
# Dispensing 3.0ul to slot 2 well ('A7')
pipettes[1].dispense(3.0, labwares[2].wells('A7'))
# Drop tips
pipettes[1].drop_tip()# No volume info available in source well, assuming enough volume...
# Picking up tips
pipettes[1].pick_up_tip()
# Aspirating 3.0ul from slot 1 well A8
pipettes[1].aspirate(3.0,labwares[1].wells('A8'))
# No volume info available in target well, assuming enough room for dispensing...
# Dispensing 3.0ul to slot 2 well ('A8')
pipettes[1].dispense(3.0, labwares[2].wells('A8'))
# Drop tips
pipettes[1].drop_tip()# No volume info available in source well, assuming enough volume...
# Picking up tips
pipettes[1].pick_up_tip()
# Aspirating 3.0ul from slot 1 well A9
pipettes[1].aspirate(3.0,labwares[1].wells('A9'))
# No volume info available in target well, assuming enough room for dispensing...
# Dispensing 3.0ul to slot 2 well ('A9')
pipettes[1].dispense(3.0, labwares[2].wells('A9'))
# Drop tips
pipettes[1].drop_tip()# No volume info available in source well, assuming enough volume...
# Picking up tips
pipettes[1].pick_up_tip()
# Aspirating 3.0ul from slot 1 well A10
pipettes[1].aspirate(3.0,labwares[1].wells('A10'))
# No volume info available in target well, assuming enough room for dispensing...
# Dispensing 3.0ul to slot 2 well ('A10')
pipettes[1].dispense(3.0, labwares[2].wells('A10'))
# Drop tips
pipettes[1].drop_tip()# No volume info available in source well, assuming enough volume...
# Picking up tips
pipettes[1].pick_up_tip()
# Aspirating 3.0ul from slot 1 well A11
pipettes[1].aspirate(3.0,labwares[1].wells('A11'))
# No volume info available in target well, assuming enough room for dispensing...
# Dispensing 3.0ul to slot 2 well ('A11')
pipettes[1].dispense(3.0, labwares[2].wells('A11'))
# Drop tips
pipettes[1].drop_tip()# No volume info available in source well, assuming enough volume...
# Picking up tips
pipettes[1].pick_up_tip()
# Aspirating 3.0ul from slot 1 well A12
pipettes[1].aspirate(3.0,labwares[1].wells('A12'))
# No volume info available in target well, assuming enough room for dispensing...
# Dispensing 3.0ul to slot 2 well ('A12')
pipettes[1].dispense(3.0, labwares[2].wells('A12'))
# Drop tips
pipettes[1].drop_tip()# No volume info available in source well, assuming enough volume...
# Picking up tips
pipettes[1].pick_up_tip()
# Aspirating 3.0ul from slot 1 well B1
pipettes[1].aspirate(3.0,labwares[1].wells('B1'))
# No volume info available in target well, assuming enough room for dispensing...
# Dispensing 3.0ul to slot 2 well ('B1')
pipettes[1].dispense(3.0, labwares[2].wells('B1'))
# Drop tips
pipettes[1].drop_tip()# No volume info available in source well, assuming enough volume...
# Picking up tips
pipettes[1].pick_up_tip()
# Aspirating 3.0ul from slot 1 well C5
pipettes[1].aspirate(3.0,labwares[1].wells('C5'))
# No volume info available in target well, assuming enough room for dispensing...
# Dispensing 3.0ul to slot 2 well ('C5')
pipettes[1].dispense(3.0, labwares[2].wells('C5'))
# Drop tips
pipettes[1].drop_tip()# No volume info available in source well, assuming enough volume...
# Picking up tips
pipettes[1].pick_up_tip()
# Aspirating 3.0ul from slot 1 well C7
pipettes[1].aspirate(3.0,labwares[1].wells('C7'))
# No volume info available in target well, assuming enough room for dispensing...
# Dispensing 3.0ul to slot 2 well ('C7')
pipettes[1].dispense(3.0, labwares[2].wells('C7'))
# Drop tips
pipettes[1].drop_tip()# No volume info available in source well, assuming enough volume...
# Picking up tips
pipettes[1].pick_up_tip()
# Aspirating 3.0ul from slot 1 well C9
pipettes[1].aspirate(3.0,labwares[1].wells('C9'))
# No volume info available in target well, assuming enough room for dispensing...
# Dispensing 3.0ul to slot 2 well ('C9')
pipettes[1].dispense(3.0, labwares[2].wells('C9'))
# Drop tips
pipettes[1].drop_tip()# No volume info available in source well, assuming enough volume...
# Picking up tips
pipettes[1].pick_up_tip()
# Aspirating 3.0ul from slot 1 well C11
pipettes[1].aspirate(3.0,labwares[1].wells('C11'))
# No volume info available in target well, assuming enough room for dispensing...
# Dispensing 3.0ul to slot 2 well ('C11')
pipettes[1].dispense(3.0, labwares[2].wells('C11'))
# Drop tips
pipettes[1].drop_tip()# No volume info available in source well, assuming enough volume...
# Picking up tips
pipettes[1].pick_up_tip()
# Aspirating 3.0ul from slot 1 well B2
pipettes[1].aspirate(3.0,labwares[1].wells('B2'))
# No volume info available in target well, assuming enough room for dispensing...
# Dispensing 3.0ul to slot 2 well ('B2')
pipettes[1].dispense(3.0, labwares[2].wells('B2'))
# Drop tips
pipettes[1].drop_tip()