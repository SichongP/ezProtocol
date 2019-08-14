# How to write a EZProtocol to use with opentrons robot
This is a brief introduction on how to write a ezProtocol

## Basics

Any protocol that can be handled by an opentron robot (or any liquid handler, if equipped with right weapons) should be able to be broken down into the below simple format:
 ```
 Volume * Reagent [+ Volume * Reagent]* = Product
 ```
 (All white spaces are for easy visualization and ignored by the program.)
 We start with a simple example:
 To mix 3ul of DNA with 17ul of water (a.k.a a dilution!), we can write a protocol like this:
 ```
 3 * DNA + 17 * Water = DilutedDNA
 ``` 
 Then if we can tell the robot where to find each reagent (DNA and Water) and where to put diluted DNA (also a reagent!), the robot can easily interpret this protocol into a language it can understand (a python script if we are using opentrons robot)
 Here is how we tell it:
 
|Reagent|Name|Slot|WellID|LabwareType|volume|
|---|---|---|---|---|---|
|DNA|Sample1|1|A1|96-PCR-flat||
|DNA|Sample2|1|A2|96-PCR-flat||
|Water|Water|2|A1|tube-rack-2ml||
|DilutedDNA|Sample1|3|A1|96-PCR-flat||
|DilutedDNA|Sample2|3|A2|96-PCR-flat||

1. Note in the above example, the `Reagent` column strictly corresponds to the protocol above. All `Reagent` listed in the protocol must be also present in this table otherwise the program will complain! (This is intended as a safety measure. I will remove it if there is a compelling reason to do so)
2. The second column, `Name` is an identifier for different samples within a same reagent. In this case, we have two DNA samples that obviously need to be diluted separately. When interpreting the protocol, the program will automatically expand it as below:
```
3 * Sample1_DNA + 17 * Water = Sample1_DilutedDNA
3 * Sample2_DNA + 17 * Water = Sample2_DilutedDNA
```
3. The third column, `Slot`, tells the program which slot on an opentron robot deck to find the sample. 

  Below is layout of opentrons robot deck:
  ![here](https://docs.opentrons.com/_images/DeckMapEmpty.png "opntrons OT2 layout") (img credit: opentrons)

4. The fourth column, `WellID`, tells the program which well on the labware to find the reagent. 
 > You're expected to ensure you don't reference non-existing wells on a labware (say 'F2' on a tuberack-2ml which has only 'A1'-'D6'). There is currently no safety check for this error.
5. The fifth column, `LabwareType`, indicates which labware (i.e 96-well plate, 2ml tube rack, etc.) is used at this slot to hold reagents.
> The name for each labware is expected to match what is used by opentrons. For a list of built in labware types, see [here](https://docs.opentrons.com/labware.html#opentrons-labware). You can also use custome labware ([see here on how to](https://docs.opentrons.com/labware.html#create))
6. The sixth column, `volume`, tells the program how much solution is present in each well. This is optional but do note that even if none of wells has `volume` filled in, this coulmn must still exist. 

## Wildcard

The philosophy of EzProtocol is to isolate generalized protocols from plates that may vary everyday. Wildcard makes this possible by allowing specifying a variable amount of liquid to transfer depending on how many samples are being run at the time.

Here is an example:

```
1.8 * (DNA) * Buffer10X + 16.2 * (DNA) * Water = Buffer1X
3 * DNA + 17 * Buffer = Product
``` 
This protocol tells the program that for each `DNA` sample, we want to dilute 1.8ul `Buffer10X` with 16.2ul `Water`. And then we want to mix 3ul `DNA` sample with 17ul diluted `Buffer1X` 
If we tell it that we have 10 `DNA` samples today, it will be automatically expanded to this:  
```
18 * Buffer10X + 162 * Water = Buffer1X
3 * DNA + 17 * Buffer = Product
```
Reagent name enclosed in a pair of parentheses (`()`) will be replaced with the number of samples corresponding to that reagent.

## Header
The header in a protocol file follows [yaml](https://yaml.org/) specifications (Don't worry about its specs. Currently only two parameters are recognized and you will learn about them in a sec).  
Header is separated from the main body by a pair of three dashes (`---`). Below is an example of a protocol file with header:

```
---
pipette: P10_single:left, P300_single:right
tiprack: 
- slot: 6
  type: tiprack-10ul
- slot: 7
  type: opentrons-tiprack-300ul
---
1.8 * (DNA) * Buffer10X + 16.2 * (DNA) * Water = Buffer1X
3 * DNA + 17 * Buffer = Product
```

The header is used to provide some overall config information along with the protocol. Currently there are two configs you must specify in the header:
1. pipette.  
   You must specify pipettes mounted on the robot and their positions (left or right)
   The name of pipette should be recognizable by opentrons, namely one of the following:  
   > P10_Single (1 - 10 ul)   
   > P10_Multi (1 - 10ul)   
   > P50_Single (5 - 50ul)   
   > P50_Multi (5 - 50ul)   
   > P300_Single (30 - 300ul)   
   > P300_Mutli (30 - 300ul)   
   > P1000_Single (100 - 1000ul)  
   A colon (`:`) follows the pipette name and is followed by either `left` or `right`.  
   > Currently there is no safety check on pipette mounting. If you put 'top' after `:` the program will still generate an opentrons script but you will run into error when running the script  
2. tipracks.  
   You must provide tipracks corresponding to the pipettes. Multiple tipracks can be provided (but only one will be attached to each pipette).  
   tiprack specs follows the below format:  
   ```
   - slot: specifies which slot on the deck tiprack is located. Should be a number 1 to 9  
     type: specifies which type of tiprack is provided. For a list of built in tipracks, see [here](https://docs.opentrons.com/labware.html#tipracks)  
   ```

   
## Detail instructions

Sometimes when pipetting some types of liquid we may wish to pipette slower, pause a second, create air gaps, mix, or touch tips on the wall. This can be achieved by providing optional arguments. See below for an example:
```
1.8 * (DNA) * Buffer10X | pause_after_aspirate:1, pause_after_dispense:1 + 16.2 * (DNA) * Water = Buffer1X
3 * DNA + 17 * Buffer = Product
```
The `pause_after_aspirate:1` and `pause_after_dispense:1` after reagent `Buffer10X` tells the program that we want the pipette to stay in position for 1 **second** after aspirating and dispensing Buffer10X because this buffer is too viscous and we wish to give it a little time for the buffer to move.  
Detail instructions are always provided after a pipe (`|`) following reagent name. Combined with wildcard, they make EZProtocol powerful and versatile. Below is a list of arguments currently supported (provided are default values):

- touch_tips:False
- air_gap:False
- blow_out:False
- mix_before_aspirate:0 (times to mix)
- mix_before_rate: 1 (fold change, 2 means aspirating and dispensing twice as fast when mixing)
- mix_after_dispense:0 (times to mix)
- mix_after_rate: 1 (fold change, 2 means aspirating and dispensing twice as fast when mixing)
- mix_volume: 0 (volume used in mixing, if 0, will use half of dispense/aspirate volume)
- aspirate_speed:0 (ul/s, 0 means using default speed)
- dispense_speed:0 (ul/s, 0 means using default speed)
- pause_after_aspirate:0 (seconds to pause)
- pause_after_dispense:0 (seconds to pause)

There you have it! That's all you need to know to write a complex, versatile protocol. Check out [sample protocol](https://github.com/SichongP/ezProtocol/blob/master/test/testProtocol.txt) and [sample plate input file](https://github.com/SichongP/ezProtocol/blob/master/test/TestInputPlate.csv) for some examples!
