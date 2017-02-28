from sys import argv

jmsservers=["Desktop_c41_Desktop_MS2_JMSServer", "Desktop_c41_Desktop_MS1_JMSServer"]
jmsQueueJNDIs=["com.seic.common.cachewf.orchestrator.CacheReloadOrchestrator", "com.seic.common.cachewf.orchestrator.LaserAppFormFeedOrchestrator"]

execfile('jython/connect.py')
domainRuntime()
qname = argv[1]
for jmsserver in jmsservers:
    # go to the path
    # print "ServerRuntimes/%s/JMSRuntime/%s.jms/JMSServers/%s/Destionations/DESKTOP-JMS-DEST!Desktop_%s_JMSServer@%s" % (jmsserver, jmsserver, jmsserver, jmsserver, qname)
    cd("ServerRuntimes/%s/JMSRuntime/%s.jms/JMSServers/%s/Destionations/DESKTOP-JMS-DEST!Desktop_%s_JMSServer@%s") % (jmsserver, jmsserver, jmsserver, jmsserver, qname)
    cmo.deleteMessages()
