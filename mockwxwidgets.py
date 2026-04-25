"""redefine elements to facilitatie testing
"""
import wx

def mock_messagebox(*args, **kwargs):
    print(f'called wx.MessageBox with args', args, kwargs)


def mock_get_text_from_user(*args, **kwargs):
    print(f'called wx.GetTextFromUser with args', args, kwargs)
    return ''


def mock_get_text_from_user_2(*args, **kwargs):
    print(f'called wx.GetTextFromUser with args', args, kwargs)
    return 'text from user'


def mock_loadfileselector(*args, **kwargs):
    print(f'called wx.LoadFileSelector with args', args, kwargs)
    return 'xxxx'


def mock_savefileselector(*args, **kwargs):
    print(f'called wx.SaveFileSelector with args', args, kwargs)
    return 'xxxx'


class MockApp:
    def __init__(self, *args):
        print('called app.__init__ with args', args)

    def MainLoop(self):  # , *args):
        print('called app.MainLoop')  #  with args', args)

    def SetTopWindow(self, *args):
        print('called app.SetTopWindow with args', args)


class MockControl:
    def __init__(self):  # , *args, **kwargs):
        print('called Control.__init__')  #  with args', args, kwargs)

    def SetFocus(self):  #  , *args, **kwargs):
        print('called Control.SetFocus')  #  with args', args, kwargs)

    def Enable(self, value):  #  , *args, **kwargs):
        print(f'called Control.Enable with arg {value}')  #  with args', args, kwargs)

    def SetLabel(self, *args, **kwargs):
        print('called Control.SetLabel with args', args, kwargs)

    def Destroy(self, *args):
        print('called Control.Destroy with args', args)


class MockFrame:
    def __init__(self, *args, **kwargs):
        print('called frame.__init__ with args', args, kwargs)

    def Show(self, *args):
        if args:
            print('called frame.Show with args', args)
        else:
            print('called frame.Show')

    def Hide(self):
        print('called frame.Hide')

    def Bind(self, *args):
        # bij meer dam twee argumenten zijn die vaak niet in de outputvoorspelling weer te geven,
        # dus maar inslikken
        print('called Frame.Bind with args', args[:2])

    def Connect(self, *args):
        print('called Frame.Connect with args', args)

    def SetIcon(self, *args):
        print('called Frame.SetIcon with args', args)

    def CreateStatusBar(self):
        print('called Frame.CreateStatusBar')
        return MockStatusBar()

    def SetStatusBar(self, *args):
        print('called Frame.GetStatusBar with args', args)

    def GetStatusBar(self):
        print('called Frame.GetStatusBar')
        return MockStatusBar()

    def SetToolBar(self, *args):
        print('called Frame.SetToolBar with args', args)

    def GetToolBar(self, *args):
        print('called Frame.GetToolBar with args', args)
        return MockToolBar()

    def SetMenuBar(self, *args):
        print('called Frame.SetMenuBar with args', args)

    def SetTitle(self, *args):
        print('called Frame.SetTitle with args', args)

    def GetTitle(self, *args):
        print('called Frame.GetTitle with args', args)
        return 'frame title'

    def SetSizer(self, *args):
        print('called Frame.SetSizer with args', args)

    def SetAutoLayout(self, *args):
        print('called Frame.SetAutoLayout with args', args)

    def Layout(self, *args):
        print('called Frame.Layout with args', args)

    def SetSize(self, *args):
        print("called Frame.SetSize with args", args)

    def SetIcon(self, *args):
        print("called Frame.SetIcon with args", args)

    def GetSize(self):
        print("called Frame.GetSize")
        return MockSize(100, 10)

    def SetPosition(self, *args):
        print("called Frame.SetPosition with args", args)

    def GetPosition(self):
        print("called Frame.GetPosition")
        return MockPoint(1, 2)

    def SetAcceleratorTable(self, *args):
        print('called Frame.SetAcceleratorTable')  #  with args', args)

    def Destroy(self, *args):
        print('called Frame.Destroy with args', args)

    def Close(self, value=False):
        print(f'called Frame.Close with arg {value}')


class MockPanel:
    def __init__(self, *args, **kwargs):
        print('called Panel.__init__ with args', args, kwargs)

    def Layout(self, *args):
        print('called Panel.Layout with args', args)

    def SetSizer(self, *args):
        print('called Panel.SetSizer with args', args)

    def SetAutoLayout(self, *args):
        print('called Panel.SetAutoLayout with args', args)

    def Show(self, *args):
        if args:
            print('called Panel.Show with args', args)
        else:
            print('called Panel.Show')

    def Bind(self, *args):
        # bij meer dam twee argumenten zijn die vaak niet in de outputvoorspelling weer te geven,
        # dus maar inslikken
        print('called Panel.Bind with args', args[:2])

    def Destroy(self, *args):
        print('called Panel.Destroy with args', args)


class MockScrolledPanel:
    def __init__(self, *args, **kwargs):
        print('called ScrolledPanel.__init__ with args', args, kwargs)

    def Layout(self, *args):
        print('called ScrolledPanel.Layout with args', args)

    def SetSizer(self, *args):
        print('called ScrolledPanel.SetSizer with args', args)

    def Fit(self, *args):
        print('called ScrolledPanel.Fit with args', args)

    def SetAutoLayout(self, *args):
        print('called ScrolledPanel.SetAutoLayout with args', args)

    def SetupScrolling(self):
        print('called ScrolledPanel.SetupScrolling')

    def ScrollChildIntoView(self, child):
        print(f'called ScrolledPanel.ScrollChildIntoView with arg {child}')

    def Show(self, *args):
        if args:
            print('called ScrolledPanel.Show with args', args)
        else:
            print('called ScrolledPanel.Show')

    def Destroy(self, *args):
        print('called ScrolledPanel.Destroy with args', args)


class MockPoint:
    def __init__(self, *args):
        print('called Point.__init__ with args', args)
        self.x = args[0]
        self.y = args[1]

    def __iter__(self):
        return iter([self.x, self.y])


class MockSize:
    def __init__(self, *args):
        print('called Size.__init__ with args', args)
        self.x = args[0]
        self.y = args[1]

    def __iter__(self):
        return iter([self.x, self.y])

    def GetWidth(self):
        print('called Size.GetWidth')
        return self.x

    def GetHeight(self):
        print('called Size.GetHeight')
        return self.y


