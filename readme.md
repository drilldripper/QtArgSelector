QtArgumentSelector
===

QtArgumentSelector is a simple GUI arguments selector for Python. 

This Program can work in Windows/Linux/MacOS.


## Demo
Let's launch a Program.

![StartView](readme_resource/StartView.png)

Click `Open Direcory` Button.

![OpenDirectory](readme_resource/OpenDirectory.png)

You can see files in selected directory.

![AllFiles](readme_resource/AllFiles.png)

When you select `Extension`, files can be filtered by file extension.

![FilteredFiles](readme_resource/FilteredFiles.png)

Select cells and click `Select Items`. This Program is closed and your scripts will start.At that time, selected data has been added to the `sys.argv`

![SelectedFiles](readme_resource/SelectedFiles.png)

### Note
Output Arguments follow the cell selection order.

For exsample, If you select "Cocoa.png" followed by "Chino.png", `sys.argv` are below.

	['/Users/drilldripper/Repositories/QtArgumentSelector/test.py', 'Cocoa.png', 'Chino.png']



## Installation
	$git clone https://github.com/drilldripper/QtArgumentSelector.git
	
	
or copy `argument_selector.py` to your project.



## Usage
Add this script to leading of the file.

```python
from argument_selector import ArgumentSelector
from PyQt5.QtWidgets import (QApplication)
import sys

# Launch PyQt Application
app = QApplication(sys.argv)
# Instantiate GUI
ex = ArgumentSelector()
app.exec_()

```

GUI will launch.

I recommend to check the _sys.argv_.

```python
# Check Arguments
print(sys.argv)

```


## Requirement
- Python 3
- PyQt 5


## Licence
MIT License

## Author
[drilldripper](https://github.com/drilldripper)
