## Testcase 1: Changing font size.
### Scenario:
* Open empty document
* Enter some text
* Go to Format->Font menu
* Change font size

### Expected result:
* Entered text's font size changed

## Testcase 2: Hiding status bar.
### Scenario:
* Open empty document in Notepad
* Ensure that there's no status bar at the bottom of the window
* Choose View->Status bar menu point

### Expected result:
* Status bar appeared at the bottom of the window

## Testcase 3: Text remplacement functionality
### Scenario:
* Open an empty Notepad document
* Enter text "aa aaa aaaa aaaaaa" to main window
* Choose Edit->Replace menu point
* Enter "aa" in 'Find what:' edit box
* Enter "QQ" in 'Replace with:' edit box
* Click 'Replace All' button

### Expected result:
* Text "QQ QQa QQQQ QQQQQQ" displayed in the main window

## Testcase 4: Inserting current time and date
### Scenario:
* Open an empty Notepad document
* Press F5 (or choose "Edit"->"Time/Date" menu point)

### Excepted result:
* Current system time in "H?H:MM [AM|PM] M?M/D?D/YYYY" format inserted to the main window

## Testcase 5: Confirm exiting
### Scenario:
* Open an empty Notepad document
* Enter some text to main notepad window
* Press alt+F4 (or try to close Notepad window)

### Excepted result:
* Exit confirmation popup window appeared with text "Do you want to save changes to Untitled?"
