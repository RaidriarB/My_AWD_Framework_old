import requests
import sys
import os
#print(os.getcwd())
#sys.path.append(os.getcwd().split("/attack")[0])

from utils import *
from payload import *
from submit import *

def attack_one(method,iplist):

	flags = []
	print("[+] 获取flag中...")
	print("-"*30)

	try:
		for ip in iplist:

			# 执行攻击脚本获取flag
			#flag = attacktest.attack_test1(ip)
			flag = method(ip)

			# 输出信息
			if flag == None:
				print("[x] 主机 {} 的flag没有获取到".format(ip))
			else:
				print("[√] 主机 {} 的flag获取成功！".format(ip))
				print(flag)
				flags.append((ip,flag))
			print("-"*30)

	except Exception as e:
		print("攻击脚本出错！出错脚本为【%s】"%method.__name__)
		
		#raise(e) #不需要抛出
	
	return flags

'''
攻击所有主机
攻击方法名需要手动指定
'''
def attack_all(iplist):
	all_round_flags = []

	try:
		attack_method = [
			attacktest.attack_test1,
			attacktest.attack_error_test1,
			attacktest.attack_test2
		]
	except Exception as e:
		raise(e)
		sys.exit("攻击方法名未定义")

	for method in attack_method:
		try:
			print("使用攻击脚本: 【%s】"%method.__name__)
			print("="*40)

			flags = attack_one(method,iplist)
			#print(flags)
			all_round_flags.append(flags)
			#print(all_round_flags)

		except Exception as e:
			print("方法出错："+method.__name__)
			raise(e)
		print("="*40)
	
	return all_round_flags