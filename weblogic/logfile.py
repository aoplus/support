from java.lang import Boolean
from java.lang import System
from java.lang import Integer
username = System.getProperty("user","weblogic")
password = System.getProperty("password","weblogic")
adminHost = System.getProperty("adminHost","localhost")
adminPort = System.getProperty("adminPort","7001")
protocol = System.getProperty("protocol","t3")
url = protocol+"://"+adminHost+":"+adminPort
fileCount = Integer.getInteger("fileCount", 100)
fileMinSize = Integer.getInteger("fileMinSize", 5120)
fileName = System.getProperty("fileName","config\\mydomain\\myserver\\myserver.log")
log4jEnabled = System.getProperty("log4jEnabled", "true")
print "Connecting to " + url + " as [" + \
  username + "," + password + "]"
# Connect to the server
connect(username,password,url)
edit()
startEdit()
# set CMO to the server log config
cd("Servers/myserver/Log/myserver")
ls ()
print "Original FileCount is " + 'get("FileCount")'
print "Setting FileCount to be " + \QfileCount\Q
set("FileCount", fileCount)
print "Original FileMinSize is " + 'get("FileMinSize")'
print "Setting FileMinSize to be " + 'fileMinSize'
set("FileMinSize", fileMinSize)
print "Original Log4jEnabled is " + 'get("Log4jLoggingEnabled")'
print "Setting Log4jLoggingEnabled to be " + 'log4jEnabled'
set("Log4jLoggingEnabled", log4jEnabled)
save()
activate()
print
ls ()
# all done...
exit()
