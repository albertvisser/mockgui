"""redefine elements to facilitatie testing
"""
import wx


class MockApp:
    def __init__(self, *args):
        print('called app.__init__()')

    def MainLoop(self, *args):
        print('called app.MainLoop()')

    def SetTopWindow(self, *args):
        print('called app.SetTopWindow()')


class MockFrame:
    def __init__(self, *args, **kwargs):
        print('called frame.__init__()')

    def Show(self, *args):
        print('called frame.Show()')

    def Hide(self, *args):
        print('called frame.Hide()')

    def GetSize(self):
        pass


class MockSize:
    def __init__(self, *args):
        self.w = args[0]
        self.h = args[1]

    def GetWidth(self):
        return self.w

    def GetHeight(self):
        return self.h


class MockIcon:
    def __init__(self, *args):
        print('called Icon.__init__()')


class MockMenuBar:
    def __init__(self, *args):
        print('called MenuBar.__init__()')

    def GetMenus(self, *args):
        print('called menubar.GetMenus()')
        return [(MockMenu(), 'label1'), (MockMenu(), 'label2')]

    def Append(self, *args):
        print('called menubar.Append()')

    def Replace(self, *args):
        print('called menubar.Replace()')


class MockMenu:
    def __init__(self, *args):
        print('called Menu.__init__()')

    def Append(self, *args):
        print('called menu.Append()')

    def Destroy(self, *args):
        print('called menu.Destroy()')


class MockMenuItem:
    def __init__(self, *args, **kwargs):
        print('called MenuItem.__init__()')

    def GetId(self, *args):
        print('called menuitem.GetId()')

    def Bind(self, *args):
        print('called menuitem.Bind()')

    def Check(self, *args):
        print(f'called menuitem.Check(`{args[0]}`)')


class MockSplitter:
    def __init__(self, *args):
        print('called MockSplitter.__init__()')

    def SetMinimumPaneSize(self, *args):
        print('called splitter.SetMinimumPaneSize()')

    def SplitVertically(self, *args):
        print('called splitter.SplitVertically()')

    def SetSashPosition(self, *args):
        print('called splitter.SetSashPosition()')

    def GetSashPosition(self, *args):
        return 55


class MockTree:
    def __init__(self, *args):
        print('called MockTree.__init__()')

    def AddRoot(self, *args):
        print('called tree.AddRoot()')

    def DeleteAllItems(self, *args):
        print('called tree.DeleteAllItems()')

    def Bind(self, *args):
        print('called tree.Bind() for method', str(args[1]).split()[2])

    def SetAcceleratorTable(self, *args):
        print('called tree.SetAcceleratorTable()')

    def Expand(self, *args):
        print('called tree.Expand()')

    def SetItemBold(self, *args):
        print(f'called tree.SetItemBold() using {args[1]}')

    def SetFocus(self):
        print('called tree.SetFocus()')

    def SelectItem(self, *args):
        print('called tree.SelectItem()')

    def GetSelection(self, *args):
        return 'selected_item'  # print('called tree.GetSelection()')

    def GetItemText(self, *args):
        return 'itemtext'  # print('called tree.GetItemText()')

    def SetItemText(self, *args):
        print('called tree.SetItemText()')

    def GetItemData(self, *args):
        return 'itemkey', 'itemtext', ['keyword']  # print('called tree.GetItemData()')

    def SetItemData(self, *args):
        print(f'called tree.SetItemData() with args `{args[1]}`')

    def GetNextSibling(self, *args):
        print('called tree.GetNextSibling()')
        return MockTreeItem('next treeitem')

    def GetPrevSibling(self, *args):
        print('called tree.GetPrevSibling()')
        return MockTreeItem('previous treeitem')

    def AppendItem(self, *args):
        print('called tree.AppendItem()')

    def PrependItem(self, *args):
        print('called tree.PrependItem()')

    def Delete(self, *args):
        print('called tree.Delete()')

    def GetFirstChild(self, *args):
        print('called tree.GetFirstChild()')
        return MockTreeItem('first item'), 0

    def GetNextChild(self, *args):
        cookie = args[1]
        print('called tree.GetNextChild()')
        if cookie == 0:
            return MockTreeItem('next item'), 1
        return MockTreeItem('not ok'), -1


