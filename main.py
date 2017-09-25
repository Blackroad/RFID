from pywinauto.application import Application

app = Application().start("notepad.exe")
app.UntitledNotepad.menu_select("&Справка->&О программе")
AboutNotepad = app['&Блокнот: сведенья']
AboutNotepad.ОКButton.click()
app.UntitledNotepad.Edit.type_keys("pywinauto Works!", with_spaces = True)
