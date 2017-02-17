from sys import argv
execfile('jython/connect.py')

qname = argv[1]
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
