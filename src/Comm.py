import bluetooth
import Config
import Debugger
import sys
import time

class Comm:
    
    def __init__(self, address, port):
        Debugger.printAction( 'Initializing Comm' )
        if Config.ENABLE_COMM:
            Debugger.printAction( 'Attempting to open bluetooth socket at '+str(address)+', port '+str(port) )
            Debugger.printAction( 'Wait...')
            self.sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            try:
                self.sock.connect( (address, port) )
            except IOError:
                print '\nERROR: Unable to open bluetooth socket, the application will terminate with -1 status code'
                sys.exit(-1)
                
            Debugger.printAction( 'Success!')
        else:
            Debugger.printAction( 'Attempting to open DUMMY bluetooth socket at '+str(address)+', port '+str(port) )
            Debugger.printAction( 'Wait...')
            time.sleep(0.5)
            Debugger.printAction( 'Success!')
        
    def sendCommand(self, command):
        
        Debugger.printCommand( 'S: '+str(command) )
        
        if Config.ENABLE_COMM == False:
            s = 'X,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15'
            Debugger.printCommand( 'R: '+s )
            return s
        
        self.sock.send(command+'\r')
        s = ""
        c = '0'
        while(c!='\r') :
            c = self.sock.recv(1)
            s = s + str(c)
        
        s = s[0:len(s)-2] # removing \n\r
        
        Debugger.printCommand( 'R: '+s )
        
        return s
        
    def close(self):
        if Config.ENABLE_COMM == False:
            return
        self.sock.close()