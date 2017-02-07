from java.lang import Boolean
from java.lang import System
from java.lang import Integer

execfile('jython/connect.py')


domainConfig()
servers=cmo.getServers()

for x in servers:
    try:
        edit()
        startedit()
        serverName = x.getName()
        print '======= Enabling webserver Log Retention for ' + serverName + '======='
        cd('/Servers/'+serverName+'/WebServer/'+serverName+'/WebServerLog/'+serverName)
        cmo.setLoggingEnabled(true)
        cmo.setNumberOfFilesLimited(true)
        cmo.setFileCount('100')
        cmo.FileMinSize('5000')
        print '======= Enabling Log Retention for ' + serverName + '======='
        cd('/Servers/'+serverName+'/Log/'+serverName)
        cmo.setLoggingEnabled(true)
        cmo.setNumberOfFilesLimited(true)
        cmo.setFileCount('100')
        cmo.FileMinSize('5000')
        save()
        activate()
        print ' '
        print ' '
        ls()
    except:
        java.lang.Exception, ex:
        print 'Exception on Changing the Log Attributes: ' + ex.toString()
        save()

# all done...
exit()

