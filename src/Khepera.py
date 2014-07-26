from Comm import *
import Config
import Debugger

class Khepera:
    
    def __init__(self, address, port):
        Debugger.printAction('Initializing Khepera robot API' )
        self.comm = Comm(address, port)
        software = self.readSoftwareVersion()
        Debugger.printAction('Khepera software: Bios ' + str( software[0]) + ', Revision ' + str( software[1]) )
        Debugger.printAction('Initializing motors')
        self.initMotors()
        
        
    def setMotorSpeeds(self, left, right):
        
        s = self.comm.sendCommand('D,l'+str(left)+',l'+str(right))
        return True
        
    def getGroundSensors(self):
        """Returns Ground Ambient sensors value, right then left"""
        return self.getProximitySensors()[9:11]
    
    def getProximitySensors(self):
        """val sens back left, val sens left 90, val sens left 45,
        val sens front left, val sens front right, val sens right 45,
        val sens right 90, val sens back right, val sens back,
        val sens ground right, val sens ground left, time stamp"""
        s = self.comm.sendCommand('N')
        return s.split(',')[1:]

    def getFrontProximitySensors(self):
        """First left then right"""
        return self.getProximitySensors()[3:5]
    
    def enableDiode(self, enabled):
        if enabled == True:
            v = 1
        else:
            v = 0
            
        self.comm.sendCommand('K,0,'+str(v))
        return
    
    def initMotors(self):
        s = self.comm.sendCommand('M')
    
    def readSoftwareVersion(self):
        s = self.comm.sendCommand('B')
        return s.split(',')[1:]