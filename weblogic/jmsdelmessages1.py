from javax.naming import Context, InitialContext
from weblogic.jndi import WLInitialContextFactory
from javax.jms import QueueSession, Queue, Session

# msservers=["myhost1:8001", "myhost2:8001", "myhost3:8001", "myhost4:8001"]
jmsservers=["Desktop_c41_Desktop_MS2_JMSServer", "Desktop_c41_Desktop_MS1_JMSServer"]
jmsQueueJNDIs=["com.seic.common.cachewf.orchestrator.CacheReloadOrchestrator", "com.seic.common.cachewf.orchestrator.LaserAppFormFeedOrchestrator"];

# for i in range(len(msservers)):
    # msserver = msservers[i] 

    jmsserver = jmsservers[i]
    properties = Properties()
#    properties[Context.PROVIDER_URL] = "t3://" + msserver
#    properties[Context.INITIAL_CONTEXT_FACTORY] = WLInitialContextFactory.name
#    print "connecting to " + msserver + "..."
    ctx = InitialContext(properties)
    print "successfully connected to ", msserver
    
    connectionFactory = ctx.lookup("weblogic/jms/XAConnectionFactory" )
    queueCon = connectionFactory.createQueueConnection();
    queueCon.start()
    queueSession = queueCon.createQueueSession( false, Session.AUTO_ACKNOWLEDGE );
    for jmsqueue in jmsQueueJNDIs:
        theJNDI = jmsserver + "@" + jmsqueue
        queue = ctx.lookup(theJNDI)
        
        queueReceiver = queueSession.createReceiver(queue) # "ISTEST='true'"
        condition = True
        print "deleting messages from " + theJNDI
        while (condition):
            message = queueReceiver.receiveNoWait()
            if (message != None):
                print 'ack on message'
                message.acknowledge();
            condition = (message != None)
          

