from app_connect import AAECapp
import time


#Tray Label Inconsistancy - Bad Part ID
def Scan_Tray_Label_Inconsistancy():
    try:
        AAEC = AAECapp()
        # click 'start'
        AAEC.main_app_start()
        AAEC.log_in()
        # wait for test print dialog
        AAEC.printer_label_dialog.wait('ready',10,1)
        AAEC.printer_label_dialog.Yes.click()
        # # lot input
        AAEC.confirmation_form('Accept')
        AAEC.pa_tracker('PA Track')
        # expected: Dialog is displayed with appropriate text
        assert (AAEC.get_label_text('Read RFID')) == 'Get tray label and read RFID. ' \
                                                     'Contact area leader if RFID does not read.'
        AAEC.rfid_manual_submit()
        # # expected: Dialog is displayed with appropriate text
        assert (AAEC.get_label_text('Scan the label 2D matrix')) == 'Scan the Printed Label 2D matrix. Contact area leader if matrix does not scan.'
        AAEC.lot_input(lot_id=',L3ASY001,L3ASY002')
        # # finish
        assert AAEC.label_missmatch_dialog.wait('visible ready', 20, 1)
        time.sleep(3)
        AAEC.label_missmatch_dialog.OK.click()

        # LOOP RESET
        AAEC.main_app_start()
        AAEC.log_in()
        AAEC.printer_label_dialog.wait('ready', 10, 1)
        AAEC.printer_label_dialog.Yes.click()
        # lot input
        AAEC.confirmation_form('Accept')
        AAEC.pa_tracker('PA Track')
        # expected: Dialog is displayed with appropriate text
        assert (AAEC.get_label_text('Read RFID')) == 'Get tray label and read RFID. ' \
                                                     'Contact area leader if RFID does not read.'
        AAEC.rfid_manual_submit()
        # expected: Dialog is displayed with appropriate text
        assert (AAEC.get_label_text(
            'Scan the label 2D matrix')) == 'Scan the Printed Label 2D matrix. Contact area leader if matrix does not scan.'
        AAEC.lot_input(lot_id='MA12836A009,L3ASY,L3ASY00')
        # finish
        assert AAEC.label_missmatch_dialog.wait('visible ready', 20, 1)
        time.sleep(3)
        AAEC.label_missmatch_dialog.OK.click()
    except Exception as err:
        print(err)
    else:
        print('\nTest Finished Succsessfully!')







if __name__== '__main__':
    Test_Scan_Tray_Label_Inconsistancy()