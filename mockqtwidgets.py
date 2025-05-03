"""redefine PyQt widgets to make testing easier (or possible at all)
"""
import contextlib
import types
MAXUNDO = 9


class MockCursor:
    def __init__(self, arg=None):
        if arg:
            print(f'called Cursor.__init__ with arg {arg}')
        else:
            print('called Cursor.__init__')

    def insertImage(self, arg):
        print(f'called Cursor.insertImage with arg {arg}')


class MockBrush:
    def __init__(self, *args):
        self._col = args[0] if args[0] in ('fg', 'bg') else 'brush'
    def color(self):
        return f'{self._col} color'
    def style(self):
        return 'brush style'


class MockColor:
    def __init__(self, arg):
        self._colortext = f"'color {arg}'"

    def __str__(self):
        return self._colortext


# class MockControl:
#     def setVisible(self, value):
#         print(f'called control.setVisible with args `{type(self)}`, `{value}`')
class MockEvent:
    def __init__(self, **kwargs):
        self._key = None
        if 'key' in kwargs:
            self._key = kwargs['key']

    def key(self):
        return self._key

    def x(self):
        return 'x'

    def y(self):
        return 'y'

    def pos(self):
        return ('x', 'y')

    def position(self):
        return MockPointF(1.1, 2.2)

    def button(self):
        return None

    def accept(self):
        print('called event.accept')

    def ignore(self):
        print('called event.ignore')


class MockPointF:
    def __init__(self, *args):
        if len(args) == 2:
            self._x = args[0]
            self._y = args[1]

    def toPoint(self):
        return (int(self._x), int(self._y))


class MockSignal:
    def __init__(self, *args):
        print('called Signal.__init__')

    def connect(self, *args):
        print('called Signal.connect with args', args)

    def disconnect(self):
        print('called Signal.disconnect')


class MockAction:
    triggered = MockSignal()

    def __init__(self, *args):
        self.parent = args[-1] if args else None
        self.label = args[-2] if len(args) > 1 else ''
        self._icon = args[0] if len(args) > 2 else None
        if self._icon:
            args = ('item of type Icon',) + args[1:]
        print('called Action.__init__ with args', args)
        self._shortcuts = []
        self.checkable = self.checked = False
        self.statustip = ''

    def setCheckable(self, state):
        self.checkable = state

    def setDisabled(self, state):
        print(f'called Action.setDisabled with arg `{state}`')

    def setEnabled(self, state):
        print(f'called Action.setEnabled with arg `{state}`')

    def setChecked(self, state):
        print(f'called Action.setChecked with arg `{state}`')
        self.checked = state

    def isChecked(self):
        print('called Action.isChecked')
        return self.checked

    def setText(self, data):
        print(f'called Action.setText with arg `{data}`')
        self.label = data

    def text(self):
        print('called Action.text')
        return self.label

    def setFont(self, data):
        print(f'called Action.setFont')

    def setIcon(self, data):
        print(f'called Action.setIcon with arg `{data}`')
        self._icon = data

    def setShortcut(self, data):
        print(f'called Action.setShortcut with arg `{data}`')
        self._shortcuts = [data]

    def setShortcuts(self, data):
        print(f'called Action.setShortcuts with arg `{data}`')
        self._shortcuts = data

    def shortcuts(self):
        print(f'called Action.shortcuts')
        return self._shortcuts

    def setStatusTip(self, data):
        self.statustip = data

    def setToolTip(self, data):
        print(f"called Action.setTooltip with arg '{data}'")


class MockShortcut:
    activated = MockSignal()
    def __init__(self, *args):
        print('called Shortcut.__init__ with args', args)


class MockApplication:
    def __init__(self, *args):
        print('called Application.__init__')

    def exec_(self):  # Qt5
        print('called Application.exec_')

    def exec(self):  # Qt6
        print('called Application.exec')

    def setOverrideCursor(self, arg):
        print(f'called Application.setOverrideCursor with arg of type {type(arg)}')

    def restoreOverrideCursor(self):
        print('called Application.restoreOverrideCursor')

    def clipboard():
        print('called Application.clipboard')
        return MockClipBoard()

    def setWindowIcon(self, *args):
        print('called Application.setWindowIcon')


class MockClipBoard:
    def __init__(self):
        print('called ClipBoard.__init__')
    def setText(self, data):
        print(f"called Clipboard.setText with arg '{data}'")


class MockWidget:
    def __init__(self, *args):
        print('called Widget.__init__')

    def show(self):
        print('called Widget.show')

    def setWindowTitle(self, text):
        print(f'called Widget.setWindowTitle with arg `{text}`')

    def setWindowIcon(self, *args):
        print('called Widget.setWindowIcon')

    def resize(self, *args):
        print('called Widget.resize with args', args)

    def close(self):
        print('called Widget.close')

    def setLayout(self, *args):
        print('called Widget.setLayout')


class MockScrollBar:
    def __init__(self, *args):
        print('called ScrollBar.__init__')

    def maximum(self):
        print('called Scrollbar.maximum')
        return 99

    def setMaximum(self, value):
        print(f'called Scrollbar.setMaximum with value `{value}`')

    def setValue(self, value):
        print(f'called Scrollbar.setValue with value `{value}`')


class MockScrollArea:
    def __init__(self, *args):
        print('called ScrollArea.__init__ with args', args)

    def setWidget(self, arg):
        print(f'called ScrollArea.setWidget with arg of type `{type(arg)}`')

    def setAlignment(self, arg):
        print(f'called ScrollArea.setAlignment with arg {arg}')

    def setWidgetResizable(self, arg):
        print(f'called ScrollArea.setWidgetResizable with arg `{arg}`')

    def ensureVisible(self, *args):
        print(f'called ScrollArea.ensureVisible with args', args)

    def verticalScrollBar(self):
        print('called ScrollArea.verticalScrollBar')
        return 'vertical scrollbar'


class MockStackedWidget:
    def __init__(self, *args):
        print('called StackedWidget.__init__')

    def addWidget(self, arg):
        print(f"called StackedWidget.addWidget with arg {arg}")

    def insertWidget(self, *args):
        print("called StackedWidget.insertWidget with args", args)

    def removeWidget(self, arg):
        print(f"called StackedWidget.removeWidget with arg {arg}")

    def currentWidget(self):
        print("called StackedWidget.currentWidget")
        return 'current widget'

    def setCurrentIndex(self, num):
        print(f"called StackedWidget.setCurrentIndex with arg {num}")
        return 'current widget'

    def widget(self, num):
        print("called StackedWidget.widget with arg {num}")
        return 'widget'


class MockScrolledWidget:
    def __init__(self, *args):
        print('called ScrolledWidget.__init__')

    def verticalScrollBar(self):
        print('called ScrolledWidget.verticalScrollBar')
        return MockScrollBar()


class MockSize:
    def __init__(self, *args):
        print('called Size.__init__ with args', args)


class MockMainWindow:
    def __init__(self, *args, **kwargs):
        print('called MainWindow.__init__')
        self.app = MockApplication()

    def move(self, *args):
        print('called MainWindow.move with args', args)

    def resize(self, *args):
        print('called MainWindow.resize with args', args)

    def width(self, *args):
        print('called MainWindow.width with args', args)
        return 'width'

    def height(self, *args):
        print('called MainWindow.height with args', args)
        return 'height'

    def show(self):
        print('called MainWindow.show')

    def hide(self):
        print('called MainWindow.hide')

    def close(self):
        print('called MainWindow.close')

    def setWindowTitle(self, text):
        print(f'called MainWindow.setWindowTitle with arg `{text}`')

    def windowTitle(self):
        print('called MainWindow.windowTitle')
        return 'text'

    def setWindowIcon(self, *args):
        print('called MainWindow.setWindowIcon')

    def setWindowModality(self, arg):
        print(f"called MainWindow.setWindowModality with arg '{arg}'")

    def statusBar(self):
        print('called MainWindow.statusBar')
        return MockStatusBar()

    def menuBar(self):
        print('called MainWindow.menuBar')
        return MockMenuBar()

    def setCentralWidget(self, arg):
        print(f'called MainWidget.setCentralWindow with arg of type `{type(arg)}`')

    def addAction(self, arg):
        print('called MainWindow.addAction')

    def keyReleaseEvent(self, arg):
        print('called MainWindow.keyReleaseEvent')


