from java.util import Date
 
 
def conn():
try:
  execfile('jython/connect.py')
except ConnectionException,e:
 print 'Unable to find admin server...'
 exit()
def initalize():
 serverlist= ['app010','app011',...]
 for svr in serverlist:
 cd("/Servers/"+svr)
 urldict[svr]='t3://'+get('ListenAddress')+':'+str(get('ListenPort'))
 
def JmsStat():
 d = Date() # now
 print  d 
 
 print 'Instance         ConCur ConHi ConTot High  MsgCur MsgPnd'
 print 'Name             Count  Count Count  Count Count  Count'
 print '===========**=======**=================================='
 Ks = urldict.keys()
 Ks.sort()
 
 for key in Ks:
  try:
   connect(userConfigFile=ucf, userKeyFile=ukf,url=urldict[key])
   serverRuntime()
   cd('JMSRuntime/'+key+'.jms/JMSServers')
   curCnt= get('ConnectionsCurrentCount')
   cHiCnt=get('ConnectionsHighCount')
   cTotCnt=get('ConnectionsTotalCount')
 
   myJmsls=ls(returnMap='true')
   x=myJmsls[0]
   cd(x)
 
   hiCnt= get('MessagesHighCount')
   currCnt= get('MessagesCurrentCount')
   pendCnt= get('MessagesPendingCount')
   print '%14s   %4d   %4d  %4d  %4d  %4d  %4d' %  (key, curCnt, cHiCnt, cTotCnt,  hiCnt, currCnt, pendCnt) 
  except:
   print 'Exception...in server:', key
   pass
 quit()
 
def quit():
 d = Date() # now
 print  d
 print 'Hit any key to Re-RUN this script ...'
 Ans = raw_input("Are you sure Quit from WLST... (y/n)")
 if (Ans == 'y'):
  disconnect()
  stopRedirect() 
  exit()
else:
 JmsStat()
 
if __name__== "main":
 redirect('./logs/jmsCnt.log', 'false')
 conn()
 initalize()
 JmsStat()
