"""redefine PyQt widgets to make testing easier (or possible at all)
"""
import types

class MockCursor:
    def __init__(self, arg):
        print(f'called Cursor with arg {arg}')


class MockControl:
    def setVisible(self, value):
        print(f'called control.setVisible with args `{type(self)}`, `{value}`')


class MockSignal:
    def __init__(self, *args):
        print('called Signal.__init__')
    def connect(self, *args):
        print('called Signal.connect with args', args)


class MockAction:
    triggered = MockSignal()
    def __init__(self, text, func):
        print(f'called Action.__init__ with text `{text}`')
        self.label = text
        self.callback = func
        self.shortcuts = []
        self.checkable = self.checked = False
        self.statustip = ''
    def setCheckable(self, state):
        self.checkable = state
    def setChecked(self, state):
        self.checked = state
    def setShortcut(self, data):
        print(f'called Action.setShortcut with arg `{data}`')
    def setShortcuts(self, data):
        print(f'called Action.setShortcuts with arg `{data}`')
        self.shortcuts = data
    def setStatusTip(self, data):
        self.statustip = data


class MockApplication:
    def __init__(self, *args):
        print('called Application.__init__')
    def exec_(self):
        print('called Application.exec_')
    def setOverrideCursor(self, arg):
        print(f'called Application.setOverrideCursor with arg of type {type(arg)}')
    def restoreOverrideCursor(self):
        print('called Application.restoreOverrideCursor')


class MockWidget:
    def __init__(self, *args):
        print('called Widget.__init__')
    def show(self):
        print('called Widget.show')
    def setWindowTitle(self, *args):
        print('called Widget.setWindowTitle with args `{}`'.format(args))
    def setWindowIcon(self, *args):
        print('called Widget.setWindowIcon')
    def resize(self, *args):
        print('called Widget.resize with args `{}`'.format(args))


class MockScrollBar:
    def __init__(self, *args):
        print('called Scrollbar.__init__')
    def maximum(self):
        print('called Scrollbar.maximum')
        return 99
    def setMaximum(self, value):
        print(f'called Scrollbar.setMaximum with value `{value}`')
    def setValue(self, value):
        print(f'called Scrollbar.setValue with value `{value}`')


class MockScrollArea:
    def setWidget(self, arg):
        print(f'called ScrollArea.setWidget with arg of type `{type(arg)}`')
    def setWidgetResizable(self, arg):
        print(f'called ScrollArea.setWidgetResizable with arg `{arg}`')


class MockScrolledWidget:
    def __init__(self, *args):
        print('called ScrolledWidget.__init__')
    def verticalScrollBar(self):
        print('called ScrolledWidget.verticalScrollBar')
        return MockScrollBar()


class MockSize:
    def __init__(self, *args):
        print('called Size.__init__ with args', args)


class MockMainWindow(MockWidget):    # albumsgui: niet overerfd
    def __init__(self, *args):
        print('called MainWindow.__init__')
        self.app = MockApplication()
    def move(self, *args):
        print('called MainWindow.move with args', args)
    def resize(self, *args):
        print('called MainWindow.resize with args', args)
    def show(self):
        print('called MainWindow.show')
    def setWindowTitle(self, text):
        print(f'called MainWindow.setWindowTitle to `{text}`')
    def setCentralWidget(self, arg):
        print(f'called MainWidget.setCentralWindow with arg of type `{type(arg)}`')
    def addAction(self, arg):
        print('called MainWindow.addAction')


class MockFrame:
    HLine = '---'
    def __init__(self, parent=None):
        print('called Frame.__init__')
    def setFrameShape(self, arg):
        print(f'called Frame.setFrameShape with arg `{arg}`')
    def setLayout(self, arg):
        print(f'called Frame.setLayout with arg of type `{type(arg)}`')


class MockPixmap:
    def __init__(self, *args):
        print('called Pixmap.__init__')
    def load(self, fname):
        print(f'called Pixmap.load for `fname`')
        return 'ok'
    def scaled(self, x, y):
        print(f'called Pixmap.scaled to `{x}`, `{y}`')
        return 'ok'


class MockIcon:
    def __init__(self, *args):
        print(f'called Icon.__init__ with arg `{args[0]}`')
    def fromTheme(self, *args):
        print('called Icon.fromTheme with args', args)