class MockFrame:
    HLine = '---'
    # Box = '[]'
    Box = 32
    Raised = 6
    Shape = types.SimpleNamespace(HLine='---', Box=32)  # PyQt6
    Shadow = types.SimpleNamespace(Raised=6)  # PyQt6

    def __init__(self, parent=None):
        print('called Frame.__init__')

    def setWindowTitle(self, arg):
        print(f"called Frame.setWindowTitle wth arg '{arg}'")

    def setFrameShape(self, arg):
        print(f'called Frame.setFrameShape with arg `{arg}`')

    def setFrameStyle(self, arg):
        print(f'called Frame.setFrameStyle with arg `{arg}`')

    def setLayout(self, arg):
        print(f'called Frame.setLayout with arg of type {type(arg)}')

    def show(self):
        print('called Frame.show')

    def close(self):
        print('called Frame.close')

    def setMaximumHeight(self, number):
        print(f'called Frame.setMaximumHeight with arg `{number}`')


class MockPixmap:
    def __init__(self, *args):
        print('called Pixmap.__init__')

    def load(self, fname):
        print('called Pixmap.load for `fname`')
        return 'ok'

    def scaled(self, x, y):
        print(f'called Pixmap.scaled to `{x}`, `{y}`')
        return 'ok'

    def fill(self, color):
        print(f'called Pixmap.fill with arg {color}')


class MockIcon:
    ThemeIcon = types.SimpleNamespace(EditClear='')
    def __init__(self, arg):
        print(f'called Icon.__init__ with arg `{arg}`')

    def fromTheme(self, *args):
        print('called Icon.fromTheme with args', args)


class MockImage:
    def __init__(self, *args):
        print(f'called Image.__init__ with args', args)

    def save(self, filename):
        print(f'called image.save with arg {filename}')


class MockMenuBar:
    def __init__(self):
        print('called MenuBar.__init__')
        self.menus = []

    def clear(self):
        print('called MenuBar.clear')
        self.menus = []

    def addMenu(self, text):
        print('called MenuBar.addMenu with arg ', text)
        newmenu = MockMenu(text)
        self.menus.append(newmenu)
        return newmenu


class MockMenu:
    def __init__(self, *args):
        print('called Menu.__init__ with args', args)
        if args:
            self.menutext = args[0]
        self._actions = []
    # def addAction(self, text, func):

    def actions(self):
        return self._actions

    def addAction(self, *args):
        if len(args) == 1 and not isinstance(args[0], str):
            print('called Menu.addAction')
            self._actions.append(args[0])
            return None
        # overloads: icon, text / text, callback, shortcut(s) / icon, text, callback, shortcut(s)
        # geen idee wat ik hiervan allemaal gebruik
        if isinstance(args[0], str):
            text = args[0]
            func = args[1] if len(args) > 1 else None
        else:
            text = args[1]
            func = args[2] if len(args) > 2 else None
        print(f'called Menu.addAction with args `{text}` {func}')
        newaction = MockAction(text, func)
        self._actions.append(newaction)
        return newaction

    def addSeparator(self):
        print('called Menu.addSeparator')
        newaction = MockAction('-----', None)
        self._actions.append(newaction)
        return newaction

    def addMenu(self, *args):
        print('called Menu.addMenu with args', args)
        if not args or isinstance(args[0], str):
            return MockMenu()
        return MockAction()

    def setTitle(self, text):
        print(f"called Menu.setTitle with arg '{text}'")
        self.menutext = text

    def title(self):
        print(f"called Menu.title")
        return self.menutext

    def removeAction(self, action):
        print(f'called Menu.removeaction with arg {action}')
        self._actions.remove(action)

    def setStatusTip(self, text):
        print(f"called Menu.setStatusTip with arg '{text}'")

    def setDisabled(self, value):
        print(f"called Menu.setDisabled with arg '{value}'")

    def exec_(self, *args, **kwargs):
        print('called Menu.exec_ with args', args, kwargs)

    def exec(self, *args, **kwargs):
        print('called Menu.exec with args', args, kwargs)


class MockToolBar:
    def __init__(self, *args):
        if args:
            print('called ToolBar.__init__ with args', args)
        else:
            print('called ToolBar.__init__')

    def addAction(self, value):
        print('called ToolBar.addAction')

    def addWidget(self, value):
        print(f'called ToolBar.addWidget with arg {value}')

    def addSeparator(self):
        print('called ToolBar.addSeparator')

    def setEnabled(self, value):
        print(f'called ToolBar.setEnabled with arg {value}')

    def setIconSize(self, *args):
        print(f'called ToolBar.setIconSize')


class MockSplitter:
    def __init__(self, *args):
        print('called Splitter.__init__')

    def addWidget(self, arg):
        print(f"called Splitter.addWidget with arg of type {type(arg)}")

    def setOrientation(self, *args):
        print('called Splitter.setOrientation with args', args)

    def setSizes(self, *args):
        print('called Splitter.setSizes with args', args)

    def sizes(self, *args):
        return 'left this wide', 'right that wide'


class MockTabWidget:
    currentChanged = MockSignal()
    tabCloseRequested = MockSignal()

    def __init__(self, *args):
        print('called TabWidget.__init__')
        self._current = -1

    def resize(self, *args):
        print('called TabWidget.resize with args', args)

    def setCurrentIndex(self, num):
        print(f'called TabWidget.setCurrentIndex with arg `{num}`')
        self._current = num

    def currentIndex(self):
        print('called TabWidget.currentIndex')
        return self._current

    def currentWidget(self):
        print('called TabWidget.currentWidget')

    def setCurrentWidget(self, arg):
        print(f'called TabWidget.setCurrentWidget with arg `{arg}`')

    def addTab(self, tab, title):
        print(f'called TabWidget.addTab with args `{tab!s}` `{title}`')

    def removeTab(self, tab):
        print('called TabWidget.removeTab with arg', tab)

    def setTabText(self, *args):
        print('called TabWidget.setTabText with args', args)

    def setTabEnabled(self, *args):
        print('called TabWidget.setTabEnabled with args', args)

    def tabText(self, *args):
        print('called TabWidget.tabtext with args', args)
        return 'tab text'

    def count(self):
        print('called TabWidget.count')
        return 'number of tabs'

    def widget(self, arg):
        print('called TabWidget.widget with arg', arg)

    def clear(self):
        print('called TabWidget.clear')


class MockHeader:
    Stretch = 'stretch'
    ResizeMode = types.SimpleNamespace(Stretch='stretch')  # PyQt6
    sectionClicked = MockSignal()

    def __init__(self, *args):
        print('called Header.__init__')
        self.items = []

    def setStretchLastSection(self, value):
        print(f'called Header.setStretchLastSection with arg {value}')

    def setSectionResizeMode(self, col, mode):
        print(f'called Header.setSectionResizeMode for col {col} mode {mode}')

    def setSectionsClickable(self, value):
        print(f'called Header.setSectionsClickable with value {value}')

    def resizeSection(self, col, width):
        print(f'called Header.resizeSection for col {col} width {width}')

    def setVisible(self, value):
        print(f"called Header.setVisible with args '{value}'")


