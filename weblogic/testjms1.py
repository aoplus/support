
#Connect
execfile('jython/connect.py')
 
#Switch to the server runtime tree
serverRuntime()
 
#Navigate to the JMS Destination Runtime MBean
cd('JMSRuntime/' + serverName + '.jms/JMSServers/' + jmsservername)
cd('Destinations/' + jmsmodulename + '!' +  jmsdestname)
 
#Get the cursor (JMSMessageCursorRuntimeMBean) to browse the messages - No selector & No time out
cursor = cmo.getMessages('',0)
 
#Determine the number of messages in the destination
cursorsize = cmo.getCursorSize(cursor)
print '------------------------------------------'
print 'Total Number of Messages -> ', cursorsize
print '------------------------------------------'
 
#Get all the messages as an array of javax.management.openmbean.CompositeData
messages = cmo.getNext(cursor, cursorsize)
 
#Loop through the array of messages to print
for message in messages:
    #Create WebLogic JMSMessageInfo to get Message ID
    jmsmsginfo = JMSMessageInfo(message)
    wlmsg = jmsmsginfo.getMessage()
    wlmsgid = wlmsg.getJMSMessageID()
    #Get Message with body
    fullcursormsg = cmo.getMessage(cursor,wlmsgid)
    fulljmsmsginfo = JMSMessageInfo(fullcursormsg)
    handle = fulljmsmsginfo.getHandle()
    compdata = cmo.getMessage(cursor, handle)
    msgwithbody = JMSMessageInfo(compdata)
    #Print Key Message Headers
    print 'Message ID           - ' + msgwithbody.getMessage().getJMSMessageID()
    print 'Message Priority     -' , msgwithbody.getMessage().getJMSPriority()
    if msgwithbody.getMessage().getJMSRedelivered() == 0:
        redeliv = 'false'
    else:
        redeliv = 'true'
        print 'Message Redelivered  - ' + redeliv
        print 'Message TimeStamp    -' , msgwithbody.getMessage().getJMSTimestamp()
        print 'Message DeliveryMode -' , msgwithbody.getMessage().getJMSDeliveryMode()
 
    #Print Message Properties
    prop_enum = msgwithbody.getMessage().getPropertyNames()
    print ' '
    print 'Message Properties   :'
    print ' '
    for prop in prop_enum:
        print prop + ' - > ' + msgwithbody.getMessage().getStringProperty(prop)
        #Print Message Body
        fullwlmsg = fulljmsmsginfo.getMessage()
        print ' '
        print 'Message Body         :'
        print ' '
        if isinstance(fullwlmsg, TextMessage):
            print fullwlmsg.getText()
        else:
            if isinstance(fullwlmsg, ObjectMessage):
                print fullwlmsg.getObject()
            else:
                print '***Not a Text or Object Message***'
                print fullwlmsg.toString()
                print ' '
                print '--------------------------------------------------------------'
                print ' '
                
            #Close cursor as No Time Out specified - Best practice
            cmo.closeCursor(cursor)
 
#Disconnect & Exit
disconnect()
exit()


