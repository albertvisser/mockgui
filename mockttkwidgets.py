"""redefine ttk widgets to make testing easier (or possible at all)
"""
import types

class MockDialog:
    def __init__(self, *args, **kwargs):
        print('called Toplevel.__init__ with args', args, kwargs)
    def bind(self, *args):
        print('called Toplevel.bind with args', args)
    def destroy(self):
        print('called Toplevel.destroy')
    def focus_set(self):
        print('called Toplevel.focus_set')
    def grab_set(self):
        print('called Toplevel.grab_set')
    def wait_window(self):
        print('called Toplevel.wait_window')


# class MockFileDialog:   # filedialog is een module
def mock_askopen_nofile(**kwargs):
    print('called FileDialog.askopenfilename with args', kwargs)
    if kwargs.get('multiple', False):
        return []
    return ''


def mock_askopen_file(**kwargs):
    print('called FileDialog.askopenfilename with args', kwargs)
    if kwargs.get('multiple', False):
        return ['name1', 'name2']
    return 'filename'


# class MockMessageBox:   # messageBox is een module
def mock_show_info(*args, **kwargs):
    print('called MessageBox.showinfo with args', args, kwargs)


class MockFrame:
    def __init__(self, master=None, *args, **kwargs):
        print('called Frame.__init__ with args', type(master), args, kwargs)
    def grid(self, *args, **kwargs):
        print('called Frame.grid with args', args, kwargs)
    def state(self, *args):
        print('called Frame.state with args', args)
    def columnconfigure(self, *args, **kwargs):
        print('called Frame.columnconfigure with args', args)
    def destroy(self):
        print('called Frame.destroy')


class MockLabel:
    def __init__(self, master=None, *args, **kwargs):
        print('called Label.__init__ with args', type(master), args, kwargs)
    def grid(self, *args, **kwargs):
        print('called Label.grid with args', args, kwargs)
    def state(self, *args):
        print('called Label.state with args', args)
    def destroy(self):
        print('called Label.destroy')


class MockCheckBox:
    def __init__(self, master=None, *args, **kwargs):
        print('called CheckBox.__init__ with args', type(master), args, kwargs)
    def grid(self, *args, **kwargs):
        print('called CheckBox.grid with args', args, kwargs)
    def state(self, *args):
        print('called CheckBox.state with args', args)
    def instate(self, *args):
        print('called CheckBox.instate with args', args)
    def destroy(self):
        print('called CheckBox.destroy')


class MockComboBox:
    def __init__(self, master=None, *args, **kwargs):
        print('called ComboBox.__init__ with args', type(master), args, kwargs)
    def grid(self, *args, **kwargs):
        print('called ComboBox.grid with args', args, kwargs)
    def state(self, *args):
        print('called ComboBox.state with args', args)
    def bind(self, *args):
        print('called ComboBox.bind with args', args)
    def configure(self, **kwargs):
        print('called ComboBox.configure with args', kwargs)
    def focus_set(self):
        print('called ComboBox.focus_set')
    def destroy(self):
        print('called ComboBox.destroy')


class MockButton:
    def __init__(self, master=None, *args, **kwargs):
        print('called Button.__init__ with args', type(master), args, kwargs)
    def grid(self, *args, **kwargs):
        print('called Button.grid with args', args, kwargs)
    def state(self, *args):
        print('called Button.state with args', args)
    def bind(self, *args):
        print('called Button.bind with args', args)
    def configure(self, **kwargs):
        print('called Button.configure with args', kwargs)
    def destroy(self):
        print('called Button.destroy')


class MockEntry:
    def __init__(self, master=None, *args, **kwargs):
        print('called Entry.__init__ with args', type(master), args, kwargs)
    def grid(self, *args, **kwargs):
        print('called Entry.grid with args', args, kwargs)
    def state(self, *args):
        print('called Entry.state with args', args)
    def destroy(self):
        print('called Entry.destroy')


class MockPhotoImage:
    def __init__(self, *args):
        print('called PhotoImage.__init__ with args', args)


class MockStringVar:
    def __init__(self, *args):
        print('called StringVar.__init__ with args', args)
        self._value = None
    def set(self, arg):
        print(f"called StringVar.set with arg '{arg}'")
        self._value = arg
    def get(self):
        print('called StringVar.get')
        return self._value
    def trace_add(self, *args):
        print('called StringVar.trace_add')  #  with args', args)

class MockIntVar:
    def __init__(self, *args):
        print('called IntVar.__init__ with args', args)
        self._value = None
    def set(self, arg):
        print(f"called IntVar.set with arg {arg}")
        self._value = arg
    def get(self):
        print('called IntVar.get')
        return self._value