class MockTreeWidget:
    SingleSelection = 1
    SelectionMode = types.SimpleNamespace(SingleSelection=1)  # Qt6
    InternalMove = 4
    DragDropMode = types.SimpleNamespace(InternalMove=4)  # Qt6
    itemSelectionChanged = MockSignal()
    itemEntered = MockSignal()
    itemActivated = MockSignal()
    itemDoubleClicked = MockSignal()
    currentItemChanged = MockSignal()

    def __init__(self, *args):
        print('called Tree.__init__')

    def resize(self, *args):
        print('called Tree.resize with args', args)

    def setColumnCount(self, num):
        print(f'called Tree.setColumnCount with arg `{num}`')

    def setColumnWidth(self, col, width):
        print(f'called Tree.setColumnWidth with args {col}, {width}')

    def hideColumn(self, *args):
        print('called Tree.hideColumn')

    def resizeColumnToContents(self, colno):
        print(f'called Tree.resizeColumnToContents with arg {colno}')

    def header(self):
        print('called Tree.header')
        return MockHeader()

    def setHeaderLabels(self, label_list):
        print(f'called Tree.setHeaderLabels with arg `{label_list}`')

    def setUniformRowHeights(self, count):
        print(f'called Tree.setUniformRowHeights with arg `{count}`')

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
        return 'Tree.topLevelItem'

    def indexOfTopLevelItem(self, arg):
        print(f'called Tree.indexOfTopLevelItem with arg `{arg}`')
        return 'index'

    def takeTopLevelItem(self, arg):
        print(f'called Tree.takeTopLevelItem with arg `{arg}`')
        return 'Tree.TopLevelItem'

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

    def itemAbove(self, arg):
        print(f'called Tree.itemAbove with arg {arg}')
        return 'x'

    def itemAt(self, *args):
        if len(args) == 1:
            line, col = args[0]
            print(f'called Tree.itemAt with args', args)
        else:
            line, col = args
            print(f'called Tree.itemAt with args ({line}, {col})')
        return f'item at ({line}, {col})'

    def count(self):
        print('called Tree.count')
        return 0

    def clear(self):
        print('called Tree.clear')

    def collapseItem(self, item):
        print(f'called Tree.collapseItem with arg {item}')

    def expandItem(self, item):
        print(f'called Tree.expandItem with arg {item}')

    def mapToGlobal(self, arg):
        print('called Tree.mapToGlobal with arg', arg)
        return 'mapped-to-global'

    def visualItemRect(self, arg):
        print('called Tree.visualItemRect with arg', arg)
        return types.SimpleNamespace(bottomRight=lambda *x: 'bottom-right',
                                     center=lambda *x: 'center')

    def setAlternatingRowColors(self, arg):
        print(f'called Tree.setAlternatingRowColors with arg {arg}')

    def setSortingEnabled(self, arg):
        print(f'called Tree.setSortingEnabled with arg {arg}')

    def setDragEnabled(self, arg):
        print(f'called Tree.setDragEnabled with arg {arg}')

    def setDragDropMode(self, arg):
        print(f'called Tree.setDragDropMode with arg {arg}')

    def setAcceptDrops(self, arg):
        print(f'called Tree.setAcceptDrops with arg {arg}')

    def setDropIndicatorShown(self, arg):
        print(f'called Tree.setDropIndicatorShown with arg {arg}')

    def dropEvent(self, event):
        print(f'called Tree.dropEvent with arg {event}')

    def mousePressEvent(self, event):
        print(f'called Tree.mousePressEvent with arg {event}')

    def mouseReleaseEvent(self, event):
        print(f'called Tree.mouseReleaseEvent with arg {event}')

    def keyReleaseEvent(self, event):
        print(f'called Tree.keyReleaseEvent with arg {event}')


class MockTreeItem:
    def __init__(self, *args):   # text='', data=''):
        print('called TreeItem.__init__ with args', args)
        self._text = []
        self._data = []
        if args:
            self._text = list(args)
        else:
            self._text = []
        self.subitems = []
        self._parent = 'parent'

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

    def parent(self):
        print('called TreeItem.parent')
        return self._parent

    def addChild(self, item):
        print('called TreeItem.addChild')
        self.subitems.append(item)
        with contextlib.suppress(AttributeError):
            item._parent = self

    def insertChild(self, index, item):
        print(f'called TreeItem.insertChild at pos {index}')
        self.subitems.insert(index, item)

    def childCount(self):
        print('called TreeItem.childCount')
        return len(self.subitems)

    def child(self, num):
        print(f'called TreeItem.child with arg {num}')
        return self.subitems[num]

    def indexOfChild(self, item):
        print('called TreeItem.indexOfChild')
        return self.subitems.index(item)

    def takeChild(self, itemseq):
        print('called TreeItem.takeChild')
        return f'child no. {itemseq}'

    def removeChild(self, item):
        print('called TreeItem.removeChild')

    def sortChildren(self, *args):
        print('called TreeItem.sortChildren with args', args)

    def setHidden(self, value):
        print(f"called TreeItem.setHidden with arg `{value}`")

    def setExpanded(self, value):
        print(f"called TreeItem.setExpanded with arg `{value}`")

    def isExpanded(self):
        print(f"called TreeItem.isExpanded")
        return False

    def font(self, *args):
        return MockFont()

    def setFont(self, *args):
        print('called TreeItem.setFont')

    def setForeground(self, *args):
        print('called TreeItem.setForeground with args', args)

    def setTextAlignment(self, *args):
        print('called TreeItem.setTextAlignment with args', args)

    def setToolTip(self, *args):
        print('called TreeItem.setTooltip with args', args)


class MockFont:
    def __init__(self, *args):
        print('called Font.__init__')

    def setBold(self, value):
        print(f'called Font.setBold with arg `{value}`')

    def setItalic(self, value):
        print(f'called Font.setItalic with arg `{value}`')

    def setUnderline(self, value):
        print(f'called Font.setUnderline with arg `{value}`')

    def setStrikeOut(self, value):
        print(f'called Font.setStrikeOut with arg `{value}`')

    def bold(self):
        print(f'called Font.bold')
        return 'bold'

    def italic(self):
        print(f'called Font.italic')
        return 'italic'

    def underline(self):
        print(f'called Font.underline')
        return 'underline'

    def strikeOut(self):
        print(f'called Font.strikeOut')
        return 'strikeOut'

    def setFamily(self, *args):
        print('called Font.setFamily')

    def family(self, *args):
        print('called Font.family')
        return 'fontfamily'

    def fixedPitch(self, *args):
        print('called Font.fixedPitch')
        return 'fixedPitch'

    def setFixedPitch(self, value):
        print(f'called Font.setFixedPitch with arg `{value}`')

    def setPointSize(self, *args):
        print('called Font.setPointSize')

    def pointSize(self, *args):
        print('called Font.pointSize')
        return 'fontsize'


class MockFontInfo:
    def __init__(self, arg):
        print(f'called FontInfo.__init__ with arg {arg}')

    def family(self):
        print(f'called Font.family')
        return 'family name'


class MockFontDialog:
    def __init__(self):
        print('called FontDialog.__init__')

    def getFont(default_font, parent):
        print('called FontDialog.getFont with args', parent)
        return None, False

    def getFont2(default_font, parent):
        print('called FontDialog.getFont with args', parent)
        return MockFont(), True