class MockMenuBar:
    def __init__(self):
        self.menus = []
    def clear(self):
        self.menus = []
    def addMenu(self, text):
        newmenu = MockMenu(text)
        self.menus.append(newmenu)
        return newmenu


class MockMenu:
    def __init__(self, text):
        self.menutext = text
        self.actions = []
    def addAction(self, text, func):
        newaction = MockAction(text, func)
        self.actions.append(newaction)
        return newaction
    def addSeparator(self):
        newaction = MockAction('-----', None)
        self.actions.append(newaction)
        return newaction


class MockSplitter:
    def __init__(self, *args):
        print('called Splitter.__init__')
    def addWidget(self, *args):
        print('called Splitter.addWidget with arg `{}`'.format(args[0]))
    def setSizes(self, *args):
        print('called Splitter.setSizes with args `{}`'.format(args))
    def sizes(self, *args):
        return 'left this wide', 'right that wide'


class MockTabWidget:
    def mock_connect(*args):
        print('called connect with args', args)
    currentChanged = types.SimpleNamespace(connect=mock_connect)
    def __init__(self, *args):
        print('called QTabWidget.__init__')
        self._current = -1
    def setCurrentIndex(self, num):
        print(f'called QTabWidget.setCurrentIndex with arg `{num}`')
        self._current = num
    def currentIndex(self):
        print('called QTabWidget.currentIndex')
        return self._current
    def currentWidget(self):
        print('called QTabWidget.currentWidget')
        return None
    def addTab(self, *args):
        print('called QTabWidget.addTab with args', args)


class MockHeader:
    Stretch = 'stretch'
    def __init__(self, *args):
        print('called Header.__init__')
    def setStretchLastSection(self, value):
        print(f'called Header.setStretchLastSection with arg {value}')
    def setSectionResizeMode(self, col, mode):
        print(f'called Header.setSectionResixeMode for col {col} mode {mode}')


class MockTreeWidget:
    SingleSelection = 1
    itemSelectionChanged = MockSignal()
    itemEntered = MockSignal()
    itemDoubleClicked = MockSignal()
    currentItemChanged = MockSignal()
    def __init__(self, *args):
        print('called Tree.__init__')
    def setColumnCount(self, num):
        print(f'called Tree.setColumnCount with arg `{num}`')
    def setColumnWidth(self, col, width):
        print(f'called Tree.setColumnWidth with args {col}, {width}')
    def hideColumn(self, *args):
        print('called Tree.hideColumn')
    def header(self):
        print('called Tree.header')
        return MockHeader()
    def setHeaderLabels(self, label_list):
        print(f'called Tree.setHeaderLabels with arg `{label_list}`')
    def headerItem(self):
        return MockTreeItem()
    def setSelectionMode(self, *args):
        print('called Tree.setSelectionMode')
    def setMouseTracking(self, value):
        print(f'called Tree.setMouseTracking with arg `{value}`')
    def setFocus(self, *args):
        print('called Tree.setFocus')
    def addTopLevelItem(self, arg):
        print('called Tree.addTopLevelItem')  # with arg of type `{type(arg)}`')   spreekt vanzelf
    def topLevelItem(self, arg):
        print(f'called Tree.topLevelItem with arg `{arg}`')
        return f'Tree.topLevelItem'
    def takeTopLevelItem(self, arg):
        print(f'called Tree.takeTopLevelItem with arg `{arg}`')
        return f'Tree.TopLevelItem'
    def topLevelItemCount(self):
        print('called Tree.topLevelItemCount')
        return 0
    def scrollToItem(self, arg):
        print(f'called Tree.scrollToItem with arg `{arg}`')
    def setCurrentIndex(self, arg):
        print(f'called Tree.setCurrentIndex with arg `{arg}`')
    def setCurrentItem(self, arg):
        print(f'called Tree.setCurrentItem with arg `{arg}`')
    def currentItem(self):
        return 'called Tree.currentItem'
    def currentIndex(self):
        print('called Tree.currentIndex')
        # return 1
        return types.SimpleNamespace(row=lambda *x: 1, column=lambda *x: 0)
    def selectedItems(self):
        print('called Tree.selectedItems')
    def findItems(self, *args):
        print('called Tree.findItems with args', args)
        return []
    def indexFromItem(self, item):
        print('called Tree.indexFromItem with arg `{item}`')
        return types.SimpleNamespace(row=lambda: 1, column=lambda: 0)
    def itemBelow(self, arg):
        print(f'called Tree.itemBelow with arg {arg}')
        return 'x'
    def count(self):
        print('called Tree.count')
        return 0
    def clear(self):
        print('called Tree.clear')


