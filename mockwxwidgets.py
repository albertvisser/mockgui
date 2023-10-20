"""redefine elements to facilitatie testing
"""
import wx


# this collection originally created for notetree project
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
        print('called menuitem.Check(`{}`)'.format(args[0]))


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
        print('called tree.Bind() for method {}'.format(str(args[1]).split()[2]))
    def SetAcceleratorTable(self, *args):
        print('called tree.SetAcceleratorTable()')
    def Expand(self, *args):
        print('called tree.Expand()')
    def SetItemBold(self, *args):
        print('called tree.SetItemBold() using {}'.format(args[1]))
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
        print('called tree.SetItemData() with args `{}`'.format(args[1]))
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
        else:
            return MockTreeItem('not ok'), -1


class MockTreeItem:
    def __init__(self, *args):
        print('called MockTreeItem.__init__()')
        self.tag = args[0]
    def IsOk(self, *args):
        return not (self.tag == 'not ok')


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
        print('called editor.Enable(`{}`)'.format(args[0]))
    def Bind(self, *args):
        print('called editor.Bind() for method {}'.format(str(args[1]).split()[2]))
    def SetWrapMode(self, *args):
        print('called editor.SetWrapMode()')
    def SetCaretLineVisible(self, *args):
        print('called editor.SetCaretLineVisible()')
    def SetCaretLineBackground(self, *args):
        print('called editor.SetCaretLineBackground()')
    def SetLexer(self, *args):
        print('called editor.SetLexer()')
    def StyleSetForeground(self, *args):
        print('called editor.StyleSetForeground() for style {}'.format(args[0]))
    def StyleSetBackground(self, *args):
        print('called editor.StyleSetBackground() for style {}'.format(args[0]))
    def StyleSetBold(self, *args):
        print('called editor.StyleSetBold() for style {}'.format(args[0]))
    def StyleSetItalic(self, *args):
        print('called editor.StyleSetItalic() for style {}'.format(args[0]))
    def StyleSetUnderline(self, *args):
        print('called editor.StyleSetUnderline() for style {}'.format(args[0]))
    def SetValue(self, value):
        print('setting editor text to `{}`'.format(value))
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
        print('called statusbar.SetStatusText(`{}`)'.format(args[0]))


class MockBoxSizer:
    def __init__(self, *args, **kwargs):
        self.orient = ('vert' if args[0] == wx.VERTICAL else
                       'hori' if args[0] == wx.HORIZONTAL else '')
        print('called BoxSizer.__init__(`{}`)'.format(self.orient))
    def Add(self, *args):
        print('called {} sizer.Add()'.format(self.orient))
    def AddSpacer(self, *args):
        print('called {} sizer.AddSpacer()'.format(self.orient))
    def AddStretchSpacer(self, *args):
        print('called {} sizer.AddStretchSpacer()'.format(self.orient))
    def Fit(self, *args):
        print('called {} sizer.Fit()'.format(self.orient))
    def SetSizeHints(self, *args):
        print('called {} sizer.SetSizeHints()'.format(self.orient))


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
        print('called checkbox.SetValue(`{}`)'.format(args[0]))
    def GetValue(self, *args):
        return 'value from checkbox'


class MockTextCtrl:
    def __init__(self, *args, **kwargs):
        value = kwargs.get('value', '')
        if value:
            value = '`{}`'.format(value)
        print('called TextCtrl.__init__({})'.format(value))
    def Clear(self, *args):
        print('called text.clear()')
    def SetValue(self, *args):
        print('called text.SetValue(`{}`)'.format(args[0]))
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
            sellist = ' with arg `{}`'.format(sellist)
        print('called ComboBox.__init__(){}'.format(sellist))
    def Clear(self, *args):
        print('called combobox.clear()')
    def AppendItems(self, *args):
        print('called combobox.appenditems() with arg `{}`'.format(args[0]))
    def SetSelection(self, *args):
        print('called combobox.SetSelection(`{}`)'.format(args[0]))
    def SetValue(self, *args):
        print('called combobox.SetValue(`{}`)'.format(args[0]))
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
        print('called listbox.append() with arg `{}`'.format(args[0]))
    def SetSelection(self, *args):
        print('called listbox.SetSelection(`{}`)'.format(args[0]))
    def GetSelections(self, *args):
        return [1]
    def GetString(self, *args):
        return 'value {} from listbox'.format(args[0])
    def GetItems(self, *args):
        return ['items from listbox']
    def Delete(self, *args):
        print('delete item {} from listbox'.format(args[0]))
    def Insert(self, *args):
        print('insert `{}` into listbox'.format(args[0]))
    def GetCount(self):
        print('called listbox.GetCount()')


# subclassemn is hier bedoeld voor overervent van contextmanager protocol
class MockDialog(wx.Dialog):
    def __init__(self, parent, *args, **kwargs):
        print('called MockDialog.__init__() with args `{}`'.format(args))
    def ShowModal(self):
        return wx.ID_OK
    def confirm(self):
        return 'confirmation data'
    def Destroy(self):
        print('called dialog.Destroy()')


class MockTextDialog(wx.Dialog):
    def __init__(self, parent, *args, **kwargs):
        print('called MockTextDialog.__init__() with args `{}`'.format(args))
    def ShowModal(self):
        return wx.ID_OK
    def GetValue(self):
        return 'entered value'
    def Destroy(self):
        print('called dialog.Destroy()')


class MockChoiceDialog(wx.Dialog):
    def __init__(self, parent, *args):
        print('called MockChoiceDialog.__init__ with args `{}`'.format(args[:-1]))
    def ShowModal(self):
        return wx.ID_OK
    def SetSelection(self, value):
        print('called dialog.SetSelection(`{}`)'.format(value))
    def GetStringSelection(self):
        return 'selected value'
    def Destroy(self):
        print('called dialog.Destroy()')


class MockMessageDialog(wx.Dialog):
    def __init__(self, *args, **kwargs):
        print('called MessageDialog.__init__()')
    def SetExtendedMessage(self, *args):
        print('called dialog.SetExtendedMessage()')
    def ShowModal(self):
        print('called dialog.ShowModal()')
    def Destroy(self):
        print('called dialog.Destroy()')