class MockEditorWidget:
    "contains elements of TextEdit, RichTextEdit, Scintilla"
    # wordt in albums_gui.py aangeroepen met argumenten tekst en parent
    WrapWord = 1  # Qt5
    WrapMode = types.SimpleNamespace(WrapWord=1)  # Qt6
    SloppyBraceMatch = 2  # Qt5
    BraceMatch = types.SimpleNamespace(SloppyBraceMatch=2)  # Qt6
    PlainFoldStyle = 3  # Qt5
    FoldStyle = types.SimpleNamespace(PlainFoldStyle=3)  # Qt6
    defaultfamily = 'font family'
    defaultsize = '12pt'
    currentCharFormatChanged = MockSignal()
    cursorPositionChanged = MockSignal()
    textChanged = MockSignal()

    def __init__(self, *args):
        if args:
            print('called Editor.__init__ with args', args)
            if len(args) == 1:
                self.parent = args[0]
            else:
                self._text, self.parent, *dummy = args
        else:
            print('called Editor.__init__')
        self._text = args[0] if args else ''

    def resize(self, *args):
        print('called Editor.resize with args', args)

    def setMaximumWidth(self, number):
        print(f'called Editor.setMaximumWidth with arg `{number}`')

    def setMaximumHeight(self, number):
        print(f'called Editor.setMaximumHeight with arg `{number}`')

    def setMinimumWidth(self, number):
        print(f'called Editor.setMinimumWidth with arg `{number}`')

    def setMinimumHeight(self, number):
        print(f'called Editor.setMinimumHeight with arg `{number}`')

    def setWrapMode(self, value):
        print(f'called Editor.setWrapMode with arg `{value}`')

    def setBraceMatching(self, value):
        print(f'called Editor.setBraceMatching with arg `{value}`')

    def setAutoFormatting(self, value):
        print(f'called Editor.setAutoFormatting with arg `{value}`')

    def setAutoIndent(self, value):
        print(f'called Editor.setAutoIndent with arg `{value}`')

    def setFolding(self, value):
        print(f'called Editor.setFolding with arg `{value}`')

    def setReadOnly(self, value):
        print(f'called Editor.setReadOnly with arg `{value}`')

    def setFont(self, data):
        print(f'called Editor.setFont')  # with arg `{data}`')

    def setFontWeight(self, arg):
        print(f'called Editor.setFontWeight with arg {arg}')

    def setFontItalic(self, arg):
        print(f'called Editor.setFontItalic with arg {arg}')

    def setFontUnderline(self, arg):
        print(f'called Editor.setFontUnderline with arg {arg}')

    def setFontFamily(self, arg):
        print(f"called Editor.setFontFamily with arg '{arg}'")

    def setFontPointSize(self, arg):
        print(f"called Editor.setFontPointSize with arg '{arg}'")

    def currentFont(self):
        print(f'called Editor.currentFont')
        return MockFont()

    def setCurrentFont(self, data):
        print(f'called Editor.setCurrentFont')  # with arg `{data}`')

    def setMarginsFont(self, data):
        print(f'called Editor.setMarginsFont')  # with arg `{data}`')

    def setMarginWidth(self, *args):
        print('called Editor.setMarginWidth with args', args)

    def setMarginLineNumbers(self, *args):
        print('called Editor.setMarginLineNumbers with args', args)

    def setMarginsBackgroundColor(self, arg):
        print(f'called Editor.setMarginsBackgroundColor with arg {arg}')

    def setCaretLineVisible(self, value):
        print(f'called Editor.setCaretLineVisible with arg `{value}`')

    def setCaretLineBackgroundColor(self, value):
        print(f'called Editor.setCaretLineBackgroundColor with arg {value}')

    def setLexer(self, *args):
        print('called Editor.setLexer')  # with args', args)

    def clear(self, *args):
        print('called Editor.clear')

    def setEnabled(self, value):
        print(f'called Editor.setEnabled with arg {value}')

    def isModified(self, *args):
        return 'x'

    def setPlainText(self, value):
        print(f'called Editor.setPlainText with arg `{value}`')

    def setAcceptRichText(self, value):
        print(f'called Editor.setAcceptRichText with arg `{value}`')

    def setText(self, text):
        print(f'called Editor.setText with arg `{text}`')

    def setHtml(self, text):
        print(f'called Editor.setHtml with arg `{text}`')

    def toHtml(self):
        print(f'called Editor.toHtml')
        return self._text or 'editor text'

    def text(self):
        return 'editor text'

    def document(self):
        return MockTextDocument()

    def toPlainText(self):
        print('called Editor.toPlainText')
        return self._text or 'editor text'

    def setFocus(self, *args):
        print('called Editor.setFocus')

    def hasFocus(self, *args):
        print('called Editor.hasFocus')
        return False

    def setTabChangesFocus(self, value):
        print(f'called Editor.setTabChangesFocus with arg {value}')

    def setTabStopDistance(self, value):
        print(f'called Editor.setTabStopDistance with arg {value}')

    def insertFromMimeData(self, *args):
        print("called Editor.insertFromMimeData with args", args)

    def canInsertFromMimeData(self, data):
        print(f"called Editor.canInsertFromMimeData with arg '{data}'")
        return False

    def charformat_changed(self, arg):
        print(f'called Editor.charformat_changed')  #  with arg {arg}')

    def moveCursor(self, *args):
        print('called Editor.moveCursor with args', args)

    def textCursor(self):
        print('called Editor.textCursor')
        return MockTextCursor()

    def setTextCursor(self, *args):
        print('called Editor.setTextCursor')  #  with args', args)

    def selectAll(self):
        print('called Editor.selectAll')

    def setAlignment(self, value):
        print(f'called Editor.setAlignment with arg {int(value)}')  # PyQt5

    def mergeCurrentCharFormat(self, arg):
        print(f'called Editor.mergeCurrentCharFormat with arg {arg}')

    def focusInEvent(self, *args):
        print(f'called Editor.focusInEvent with args', args)

    def focusOutEvent(self, *args):
        print(f'called Editor.focusOutEvent with args', args)

    def find(self, *args):
        print('called Editor.find with args', args)

    def ensureCursorVisible(self):
        print('called Editor.ensureCursorVisible')


class MockTextDocument:
    ImageResource = 2
    ResourceType = types.SimpleNamespace(ImageResource=2)  # Qt6
    def __init__(self, *args):
        print('called TextDocument.__init__ with args', args)

    def addResource(self, *args):
        if args[0] == self.ImageResource:
            print("called TextDocument.addResource with args"
                  f" ({args[0]}, {type(args[1])}, {type(args[2])})")

    def setModified(self, value):
        print(f'called TextDocument.setModified with arg {value}')

    def setHtml(self, value):
        print(f"called TextDocument.setHtml with arg '{value}'")

    def setPlainText(self, text):
        print(f"called TextDocument.setPlainText with arg '{text}'")

    def toPlainText(self):
        print(f'called TextDocument.toPlainText')
        return 'plain text'

    def find(self, text):
        print(f"called TextDocument.find with arg '{text}'")

    def print(self, printer):
        print(f'called TextDocument.print with arg {printer}')

    def isModified(self):
        print('called textDocument.isModified')
        return 'modified'


class MockTextCursor:
    def __init__(self):
        print('called TextCursor.__init__')

    def hasSelection(self):
        print('called TextCursor.hasSelection')

    def position(self):
        print('called TextCursor.position')
        return 'position'

    def insertImage(self, arg):
        print(f'called Cursor.insertImage with arg {arg}')

    def setPosition(self, arg):
        print(f'called TextCursor.setPosition with arg {arg}')

    def select(self, arg):
        print(f'called TextCursor.select with arg {arg}')

    def mergeCharFormat(self, arg):
        print(f'called TextCursor.mergeCharFormat with arg {arg}')

    def blockFormat(self):
        print(f'called TextCursor.blockFormat')
        return MockTextBlockFormat()

    def setBlockFormat(self, arg):
        print(f'called TextCursor.setBlockFormat')  #  with arg {arg}')

    def mergeBlockFormat(self, arg):
        print(f'called TextCursor.mergeBlockFormat')  #  with arg {arg}')