class MockTreeItem:
    def __init__(self, *args):   # text='', data=''):
        print('called TreeWidgetItem.__init__ with args', args)
        self._text = []
        self._data = []
        if args:
            self._text = list(args)
        else:
            self._text = []
        self.subitems = []
    def setText(self, col, text):
        print(f'called TreeItem.setText with arg `{text}` for col {col}')
        if len(self._text) < col + 1:
            self._text.append(text)
        else:
            self._text[col] = text
    def text(self, col):
        print(f'called TreeItem.text for col {col}')
        return self._text[col]
    def setData(self, col, role, data):
        print(f'called TreeItem.setData to `{data}` with role {role} for col {col}')
        if len(self._data) < col + 1:
            self._data.append(data)
        else:
            self._data[col] = data
    def data(self, col, role):
        print(f'called TreeItem.data for col {col} role {role}')
        return self._data[col]
    def addChild(self, item):
        print('called TreeItem.addChild')
        self.subitems.append(item)
    def insertChild(self, index, item):
        print('called TreeItem.insertChild')
        self.subitems.insert(index, item)
    def childCount(self):
        return len(self.subitems)
    def child(self, num):
        return self.subitems[num]
    def indexOfChild(self, item):
        return self.subitems.index(item)
    def removeChild(self, item):
        print('called TreeItem.removeChild')
    def setHidden(self, value):
        print(f"called TreeItem.setHidden with arg `{value}`")
    def setExpanded(self, value):
        print(f"called TreeItem.setExpanded with arg `{value}`")
    def font(self, *args):
        return MockFont()
    def setFont(self, *args):
        print('called TreeItem.setFont')


class MockFont:
    def __init__(self):
        print('called Font.__init__')
    def setBold(self, value):
        print(f'called Font.setBold with arg `{value}`')
    def setFamily(self, *args):
        print('called Editor.setFamily')
    def setFixedPitch(self, *args):
        print('called Editor.setFixedPitch')
    def setPointSize(self, *args):
        print('called Editor.setPointSize')


class MockEditorWidget:
    "contains elements of TextEdit, RichTextEdit, Scintilla"
    # wordt in albums_gui.py aangeroepen met argumenten tekst en parent
    WrapWord = 1
    SloppyBraceMatch = 2
    PlainFoldStyle = 3
    def __init__(self, *args):
        if args:
            print('called Editor.__init__ with args', args)
            if len(args) == 1:
                self.parent = args[0]
            else:
                self.text, self.parent, *dummy = args
        else:
            print('called Editor.__init__')
        self._text = args[0] if args else ''
    def setMaximumWidth(self, number):
        print(f'called Editor.setMaximumWidth to `{number}`')
    def setMaximumHeight(self, number):
        print(f'called Editor.setMaximumHeight to `{number}`')
    def setMinimumWidth(self, number):
        print(f'called Editor.setMinimumWidth to `{number}`')
    def setMinimumHeight(self, number):
        print(f'called Editor.setMinimumHeight to `{number}`')
    def setWrapMode(self, *args):
        print('called Editor.setWrapMode')
    def setBraceMatching(self, *args):
        print('called Editor.setBraceMatching')
    def setAutoIndent(self, *args):
        print('called Editor.setAutoIndent')
    def setFolding(self, *args):
        print('called Editor.setFolding')
    def setReadOnly(self, value):
        print('called Editor.setReadOnly with value `{}`'.format(value))
    def setFont(self, data):
        print('called Editor.setFont')
    def setMarginsFont(self, data):
        print('called Editor.setMarginsFont')
    def setMarginWidth(self, *args):
        print('called Editor.setMarginWidth')
    def setMarginLineNumbers(self, *args):
        print('called Editor.setMarginLineNumbers')
    def setMarginsBackgroundColor(self, *args):
        print('called Editor.setMarginsBackgroundColor')
    def setCaretLineVisible(self, *args):
        print('called Editor.setCaretLineVisible')
    def setCaretLineBackgroundColor(self, *args):
        print('called Editor.setCaretLineBackgroundColor')
    def setLexer(self, *args):
        print('called Editor.setLexer')
    def clear(self, *args):
        print('called Editor.clear')
    def setEnabled(self, value):
        print(f'called Editor.setEnabled with arg {value}')
    def isModified(self, *args):
        return 'x'
    def setText(self, text):
        print(f'called Editor.setText with arg `{text}`')
    def text(self, *args):
        return 'editor text'
    def toPlainText(self, *args):
        print('called Editor.toPlainText')
        return self._text or 'editor text'
    def setFocus(self, *args):
        print('called Editor.setFocus')


