from sys import argv
execfile('jython/connect.py')

qname = argv[1]  # Take the argument from command line
servers = domainRuntimeService.getServerRuntimes(); # check the servers and keep it in servers vriable, the server is going to be a list, i.e. there would be multiple servers.
if (len(servers) > 0): # check if the there are more tahn 0 server. i.e. this is a check to ensure we are only checking the server.
    for server in servers: # now we iterate over servers.
        jmsRuntime = server.getJMSRuntime(); # from the server, get the server JMSRuntime info
        jmsServers = jmsRuntime.getJMSServers(); # from every server collect the JMS servers, i.e. JMS=Java Messaging service 
        for jmsServer in jmsServers: #now iterate overjmsservers
            destinations = jmsServer.getDestinations(); # collect the JMSserverDestination, which is c41_gwm_desktop!c41_GWMP_Desktop_MS1 etc.
            for destination in destinations: #iterate over the detstination
                destname = destination.getName() # add the desinationname in destination variable.
                if qname in destname: #check wether the argument given on command line matches the quename.
                    if destination.getMessagesCurrentCount() > 0: # if the above match works, then check the message count, if the message count is more than 0, 
                        msgcnt = destination.getMessagesCurrentCount() # get the no. of matches att this into a variable.
                        print "No. of current messages in queue:", msgcnt # print the no. of sg present.
                        print "Deleting Messages"
                        destination.deleteMessages() # Delete the messages from the message queues.
                        print "No. of Messages Deleted:" , msgcnt
                    else:
                        print "There are" + destination.getMessageCurrentCount() + "messages in the queue" # if the destionation.getMessagecurrentCount is 0 just print this line, saying there are no messages.
