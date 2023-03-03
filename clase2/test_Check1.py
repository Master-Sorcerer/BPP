import pytest
from Check1 import sender,scanner,checker

def test_checker():
    with open("filepytest.log", "w") as f:
        #Writes a file with  public, invalid and duplicated  proper ip
	    f.write("8.8.8.8 \n 192.168.0.1 \n 290.23.13.4 \n 192.168.0.1")
    listest=checker(logfolder='./')
    #Checks that only one valid entry is there
    assert listest== ['192.168.0.1']
    assert len(listest) == 1

def test_scanner():
    #test the scanner with the google.com ip address and port
	assert scanner(ip_list=["142.250.200.14"]) == ["142.250.200.14: 80"]


def test_sender():
    import base64
    import paramiko
    from cryptography.fernet import Fernet
    #creates a test list containing a string
    my_list=['testing']
    #calls the sender function with the test list, sender returns fernet object
    fernet = sender(my_list=my_list)
    #opens the file created by the function and reads it before its encrypted 
    with open ("info.txt","r") as f:
        list= f.readlines()
    string = "testing"
    assert (string in list[0]) == True 
    #retrieve the file after is sent encrypted
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect("192.168.0.75", username="User", password="password123")
    sftp =ssh.open_sftp()
    sftp.get("C:\/Users\/User\/infotext","encryptedtext")
    #Opens the file and decrypts it with the key provided
    with open ("encryptedtext", "rb") as f:
        data=f.read()
    #key = base64.urlsafe_b64decode (bytes(info[0].rstrip().encode(), 'utf-8'))
    #datax = bytes(data, 'utf-8')
    #fernet= Fernet(key)
    decrypted =fernet.decrypt(data)
    print(decrypted.decode('utf-8'))
    assert (string in decrypted.decode('utf-8')) == True


