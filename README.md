# EzCombo.py

<p align="center">
  <img width="171‬" height="102" src="https://i.imgur.com/c71GUHG.png">
</p>

A Very Easy way to Load and Choose Combos from a ComboList.

Example:

Lets pretend Comblist.txt contains these lines: 

 example1:Pass1
 
 example2:Pass2
 
 example3:Pass3
 

```python
from lib import EZCombo
ComboIterator = 0
EZCombo.LoadCombos('ComboList.txt')
EZCombo.PullCombo(ComboIterator)
print(EZCombo.Username +':'+EZCombo.Password)
>>>example1:Pass1
```
Remember that lists in python start at 0 and go up!


Quick Usage:

Step 1) Put this file in the same folder as your project, or load it as a package

Step 2) Call the function you want ex: LoadCombos(ComboPath) 

Step 3) Call PullCombo(ComboIterator) to retreive a new Combo. Iterate ComboIterator in your other functions ex: ComboIterator += 1

Thats all.

To Load a Library:

Step 1) Create a folder named "Lib" in your projects directory.

Step 2) Create a file named __init__.py inside of the Lib Folder

Step 3) Put EzCombo.py inside of the Lib folder.

Step 4) import to your python script using from lib import EzCombo

Expanded Documentation:

LoadCombos(ComboPath) < Used to Load your Combolist. Must be called before any other function. ComboPath is the path to your combolist. ex: LoadCombos('Combo.txt')

PullCombo(ComboIterator) < Used to Pull a Combo from your list. Default Starts at 0. returns a Username and Password Variable. 

RemoveCombo(Combo) < Used to Remove a Combo from your ComboList. (Doesnt effect your Combo txt file. It effects the Libs internal list.) Combo must be in format Username:Password

GoodCombo(capture , data) < Used to save data from checker. capture is the capture name you want. data is the captured or scraped data. ex: example1:pass1 | Total Bits: 0

SaveValids(SaveName) < Used to save your good Combos in a txt file. Change SaveName to whatever you want your list to be saved as. Must use GoodCombo(capture, data) from above first to fill its list.

BadCombo() < Returns the current User:Pass as a bad combo. Adds it to the Fail List.

SaveFails(SaveName) < Saves the failed combos from checking. Set savename to what you want the filename to be. ex SaveFails('Fails.txt')