class MockBitmap:
    def __init__(self, *args):
        print('called Bitmap.__init__ with args', args)
        self._fname = args[0] if len(args) > 0 else ''
    def __repr__(self):
        return f"Bitmap created from '{self._fname}'"


class MockIcon:
    def __init__(self, *args):
        print('called Icon.__init__ with args', args)
        self._fname = args[0] if len(args) > 0 else ''
    def __repr__(self):
        return f"Icon created from '{self._fname}'"


class MockTaskBarIcon:
    def __init__(self, *args):
        print('called TaskBarIcon.__init__ with args', args)


class MockMenuBar:
    def __init__(self, *args):
        print('called MenuBar.__init__ with args', args)

    def __repr__(self):
        return 'A MenuBar'

    def GetMenus(self):
        print('called menubar.GetMenus')
        return [(MockMenu(), 'label1'), (MockMenu(), 'label2')]

    def GetMenu(self, *args):
        print('called menubar.GetMenus with args', args)
        return MockMenu()

    def Append(self, *args):
        print('called menubar.Append with args', args)

    def Replace(self, *args):
        print('called menubar.Replace with args', args)

    def EnableTop(self, *args):
        print('called menubar.EnableTop with args', args)


class MockMenu:
    def __init__(self, *args):
        print('called Menu.__init__ with args', args)

    def __repr__(self):
        return 'A Menu'

    def AppendSeparator(self, *args):
        print('called menu.AppendSeparator with args', args)

    def Append(self, *args):
        if isinstance(args[0], (str, int)):
            print('called menu.Append with args', args)
        else:
            print('called menu.Append with args', type(args[0]).__name__)

    def AppendSubMenu(self, *args):
        print('called menu.AppendSubMenu with args', args)

    def Destroy(self):  # , *args):
        print('called menu.Destroy')  #  with args', args)

    def Delete(self, *args):
        print('called menu.Delete with args', args)

    def Enable(self, *args):
        print(f'called menu.Enable with args', args)

    def SetLabel(self, *args):
        print(f"called menu.SetLabel with args", args)

    def SetTitle(self, arg):
        print(f"called menu.SetTitle with arg '{arg}'")

    def GetTitle(self):
        print('called menu.GetTitle')
        return 'xxx'

    def GetMenuItems(self):
        print('called menu.GetMenuItems')
        return []

    def GetParent(self):
        print('called menu.GetParent')


class MockMenuItem:
    def __init__(self, *args, **kwargs):
        print('called MenuItem.__init__ with args', args, kwargs)

    def GetId(self):  # , *args):
        print('called menuitem.GetId')  #  with args', args)
        return 'NewID'

    # def Bind(self, *args):
    #     print('called menuitem.Bind with args', args)

    def SetBitmap(self, *args):
        print('called menuitem.SetBitmap with args', args)

    def Check(self, value):
        print(f'called menuitem.Check with arg {value}')

    def IsChecked(self):
        print(f'called menuitem.IsChecked')
        return 'value'

    def IsSubMenu(self):
        print(f'called menuitem.IsSubMenu')
        return False

    def Enable(self, value):
        print(f'called menuitem.Enable with arg {value}')

    def GetItemLabelText(self):
        print('called menuitem.GetItemLabelText')

    def SetItemLabel(self, arg):
        print(f"called menuitem.SetItemLabel with arg '{arg}'")

    def SetHelp(self, arg):
        print(f"called menuitem.SetHelp with arg '{arg}'")


class MockToolBar:
    def __init__(self, *args):
        print('called ToolBar.__init__ with args', args)

    def __repr__(self):
        return 'A ToolBar'

    def GetMenus(self, *args):
        print('called menubar.GetMenus with args', args)
        return [(MockMenu(), 'label1'), (MockMenu(), 'label2')]

    def AddSeparator(self, *args):
        print('called Toolbar.AddSeparator with args', args)

    def AddTool(self, *args, **kwargs):
        print('called Toolbar.AddTool with args', args, kwargs)

    def AddCheckTool(self, *args, **kwargs):
        print('called Toolbar.AddCheckTool with args', args, kwargs)

    def AddControl(self, *args):
        print('called Toolbar.AddControl with args', args)

    def Replace(self, *args):
        print('called Toolbar.Replace with args', args)

    def SetToolBitmapSize(self, *args):
        print('called Toolbar.SetToolBitmapSize with args', args)

    def Realize(self, *args):
        print('called Toolbar.Realize with args', args)


class MockSplitter:
    def __init__(self, *args, **kwargs):
        print('called Splitter.__init__ with args', args, kwargs)

    def SetMinimumPaneSize(self, *args):
        print('called splitter.SetMinimumPaneSize with args', args)

    def SplitVertically(self, *args):
        print('called splitter.SplitVertically with args', args)

    def SplitHorizontally(self, *args):
        print('called splitter.SplitHorizontally with args', args)

    def SetSashPosition(self, *args):
        print('called splitter.SetSashPosition with args', args)
        check = int(args[0])  # force TypeError on wrong first argument

    def GetSashPosition(self):  # , *args):
        print('called splitter.SetSashPosition')
        return 55


class MockNoteBook:
    def __init__(self, *args, **kwargs):
        print('called NoteBook.__init__ with args', args, kwargs)

    def Bind(self, *args):
        print('called NoteBook.Bind with args', args)

    def GetPageCount(self, *args):
        print('called NoteBook.GetPageCount with args', args)
        return 'pagecount'

    def GetPage(self, *args):
        print('called NoteBook.GetPage with args', args)
        return 'page'

    def GetCurrentPage(self):
        print('called NoteBook.GetCurrentPage')
        return 'page'

    def GetSelection(self, *args):
        print('called NoteBook.GetSelection with args', args)
        return 'selection'

    def SetSelection(self, *args):
        print('called NoteBook.SetSelection with args', args)

    def AdvanceSelection(self, *args):
        print('called NoteBook.AdvanceSelection with args', args)

    def DeleteAllPages(self, *args):
        print('called NoteBook.DeleteAllPages with args', args)

    def DeletePage(self, *args):
        print('called NoteBook.DeletePage with args', args)

    def AddPage(self, *args):
        print('called NoteBook.AddPage with args', args)

    def RemovePage(self, *args):
        print('called NoteBook.RemovePage with args', args)

    def InsertPage(self, *args):
        print('called NoteBook.InsertPage with args', args)

    def SetPageText(self, *args):
        print('called NoteBook.SetPageText with args', args)

    def GetPageText(self, *args):
        print('called NoteBook.GetPageText with args', args)
        return 'title'

    def HitTest(self, *args):
        print('called NoteBook.HitTest with args', args)
        return 'itemno', -1


