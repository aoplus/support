from sys import argv
execfile('jython/connect.py')

#query qname, if the message count in qname is 0, print the msgcnt as 0, if the msg count in qname is more than 0, delete messages.

qname = argv[1]
domainname = ['c41_Desktop_MS1', 'c41_Desktop_MS2']
qnames = ['com.seic.common.cachewf.orchestrator.LaserAppFormFeedOrchestrator', 'com.seic.common.cachewf.orchestrator.CacheReloadOrchestrator', 'GMH.JMS.INPUT.QUEUE']
# destname = ['DESKTOP-JMS-DEST!Desktop_c41_Desktop_MS1_JMSServer@com.seic.common.cachewf.orchestrator.CacheReloadOrchestrator', 'DESKTOP-JMS-DEST!Desktop_c41_Desktop_MS1_JMSServer@com.seic.common.cachewf.orchestrator.LaserAppFormFeedOrchestrator']
# dest1stpart = 'DESKTOP-JMS-DEST'

def makeDestName(x,z):
    """ Create destination name to cd to.
    x = domainname
    z = qname
    """
    destName = "DESKTOP-JMS-DEST!Desktop_" + x + "_JMSServer@" +z
    path = "ServerRuntimes/" + x + "/JMSRuntime/" + x + ".jms/JMSServers/Desktop_c41_" + x + "_JMSServer/Destinations/" + destName
    print path

def chkdelCurMsgCnt():
    if getMessagesCurrentCount() >0:
        cmsgcnt = cmo.getMessagesCurrentCount();
        print "%s: Current Msg Count is %s", (qname, cmsgcnt)
        print "Deleting %s current messages", cmsgcnt
#        cmo.deleteMessages('')
    else:
        print "%s: Current Msg Count is %s",  (qname, cmo.getMessagesCurrentCount())

def chkdelHighMgcnt():
    if getMessgaesHighCount() >0:
        hmsgcnt = cmo.getMessagesHighCount();
        print "%s: High Msg Count is %s", (qname, hmsgcnt)
        print "Deleting %s high messages",  hmsgcnt
#        cmo.deleteMessages('')
    else:
        print "%s: current msg count is %s", (qname, cmo.getMessagesCurrentCount())


if qname in qnames:
    for domain in domainname:
        qpath = makeDestName(domain, qname)
        print qpath
        bean = getMBean(qpath)
        print bean
        # cd(qpath)
        chkdelCurMsgCnt()
##############################################################################################################
# servers = domainRuntimeService.getServerRuntimes();                                                        #
# if (len(servers) > 0):                                                                                     #
#     for server in servers:                                                                                 #
#         jmsRuntime = server.getJMSRuntime();                                                               #
#         jmsServers = jmsRuntime.getJMSServers();                                                           #
#         for jmsServer in jmsServers:                                                                       #
#             destinations = jmsServer.getDestinations();                                                    #
#             for destination in destinations:                                                               #
#                 destname = destination.getName()                                                           #
#                 if qname in destname:                                                                      #
#                     if destination.getMessagesCurrentCount() > 0:                                          #
#                         msgcnt = destination.getMessagesCurrentCount()                                     #
#                         print "No. of current messages in queue:", msgcnt                                  #
#                         print "Deleting Messages"                                                          #
#                         destination.deleteMessages()                                                       #
#                         print "No. of Messages Deleted:" , msgcnt                                          #
#                     else:                                                                                  #
#                         print "There are" + destination.getMessageCurrentCount() + "messages in the queue" #
##############################################################################################################
