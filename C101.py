import dropbox
class TransferData:
    def __init__(self,accessToken):
        self.accessToken=accessToken
    
    def uploadFile(self,FileFrom,FileTo):
        dbx=dropbox.Dropbox(self.accessToken)
        f=open(FileFrom,'rb')
        dbx.files_upload(f.read(),FileTo)


def main():
    accessToken='sl.A2BgnVbi6Mbfe2g8Fxt24XHRUrubuNEfPC_gxei46GL9TCcnG-pdRURHGCQn-vaCtaaGEwvNQvJpdnP1iNy-BSXJh4MP5VlKON0C4IUnU_KrS2mmEfMaUZaBgrK3xClXMgCozHU'
    transferdata=TransferData(accessToken)
    FileFrom=input('Enter the file path to transfer')
    FileTo=input('Enter the file path to upload to dropbox')
    transferdata.uploadFile(FileFrom,FileTo)
    print('file has been moved to the dropbox')