class MockSysTrayIcon:
    def __init__(self, *args):
        print('called TrayIcon.__init__')
        self.activated = MockSignal()
    def showMessage(self, *args):
        print('called TrayIcon.showMessage')
    def setToolTip(self, *args):
        print('called TrayIcon.setToolTip')
    def hide(self):
        print('called TrayIcon.hide')
    def show(self):
        print('called TrayIcon.show')


class MockStatusBar:
    def showMessage(self, text):
        print(f'called StatusBar.showMessage with arg `{text}`')


class MockDialog:
    def __init__(self, parent, *args):
        self.parent = parent
        print('called Dialog.__init()__ with args `{}`'.format(args))
    def exec_(self):
        print('called Dialog.exec_')
        # self.parent.dialog_data = {'x': 'y'}
        # return gui.qtw.QDialog.Accepted
    def setWindowTitle(self, *args):
        print('called Dialog.setWindowTitle with args', args)
    def setLayout(self, *args):
        print('called Dialog.setLayout')
    def accept(self):
        print('called Dialog.accept')
        return gui.qtw.QDialog.Accepted
    def reject(self):
        print('called Dialog.reject')
        return gui.qtw.QDialog.Rejected


class MockInputDialog:
    def __init__(self, *args, **kwargs):
        print('called InputDialog.__init__')
    def getItem(parent, *args, **kwargs):
        print('called InputDialog.getItem with args', args, kwargs)
        return '', False


class MockVBoxLayout:
    def __init__(self, *args):
        print('called VBox.__init__')
        self._count = 0
    def addWidget(self, *args):
        # print('called VBox.addWidget')
        print(f'called VBox.addWidget with arg of type {type(args[0])}')
        self._count += 1
    def addLayout(self, *args):
        # print('called VBox.addLayout')
        print(f'called VBox.addLayout with arg of type {type(args[0])}')
        self._count += 1
    def insertLayout(self, *args):
        print(f'called VBox.insertLayout with arg1 {args[0]} and arg2 of type {type(args[1])}')
        self._count += 1
    def addStretch(self, *args):
        print('called VBox.addStretch')
        self._count += 1
    def addSpacing(self, *args):
        print('called VBox.addSpacing')
        self._count += 1
    def count(self):
        return self._count


class MockHBoxLayout:
    def __init__(self, *args):
        print('called HBox.__init__')
        self._count = 0
    def addWidget(self, *args):
        # print('called HBox.addWidget')
        print(f'called HBox.addWidget with arg of type {type(args[0])}')
        self._count += 1
    def addLayout(self, *args):
        # print('called HBox.addLayout')
        print(f'called HBox.addLayout with arg of type {type(args[0])}')
        self._count += 1
    def addSpacing(self, *args):
        print('called HBox.addSpacing')
        self._count += 1
    def addStretch(self, *args):
        print('called HBox.addStretch')
        self._count += 1
    def insertStretch(self, *args):
        print('called HBox.insertStretch')
        self._count += 1
    def count(self):
        return self._count
    def itemAt(self, num):
        pass


class MockGridLayout:
    def __init__(self, *args):
        print('called Grid.__init__')
    def addWidget(self, *args):
        # print('called Grid.addWidget')
        print(f'called Grid.addWidget with arg of type {type(args[0])} at {args[1:]}')
    def addLayout(self, *args):
        # print('called Grid.addLayout')
        print(f'called Grid.addLayout with arg of type {type(args[0])} at {args[1:]}')
    def addSpacing(self, *args):
        print('called Grid.addSpacing')
    def addStretch(self, *args):
        print('called Grid.addStretch')
    def insertStretch(self, *args):
        print('called Grid.insertStretch')