class MockTextBlockFormat:
    def __init__(self, *args):
        print('called TextBlockFormat.__init__ with args', args)

    def indent(self):
        print("called TextBlockFormat.indent")
        return 1

    def setIndent(self, value):
        print(f"called TextBlockFormat.setIndent with arg {value}")

    def setLineHeight(self, *args):
        print("called TextBlockFormat.setLineHeight with args", args)

    def topMargin(self):
        print("called TextBlockFormat.topMargin")
        return 1

    def setTopMargin(self, value):
        print(f"called TextBlockFormat.setTopMargin with arg {value}")

    def bottomMargin(self):
        print("called TextBlockFormat.bottomMargin")
        return 1

    def setBottomMargin(self, value):
        print(f"called TextBlockFormat.setBottomMargin with arg {value}")


class MockTextCharFormat:
    def __init__(self, *args):
        print('called TextCharFormat.__init__ with args', args)
    def font(self):
        print(f'called TextCharFormat.font')
        return 'a font'
    def setFont(self, arg):
        print(f'called TextCharFormat.setFont')  # with arg {arg}')
    def setFontFamily(self, arg):
        print(f'called TextCharFormat.setFontFamily with arg {arg}')
    def setFontWeight(self, arg):
        print(f'called TextCharFormat.setFontWeight with arg {arg}')
    def setFontPointSize(self, arg):
        print(f'called TextCharFormat.setFontPointSize with arg {arg}')
    def setFontItalic(self, arg):
        print(f'called TextCharFormat.setFontItalic with arg {arg}')
    def setFontUnderline(self, arg):
        print(f'called TextCharFormat.setFontUnderline with arg {arg}')
    def setFontStrikeOut(self, arg):
        print(f'called TextCharFormat.setFontStrikeOut with arg {arg}')
    def setFontFixedPitch(self, arg):
        print(f'called TextCharFormat.setFontFixedPitch with arg {arg}')
    def setForeground(self, arg):
        print(f'called TextCharFormat.setForeground with arg {arg}')
    def foreground(self):
        print(f'called TextCharFormat.foreground')
        return MockBrush('fg')
    def setBackground(self, arg):
        print(f'called TextCharFormat.setBackground with arg {arg}')
    def background(self):
        print(f'called TextCharFormat.background')
        return MockBrush('bg')


class MockSysTrayIcon:
    activated = MockSignal()

    def __init__(self, *args):
        print('called TrayIcon.__init__')

    def showMessage(self, *args):
        print('called TrayIcon.showMessage with args', args)

    def setToolTip(self, *args):
        print('called TrayIcon.setToolTip with args', args)

    def hide(self):
        print('called TrayIcon.hide')

    def show(self):
        print('called TrayIcon.show')


class MockStatusBar:
    def __init__(self, *args):
        print('called StatusBar.__init__ with args', args)

    def showMessage(self, text):
        print(f'called StatusBar.showMessage with arg `{text}`')

    def addWidget(self, arg, **kwargs):
        print(f'called StatusBar.addWidget with args (item of type {type(arg)},)', kwargs)

    def addPermanentWidget(self, arg, **kwargs):
        print(f'called StatusBar.addPermanentWidget with args (item of type {type(arg)},)', kwargs)


class MockDialog:
    def __init__(self, parent=None, *args, **kwargs):
        self.parent = parent
        print('called Dialog.__init__ with args', parent, args, kwargs)

    def exec_(self):  # Qt5
        print('called Dialog.exec_')

    def exec(self):  # Qt6
        print('called Dialog.exec')

    def resize(self, *args):
        print('called Dialog.resize with args', args)

    def show(self):
        print('called Dialog.show')

    def setWindowTitle(self, *args):
        print('called Dialog.setWindowTitle with args', args)

    def setWindowIcon(self, *args):
        print('called Dialog.setWindowIcon with args', args)

    def setLayout(self, *args):
        print('called Dialog.setLayout')

    def accept(self):
        print('called Dialog.accept')
        return 'Accepted'

    def reject(self):
        print('called Dialog.reject')
        return 'Rejected'

    def done(self, value):
        print(f'called Dialog.done with arg `{value}`')

    def addAction(self, arg):
        print('called Dialog.addAction')


def get_item(parent, *args, **kwargs):
    print('called InputDialog.getItem with args', parent, args, kwargs)
    return '', False


def get_text(parent, *args, **kwargs):
    print('called InputDialog.getText with args', parent, args, kwargs)
    return '', False


class MockInputDialog:
    getText = staticmethod(get_text)
    getItem = staticmethod(get_item)

    def __init__(self, *args, **kwargs):
        print('called InputDialog.__init__')


def get_open(parent, *args, **kwargs):
    print('called FileDialog.getOpenFileName with args', parent, args, kwargs)
    return '', False  # canceled


def get_open2(parent, *args, **kwargs):
    print('called FileDialog.getOpenFileNames with args', parent, args, kwargs)
    return [], False  # canceled


def get_save(parent, *args, **kwargs):
    print('called FileDialog.getSaveFileName with args', parent, args, kwargs)
    return '', False  # canceled


def get_dir(parent, *args, **kwargs):
    print('called FileDialog.getExistingDirectory with args', parent, args, kwargs)
    return ''  # canceled


class MockFileDialog:
    getOpenFileName = staticmethod(get_open)
    getOpenFileNames = staticmethod(get_open2)
    getSaveFileName = staticmethod(get_save)
    getExistingDirectory = staticmethod(get_dir)

    def __init__(self, *args, **kwargs):
        print('called Filedialog.__init__')


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

    def __len__(self):
        return self._count

    def count(self):
        return self._count

    def removeWidget(self, *args):
        print(f'called VBox.removeWidget with arg of type {type(args[0])}')
        self._count -= 1

    def removeItem(self, *args):
        print('called VBox.removeItem')
        # self._count -= 1

    def itemAt(self, rownum):
        print(f'called VBox.itemAt with arg {rownum}')
        return f'widget at {rownum}'

    def update(self):
        print('called VBox.update')


class MockHBoxLayout:
    def __init__(self, *args):
        print('called HBox.__init__')
        self._count = 0

    def addWidget(self, *args, **kwargs):
        # print('called HBox.addWidget')
        if kwargs:
            print(f'called HBox.addWidget with arg of type {type(args[0])}, kwargs', kwargs)
        else:
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

    def takeAt(self, num):
        pass

    def update(self):
        print('called HBox.update')


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

    def setRowMinimumHeight(self, *args):
        print('called Grid.setRowMinimumHeight with args', args)

    def setColumnStretch(self, *args):
        print('called Grid.setColumnStretch with args', args)

    def count(self):
        print('called Grid.count')
        return 3

    def rowCount(self):
        print('called Grid.rowCount')
        return 1

    def columnCount(self):
        print('called Grid.columnCount')
        return 1

    def removeItem(self, *args):
        print('called Grid.removeItem with args', args)

    def itemAtPosition(self, *args):
        print('called Grid.itemAtPosition with args', args)
        return 'itematpos'

    def update(self):
        print('called Grid.update')

    def removeWidget(self, *args):
        print(f'called Grid.removeWidget with arg of type {type(args[0])}')