class MockTree:
    def __init__(self, *args, **kwargs):
        print('called Tree.__init__ with args', args, kwargs)

    def AddRoot(self, *args):
        print('called tree.AddRoot with args', args)
        return 'The Root'

    def GetRootItem(self):
        print('called tree.GetRootItem')
        return 'rootitem'

    def AddColumn(self, *args):
        print('called tree.AddColumn with args', args)

    def SetMainColumn(self, *args):
        print('called tree.SetMainColumn with args', args)

    def SetColumnWidth(self, *args):
        print('called tree.SetColumnWidth with args', args)

    def DeleteAllItems(self):
        print('called tree.DeleteAllItems')

    def ItemHasChildren(self, *args):
        print('called tree.ItemHasChildren with args', args)
        return False

    def ExpandAllChildren(self, *args):
        print('called tree.ExpandAllChildren with args', args)

    def CollapseAllChildren(self, *args):
        print('called tree.CollapseAllChildren with args', args)

    def Bind(self, *args):
        # print('called tree.Bind() for method', str(args[1]).split()[2])
        print('called tree.Bind with args', args)

    def SetAcceleratorTable(self, *args):
        print('called tree.SetAcceleratorTable')  #  with args', args)

    def Expand(self, *args):
        print('called tree.Expand with args', args)

    def Collapse(self, *args):
        print('called tree.Collapse with args', args)

    def IsCollapsed(self, *args):
        print('called tree.IsCollapsed with args', args)
        return False

    def IsExpanded(self, *args):
        print('called tree.IsExpanded with args', args)
        return False

    def SetItemBold(self, *args):
        # print(f'called tree.SetItemBold() using {args[1]}')
        print(f'called tree.SetItemBold with args', args)

    def SetFocus(self):
        print('called tree.SetFocus')

    def HitTest(self, *args):
        print('called tree.HitTest with args', args)
        return None, 0

    def SelectItem(self, *args):
        print('called tree.SelectItem with args', args)
        # return 'selected_item'

    def GetSelection(self):
        print('called tree.GetSelection')  #  with args', args)
        return 'selection'

    def SetFocusedItem(self, *args):
        print('called tree.SetFocusedItem with args', args)
        # return 'focused_item'

    def GetFocusedItem(self):
        print('called tree.GetFocusedItem')  #  with args', args)
        return 'focused item'

    def GetItemText(self, *args):
        print('called tree.GetItemText with args', args)
        return 'itemtext'

    def SetItemText(self, *args):
        print('called tree.SetItemText with args', args)

    def SetItemTextColour(self, *args):
        print('called tree.SetItemTextColour with args', args)

    def GetItemParent(self, *args):
        print('called tree.GetItemParent with args', args)
        return 'parent'

    def GetItemData(self, *args):
        print('called tree.GetItemData with args', args)
        return 'itemdata'

    def SetItemData(self, *args):
        print(f'called tree.SetItemData() with args', args)

    def GetNextSibling(self, *args):
        print('called tree.GetNextSibling')  #  with args', args)
        return MockTreeItem('next treeitem')

    def GetPrevSibling(self, *args):
        print('called tree.GetPrevSibling')  #  with args', args)
        return MockTreeItem('previous treeitem')

    def AppendItem(self, *args):
        print('called tree.AppendItem with args', args)
        return 'appended item'

    def PrependItem(self, *args):
        print('called tree.PrependItem with args', args)
        return 'prepended item'

    def InsertItem(self, *args):
        print('called tree.InsertItem with args', args)
        return 'inserted item'

    def Delete(self, *args):
        print('called tree.Delete with args', args)

    def GetChildrenCount(self, *args):
        print('called Tree.GetChildrenCount with args', args)
        return 0

    def GetFirstChild(self, *args):
        print('called tree.GetFirstChild with args', args)
        return MockTreeItem('first'), 0

    def GetNextChild(self, *args):
        cookie = args[1]
        print('called tree.GetNextChild with args', args)
        if cookie == 0:
            return MockTreeItem('next'), 1
        return MockTreeItem('not ok'), -1

    def GetLastChild(self, *args):
        print('called tree.GetLastChild with args', args)
        return MockTreeItem('last')

    def SortChildren(self, *args):
        print('called tree.SortChildren with args', args)

    def EnsureVisible(self, *args):
        print('called tree.EnsureVisible with args', args)


class MockTreeItem:
    def __init__(self, *args):
        print('called TreeItem.__init__ with args', args)
        self.tag = args[0]

    def __repr__(self):
        return self.tag

    def IsOk(self):
        print('called TreeItem.IsOk')
        return self.tag != 'not ok'


class MockFont:
    def __init__(self, *args):
        print('called Font.__init__ with args', args)

    def SetFamily(self, *args):
        print('called font.SetFamily with args', args)

    def SetPointSize(self, *args):
        print('called font.SetPointSize with args', args)


