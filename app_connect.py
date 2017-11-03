from pywinauto.application import Application

class AAECapp(Application):
    def __init__(self):
        Application.__init__(self)
        self.app = self.connect(path=r'C:\Dev\RFID_Master\Dev-branch-FW-FinalPackCAPA-branch\AAEC\ECL\ECLUnitTestUI\ECLUnitTestUI\bin\x86\Debug\AAEC.exe')
        self.manual_camera = self.app['Manual Camera: Manual']
        self.main_form = self.app["- ()"]
        self.login = self.app['Login']
        self.printer_label_dialog = self.app['Label Printer Test']
        self.RFID_dialog = self.app['Read RFID']
        self.RFID_manual_input = self.app['RFID Dialog']
        self.SCAN_dialog = self.app['Scan the label 2D matrix']
        self.PA_Tracker = self.app['Part Tracker']
        self.label_missmatch_dialog = self.app['Error: 2D/Drop File Mismatch']
        self.reprint_not_authorized = self.app['Reprint not authorized']
        self.reprint_login_warn = self.app['Reprint was successful.']
        self.incorrect_preamble = self.app['Incorrect label preamble']


    def main_app_start(self):
        self.main_form.type_keys("^{F5}")
        self.main_form.Start.click()


    def log_in(self,reallogin=False):
        if (reallogin)is False:
            self.login.type_keys("^{F5}")
        elif reallogin is True:
            self.login.UserNameEdit.type_keys('ent\\velycv1')
            self.login.PasswordEdit.type_keys('Drulich121314')
            self.login.Login.click()



    def lot_input(self,lot_id):
        self.manual_camera.wait('ready visible',timeout=20,retry_interval=1)
        self.manual_camera.type_keys("{BACKSPACE}")
        self.manual_camera.type_keys(lot_id)
        self.manual_camera.Submit.click()

    def rfid_manual_submit(self,value=None):
        if value is None:
            self.RFID_manual_input.wait('ready visible',timeout=20,retry_interval=1)
            self.RFID_manual_input.Submit.click()
        else:
            self.RFID_manual_input.edit.type_keys(value)
            self.RFID_manual_input.Add.click()
            self.RFID_manual_input.Submit.click()

    def get_label_text(self,win_title):
        win = self.app[win_title].Static.texts()
        win2 = self.app[win_title].Static2.texts()
        if win == ['']:
            for i in win2:
             return i
        else:
            for i in win:
                return i


    def confirmation_form(self,action):
        self.main_form[action].wait('visible',5,1)
        self.main_form[action].click()

    def pa_tracker(self,action):
        self.PA_Tracker.wait('ready visible', timeout=5,retry_interval=1)
        self.PA_Tracker[action].click()
        if action == 'PA Track':
            self.PA_Tracker['Accept'].wait('enabled',timeout=20)
        else:
            pass
        self.PA_Tracker['Accept'].click()













