class MockLabel:
    def __init__(self, *args):
        if args:
            print('called Label.__init__ with args', args)
            self._text = args[0]
        else:
            print('called Label.__init__')
            self._text = ''

    def setVisible(self, value):
        print(f'called Label.setVisible with arg `{value}`')

    def setMinimumWidth(self, number):
        print(f'called Label.setMinimumWidth with arg `{number}`')

    def setMinimumHeight(self, number):
        print(f'called Label.setMinimumHeight with arg `{number}`')

    def setMaximumWidth(self, number):
        print(f'called Label.setMaximumWidth with arg `{number}`')

    def setText(self, text):
        print(f'called Label.setText with arg `{text}`')
        self._text = text

    def text(self):
        return self._text

    def setPixmap(self, data):
        print('called Label.setPixmap')

    def setOpenExternalLinks(self, target):
        print(f"called Label.setOpenExternalLinks with arg '{target}'")

    def setWordWrap(self, value):
       print(f'called Label.setWordWrap with arg {value}')

    def close(self):
        print('called Label.close')


class MockCheckBox:
    clicked = MockSignal()
    toggled = MockSignal()
    stateChanged = MockSignal()
    checkStateChanged = MockSignal()

    def __init__(self, *args):
        if args and isinstance(args[0], str):
            print(f"called CheckBox.__init__ with text '{args[0]}'")
            self.textvalue = args[0]
        else:
            print('called CheckBox.__init__')
            self.textvalue = ''
        self.checked = False

    def setEnabled(self, value):
        print(f'called CheckBox.setEnabled with arg {value}')

    def setDisabled(self, value):
        print(f'called CheckBox.setDisabled with arg {value}')

    def setChecked(self, value):
        print(f'called CheckBox.setChecked with arg {value}')
        self.checked = value

    def setCheckable(self, state):
        print(f'called CheckBox.setCheckable with arg {state}')
        self.checkable = state

    def toggle(self):
        print(f'called CheckBox.toggle')
        self.checked = not self.checked

    def isChecked(self):
        print('called CheckBox.isChecked')
        return self.checked

    def checkState(self):
        print('called CheckBox.checkState')
        return self.checked

    def text(self):
        return self.textvalue

    def setFocus(self, *args):
        print('called CheckBox.setFocus')

    def close(self):
        print('called CheckBox.close')

    def setFixedWidth(self, count):
        print(f"called CheckBox.setFixedWidth with arg '{count}'")


class MockComboBox:
    currentIndexChanged = MockSignal()
    currentTextChanged = MockSignal()
    editTextChanged = MockSignal()
    activated = MockSignal()

    def __init__(self, *args, **kwargs):
        print('called ComboBox.__init__')
        self._items = kwargs.get('items', [])
        self._index = 1

    def setMaximumWidth(self, number):
        print(f'called ComboBox.setMaximumWidth with arg `{number}`')

    def setMinimumWidth(self, number):
        print(f'called ComboBox.setMinimumWidth with arg `{number}`')

    def setEnabled(self, value):
        print(f'called ComboBox.setEnabled with arg {value}')

    def clear(self):
        print('called ComboBox.clear')

    def clearEditText(self):
        print('called ComboBox.clearEditText')

    def setEditText(self, text):
        print(f'called ComboBox.setEditText with arg `{text}`')

    def addItem(self, *item):
        print(f'called ComboBox.addItem with arg `{item[0]}`', end='')
        if len(item) == 2:
            print(f', userdata = {item[1]}')
        else:
            print()

    def addItems(self, itemlist):
        print(f'called ComboBox.addItems with arg {itemlist}')

    def insertItem(self, row, item):
        print(f'called ComboBox.insertItem with args ({row}, {item})')

    def insertItems(self, row, itemlist):
        print(f'called ComboBox.insertItems with args ({row}, {itemlist})')

    def height(self):
        return 100

    def setEditable(self, value):
        print(f'called ComboBox.setEditable with arg `{value}`')

    def setCurrentIndex(self, value):
        print(f'called ComboBox.setCurrentIndex with arg `{value}`')
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
        print(f'called ComboBox.setToolTip({value})')

    def setFocus(self):
        print('called ComboBox.setFocus')

    def setCompleter(self, arg):
        print('called ComboBox.setCompleter with arg', arg)

    def setAutoCompletionCaseSensitivity(self, arg):
        print('called ComboBox.setAutoCompletionCaseSensitivity with arg', arg)

    def completer(self):
        print('called ComboBox.completer')
        return MockCompleter()

    def count(self):
        print('called ComboBox.count')
        return 0

    def itemText(self, number):
        print(f'called ComboBox.itemText with value `{number}`')
        return str(number)

    def close(self):
        print('called ComboBox.close')

    def setFocus(self):
        print('called ComboBox.setFocus')

    def findText(self, *args):
        print('called ComboBox.findText with args', args)
        return 1

    def setMinimumContentsLength(self, value):
        print(f'called ComboBox.setMinimumContentsLength with arg {value}')

    def close(self):
        print('called ComboBox.close')


class MockCompleter:
    def setCaseSensitivity(self, arg):
        print(f"called Completer.setCaseSensitivity with arg {arg}")


class MockFontComboBox(MockComboBox):
    # activated = {str: MockSignal()}
    pass


class MockPushButton:
    clicked = MockSignal()

    def __init__(self, *args, **kwargs):
        print('called PushButton.__init__ with args', args, kwargs)
        self._text = args[0] if args else ''
        self._enabled = False

    def setMaximumWidth(self, number):
        print(f'called PushButton.setMaximumWidth with arg `{number}`')

    def setEnabled(self, value):
        print(f'called PushButton.setEnabled with arg `{value}`')
        self._enabled = value

    def setDisabled(self, value):
        print(f'called PushButton.setDisabled with arg `{value}`')
        self._enabled = not value

    def isEnabled(self):
        # print(f'called PushButton.isEnabled')
        return self._enabled

    def setDefault(self, value):
        print(f'called PushButton.setDefault with arg `{value}`')

    def setIcon(self, value):
        print(f'called PushButton.setIcon with arg `{value}`')

    def setFixedSize(self, *args):
        print('called PushButton.setFixedSize with args', args)

    def setIconSize(self, arg):
        print(f'called PushButton.setIconSize with arg of type {type(arg)}')

    def text(self):
        return self._text

    def setText(self, value):
        print(f'called PushButton.setText with arg `{value}`')
        self._text = value

    def setMenu(self, *args):
        print('called PushButton.setMenu()')

    def setShortcut(self, *args):
        print('called PushButton.setShortcut with args', args)

    def setToolTip(self, value):
        print(f'called PushButton.setToolTip with arg `{value}`')

    def close(self):
        print('called PushButton.close')


class MockRadioButton:
    clicked = MockSignal()
    toggled = MockSignal()

    def __init__(self, *args, **kwargs):
        print('called RadioButton.__init__ with args', args, kwargs)
        self._text = args[0] if args else ''
        self._checked = False

    def isChecked(self):
        print('called RadioButton.isChecked')
        return self._checked

    def setChecked(self, value):
        print(f'called RadioButton.setChecked with arg `{value}`')
        self._checked = value

    def setEnabled(self, value):
        print(f'called RadioButton.setEnabled with arg `{value}`')

    def text(self):
        return self._text

    def setText(self, value):
        print(f'called RadioButton.setText with arg `{value}`')
        self._text = value

    def setFocus(self):
        print('called RadioButton.setFocus')


