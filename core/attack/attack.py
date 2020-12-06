import requests
import sys
import os
#print(os.getcwd())
#sys.path.append(os.getcwd().split("/attack")[0])

from core.utils import *
from core.payload import *
from core.submit import *

'''
使用单个payload攻击iplist中所有主机
'''
def attack_one(method,iplist):

	flags = []
	print("  [+] 获取flag中...")
	print("  "+"-"*30)

	try:
		for ip in iplist:

			# 执行攻击脚本获取flag
			flag = eval("getflag." + method)(ip)

			# 输出信息
			if flag == None:
				print("  [x] 主机 {} 的flag没有获取到".format(ip))
			else:
				print("  [√] 主机 {} 的flag获取成功！".format(ip))
				print("  "+flag)
				flags.append((ip,flag))
			print("  "+"-"*30)

	except Exception as e:
		print("攻击脚本出错！出错脚本为【%s】"%method)
		#raise(e) #不需要抛出
	
	return flags

'''
用所有payload攻击所有主机
攻击方法名需要手动指定
'''
def attack_all(iplist):
	all_round_flags = []
	attack_method = []

	# 获取attack/getflag.py的所有方法
	ori_method = dir(getflag)
	for met in ori_method:
		if not met.startswith("__"):
			if met.startswith("attack"):
				attack_method.append(met)

	for method in attack_method:
		try:
			print("使用攻击脚本: 【%s】" % method)
			print("="*40)

			flags = attack_one(method,iplist)
			all_round_flags.append(flags)

		except Exception as e:
			print("方法出错：" + method)
			raise(e)
		print("="*40)
	
	return all_round_flags