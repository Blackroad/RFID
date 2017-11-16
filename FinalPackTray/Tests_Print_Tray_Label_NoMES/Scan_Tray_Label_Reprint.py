from app_connect import AAECapp
import time


def Test_Scan_Tray_Label_Inconsistancy():
    try:
        AAEC = AAECapp()
        # click 'start'
        AAEC.main_app_start()
        AAEC.log_in()
        # wait for test print dialog
        AAEC.printer_label_dialog.wait('ready',10,1)
        AAEC.printer_label_dialog.Yes.click()
        # lot input
        AAEC.lot_input(lot_id='L3ASY001')
        AAEC.lot_input(lot_id='L3ASY002')
        AAEC.confirmation_form('Accept')
        AAEC.pa_tracker('PA Track')
        # AAEC.RFID_dialog.Cancel.click()
        AAEC.RFID_dialog.Reprint.click()
        Reprint(AAEC)
        AAEC.rfid_manual_submit(value='B12114A')
        assert AAEC.get_label_text('Incorrect label preamble') == 'Incorrect label preamble. Contact area leaders.'
        AAEC.incorrect_preamble.Reprint.click()
        Reprint(AAEC)
        AAEC.rfid_manual_submit()
        AAEC.SCAN_dialog.Reprint.click()
        Reprint(AAEC)
        AAEC.rfid_manual_submit()
        AAEC.lot_input(lot_id='MA12836A009,L3ASY001,L3ASY002')
    except Exception as err:
        print(err)
    else:
        print('\nTest Finished Succsessfully!')

# reprint method
def Reprint(AAEC):
    AAEC.log_in()
    AAEC.reprint_not_authorized.wait('ready visible')
    assert AAEC.get_label_text('Reprint not authorized') == 'User is not Authorized for this Operation'
    AAEC.reprint_not_authorized.OK.click()
    AAEC.log_in(reallogin=True)
    assert AAEC.get_label_text(
        'Reprint was successful.') == 'WARNING: The area leader is still logged in. The Assembler should log in again on the next screen to continue the process under their User ID.'
    AAEC.reprint_login_warn.OK.click()
    AAEC.log_in()


if __name__== '__main__':
    Test_Scan_Tray_Label_Inconsistancy()