class MockEditor:   # actually a StyledTextCtrl
    def __init__(self, *args, **kwargs):
        print('called Editor.__init__ with args', args, kwargs)
        self.IsModified = 'ismodified'

    def Clear(self):
        print('called editor.Clear')

    def Undo(self):
        print('called editor.Undo')

    def Redo(self):
        print('called editor.Redo')

    def Cut(self):
        print('called editor.Cut')

    def Copy(self):
        print('called editor.Copy')

    def Paste(self):
        print('called editor.Paste')

    def SelectAll(self):
        print('called editor.SelectAll')

    def Enable(self, *args):
        print(f'called editor.Enable with args', args)

    def Bind(self, *args):
        print('called editor.Bind with args', args)

    def SetWrapMode(self, *args):
        print('called editor.SetWrapMode with args', args)

    def SetCaretLineVisible(self, *args):
        print('called editor.SetCaretLineVisible with args', args)

    def SetCaretLineBackground(self, *args):
        print('called editor.SetCaretLineBackground with args', args)

    def SetLexer(self, *args):
        print('called editor.SetLexer with args', args)

    def SetStyle(self, *args):
        print('called editor.SetStyle with args', args)

    def BeginStyle(self, *args):
        print('called editor.BeginStyle with args', args)

    def BeginFont(self, *args):
        print('called editor.BeginFont with args', args)

    def BeginTextColour(self, *args):
        print('called editor.BeginTextColour with args', args)

    def StyleSetForeground(self, *args):
        print('called editor.StyleSetForeground with args', args)

    def StyleSetBackground(self, *args):
        print('called editor.StyleSetBackground with args', args)

    def StyleSetBold(self, *args):
        print('called editor.StyleSetBold with args', args)

    def StyleSetItalic(self, *args):
        print('called editor.StyleSetItalic with args', args)

    def StyleSetUnderline(self, *args):
        print('called editor.StyleSetUnderline with args', args)

    def SetValue(self, value):
        print(f'called editor.SetValue with arg `{value}`')

    def SetText(self, value):
        print(f'called editor.SetText with arg `{value}`')

    def SetReadOnly(self, value):
        print(f'called editor.SetReadOnly with arg `{value}`')

    def GetValue(self):
        print('called editor.GetValue')
        return 'fake editor value'

    def SetFocus(self):
        print('called editor.SetFocus')

    def SetInsertionPoint(self, *args):
        print('called editor.SetInsertionPoint with args', args)

    def GetInsertionPoint(self):
        print('called editor.GetInsertionPoint')
        return 'insert here'

    def GetSelectionRange(self, *args):
        print('called editor.GetSelectionRange with args', args)
        return 'range'

    def ScrollIntoView(self, *args):
        print('called editor.ScrollIntoView with args', args)


class MockTrayIcon:
    def __init__(self, *args):
        print('called TrayIcon.__init__ with args', args)

    def SetIcon(self, *args, **kwargs):
        print('called trayicon.SetIcon with args', args, kwargs)

    def Bind(self, *args, **kwargs):
        print('called trayicon.Bind with args', args, kwargs)

    def Destroy(self):  # , *args):
        print('called trayicon.Destroy')  #  with args', args)


class MockAcceleratorEntry:
    def __init__(self, *args, **kwargs):
        print('called AcceleratorEntry.__init__ with args', args, kwargs)

    def FromString(self, *args):
        print('called AcceleratorEntry.FromString with args', args)
        return True


class MockAcceleratorTable:
    def __init__(self, *args):
        count = len(args[0])
        print(f'called AcceleratorTable.__init__ with {count} AcceleratorEntries')  # args', args)


class MockEvent:
    def __init__(self, *args):
        print('called event.__init__ with args', args)

    def GetString(self):
        print('called event.GetString')
        return 'qqq'

    def GetItem(self):
        print('called event.GetItem')
        return 'treeitem'

    def GetSelection(self):
        print('called event.GetSelection')
        return 'index'

    def GetPosition(self):
        print('called event.GetPosition')
        return 'position'

    def GetX(self):
        print('called event.GetX')
        return 'x'

    def GetY(self):
        print('called event.GetY')
        return 'y'

    def GetEventWidget(self):
        print('called event.GetEventWidget')

    def GetEventObject(self):
        print('called event.GetEventObject')

    def Skip(self):
        print('called event.Skip')

    def Veto(self):
        print('called event.Veto')

    def Check(self, *args):
        print('called event.Check with args', args)


class MockStatusBar:
    def __init__(self, *args):
        print('called StatusBar.__init__ with args', args)
    def SetStatusText(self, *args):
        print(f'called statusbar.SetStatusText with args', args)
    def SetFieldsCount(self, *args):
        print(f'called statusbar.SetFieldsCount with args', args)


class MockBoxSizer:
    def __init__(self, *args, **kwargs):
        self.orient = ('vert' if args and args[0] == wx.VERTICAL else
                       'hori' if args and args[0] == wx.HORIZONTAL else '')
        print(f'called BoxSizer.__init__ with args', args)

    def __repr__(self):
        return f'{self.orient} sizer'

    def Add(self, *args):
        if isinstance(args[0], str):
            print(f'called {self.orient} sizer.Add with args', args)
        else:
            print(f'called {self.orient} sizer.Add with args {type(args[0]).__name__}', args[1:])

    def Insert(self, *args):
        print(f'called BoxSizer.Insert with args', args)

    def Remove(self, *args):
        print(f'called BoxSizer.Remove with args', args)

    def AddSpacer(self, *args):
        print(f'called {self.orient} sizer.AddSpacer with args', args)

    def AddStretchSpacer(self):  # , *args):
        print(f'called {self.orient} sizer.AddStretchSpacer')  #  with args', args)

    def Fit(self , *args):
        print(f'called {self.orient} sizer.Fit with args', args)

    def Layout(self , *args):
        print(f'called {self.orient} sizer.Layout with args', args)

    def SetSizeHints(self, *args):
        print(f'called {self.orient} sizer.SetSizeHints with args', args)


class MockGridSizer:
    def __init__(self, *args, **kwargs):
        print('called GridSizer.__init__ with args', args, kwargs)

    def Add(self, *args, **kwargs):
        if kwargs:
            print(f'called GridSizer.Add with args {type(args[0]).__name__}', args[1:], kwargs)
        else:
            print(f'called GridSizer.Add with args {type(args[0]).__name__}', args[1:])

    def AddGrowableCol(self, *args):
        print(f'called GridSizer.AddGrowableCol with args', args)

    def GetCols(self):
        print('called GridSizer.Cols')
        return 'cols'


class MockFlexGridSizer:
    def __init__(self, *args, **kwargs):
        print('called FlexGridSizer.__init__ with args', args, kwargs)

    def Add(self, *args):
        if isinstance(args[0], str):
            print(f'called FlexGridSizer.Add with args', args)
        else:
            print(f'called FlexGridSizer.Add with args {type(args[0]).__name__}', args[1:])

    def AddMany(self, *args):
        arrgs = ""
        for arg in args[0]:
            if isinstance(arg[0], str):
                arrgs += f'{arg}, '
            else:
                arrgs += f'{type(arg[0]).__name__}, {arg[1:]}, '
        print(f'called FlexGridSizer.AddMany with args', arrgs.removesuffix(', '))


class MockStaticLine:
    def __init__(self, *args, **kwargs):
        print('called StaticLine.__init__ with args', args, kwargs)


