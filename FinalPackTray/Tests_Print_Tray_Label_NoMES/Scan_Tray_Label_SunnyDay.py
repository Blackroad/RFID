from app_connect import AAECapp


# Sunny day sequence - wolkthrough
def Print_Tray_Label_NoMES():
    try:
        AAEC = AAECapp()
        # click 'start'
        AAEC.main_app_start()
        AAEC.log_in()
        # wait for test print dialog
        AAEC.printer_label_dialog.wait('ready',10,1)
        AAEC.printer_label_dialog.Yes.click()
        # lot input
<<<<<<< HEAD:FinalPackTray/Tests_Print_Tray_Label_NoMES/Scan_Tray_Label_SunnyDay.py
        # AAEC.lot_input(lot_id='L3ASY001')
        # AAEC.lot_input(lot_id='L3ASY002')
        # AAEC.confirmation_form('Accept')
        # AAEC.pa_tracker('PA Track')
=======
        AAEC.lot_input(lot_id=['L3ASY002','L3ASY003'])
        AAEC.confirmation_form('Accept')
        AAEC.pa_tracker('PA Track')
>>>>>>> 9a439d009821e89cf129e352a0d9785eadf8a979:FinalPackTray/Tests_Print_Tray_Label_NoMES/Scan_Tray_Label_SunnyDay.py
        # expected: Dialog is displayed with appropriate text
        assert (AAEC.get_label_text('Read RFID')) == 'Get tray label and read RFID. Contact area leader if RFID does not read.'
        AAEC.rfid_manual_submit()
        # expected: Dialog is displayed with appropriate text
        assert (AAEC.get_label_text('Scan the label 2D matrix')) == 'Scan the Printed Label 2D matrix. Contact area leader if matrix does not scan.'
        AAEC.lot_input(lot_id='MA12836A009,L3ASY001,L3ASY002')
        # finish
        assert AAEC.manual_camera.wait('visible ready', 10, 1)
    except Exception as err:
        print(err)
    else:
        print('\nTest Finished Succsessfully!')


if __name__== '__main__':
    Print_Tray_Label_NoMES()




