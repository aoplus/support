from sys import argv
execfile('jython/connect.py')

#query qname, if the message count in qname is 0, print the msgcnt as 0, if the msg count in qname is more than 0, delete messages.

qname = argv[1]
domainname = ['c41_Desktop_MS1', 'c41_Desktop_MS2']
qnames = ['com.seic.common.cachewf.orchestrator.LaserAppFormFeedOrchestrator', 'com.seic.common.cachewf.orchestrator.CacheReloadOrchestrator']
destname = ['DESKTOP-JMS-DEST!Desktop_c41_Desktop_MS1_JMSServer@com.seic.common.cachewf.orchestrator.CacheReloadOrchestrator', 'DESKTOP-JMS-DEST!Desktop_c41_Desktop_MS1_JMSServer@com.seic.common.cachewf.orchestrator.LaserAppFormFeedOrchestrator']
dest1stpart = 'DESKTOP-JMS-DEST'

def makeDestName(x, y, z):
    """ Create destination name to cd to.
    x = domainname
    y = dest1stpart
    z = qname
    """
    destName = y + '!Desktop'+x+'_JMSServer@' +z
    path = 'ServerRuntimes/' + x + '/JMSRuntime/' + x + ".jms/JMSServers" + x + "_JMSServer/Destinations" + destname
    print destName()
    print path()

def chkMsgsCnt(z):
    cd(x);
    if getMessagesCurrentCount() >0:
        cmsgcnt = getMessagesCurrentCount();
        print "%s: Current Msg Count is %s", %(qname, cmsgcnt())
        print "Deleting %s current messages", %(cmsgcnt)
    else:
        print "%s: Current Msg Count is %s", %(qname, getMessagesCurrentCount())
    if getMessgaesHighCount() >0:
        hmsgcnt = getMessagesHighCount();
        print "%s: High Msg Count is %s", (qname, hmsgcnt())
        print "Deleting %s high messages", %(hmsgcnt)
    else:
        print "%s: current msg count is %s", (qname, getMessagesCurrentCount())



        
servers = domainRuntimeService.getServerRuntimes();
if (len(servers) > 0):
    for server in servers:
        jmsRuntime = server.getJMSRuntime();
        jmsServers = jmsRuntime.getJMSServers();
        for jmsServer in jmsServers:
            destinations = jmsServer.getDestinations();
            for destination in destinations:
                destname = destination.getName()
                if qname in destname:
                    if destination.getMessagesCurrentCount() > 0:
                        msgcnt = destination.getMessagesCurrentCount()
                        print "No. of current messages in queue:", msgcnt
                        print "Deleting Messages"
                        destination.deleteMessages()
                        print "No. of Messages Deleted:" , msgcnt
                    else:
                        print "There are" + destination.getMessageCurrentCount() + "messages in the queue"