class MockTreeItem:
    def __init__(self, *args):
        print('called MockTreeItem.__init__()')
        self.tag = args[0]

    def IsOk(self, *args):
        return self.tag != 'not ok'


class MockFont:
    def __init__(self):
        print('called MockFont.__init__()')

    def SetFamily(self, *args):
        print('called font.SetFamily()')

    def SetPointSize(self, *args):
        print('called font.SetPointSize()')


class MockEditor:   # actually a StyledTextCtrl
    def __init__(self, *args):
        print('called MockEditor.__init__()')
        self.IsModified = 'ismodified'

    def Clear(self, *args):
        print('called editor.Clear()')

    def Enable(self, *args):
        print(f'called editor.Enable(`{args[0]}`)')

    def Bind(self, *args):
        print('called editor.Bind() for method', str(args[1]).split()[2])

    def SetWrapMode(self, *args):
        print('called editor.SetWrapMode()')

    def SetCaretLineVisible(self, *args):
        print('called editor.SetCaretLineVisible()')

    def SetCaretLineBackground(self, *args):
        print('called editor.SetCaretLineBackground()')

    def SetLexer(self, *args):
        print('called editor.SetLexer()')

    def StyleSetForeground(self, *args):
        print(f'called editor.StyleSetForeground() for style {args[0]}')

    def StyleSetBackground(self, *args):
        print(f'called editor.StyleSetBackground() for style {args[0]}')

    def StyleSetBold(self, *args):
        print(f'called editor.StyleSetBold() for style {args[0]}')

    def StyleSetItalic(self, *args):
        print(f'called editor.StyleSetItalic() for style {args[0]}')

    def StyleSetUnderline(self, *args):
        print(f'called editor.StyleSetUnderline() for style {args[0]}')

    def SetValue(self, value):
        print(f'setting editor text to `{value}`')

    def GetValue(self):
        return 'fake editor value'

    def SetFocus(self):
        print('called editor.SetFocus()')


class MockTrayIcon:
    def __init__(self, *args):
        print('called TrayIcon.__init__()')

    def SetIcon(self, *args):
        print('called trayicon.SetIcon()')

    def Bind(self, *args, **kwargs):
        print('called trayicon.Bind()')

    def Destroy(self, *args):
        print('called trayicon.Destroy()')


class MockAcceleratorEntry:
    def __init__(self, *args, **kwargs):
        print('called AcceleratorEntry.__init__()')

    def FromString(self, *args):
        print('called MockAcceleratorEntry.FromString()')
        return True


class MockAcceleratorTable:
    def __init__(self, *args):
        print('called AcceleratorTable.__init__()')


class MockEvent:
    def __init__(self):
        print('called event.__init__()')

    def GetItem(self):
        return 'treeitem'

    def Skip(self):
        print('called event.Skip()')


class MockStatusBar:
    def SetStatusText(self, *args):
        print(f'called statusbar.SetStatusText(`{args[0]}`)')


class MockBoxSizer:
    def __init__(self, *args, **kwargs):
        self.orient = ('vert' if args[0] == wx.VERTICAL else
                       'hori' if args[0] == wx.HORIZONTAL else '')
        print(f'called BoxSizer.__init__(`{self.orient}`)')

    def Add(self, *args):
        print(f'called {self.orient} sizer.Add()')

    def AddSpacer(self, *args):
        print(f'called {self.orient} sizer.AddSpacer()')

    def AddStretchSpacer(self, *args):
        print(f'called {self.orient} sizer.AddStretchSpacer()')

    def Fit(self, *args):
        print(f'called {self.orient} sizer.Fit()')

    def SetSizeHints(self, *args):
        print(f'called {self.orient} sizer.SetSizeHints()')


class MockGridSizer:
    def __init__(self, *args, **kwargs):
        print('called GridSizer.__init__()')

    def Add(self, *args):
        print('called gridsizer.Add()')


class MockStaticText:
    def __init__(self, *args, **kwargs):
        print('called StaticText.__init__()')


class MockCheckBox:
    def __init__(self, *args, **kwargs):
        print('called CheckBox.__init__()')

    def SetValue(self, *args):
        print(f'called checkbox.SetValue(`{args[0]}`)')

    def GetValue(self, *args):
        return 'value from checkbox'


