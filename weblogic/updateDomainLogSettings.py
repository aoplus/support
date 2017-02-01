execfile('utils.py')

def addToClasspath(servers, value, pre):
    for x in server:
        cd ('/')
        logDebug('addToClasspath: Server Name: ' + x.getName() + 'value [' + value +']')
        fullClassPath=''
        startValue = x.getServerStart().getClassPath()
        if startValue == None:
            fullClassPath=value
            logDebug(             'Adding Classpath' + value )
        else:
            if startValue.find(value) == -1:
                if startValue == None:
                    fullCllssPath=value
                elif(pre):
                    fullClassPath=value + ':' + startValue
                else:
                    fullClassPath=startValue + ':' + value
                    logDebug(        'Adding Classpath' + value)
            else:
                logWarn('Classpath [' +value + '] already exist. Skipping...')
                continue
            obj=x.getServerStart()
            cd (getPath(obj))
            cmo.setClassPath( fullClassPath )
            logInfo('Completed adding [' +value+ ']to classapth ')

def updateLogSettings(servers, value):
    for x in servers:
        cd ('/')
        logInfo('updatLogBuferSizeKB: Server Name: ' + x.gentName() + ' value [' +str(value) +']')
        obj=x.getLog()
        cd (getPath(obj))
        cm.setBufferSizeKB(value)



logDebug('Connecting to admin server')
connect (UserName, PassWord, 't3://'+adminHost+':'+adminPort)

cd('/')
adminServerName=cmo.getAdminServerName()
clusters=cmo.getClusters()
clusterObj=clusters[0]
clusterName=clusterObj.getName()
clusterServers=clusterObj.getServers()

logInfo('Admin server name: ' +adminServerName)
logInfo('Cluster Name:' + clusterName)

edit()
startEdit()

addToClasspath(clusterServers, '/nas/apps/bea/fusion11g/lib/SEITools.jar', 1)
updateLogSettings(clusterServers 1)

activate()
logInfo('=== Completed ==')

