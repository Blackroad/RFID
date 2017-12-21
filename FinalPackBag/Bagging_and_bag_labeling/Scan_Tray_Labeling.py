from app_connect import AAECapp
import traceback


# Sunny day sequence - wolkthrough (FinalBag)
def test_scan_rfid_epc():
    try:
        AAEC = AAECapp()
        # click 'start'
        AAEC.main_app_start()
        AAEC.log_in()
        AAEC.printer_label_dialog.wait('visible ready enabled',20,2)
        AAEC.printer_label_dialog.Yes.click()
        AAEC.rfid_manual_submit(value=['A00001'])
        AAEC.lot_input(
            lot_id=['MA12836A009,L3ASY166'])
        AAEC.chumber_ready()
        AAEC.rfid_manual_submit() #Bag integrity check
        AAEC.rfid_manual_submit(value=['A00001'])
        AAEC.rfid_manual_submit(value=['B00001'])
        AAEC.lot_input(
            lot_id=['MA12836A009,L3ASY166'])
        AAEC.chumber_ready() #Bag integrity check
        AAEC.rfid_manual_submit(value=['B00001'])
        AAEC.rfid_manual_submit(value=['B00001', 'A00001'])
    except Exception as error:
        print(error)
        traceback.print_exc()
    else:
        print('\nTest Finished Succsessfully!')


if __name__== '__main__':
    test_scan_rfid_epc()