class MockLineEdit:
    textChanged = MockSignal()
    textEdited = MockSignal()
    EchoMode = types.SimpleNamespace(Normal=0, Password=2)

    def __init__(self, *args):
        print('called LineEdit.__init__')
        for arg in args:
            if isinstance(arg, str):
                self._text = arg
                break
        else:
            self._text = ''

    def setReadOnly(self, value):
        print(f'called LineEdit.setReadOnly with arg `{value}`')

    def setEnabled(self, value):
        print(f'called LineEdit.setEnabled with arg {value}')

    def setDisabled(self, value):
        print(f'called LineEdit.setDisabled with arg {value}')

    def setMaximumHeight(self, value):
        print(f'called LineEdit.setMaximumHeight with arg `{value}`')

    def setMinimumHeight(self, value):
        print(f'called LineEdit.setMinimumHeight with arg `{value}`')

    def setMaximumWidth(self, value):
        print(f'called LineEdit.setMaximumWidth with arg `{value}`')

    def setFixedWidth(self, value):
        print(f'called LineEdit.setFixedWidth with arg `{value}`')

    def setMinimumWidth(self, value):
        print(f'called LineEdit.setMinimumWidth with arg `{value}`')

    def clear(self):
        print('called LineEdit.clear')
        self._text = ''

    def close(self):
        print('called LineEdit.close')

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
        print('called LineEdit.setFocus')

    def setEchoMode(selfi, value):
        print(f'called LineEdit.setEchoMode with arg {value}')


class MockButtonBox:
    Ok = 1  # Qt5
    Cancel = 2  # Qt5
    ActionRole = 9  # Qt5
    StandardButton = types.SimpleNamespace(Ok=1, Cancel=2)  # Qt6
    ButtonRole = types.SimpleNamespace(ActionRole=9)  # Qt6
    accepted = MockSignal()
    rejected = MockSignal()

    def __init__(self, *args):
        print('called ButtonBox.__init__ with args', args)

    def addButton(self, *args):
        print('called ButtonBox.addButton with args', args)


class MockButtonGroup:
    def __init__(self, *args):
        print('called ButtonGroup.__init__ with args', args)
        self._buttons = {}
        self._lastid = -1

    def addButton(self, button, buttonid=-1):
        print(f"called ButtonGroup.addButton with arg of type {type(button)}", end='')
        if buttonid == -1:
            print()
            self._lastid -= 1
            self._buttons[self._lastid] = button
        else:
            print(f' and id {buttonid}')
            self._buttons[buttonid] = button

    def button(self, button_id):
        print(f"called ButtonGroup.button with arg '{button_id}'")
        return self._buttons[button_id]

    def id(self, button):
        print(f"called ButtonGroup.id with arg of type {type(button)}")
        for button_id, button_ in self._buttons.items():
            if button_ is button:
                return button_id
        return None

    def buttons(self, *args):
        print('called ButtonGroup.buttons')
        return list(self._buttons.values())

    def checkedButton(self):
        print('called ButtonGroup.checkedButton')
        for button in self._buttons.values():
            if button.isChecked():
                return button
        return None

    def setExclusive(self, value):
        print(f'called ButtonGroup.setExclusive with arg {value}')


def show_information(parent, caption, message, *args):
    print(f'called MessageBox.information with args `{parent}` `{caption}` `{message}`')


def show_critical(parent, caption, message, *args):
    print(f'called MessageBox.critical with args `{parent}` `{caption}` `{message}`')


def ask_question(parent, caption, message, buttons, defaultButton=None):
    if defaultButton:
        print('called MessageBox.question with args'
              f' `{parent}` `{caption}` `{message}` `{buttons}` `{defaultButton}`')
    else:
        print(f'called MessageBox.question with args `{parent}` `{caption}` `{message}` `{buttons}`')
    return MockMessageBox.No


class MockMessageBox:
    Ok = 1
    Cancel = 2
    Yes = 4
    No = 8
    StandardButton = types.SimpleNamespace(Ok=1, Cancel=2, Yes=4, No=8)  # Qt6
    AcceptRole = 1
    ButtonRole = types.SimpleNamespace(AcceptRole=1)  # Qt6
    Information = 2
    Icon = types.SimpleNamespace(Information=2)  # Qt6
    information = staticmethod(show_information)
    critical = staticmethod(show_critical)
    question = staticmethod(ask_question)

    def __init__(self, *args, **kwargs):
        print('called MessageBox.__init__ with args', args, kwargs)

    def setText(self, text):
        print(f'called MessageBox.setText with arg `{text}`')

    def setWindowTitle(self, arg):
        print(f'called MessageBox.setWindowTitle with arg `{arg}`')

    def setInformativeText(self, text):
        print(f'called MessageBox.setInformativeText with arg `{text}`')

    def setStandardButtons(self, *args):
        print('called MessageBox.setStandardButtons')

    def setDefaultButton(self, arg):
        print(f'called MessageBox.setDefaultButton with arg `{arg}`')

    def setDetailedText(self, arg):
        print(f'called MessageBox.setDetailedText with arg `{arg}`')

    def setEscapeButton(self, arg):
        print(f'called MessageBox.setEscapeButton with arg `{arg}`')

    def addButton(self, *args):
        print(f'called MessageBox.addButton with arg `{args}`')

    def exec_(self, *args):  # Qt5
        print('called MessageBox.exec_')

    def exec(self, *args):  # Qt6
        print('called MessageBox.exec')

    def close(self, *args):
        print('called MessageBox.close')

    def clickedButton(self):
        print('called MessageBox.clickedButton')
        return 'button'


class MockSpinBox:
    valueChanged = MockSignal()
    def __init__(self, *args):
        print('called SpinBox.__init__')
        value = args[0] if args else 0
        self._value = value
    def setMinimum(self, count):
        print(f"called SpinBox.setMinimum with arg '{count}'")
    def setMaximum(self, count):
        print(f"called SpinBox.setMaximum with arg '{count}'")
    def setFixedWidth(self, count):
        print(f"called SpinBox.setFixedWidth with arg '{count}'")
    def setValue(self, arg):
        print(f"called SpinBox.setValue with arg '{arg}'")
        self._value = arg
    def value(self):
        print(f"called SpinBox.value")
        return self._value
    def close(self):
        print(f"called SpinBox.close")


class MockListBox:
    itemDoubleClicked = MockSignal()
    itemActivated = MockSignal()
    currentItemChanged = MockSignal()

    def __init__(self, *args):
        print('called List.__init__')
        self.list = []

    def setVisible(self, value):
        print(f'called List.setVisible with arg `{value}`')

    def setMinimumWidth(self, number):
        print(f'called List.setMinimumWidth with arg `{number}`')

    def setMinimumHeight(self, number):
        print(f'called List.setMinimumHeight with arg `{number}`')

    def __len__(self):
        return len(self.list)

    def count(self):
        return len(self.list)

    def clear(self):
        print('called List.clear')

    def setSelectionMode(self, *args):
        print('called List.setSelectionMode')

    def addItems(self, itemlist):
        print(f'called List.addItems with arg `{itemlist}`')

    def insertItems(self, row, itemlist):
        print(f'called List.insertItems with args ({row}, {itemlist})')

    def insertItem(self, row, item):
        print(f'called List.insertItem with args ({row}, item of type {type(item)})')

    def setCurrentItem(self, item):
        print('called List.setCurrentItem')

    def currentItem(self):
        print('called List.currentItem')
        return 'current item'

    def openPersistentEditor(self, arg):
        print(f'called List.openPersistentEditor with arg {arg}')

    def editItem(self, arg):
        print(f'called editItem with arg {arg}')

    def closePersistentEditor(self, arg):
        print(f'called List.closePersistentEditor with arg {arg}')

    def setCurrentRow(self, row):
        print(f'called List.setCurrentRow with rownumber {row}')
        self.row = row

    def currentRow(self):
        print(f'called List.currentRow')
        return 'current row'

    def item(self, row):
        try:
            result = self.list[row]
        except IndexError:
            print(f"called List.item with arg {row}'")
            result = None
        return result
    # def setFocus(self, value):
    #     print(f'called List.setFocus with arg `{value}`')

    def setFocus(self, *args):
        if args:
            print(f'called List.setFocus with arg `{args[0]}`')
        else:
            print('called List.setFocus')

    def selectedItems(self):
        print('called List.selectedItems')

    def takeItem(self, value):
        print(f'called List.takeItem with arg `{value}`')  # on `{self.list}`')

    def row(self, value):
        print(f'called List.row with arg `{value}`')  #  on `{self.list}`')
        return value

    def addItem(self, value):
        print(f'called List.addItem with arg `{value}`')  # on `{self.list}`')
        self.list.append(value)