class MockStaticBox:
    def __init__(self, *args, **kwargs):
        print('called StaticBox.__init__ with args', args, kwargs)


# class MockStaticBoxSizer:
#     def __init__(self, *args, **kwargs):
#         print('called StaticBoxSizer.__init__ with args', args, kwargs)


class MockStaticText:
    def __init__(self, *args, **kwargs):
        print('called StaticText.__init__ with args', args, kwargs)

    def SetLabel(self, *args, **kwargs):
        print('called StaticText.SetLabel with args', args, kwargs)


class MockCheckBox:
    def __init__(self, *args, **kwargs):
        print('called CheckBox.__init__ with args', args, kwargs)
        self._checked = None

    def SetValue(self, *args):
        print(f'called checkbox.SetValue with args', args)
        self._checked = args[0]

    def GetValue(self):
        print(f'called checkbox.GetValue')
        return self._checked if self._checked is not None else 'value from checkbox'

    def Check(self, value):
        print(f'called checkbox.Check with arg {value}')

    def IsChecked(self):
        print('called checkbox.IsChecked')
        return self._checked if self._checked is not None else 'value from checkbox'

    def Bind(self, *args, **kwargs):
        print('called CheckBox.Bind with args', args, kwargs)

    def GetId(self):  # , *args, **kwargs):
        print('called CheckBox.GetId')  #  with args', args, kwargs)
        return 'id'

    def Enable(self, state):
        print(f'called CheckBox.Enable with arg {state}')

    def Clear(self):
        print('called CheckBox.Clear')

    def Destroy(self, *args):
        print('called CheckBox.Destroy with args', args)


class MockCheckListBox:
    def __init__(self, *args, **kwargs):
        print('called CheckListBox.__init__ with args', args, kwargs)

    def GetItems(self):
        print(f'called CheckListBox.GetItems')
        return ['item', 'list']

    def Check(self, *args):
        print('called CheckListBox.Check with args', args)

    def IsChecked(self, arg):
        print(f'called CheckListBox.IsChecked with arg {arg}')
        return True

    def GetCheckedStrings(self):
        print('called CheckListBox.GetCheckedStrings')
        return 'checked', 'strings'

    def SetSelection(self, *args):
        print('called CheckListBox.SetSelection with args', args)

    def GetCount(self, *args):
        print('called CheckListBox.GetCount')
        return 2


class MockTextCtrl:
    def __init__(self, *args, **kwargs):
        value = kwargs.get('value', '')
        if value:
            value = f'`{value}`'
        print(f'called TextCtrl.__init__ with args', args, kwargs)

    def Bind(self, *args):
        print('called TextCtrl.Bind with args', args)

    def Clear(self):  # , *args):
        print('called text.Clear')  #  with args', args)

    def SetValue(self, *args):
        print(f'called text.SetValue with args', args)

    def GetValue(self):
        print('called text.GetValue')
        return 'value from textctrl'

    def Enable(self, value):
        print(f'called text.Enable with arg {value}')

    def SetEditable(self, value):
        print(f'called text.SetEditable with arg {value}')

    def IsModified(self):
        print(f'called text.IsModified')
        return 'modified'

    def SetModified(self, value):
        print(f'called text.SetModified with arg {value}')

    def Refresh(self):
        print('called text.Refresh')

    def MoveEnd(self):
        print('called text.MoveEnd')

    def GetBuffer(self):
        print('called text.GetBuffer')
        return MockBuffer()

    def GetInsertionPoint(self):
        print('called text.GetInsertionPoint')
        return 'insertion point'
    def GetStyle(self, *args):
        print('called text.GetStyle with args', args)
        return False
    def SetStyle(self, *args):
        print('called text.SetStyle')
    def SetFocus(self):
        print('called text.SetFocus')
    def HasFocus(self):
        print('called text.HasFocus')
        return False
    def HasSelection(self):
        print('called text.HasSelection')
        return False
    def GetSelectionRange(self):
        print('called text.GetSelectionRange')
        return 'selectionrange'


class MockBuffer:
    "stub for RichTextBuffer"
    def __init__(self):
        print('called RichTextBuffer.__init__')
    def AddHandler(self, *args):
        print('called RichTextBuffer.AddHandler with args', args)


class MockHandler:
    "stub for RichTextXMLHandler"
    def __init__(self):
        print('called RichTextXMLHandler.__init__')
    def LoadFile(self, *args):
        print('called RichTextXMLHandler.LoadFile with args', args)
    def SaveFile(self, *args):
        print('called RichTextXMLHandler.SaveFile with args', args)


class MockTextAttr:
    "stub for RichTextAttr"
    def __init__(self):
        print('called RichTextAttr.__init__')
    def __repr__(self):
        return 'richtextattr'
    def SetFlags(self, *args):
        print('called RichTextAttr.SetFlags with args', args)
    def SetLeftIndent(self, *args):
        print('called RichTextAttr.SetLeftIndent with args', args)
    def GetLeftIndent(self):
        print('called RichTextAttr.GetLeftIndent')
        return 'leftindent'
    def SetFont(self, *args):
        print('called RichTextAttr.SetFont with args', args)
    def SetTextColour(self, *args):
        print('called RichTextAttr.SetTextColour with args', args)
    def SetBackgroundColour(self, *args):
        print('called RichTextAttr.SetBackgroundColour with args', args)
    def GetFont(self, *args):
        print('called RichTextAttr.GetFont')
        return 'Font'
    def SetLineSpacing(self, *args):
        print('called RichTextAttr.SetLineSpacing with args', args)
    def GetParagraphSpacingAfter(self):
        print('called RichTextAttr.GetParagraphSpacingAfter')
        return 100
    def SetParagraphSpacingAfter(self, *args):
        print('called RichTextAttr.SetParagraphSpacingAfter with args', args)


class MockTextRange:
    "stub for RichTextRange"
    def __init__(self, *args):
        print('called RichTextRange.__init__ with args', args)
    def __repr__(self):
        return 'richtextrange'


class MockFontData:
    def __init__(self):
        print('called FontData.__init__')
    def EnableEffects(self, value):
        print(f'called FontData.EnableEffects with arg {value}')
    def SetInitialFont(self, *args):
        print('called FontData.SetInitialFont with args', args)
    def GetChosenFont(self):
        print('called FontData.GetChosenFont')
        return ''


