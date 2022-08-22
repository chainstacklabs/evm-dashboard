
from time import sleep
from datetime import datetime
import gspread


#location of google_credential.json file
GOOGLE_CREDENTIAL_LOCATION = "<CREDENTIAL-JSON-FILE>"

#name of the spreadsheet
GOOGLE_SPREADSHEET_NAME = "<GOOGLE-SHEET-NAME>"

def pause_execution():
        print("####### Execution Paused #######")
        sleep(60)

def addDataToSheet(_new_block):
        drive = gspread.service_account(filename=GOOGLE_CREDENTIAL_LOCATION)
        sheet = drive.open(GOOGLE_SPREADSHEET_NAME).sheet1
        blockInfo = extractBlockDetails(_new_block)
        try:
            sheet.append_row(blockInfo)
        except Exception as e:
            #if we encounter "write quota exceeded" error
            if e.args[0]['code'] == 429:
                #pause the execution for a minute
                pause_execution()
                #retry with same data
                addDataToSheet(_new_block)          

#function to extract the details from the block
def extractBlockDetails(_new_block):
    size = _new_block['size']
    gasUsed = _new_block['gasUsed']
    gasLimit = _new_block['gasLimit']
    transactionNumber = len(_new_block['transactions'])
    baseFeePerGas = _new_block['baseFeePerGas']
    difficulty = _new_block['difficulty']
    unixTimestamp = int(_new_block['timestamp'])
    #converting the unix timestamp
    timestamp = datetime.utcfromtimestamp(unixTimestamp).strftime('%Y-%m-%d %H:%M')
    #returning the details in the form of a list
    return [size,gasUsed,gasLimit,transactionNumber,baseFeePerGas,difficulty,timestamp]