class MockLabel:
    def __init__(self, *args):
        if args:
            print('called Label.__init__ with args', args)
            self._text = args[0]
        else:
            print('called Label.__init__')
    def setVisible(self, value):
        print(f'called Label.setVisible to `{value}`')
    def setMinimumWidth(self, number):
        print(f'called Label.setMinimumWidth to `{number}`')
    def setMinimumHeight(self, number):
        print(f'called Label.setMinimumHeight to `{number}`')
    def setMaximumWidth(self, number):
        print(f'called Label.setMaximumWidth to `{number}`')
    def setText(self, text):
        print(f'called Label.setText with arg `{text}`')
        self._text = text
    def text(self):
        return self._text
    def setPixmap(self, data):
        print(f'called Label.setPixmap')


class MockCheckBox:
    def __init__(self, *args):
        print('called CheckBox.__init__')
        self.checked = None
        self.textvalue = args[0] if args else ''
    def setEnabled(self, value):
        print(f'called CheckBox.setEnabled with arg {value}')
    def setChecked(self, value):
        print(f'called CheckBox.setChecked with arg {value}')
        self.checked = value
    def isChecked(self):
        print('called CheckBox.isChecked')
        return self.checked
    def text(self):
        return self.textvalue


class MockComboBox:
    currentIndexChanged = MockSignal()
    def __init__(self, *args, **kwargs):
        print('called ComboBox.__init__')
        self._items = kwargs.get('items', [])
        self._index = 1
    def setMaximumWidth(self, number):
        print(f'called ComboBox.setMaximumWidth to `{number}`')
    def setMinimumWidth(self, number):
        print(f'called ComboBox.setMinimumWidth to `{number}`')
    def clear(self):
        print('called ComboBox.clear')
    def clearEditText(self):
        print('called ComboBox.clearEditText')
    def addItem(self, item):
        print(f'called ComboBox.addItems with arg `{item}`')
    def addItems(self, itemlist):
        print(f'called ComboBox.addItems with arg {itemlist}')
    def height(self):
        return 100
    def setEditable(self, value):
        print('called ComboBox.setEditable with arg `{value}`')
        # self.checked = value ??
    def setCurrentIndex(self, value):
        print(f'called ComboBox.setCurrentIndex with arg `{value}`')
        # self.checked = value ??
        self._index = value
    def currentIndex(self):
        print('called ComboBox.currentIndex')
        return self._index
    def setCurrentText(self, text):
        print(f'called ComboBox.setCurrentText with arg `{text}`')
    def currentText(self):
        print('called ComboBox.currentText')
        return 'current text'
    def setToolTip(self, value):
        print(f'called combo.setToolTip({value})')
    def setFocus(self):
        print('called ComboBox.setFocus')
    def count(self):
        print('called ComboBox.count')
        return 0
    def itemText(self, number):
        print(f'called ComboBox.itemText with value `{number}`')


class MockPushButton:
    clicked = MockSignal()
    def __init__(self, *args):
        print('called PushButton.__init__ with args', args)
        self._text = args[0] if args else ''
    def setMaximumWidth(self, number):
        print(f'called PushButton.setMaximumWidth to `{number}`')
        print(f'called PushButton.setText with arg `{value}`')
    def setEnabled(self, value):
        print(f'called PushButton.setEnabled with arg `{value}`')
    def setDefault(self, value):
        print(f'called PushButton.setDefault with arg `{value}`')
    def setIcon(self, value):
        print(f'called PushButton.setIcon with arg `{value}`')
    def setIconSize(self, arg):
        print(f'called PushButton.setIconSize with arg of type {type(arg)}')
        print('called PushButton.__init__')
    def text(self):
        return self._text
    def setText(self, value):
        self._text = value
    def setMenu(self, *args):
        print('called PushButton.setMenu()')
    def setShortcut(self, *args):
        print('called PushButton.setShortcut with args', args)
    def setToolTip(self, value):
        print(f'called PushButton.setToolTip with arg `{value}`')