class MockButton:
    def __init__(self, *args, **kwargs):
        print('called Button.__init__ with args', args, kwargs)
        self._label = kwargs.get('label', '')

    def Bind(self, *args, **kwargs):
        print('called Button.Bind with args', args, kwargs)

    def Enable(self, state):
        print(f'called Button.Enable with arg {state}')

    def IsEnabled(self):
        print('called Button.IsEnabled')
        return False

    def GetId(self):  # , *args, **kwargs):
        print('called Button.GetId')  #  with args', args, kwargs)
        return 'id'

    def GetLabel(self):
        print('called Button.GetLabel')
        return self._label

    def SetLabel(self, text):
        print(f"called Button.SetLabel with arg '{text}'")
        self._label = text

    def SetHelpText(self, value):
        print(f"called Button.SetHelpText with arg '{value}'")

    def Show(self):
        print('called Button.Show')

    def Hide(self):
        print('called Button.Hide')


class MockRadioButton:
    def __init__(self, *args, **kwargs):
        print('called RadioButton.__init__ with args', args, kwargs)

    def SetValue(self, *args):
        print(f'called radiobutton.SetValue with args', args)

    def GetValue(self):  # , *args):
        print(f'called radiobutton.GetValue')  #  with args', args)
        return 'value from radiobutton'


class MockComboBox:
    def __init__(self, *args, **kwargs):
        sellist = kwargs.get('choices', '')
        if sellist:
            sellist = f' with arg `{sellist}`'
        print(f'called ComboBox.__init__ with args', args, kwargs)

    def Enable(self, value):
        print(f'called combobox.Enable with arg {value}')

    def Clear(self):  # , *args):
        print('called combobox.clear')  #  with args', args)

    def Bind(self, *args, **kwargs):
        print('called ComboBox.Bind with args', args, kwargs)

    def Append(self, *args):
        print('called combobox.Append with args' ,args)

    def AppendItems(self, *args):
        print('called combobox.AppendItems with args' ,args)

    def GetSelection(self):
        print('called combobox.GetSelection')
        return 'selection'

    def GetStringSelection(self):
        print('called combobox.GetStringSelection')
        return 'current text'

    def SetSelection(self, *args):
        print('called combobox.SetSelection with args', args)

    def SetStringSelection(self, *args):
        print('called combobox.SetStringSelection with args', args)

    def GetString(self, *args):
        print('called combobox.GetString with args', args)
        return f'str{args[0]}'

    def SetValue(self, *args):
        print('called combobox.SetValue with args', args)

    def GetClientData(self, *args):
        print('called combobox.GetClientData with args', args)
        return args[0]

    def GetValue(self):  # , *args):
        print('called combobox.GetValue')  #  with args', args)
        return 'value from combobox'

    def GetItems(self):  # , *args):
        print('called combobox.GetItems')  #  with args', args)
        return []

    def AutoComplete(self, *args):
        print(f'called combobox.AutoComplete with args', args)


class MockSpinCtrl:
    def __init__(self, *args, **kwargs):
        print('called SpinCtrl.__init__ with args', args, kwargs)

    def Bind(self, *args):
        print('called SpinCtrl.bind with args', args)

    def SetFocus(self):  # , *args):
        print('called SpinCtrl.SetFocus')  #  with args', args)

    def GetValue(self):  # , *args):
        print(f'called SpinCtrl.GetValue')  #  with args', args)
        if hasattr(self, '_value'):
            return self._value
        return 'value from spinctrl'

    def SetValue(self, *args):
        print(f'called SpinCtrl.SetValue with args', args)
        self._value = args[0]

    def SetMax(self, *args):
        print(f'called SpinCtrl.SetMax with args', args)

    def SetRange(self, *args):
        print(f'called SpinCtrl.SetRange with args', args)


class MockListBox:
    def __init__(self, *args, **kwargs):
        print('called ListBox.__init__ with args', args, kwargs)

    def Bind(self, *args):
        print('called listbox.bind with args', args)

    def SetFocus(self):  # , *args):
        print('called listbox.SetFocus')  #  with args', args)

    def Append(self, *args):
        print(f'called listbox.Append with args', args)

    def SetSelection(self, *args):
        print(f'called listbox.SetSelection with args', args)

    def GetSelection(self):
        print(f'called listbox.GetSelection')
        return 1

    def GetSelections(self):
        print(f'called listbox.GetSelections')
        return [1]

    def GetString(self, *args):
        return f'value {args[0]} from listbox'

    def GetItems(self, *args):
        return ['items from listbox']

    def Delete(self, *args):
        print(f'called listbox.Delete with args', args)

    def Insert(self, *args):
        print(f'called listbox.Insert with args', args)

    def InsertItem(self, *args):
        print('called ListBox.InsertItem with args', args)

    def InsertItems(self, *args):
        print('called ListBox.InsertItems with args', args)

    def GetCount(self):
        print('called listbox.GetCount')


class MockListItem:
    def __init__(self, text=''):
        self._itemtext = text
    def __repr__(self):
        return self._itemtext
    def GetId(self):
        print('called item.GetId')
        return 'id'
    def GetText(self):
        print('called item.GetText')
        return self._itemtext
    def SetText(self, arg):
        print(f"called item.SetText with arg '{arg}'")
        self._itemtext = arg
    def SetWidth(self, arg):
        print(f"called item.SetWidth with arg {arg}")
    def GetData(self):
        print('called item.GetData')
        return 'itemdata'


