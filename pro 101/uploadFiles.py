import dropbox
import os 
from  dropbox.files  import WriteMode

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)
        for root,dirs,files in os.walk(file_from):
            for filename in files:
                local_path=os.join(root,filename)
                relative_path=os.path.relpath(local_path,file_From)
            dropbox_path=os.path.join(file_to,relative_path)
            with open(file_from, 'rb') as f:
                dbx.files_upload(f.read(), dropbox_path,mode=WriteMode('overwrite'))

def main():
    access_token = 'sl.BHTMxgJHCWtBcp_9WpwbdmL1ETlWLSUpllRLrPLM6OApEY6htromN4gvF6sB8e6zQiXXpM3UD7YqjDrWVIyhe8kqNjx7zYW79D9LdK_7ypq8AL6t-c6x0rkEJwwdDkfOw3HzhWViC55l'
    transferData = TransferData(access_token)
    
    file_from = str(input("enter the file path transfer"))
    file_to = input("enter the full path to upload to dropbox")  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)
    print("file has been moved to cloud storage..")

if __name__ == '__main__':
    main()