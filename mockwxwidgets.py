"""redefine elements to facilitatie testing
"""
import wx


class MockApp:
    def __init__(self, *args):
        print('called app.__init__ with args', args)

    def MainLoop(self):  # , *args):
        print('called app.MainLoop')  #  with args', args)

    def SetTopWindow(self, *args):
        print('called app.SetTopWindow with args', args)


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
        print('called Frame.Bind with args', args)

    def Connect(self, *args):
        print('called Frame.Connect with args', args)

    def SetIcon(self, *args):
        print('called Frame.SetIcon with args', args)

    def SetMenuBar(self, *args):
        print('called Frame.SetMenuBar with args', args)

    def SetSizer(self, *args):
        print('called Frame.SetSizer with args', args)

    def SetAutoLayout(self, *args):
        print('called Frame.SetAutoLayout with args', args)

    def GetSize(self):
        pass

    def GetPosition(self):
        print("called Frame.GetPosition")
        return 1, 2

    def SetAcceleratorTable(self, *args):
        print('called Frame.SetAcceleratorTable')  #  with args', args)

    def Destroy(self, *args):
        print('called Frame.Destroy with args', args)

    def Close(self, value):
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


class MockSize:
    def __init__(self, *args):
        print('called Size.__init__ with args', args)
        self.w = args[0]
        self.h = args[1]

    def GetWidth(self):
        print('called Size.GetWidth')
        return self.w

    def GetHeight(self):
        print('called Size.GetHeight')
        return self.h


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

    def GetMenus(self, *args):
        print('called menubar.GetMenus with args', args)
        return [(MockMenu(), 'label1'), (MockMenu(), 'label2')]

    def Append(self, *args):
        print('called menubar.Append with args', args)

    def Replace(self, *args):
        print('called menubar.Replace with args', args)


class MockMenu:
    def __init__(self, *args):
        print('called Menu.__init__ with args', args)

    def __repr__(self):
        return 'A Menu'

    def AppendSeparator(self, *args):
        print('called menu.AppendSeparator with args', args)

    def Append(self, *args):
        print('called menu.Append with args', args)

    def Destroy(self):  # , *args):
        print('called menu.Destroy')  #  with args', args)


class MockMenuItem:
    def __init__(self, *args, **kwargs):
        print('called MenuItem.__init__ with args', args)

    def GetId(self):  # , *args):
        print('called menuitem.GetId')  #  with args', args)
        return 'NewID'

    def Bind(self, *args):
        print('called menuitem.Bind with args', args)

    def Check(self, value):
        print(f'called menuitem.Check with arg {value}')


class MockSplitter:
    def __init__(self, *args):
        print('called Splitter.__init__ with args', args)

    def SetMinimumPaneSize(self, *args):
        print('called splitter.SetMinimumPaneSize with args', args)

    def SplitVertically(self, *args):
        print('called splitter.SplitVertically with args', args)

    def SetSashPosition(self, *args):
        print('called splitter.SetSashPosition with args', args)

    def GetSashPosition(self):  # , *args):
        print('called splitter.SetSashPosition')
        return 55


class MockNoteBook:
    def __init__(self, *args):
        print('called NoteBook.__init__ with args', args)

    def Bind(self, *args):
        print('called NoteBook.Bind with args', args)

    def GetPageCount(self, *args):
        print('called NoteBook.GetPageCount with args', args)
        return 'pagecount'

    def GetPage(self, *args):
        print('called NoteBook.GetPage with args', args)
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

    def AddColumn(self, *args):
        print('called tree.AddColumn with args', args)

    def SetMainColumn(self, *args):
        print('called tree.SetMainColumn with args', args)

    def SetColumnWidth(self, *args):
        print('called tree.SetColumnWidth with args', args)

    def DeleteAllItems(self):  # , *args):
        print('called tree.DeleteAllItems')  #  with args', args)

    def Bind(self, *args):
        # print('called tree.Bind() for method', str(args[1]).split()[2])
        print('called tree.Bind with args', args)

    def SetAcceleratorTable(self, *args):
        print('called tree.SetAcceleratorTable')  #  with args', args)

    def Expand(self, *args):
        print('called tree.Expand with args', args)

    def SetItemBold(self, *args):
        # print(f'called tree.SetItemBold() using {args[1]}')
        print(f'called tree.SetItemBold with args', args)

    def SetFocus(self):
        print('called tree.SetFocus')

    def SelectItem(self, *args):
        print('called tree.SelectItem with args', args)
        return 'selected_item'

    def GetSelection(self):
        print('called tree.GetSelection')  #  with args', args)
        return 'selection'

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
        return 'itemkey', 'itemtext', ['keyword']

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

    def Delete(self, *args):
        print('called tree.Delete with args', args)

    def GetFirstChild(self, *args):
        print('called tree.GetFirstChild')  #  with args', args)
        return MockTreeItem('first item'), 0

    def GetNextChild(self, *args):
        cookie = args[1]
        print('called tree.GetNextChild')  #  with args', args)
        if cookie == 0:
            return MockTreeItem('next item'), 1
        return MockTreeItem('not ok'), -1


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
    def __init__(self, *args):
        print('called Editor.__init__ with args', args)
        self.IsModified = 'ismodified'

    def Clear(self):  # , *args):
        print('called editor.Clear')  #  with args', args)

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

    def GetValue(self):
        print('called editor.GetValue')
        return 'fake editor value'

    def SetFocus(self):
        print('called editor.SetFocus')


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

    def GetX(self):
        print('called event.GetX')
        return 'x'

    def GetY(self):
        print('called event.GetY')
        return 'y'

    def Skip(self):
        print('called event.Skip')  #  with args', args)