class MockListCtrl:
    def __init__(self, *args, **kwargs):
        print('called ListCtrl.__init__ with args', args, kwargs)
        self._nextitemcounter = 0

    def Bind(self, *args):
        print('called ListCtrl.Bind with args', args)

    def Unbind(self, *args):
        print('called ListCtrl.Unbind with args', args)

    def AppendColumn(self, *args):
        print('called ListCtrl.AppendColumn with args', args)

    def InsertColumn(self, *args):
        print('called ListCtrl.InsertColumn with args', args)

    def DeleteColumn(self, *args):
        print('called ListCtrl.DeleteColumn with args', args)

    def SetColumnWidth(self, *args):
        print('called ListCtrl.SetColumnWidth with args', args)

    def resizeLastColumn(*args):
        # eigenlijk een methode van een mixin die we hierbij altijd gebruiken, daarom geen self
        if isinstance(args[0], MockListCtrl):
            args = args[1:]
        print('called ListCtrl.resizeLastColumn with args', args)

    def SetColumn(self, *args):
        print('called ListCtrl.SetColumn with args', args)

    def GetColumn(self, *args):
        print('called ListCtrl.GetColumn with args', args)
        return MockListItem()

    def EnsureVisible(self, *args):
        print('called ListCtrl.EnsureVisible with args', args)

    def Append(self, *args):
        print('called ListCtrl.Append with args', args)
        return 'itemindex'

    def InsertItem(self, *args):
        print('called ListCtrl.InsertItem with args', args)
        return 'itemindex'

    def SetItem(self, *args):
        print('called ListCtrl.SetItem with args', args)

    def GetItem(self, *args):
        print('called ListCtrl.GetItem with args', args)
        return MockListItem(f'item {args[0]}')

    def SetItemData(self, *args):
        print('called ListCtrl.SetItemData with args', args)

    def GetItemData(self, *args):
        print('called ListCtrl.GetItemData with args', args)
        return args[0]

    def SetItemText(self, *args):
        print('called ListCtrl.SetItemText with args', args)

    def GetItemText(self, *args):
        print('called ListCtrl.GetItemText with args', args)
        return args[0]

    def GetItemCount(self):
        print('called ListCtrl.GetItemCount')
        return 2

    def DeleteAllItems(self):
        print('called ListCtrl.DeleteAllItems')

    def RefreshRows(self):
        print('called ListCtrl.RefreshRows')

    def Select(self, *args):
        print('called ListCtrl.Select with args', args)

    def GetFirstSelected(self):
        print('called ListCtrl.GetFirstSelected')
        return -1

    def GetFirstSelected_2(self):
        print('called ListCtrl.GetFirstSelected')
        return 0

    def GetNextSelected(self, item):
        print('called ListCtrl.GetNextSelected')
        self._nextitemcounter += 1
        if self._nextitemcounter == 1:
            return self._nextitemcounter
        return -1

    def SetImageList(self, *args):
        print('called ListCtrl.SetImageList with args', args)

    def SortListItems(self, *args):
        print('called ListCtrl.SortListItems with args', args)


class MockListCtrlAutoWidthMixin:
    def __init__(self, *args, **kwargs):
        print('called ListCtrlAutoWidthMixin.__init__ with args', args, kwargs)


class MockEditableListBox:
    def __init__(self, *args, **kwargs):
        print('called EditableListBox.__init__ with args', args, kwargs)

    def SetStrings(self, *args):
        print('called EditableListBox.SetStrings with args', args)

    def GetStrings(self):
        print('called EditableListBox.GetStrings')
        return ['strings', 'from', 'elb']


class MockColumnSorterMixin:
    def __init__(self, *args, **kwargs):
        print('called ColumnSorterMixin.__init__ with args', args, kwargs)

    def SortListItems(self, *args):
        print('called ColumnSorterMixin.SortListItems with args', args)


class MockListRowHighlighter:
    def __init__(self, *args, **kwargs):
        print('called ListRowHighlighter.__init__ with args', args, kwargs)


class MockGrid:
    def __init__(self, *args, **kwargs):
        print('called Grid.__init__ with args', args, kwargs)

    def CreateGrid(self, *args):
        print('called Grid.CreateGrid with args', args)

    def Bind(self, *args):
        print('called Grid.Bind with args', args)

    def SetRowLabelSize(self, *args):
        print('called Grid.SetRowLabelSize with args', args)

    def SetRowLabelValue(self, *args):
        print('called Grid.SetRowLabelValue with args', args)

    def SetColLabelValue(self, *args):
        print('called Grid.SetColLabelValue with args', args)

    def SetColLabelSize(self, *args):
        print('called Grid.SetColLabelSize with args', args)

    def SetColSize(self, *args):
        print('called Grid.SetColSize with args', args)

    def SetReadOnly(self, *args):
        print('called Grid.SetReadOnly with args', args)

    def SetCellTextColour(self, *args):
        print('called Grid.SetCellTextColour with args', args)

    def SetCellValue(self, *args):
        print('called Grid.SetCellValue with args', args)

    def GetCellValue(self, *args):
        print('called Grid.GetCellValue with args', args)
        return f'value at {args}'

    def SelectBlock(self, *args):
        print('called Grid.SelectBlock with args', args)

    def AppendRows(self, *args):
        print('called Grid.AppendRows with args', args)

    def DeleteRows(self, *args):
        print('called Grid.DeleteRows with args', args)

    def InsertCols(self, *args):
        print('called Grid.InsertCols with args', args)

    def DeleteCols(self, *args):
        print('called Grid.DeleteCols with args', args)

    def ShowRow(self, *args):
        print('called Grid.ShowRow with args', args)

    def GoToCell(self, *args):
        print('called Grid.GoToCell with args', args)

    def GetSelectedRows(self):
        print('called Grid.GetSelectedRows')
        return []

    def GetNumberRows(self, *args):
        print('called Grid.GetNumberRows with args', args)
        return 0

    def GetNumberCols(self, *args):
        print('called Grid.GetNumberCols with args', args)
        return 0


class MockDialog:
    def __init__(self, parent, *args, **kwargs):
        print('called Dialog.__init__ with args', args, kwargs)
        self.parent = parent

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return True

    def SetIcon(self, *args):
        print("called Dialog.SetIcon with args", args)

    def Show(self):
        print('called Dialog.Show')

    def EndModal(self, arg):
        print(f'called Dialog.EndModal with arg {arg}')

    def ShowModal(self):
        print('called Dialog.ShowModal')
        return wx.ID_OK

    # def Accept(self):
    #     print('called Dialog.Accept')

    def confirm(self):
        """methode gedefinieerd in notetree.wx_gui op alle subklassen van Dialog
        """
        return 'confirmation data'

    def Destroy(self):
        print('called dialog.Destroy')

    def SetSizer(self, *args):
        print('called dialog.SetSizer with args', args)

    def SetTitle(self, text):
        print(f"called dialog.SetTitle with arg '{text}'")

    def SetPosition(self, *args):
        print("called dialog.SetPosition with args", args)

    def GetAffirmativeId(self):
        return wx.ID_OK

    def SetAffirmativeId(self, *args):
        print('called dialog.SetAffirmativeId with args', args)

    def SetEscapeId(self, *args):
        print('called dialog.SetEscapeId with args', args)

    def GetId(self, *args):
        print('called dialog.GetId with args', args)

    def SetSize(self, *args):
        print(f"called dialog.SetSize with args", args)

    def SetAutoLayout(self, *args):
        print('called dialog.SetAutoLayout with args', args)

    def SetAcceleratorTable(self, *args):
        print('called dialog.SetAcceleratorTable')  #  with args', args)

    def CreateButtonSizer(self, *args):
        print('called dialog.CreateButtonSizer with args', args)
        return MockBoxSizer()

    def Bind(self, *args):
        # bij meer dam twee argumenten zijn die vaak niet in de outputvoorspelling weer te geven,
        # dus maar inslikken
        print('called dialog.Bind with args', args[:2])

    def Layout(self, *args):
        print('called dialog.Layout with args', args)

    def SetFocus(self):
        print('called dialog.SetFocus')