class MockListItem:
    def __init__(self, *args):
        if args:
            print('called ListItem.__init__ with args', args)
            self._name = args[0] if args else ''
        else:
            print('called ListItem.__init__')
            self._name = ''

    def text(self):
        return self._name

    def setText(self, name):
        print(f"called ListItem.setText with arg '{name}'")
        self._name = name

    def setData(self, *args):
        print("called ListItem.setData with args", args)
        self._data = {args[0]: args[1]}

    def setSelected(self, arg):
        print(f'called ListItem.setSelected with arg `{arg}` for `{self._name}`')


class MockTableItem:
    def __init__(self, arg=''):
        print(f"called TableItem.__init__ with arg '{arg}'")
        self._text = arg
    def setText(self, value):
        print(f"called TableItem.setText with arg '{value}'")
        self._text = value
    def text(self):
        return self._text
    def setFlags(self, flags):
        print(f'called TableItem.setFlags with arg {flags}')
    def flags(self):
        print('called TableItem.flags')
        return 8
    def setToolTip(self, value):
        print('called TableItem.setToolTip with arg', value)


class MockTableSelectionRange:
    def __init__(self, *args):
        print('called TableRange.__init__ with args', args)
        self._fromrow, self._fromcol, self._maxrow, self._maxcol = (0, 0, 0, 0)
        if args:
            self._fromrow, self._fromcol, self._maxrow, self._maxcol = args
        self._rows = self._maxrow - self._fromrow + 1
        self._cols = self._maxcol - self._fromcol + 1

    def topRow(self):
        print(f"called TableRange.topRow")
        return self._fromrow

    def rowCount(self):
        print(f"called TableRange.rowCount")
        return self._rows


class MockTable:
    cellDoubleClicked = {(int, int): MockSignal}
    def __init__(self, *args):
        print('called Table.__init__ with args', args)
        self._cols = 0
        self._rows = 0
        self._header = MockHeader()
        self._vhead = MockHeader()
        self._items = {}

    def setColumnWidth(self, *args):
        print(f"called Table.setColumnWidth with args", args)

    def resizeColumnsToContents(self):
        print("called Table.resizeColumnsToContents")

    def setColumnCount(self, count):
        print(f"called Table.setColumnCount with arg '{count}'")
        self._cols = count

    def setRowCount(self, count):
        print(f"called Table.setRowCount with arg '{count}'")
        self._rows = count

    def rowCount(self):
        print(f"called Table.rowCount")
        return self._rows

    def columnCount(self):
        print(f"called Table.columnCount")
        return self._cols

    def setHorizontalHeaderLabels(self, headerlist):
        print(f"called Table.setHorizontalHeaderLabels with arg '{headerlist}'")
        for item in headerlist:
            self._header.items.append(item)

    def horizontalHeader(self):
        print("called Table.horizontalHeader")
        return self._header

    def verticalHeader(self):
        print("called Table.verticalHeader")
        return self._vhead

    def setTabKeyNavigation(self, value):
        print(f"called Table.setTabKeyNavigation with arg {value}")

    def insertRow(self, rownum):
        print(f"called Table.insertRow with arg '{rownum}'")
        self._rows += 1

    def insertColumn(self, colnum):
        print(f"called Table.insertColumn with arg '{colnum}'")
        self._cols += 1

    def currentColumn(self):
        print("called Table.currentColumn")
        return 1

    def currentRow(self):
        print("called Table.currentRow")
        return 2

    def removeRow(self, rownum):
        print(f"called Table.removeRow with arg '{rownum}'")
        self._rows -= 1

    def removeColumn(self, colnum):
        print(f"called Table.removeColumn with arg '{colnum}'")
        self._cols -= 1

    def setItem(self, x, y, item):
        print(f"called Table.setItem with args ({x}, {y}, item of type {type(item)})")
        self._items[(x, y)] = item

    def item(self, x, y):
        print(f"called Table.item with args ({x}, {y})")
        with contextlib.suppress(KeyError):
            return self._items[(x, y)]
        return None

    def clear(self):
        print("called Table.clear")

    def clearContents(self):
        print("called Table.clearContents")

    def scrollToBottom(self):
        print("called Table.scrollToBottom")

    def setFocus(self):
        print("called Table.setFocus")

    def setCurrentCell(self, *args):
        print("called Table.setCurrentCell with args", args)

    def setGridStyle(self, arg):
        print(f"called Table.setGridStyle with arg {arg}")

    def findItems(self, *args):
        print('called Table.findItems with args', args)
        return []

    def selectedRanges(self):
        print('called Table.selectedRanges')
        return []

    def selectedItems(self):
        print('called Table.selectedItems')
        return []

    def setRowHeight(self, *args):
        print("called Table.setRowHeight with args", args)


class MockFontMetrics:
    def __init__(self, *args):
        print('called Fontmetrics.__init__()')

    def width(self, *args):  # Qt5
        print('called Editor.width()')

    def horizontalAdvance(self, *args):  # Qt6
        print('called Editor.horizontalAdvance()')


class MockLexer:
    def __init__(self, *args):
        print('called Lexer.__init__()')

    def setDefaultFont(self, *args):
        print('called Editor.setDefaultFont')


class MockWebEngineView:
    def __init__(self, *args):
        print('called WebEngineView.__init__()')

    def setHtml(self, *args, **kwargs):
        print('called WebEngineView.setHtml() with args', args, kwargs)


class MockUndoStack:
    cleanChanged = MockSignal()
    indexChanged = MockSignal()

    def __init__(self, *args):
        print("called UndoStack.__init__ with args", args)
        self._parent = args[0]
        self._undolimit = MAXUNDO
    def parent(self):
        return self._parent
    def undoLimit(self):
        print("called UndoRedoStack.undoLimit")
        return self._undolimit
    def setUndoLimit(self, count):
        print(f"called UndoRedoStack.setUndoLimit with arg {count}")
        self._undolimit = count
    def clear(self):
        print("called UndoRedoStack.clear")
    def push(self, arg):
        print(f"called UndoRedoStack.push")
    def undo(self):
        print(f"called UndoRedoStack.undo")
    def redo(self):
        print(f"called UndoRedoStack.redo")


class MockUndoCommand:
    def __init__(self, *args, **kwargs):
        print("called UndoCommand.__init__ with args", args, kwargs)


class MockUrl:
    def __init__(self, *args):
        print('called Url.__init__ with args', args)

    @staticmethod
    def fromLocalFile(arg):
        print(f"called Url.fromLocalFile with arg '{arg}'")
        return arg


class MockPoint:
    def __init__(self, *args):
        print('called Point.__init__ with args', args)


class MockPrintPreviewDialog:
    paintRequested = MockSignal()

    def __init__(self, *args):
        print('called PrintPreviewDialog.__init__ with args', args)

    def exec(self):
        print('called PrintPreviewDialog.exec')

    def done(self, value):
        print(f'called PrintPreviewDialog.done with arg {value}')
