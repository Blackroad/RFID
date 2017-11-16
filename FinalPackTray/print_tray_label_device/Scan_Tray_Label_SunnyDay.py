from app_connect import AAECapp


# Sunny day sequence - wolkthrough
def Print_Tray_Label_NoMES():
    loopcount = 4
    try:
        AAEC = AAECapp()
        # click 'start'
        AAEC.main_app_start()
        AAEC.log_in()
        AAEC.printer_label_dialog.wait('ready',10,1)
        AAEC.printer_label_dialog.Yes.click()
        AAEC.lot_input(lot_id=['L3ASY002','L3ASY003','L3ASY004','L3ASY005','L3ASY006','L3ASY007','L3ASY008','L3ASY009','L3ASY010','L3ASY011'])
        #AAEC.lot_input(lot_id=['L3ASY002', 'L3ASY003'])
        # expected: Dialog is displayed with appropriate text
        assert (AAEC.get_label_text('Read RFID')) == 'Get tray label and read RFID. Contact area leader if RFID does not read.'
        # expected: Dialog is displayed with appropriate text
        assert (AAEC.get_label_text('Scan the label 2D matrix')) == 'Scan the Printed Label 2D matrix. Contact area leader if matrix does not scan.'
        # finish
        AAEC.lot_input(
            lot_id=['L3ASY002', 'L3ASY003', 'L3ASY004', 'L3ASY005', 'L3ASY006', 'L3ASY007', 'L3ASY008', 'L3ASY009',
                    'L3ASY010', 'L3ASY011'])
       # AAEC.lot_input(lot_id=['L3ASY002', 'L3ASY003'])
        assert (AAEC.get_label_text(
            'Read RFID')) == 'Get tray label and read RFID. Contact area leader if RFID does not read.'
        # expected: Dialog is displayed with appropriate text
        assert (AAEC.get_label_text(
            'Scan the label 2D matrix')) == 'Scan the Printed Label 2D matrix. Contact area leader if matrix does not scan.'
    except Exception as err:
        print(err)
    else:
        print('\nTest Finished Succsessfully!')



if __name__== '__main__':
    Print_Tray_Label_NoMES()