class MockFileDialog:
    def __init__(self, parent, *args, **kwargs):
        print('called FileDialog.__init__ with args', args, kwargs)

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return True

    def ShowModal(self):
        print('called FileDialog.ShowModal')
        return wx.ID_OK

    def GetDirectory(self):
        print('called FileDialog.GetDirectory')
        return 'dirname'

    def GetFilename(self):
        print('called FileDialog.GetFilename')
        return 'filename'

    def GetPath(self):
        print('called FileDialog.GetPath')
        return 'dirname/filename'

    def Destroy(self):
        print('called FileDialog.Destroy with args', args)


class MockDirDialog:
    def __init__(self, parent, *args, **kwargs):
        print('called DirDialog.__init__ with args', args, kwargs)

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return True

    def ShowModal(self):
        print('called DirDialog.ShowModal')
        return wx.ID_OK

    def GetPath(self):
        print('called DirDialog.GetPath')
        return 'dirname'

    def Destroy(self):
        print('called DirDialog.Destroy with args', args)


class MockTextDialog:
    def __init__(self, parent, *args, **kwargs):
        print('called TextDialog.__init__ with args', args, kwargs)

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return True

    def ShowModal(self):
        print('called TextDialog.ShowModal')
        return wx.ID_CANCEL

    def GetValue(self):
        print('called TextDialog.GetValue')
        return ''

    def Destroy(self):
        print('called TextDialog.Destroy with args', args)


class MockChoiceDialog:
    def __init__(self, parent, *args):
        print('called ChoiceDialog.__init__ with args', args[:-1])

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return True

    def ShowModal(self):
        print('called ChoiceDialog.ShowModal')
        return wx.ID_CANCEL

    def SetSelection(self, value):
        print(f"called ChoiceDialog.SetSelection with arg '{value}'")

    def GetStringSelection(self):
        print(f'called ChoiceDialog.GetStringSelection')
        return 'selected value'

    def Destroy(self):
        print('called ChoiceDialog.Destroy with args', args)


class MockFontDialog:
    def __init__(self, parent, *args):
        print('called FontDialog.__init__ with args', args[:-1])

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return True

    def ShowModal(self):
        print('called FontDialog.ShowModal')
        return wx.ID_CANCEL

    def GetFontData(self):
        print(f'called FontDialog.GetFontData')
        return MockFontData()


class MockMessageDialog:
    def __init__(self, *args, **kwargs):
        print('called MessageDialog.__init__ with args', args, kwargs)

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return True

    def SetExtendedMessage(self, *args):
        print('called MessageDialog.SetExtendedMessage with args', args)

    def ShowModal(self):
        print('called MessageDialog.ShowModal')

    def Destroy(self):
        print('called MessageDialog.Destroy')


class MockBrowse:
    def __init__(self, *args, **kwargs):
        print('called FileBrowseButtonWithHistory.__init__ with args', args, kwargs)
        self._history = []

    def GetHistory(self):
        print('called FileBrowseButtonWithHistory.GetHistory')
        return self._history

    def SetHistory(self, history):
        print('called FileBrowseButtonWithHistory.SetHistory with arg', history)
        self._history = history

    def SetValue(self, *args, **kwargs):
        print('called FileBrowseButtonWithHistory.SetValue with args', args, kwargs)

    def GetHistoryControl(self):
        print('called FileBrowseButtonWithHistory.GetHistoryControl')
        return MockComboBox()


class MockFileBrowse:
    def __init__(self, *args, **kwargs):
        print('called FileBrowseButton.__init__ with args', args, kwargs)
        self._history = []

    def SetValue(self, *args, **kwargs):
        print('called FileBrowseButton.SetValue with args', args, kwargs)

    def GetValue(self):
        print('called FileBrowseButton.GetValue')
        return 'value from filebrowse'

    def Destroy(self, *args):
        print('called FileBrowseButton.Destroy with args', args)


class MockColour:
    def __init__(self, *args):
        print('called colour.__init__ with args', args)


class MockTextDataObject:
    def __init__(self):
        print('called TextDataObject.__init__')
        self._text = '(None)'

    def __str__(self):
        return self._text

    def SetText(self, text):
        print(f"called TextDataObject.SetText with arg '{text}'")
        self._text = text


class MockClipboard:
    @staticmethod
    def Get():
        print('called Clipboard.Get')
        return MockClipboard()

    def Open(self):
        print('called Clipboard.Open')
        return True

    def SetData(self, data):
        print(f"called Clipboard.SetData with arg '{data}'")

    def Close(self):
        print('called Clipboard.Close')


class MockImageList:
    def __init__(self, *args):
        print('called ImageList.__init__ with args', args)
    def Add(self, *args):
        print('called ImageList.Add with args', args)
        return args[0]


class MockEmbeddedImage:
    def __init__(self, *args):
        print('called PyEmbeddedImage.__init__')
    def GetBitmap(self, *args):
        print('called PyEmbeddedImage.GetBitmap')
        return 'bitmap from image'


class MockEasyPrinting:
    def __init__(self):
        print('called HtmlEasyPrinting.__init__')

    def SetHeader(self, *args):
        print('called HtmlEasyPrinting.SetHeader with args', args)

    def PreviewText(self, *args):
        print('called HtmlEasyPrinting.PreviewText with args', args)


class MockWebView:
    def New(self):
        print('called WebView.New')
        return MockWebView()

    def SetPage(self, *args):
        print('called WebView.SetPage with args', args)
