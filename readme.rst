MockGui
=======

This "library" is intended to facilitate my way of testing the GUI parts of my programs.
I use ``pytest`` with heavy monkeypatching, and these modules contain mocks of various widget classes from the GUI libraries. 
Since I try to move most of the behaviour away from the presentation logic - or the other way aound - the mock objects mostly contain print statements to enable verification of how and if the classes and their methods are called, and if needed standard return values for further processing.


How to use
----------

For the moment I try not to bother with the official way to install packages, as long as it works.
Therefore I just created a symlink to this project directory in *~/.local/lib/pythonx.y/site-packages* so that I can do ``from mockgui import mockqtwidgets as mockqtw`` in the test module.
