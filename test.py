# *-*coding:utf-8
# *-*coding:utf-8
import os,sys,io
from wxpy import *
import pandas as pd

import matplotlib.image as mpimg
import matplotlib.pyplot as plt 

#sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
reload(sys)
sys.setdefaultencoding('utf-8')

def showpic(uuid, status, qrcode):
	print 'showpic',uuid#, status, qrcode
	lena=mpimg.imread("qr.png")
	plt.imshow(lena)
	return uuid, status, qrcode
def login_callback(): #afer logged
	pass
def qr_callback():#afer got qr
	pass
bot=Bot(cache_path=False,
#qr_path="./",
qr_callback=showpic)
bot.auto_mark_as_read = True


my_friend = bot.friends().search(u'风')[0]                                                               
tuling = Tuling(api_key='562fbf9b0c0d4b61ada837fa5f2f83b4')
@bot.register(my_friend)
def reply_my_friend(msg):
    tuling.do_reply(msg)
	
#embed()


friends=bot.friends()
f1=bot.friends()[0]
f2=bot.friends()[1]
df = pd.DataFrame(f1.raw)
# for f in bot.friends():
	# df=df.append(pd.Series(f.raw),ignore_index=True)
# print df

#regitster message event
@bot.register()
def print_message(msg): 
	print(msg.text) #print msg
	return u"recieved:"+msg.text	#reply msg
embed()
embed()
