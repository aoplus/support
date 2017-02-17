from java.lang import Boolean
from java.lang import System
from java.lang import Integer

execfile('jython/connect.py')  #String to connect to the weblogic server.


domainConfig()
servers=cmo.getServers()

def updateHTTPlog(x):
    """
    Function to update the http log files for weblogic domain
    """
    print '======= Enabling webserver Log Retention for ' + serverName + '======='
    cd('/Servers/'+x+'/WebServer/'+x+'/WebServerLog/'+x) # change directory to the servers webserver log path
    cmo.setLoggingEnabled(true) # ENable logging
    cmo.setNumberOfFilesLimited(true) # Enable the retention of log files.
    cmo.setFileCount('100')  #number of http log files to be retained.

def updateGeneralLog(x):
    """
    function to update the general logs.
    """
    print '======= Enabling Log Retention for ' + serverName + '======='
    cd('/Servers/'+x+'/Log/'+x) # Change directory to weblogic server's general log location.
    cmo.setLog4jLoggingEnabled(true)  # Enable logging
    cmo.setNumberOfFilesLimited(true) # ENable the retention of log files
    cmo.setFileCount('100')  #Set the number of files to be retained.

for x in servers:
    try:
        edit()
        startEdit()
        serverName = x.getName()
        if serverName is not 'adminserver': # test to check if the serverName is not adminserver and then run the below commands.
            updateGeneralLog(serverName)
            updateHTTPlog(serverName)
        save()
        activate()
        print ' '
        
        print ' '
        ls()
    except java.lang.Exception, ex:
        print 'Exception on Changing the Log Attributes: ' + ex.toString()
        save()

# all done...
exit()