class MockLineEdit:
    def __init__(self, *args):
        print('called LineEdit.__init__')
        self._text = args[0] if args else '..'
    def setReadOnly(self, value):
        print(f'called LineEdit.setReadOnly with arg `{value}`')
    def setMaximumHeight(self, value):
        print(f'called LineEdit.setMaximumHeight with arg `{value}`')
    def setMinimumHeight(self, value):
        print(f'called LineEdit.setMinimumHeight with arg `{value}`')
    def clear(self):
        print('called LineEdit.clear')
    def setText(self, text):
        print(f'called LineEdit.setText with arg `{text}`')
        self._text = text
    def insert(self, text):
        print(f'called LineEdit.insert with arg `{text}`')
        self._text += text
    def text(self):
        print('called LineEdit.text')
        return self._text
    def setFocus(self):
        print(f'called LineEdit.setFocus')


class MockButtonBox:
    Ok = 1
    Cancel = 2
    accepted = MockSignal()
    rejected = MockSignal()
    def __init__(self, *args):
        print('called ButtonBox.__init__ with args', args)


class MockMessageBox:
    Ok = 1
    Cancel = 2
    Yes = 4
    No = 8
    AcceptRole = 1
    Information = 2
    def __init__(self, *args, **kwargs):
        print('called MessageBox.__init__ with args', args, kwargs)
    def setText(self, text):
        print(f'called MessageBox.setText with arg `{text}`')
    def setInformativeText(self, *args):
        print('called MessageBox.setInformativeText')
    def setStandardButtons(self, *args):
        print('called MessageBox.setStandardButtons')
    def setDefaultButton(self, arg):
        print(f'called MessageBox.setDefaultButton with arg `{arg}`')
    def setEscapeButton(self, arg):
        print(f'called MessageBox.setEscapeButton with arg `{arg}`')
    def addButton(self, *args):
        print(f'called MessageBox.addButton with arg `{args}`')
    def exec_(self, *args):
        print(f'called MessageBox.exec_')
    def clickedButton(self):
        print(f'called QMessageBox.clickedButton')
        return 'button'
    def information(parent, caption, message):
        print(f'called MessageBox.information with args `{caption}` `{message}`')
    def question(parent, caption, message, buttons, default):
        print('called MessageBox.question with args'
              f' `{caption}` `{message}` `{buttons}` `{default}`')
        return No  # 8


class MockListBox:
    itemDoubleClicked = MockSignal()
    def __init__(self, *args):
        print('called List.__init__')
        try:
            self.list = args[0]
        except IndexError:
            self.list = []
    def setVisible(self, value):
        print(f'called List.setVisible to `{value}`')
    def setMinimumWidth(self, number):
        print(f'called List.setMinimumWidth to `{number}`')
    def setMinimumHeight(self, number):
        print(f'called List.setMinimumHeight to `{number}`')
    def __len__(self):
        return len(self.list)
    def clear(self):
        print('called List.clear()')
    def setSelectionMode(self, *args):
        print('called List.setSelectionMode')
    def addItems(self, itemlist):
        print(f'called List.addItems with arg `{itemlist}`')
    def currentItem(self):
        pass
    def setCurrentRow(self, row):
        print(f'called List.setCurrentRow with rownumber {row}')
    def item(self, *args):
        return self.list[args[0]]
    def setFocus(self, value):
        print(f'called List.setFocus with arg `{value}`')
    def selectedItems(self):
        print(f'called List.selectedItems on `{self.list}`')
    def takeItem(self, value):
        print(f'called List.takeItem with arg `{value}` on `{self.list}`')
    def row(self, value):
        print(f'called List.row with arg `{value}` on `{self.list}`')
        return value
    def addItem(self, value):
        print(f'called List.addItem with arg `{value}` on `{self.list}`')
        self.list.append(value)


class MockListItem:
    def __init__(self, *args):
        print('called ListItem.__init__')
        self.name = args[0]
    def text(self):
        return self.name
    def setSelected(self, arg):
        print(f'called ListItem.setSelected with arg `{arg}` for `{self.name}`')


class MockFontMetrics:
    def __init__(self, *args):
        print('called Fontmetrics.__init__()')
    def width(self, *args):
        print('called Editor.width()')


class MockLexerDiff:
    def __init__(self, *args):
        print('called Lexer.__init__()')
    def setDefaultFont(self, *args):
        print('called Editor.setDefaultFont')
