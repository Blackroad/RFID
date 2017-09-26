from pywinauto.application import Application



app = Application().start("notepad.exe")
app.UntitledNotepad.menu_select("Help -> About Notepad")
AboutNotepad = app['About Notepad']
AboutNotepad.ОКButton.click()
app.UntitledNotepad.Edit.type_keys("pywinauto Works!", with_spaces = True)
