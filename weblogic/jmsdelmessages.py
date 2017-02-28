
from sys import argv
from weblogic.jms.extensions import JMSMessageInfo
from javax.jms import TextMessage
from javax.jms import ObjectMessage

execfile('jython/connect.py')

qname = argv[1]
domainRuntime()
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
                    if destination.getMessagesPendingCount() > 0:
                        msgcnt = destination.getMessagesPendingCount()
                        cursor = destination.getMessages('',0)
                        cursorsize = destination.getCursorSize(cursor)
                        messages = destination.getNext(cursor, cursorsize)
                        for message in messages:
                                jmsmsginfo = JMSMessageInfo(message)
                                wlmsg = jmsmsginfo.getMessage()
                                wlmsgid = wlmsg.getJMSMessageID()
                                print str(wlmsgid) +":"+ str(wlmsg)
                                #Get Message with body
                                fullcursormsg = destination.getMessage(cursor,wlmsgid)
                                fulljmsmsginfo = JMSMessageInfo(fullcursormsg)
                                handle = fulljmsmsginfo.getHandle()
                                compdata = destination.getMessage(cursor, handle)
                                msgwithbody = JMSMessageInfo(compdata)
                                #Print Key Message Headers
                                print 'Message ID           - ' + msgwithbody.getMessage().getJMSMessageID()
                                print 'Message Priority     -' , msgwithbody.getMessage().getJMSPriority()
				edit()
				startEdit()
                                destination.deleteMessages(wlmsgid)
                        print destination
                        exit()
                        # print destination.getParent()
                        # print destination.getMessages('',0)
                        # print "No. of current messages in queue: ", msgcnt
                        # print "Deleting Messages"
                        # destination.deleteMessages( '' )
                        #print "No. of Messages Deleted: " , destination.getMessagesDeletedCurrentCount()
                    else:
                        print "There are " + str(destination.getMessagesPendingCount()) + " messages in the queue"


