import Config


def printCommand( text ):
    if Config.DEBBUGER_PRINT_COMMAND:
        print 'COMMAND: ' + text
    
def printAction( text ):
    if Config.DEBBUGER_PRINT_ACTION:
        print 'ACTION: ' + text
        
def printConfig( name, value ):
    if Config.DEBBUGER_PRINT_CONFIG:
        print '' + str(name)+' = ' + str(value)