class MockTextCtrl:
    def __init__(self, *args, **kwargs):
        value = kwargs.get('value', '')
        if value:
            value = f'`{value}`'
        print(f'called TextCtrl.__init__({value})')

    def Clear(self, *args):
        print('called text.clear()')

    def SetValue(self, *args):
        print(f'called text.SetValue(`{args[0]}`)')

    def GetValue(self, *args):
        return 'value from textctrl'


class MockButton:
    def __init__(self, *args, **kwargs):
        print('called Button.__init__()')

    def Bind(self, *args, **kwargs):
        print('called Button.Bind()')

    def GetId(self, *args, **kwargs):
        print('called Button.GetId()')


class MockComboBox:
    def __init__(self, *args, **kwargs):
        sellist = kwargs.get('choices', '')
        if sellist:
            sellist = f' with arg `{sellist}`'
        print(f'called ComboBox.__init__(){sellist}')

    def Clear(self, *args):
        print('called combobox.clear()')

    def AppendItems(self, *args):
        print(f'called combobox.appenditems() with arg `{args[0]}`')

    def SetSelection(self, *args):
        print(f'called combobox.SetSelection(`{args[0]}`)')

    def SetValue(self, *args):
        print(f'called combobox.SetValue(`{args[0]}`)')

    def GetValue(self, *args):
        return 'value from combobox'


class MockListBox:
    def __init__(self, *args, **kwargs):
        # sellist = kwargs.get('choices', '')
        # if sellist:
        #     sellist = ' with arg `{}`'.format(sellist)
        # print('called ListBox.__init__(){}'.format(sellist))
        print('called ListBox.__init__()')

    def Bind(self, *args):
        print('called listbox.bind()')

    def SetFocus(self, *args):
        print('called listbox.SetFocus()')

    def Append(self, *args):
        print(f'called listbox.append() with arg `{args[0]}`')

    def SetSelection(self, *args):
        print(f'called listbox.SetSelection(`{args[0]}`)')

    def GetSelections(self, *args):
        return [1]

    def GetString(self, *args):
        return f'value {args[0]} from listbox'

    def GetItems(self, *args):
        return ['items from listbox']

    def Delete(self, *args):
        print(f'delete item {args[0]} from listbox')

    def Insert(self, *args):
        print(f'insert `{args[0]}` into listbox')

    def InsertItems(self, *args):
        print('called ListBox.InsertItems with args', args)

    def GetCount(self):
        print('called listbox.GetCount()')


class MockDialog:
    def __init__(self, parent, *args, **kwargs):
        print('called MockDialog.__init__() with args', args, kwargs)

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return True

    def ShowModal(self):
        return wx.ID_OK

    def confirm(self):
        return 'confirmation data'

        print('called dialog.Destroy')

    def SetTitle(self, text):
        print(f"called dialog.SetTitle with arg '{text}'")

    def SetAffirmativeId(self, *args):
        print('called dialog.SetAffirmativeId')

    def GetId(self, *args):
        print('called dialog.GetId')

    def SetSizer(self, text):
        print(f"called dialog.SetSizer")

    def SetAutoLayout(self, *args):
        print('called dialog.SetAutoLayout')

    def Layout(self, *args):
        print('called dialog.Layout')


class MockTextDialog:
    def __init__(self, parent, *args, **kwargs):
        print('called MockTextDialog.__init__() with args', args, kwargs)

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return True

    def ShowModal(self):
        return wx.ID_OK

    def GetValue(self):
        return 'entered value'

    def Destroy(self):
        print('called dialog.Destroy()')


class MockChoiceDialog:
    def __init__(self, parent, *args):
        print('called MockChoiceDialog.__init__ with args', args[:-1])

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return True

    def ShowModal(self):
        return wx.ID_OK

    def SetSelection(self, value):
        print(f'called dialog.SetSelection(`{value}`)')

    def GetStringSelection(self):
        return 'selected value'

    def Destroy(self):
        print('called dialog.Destroy()')


class MockMessageDialog:
    def __init__(self, *args, **kwargs):
        print('called MessageDialog.__init__()')

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return True

    def SetExtendedMessage(self, *args):
        print('called dialog.SetExtendedMessage()')

    def ShowModal(self):
        print('called dialog.ShowModal()')

    def Destroy(self):
        print('called dialog.Destroy()')