class MockStatusBar:
    def SetStatusText(self, *args):
        print(f'called statusbar.SetStatusText with args', args)


class MockBoxSizer:
    def __init__(self, *args, **kwargs):
        self.orient = ('vert' if args[0] == wx.VERTICAL else
                       'hori' if args[0] == wx.HORIZONTAL else '')
        print(f'called BoxSizer.__init__ with args', args)

    def __repr__(self):
        return f'{self.orient} sizer'

    def Add(self, *args):
        print(f'called {self.orient} sizer.Add with args', '<item>', args[1:])

    def AddSpacer(self, *args):
        print(f'called {self.orient} sizer.AddSpacer with args', args)

    def AddStretchSpacer(self):  # , *args):
        print(f'called {self.orient} sizer.AddStretchSpacer')  #  with args', args)

    def Fit(self , *args):
        print(f'called {self.orient} sizer.Fit with args', args)

    def SetSizeHints(self, *args):
        print(f'called {self.orient} sizer.SetSizeHints with args', args)


class MockGridSizer:
    def __init__(self, *args, **kwargs):
        print('called GridSizer.__init__ with args', args, kwargs)

    def Add(self, *args):
        print('called GridSizer.Add with args', '<item>', args[1:])


class MockFlexGridSizer:
    def __init__(self, *args, **kwargs):
        print('called FlexGridSizer.__init__ with args', args, kwargs)

    def Add(self, *args):
        print('called FlexGridSizer.Add with args', '<item>', args[1:])


class MockStaticText:
    def __init__(self, *args, **kwargs):
        print('called StaticText.__init__ with args', args, kwargs)


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


class MockTextCtrl:
    def __init__(self, *args, **kwargs):
        value = kwargs.get('value', '')
        if value:
            value = f'`{value}`'
        print(f'called TextCtrl.__init__ with args', args, kwargs)

    def Clear(self):  # , *args):
        print('called text.Clear')  #  with args', args)

    def SetValue(self, *args):
        print(f'called text.SetValue with args', args)

    def GetValue(self):
        print(f'called text.GetValue')
        return 'value from textctrl'


class MockButton:
    def __init__(self, *args, **kwargs):
        print('called Button.__init__ with args', args, kwargs)

    def Bind(self, *args, **kwargs):
        print('called Button.Bind with args', args, kwargs)

    def GetId(self):  # , *args, **kwargs):
        print('called Button.GetId')  #  with args', args, kwargs)

    def SetHelpText(self, value):
        print(f"called Button.SetHelpText with arg '{value}'")


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

    def Clear(self):  # , *args):
        print('called combobox.clear')  #  with args', args)

    def AppendItems(self, *args):
        print(f'called combobox.AppendItems with args' ,args)

    def SetSelection(self, *args):
        print(f'called combobox.SetSelection with args', args)

    def SetStringSelection(self, *args):
        print(f'called combobox.SetStringSelection with args', args)

    def SetValue(self, *args):
        print(f'called combobox.SetValue with args', args)

    def GetValue(self):  # , *args):
        print(f'called combobox.GetValue')  #  with args', args)
        return 'value from combobox'


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

    def GetSelections(self, *args):
        return [1]

    def GetString(self, *args):
        return f'value {args[0]} from listbox'

    def GetItems(self, *args):
        return ['items from listbox']

    def Delete(self, *args):
        print(f'called listbox.Delete with args', args)

    def Insert(self, *args):
        print(f'called listbox.Insert with args', args)

    def InsertItems(self, *args):
        print('called ListBox.InsertItems with args', args)

    def GetCount(self):
        print('called listbox.GetCount')


class MockDialog:
    def __init__(self, parent, *args, **kwargs):
        print('called Dialog.__init__ with args', args, kwargs)

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return True

    def ShowModal(self):
        return wx.ID_OK

    def Accept(self):
        print('called Dialog.Accept')

    def confirm(self):
        """methode gedefinieerd in notetree.wx_gui op alle subklassen van Dialog
        """
        return 'confirmation data'

    def Destroy(self):
        print('called dialog.Destroy')

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

    def SetSizer(self, *args):
        print(f"called dialog.SetSizer with args", args)

    def SetAutoLayout(self, *args):
        print('called dialog.SetAutoLayout with args', args)

    def Layout(self, *args):
        print('called dialog.Layout with args', args)


class MockTextDialog:
    def __init__(self, parent, *args, **kwargs):
        print('called TextDialog.__init__ with args', args, kwargs)

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return True

    def ShowModal(self):
        return wx.ID_OK

    def GetValue(self):
        print('called TextDialog.GetValue')
        return 'entered value'

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
        return wx.ID_OK

    def SetSelection(self, value):
        print(f"called ChoiceDialog.SetSelection with arg '{value}'")

    def GetStringSelection(self):
        print(f'called ChoiceDialog.GetStringSelection')
        return 'selected value'

    def Destroy(self):
        print('called ChoiceDialog.Destroy with args', args)


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


class MockColour:
    def __init__(self, *args):
        print('called colour.__init__ with args', args)
