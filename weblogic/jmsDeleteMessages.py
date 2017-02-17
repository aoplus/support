execfile('jython/connect.py')
servers = domainRuntimeService.getServerRuntimes();
if (len(servers) > 0):
    for server in servers:
        jmsRuntime = server.getJMSRuntime();
        jmsServers = jmsRuntime.getJMSServers();
        for jmsServer in jmsServers:
            print 'Jms Servename'
            print jmsServer
            print ''
            print ''
            destinations = jmsServer.getDestinations();
            for destination in destinations:
                print '+++++++ Destinations ++++++++'
                destname = destination.getName()
                if com.seic.common.cachewf.orchestrator.LaserAppFormFeedOrchestrator in destname:
                #print dir(destination)
                # print destination.getDestination()
                    print destination.getName()
                    print destination.getParent()
