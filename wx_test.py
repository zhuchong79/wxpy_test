# -*-coding:utf-8
import os
from wxpy import *
import json
import pandas
#bot = Bot()
#bot.file_helper.send("hello")
#@bot.register()
#def print_message(msg): 
#	print(msg.text) 
#	return msg.text
#embed()

bot = Bot(cache_path=True)
#embed()
def test1():
	friends=bot.friends()
	print friends.stats()
	friends_stat = bot.friends().stats()
	print json.dumps(friends.stats)#,encoding='GBK')
	friend_loc = [] # 每一个元素是一个二元列表，分别存储地区和人数信息
	for province, count in friends_stat["province"].iteritems():
		if province != "":
			friend_loc.append([province, count])

	# 对人数倒序排序
	friend_loc.sort(key=lambda x: x[1], reverse=True)

	# 打印人数最多的10个地区
	for item in friend_loc[:10]:
	 print item[0], item[1]

def test2():
	global bot
	for i in bot.friends():
		print i
def test3():
	for i in bot.friends():
		for name,value in vars(i).items():
			#print type(name),type(value)
			#print name,value
			if type(value) == dict and value :
				print value[u'NickName'].encode('utf-8')
				ps=pandas.Series(value)
				print ps
			
test3()