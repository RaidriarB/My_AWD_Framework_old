import requests
import sys
import os
#print(os.getcwd())
#sys.path.append(os.getcwd().split("/attack")[0])

from utils import *
from payload import *
from submit import *

'''
使用单个payload攻击target_list中所有主机
'''
def attack_one(method,target_list):

	flags = []
	success_attack = 0
	fail_attack = 0

	print("  [+] 获取flag中...")

	try:
		for target in target_list:

			# 执行攻击脚本获取flag
			flag = eval("getflag." + method)(target)

			# 输出信息
			if flag == None:
				fail_attack += 1
				print("  [x] 主机 {} 的flag没有获取到".format(target))
			else:
				success_attack += 1
				print("  [√] 主机 {} 获取成功！".format(target)+flag)
				flags.append((target,flag))

	except Exception as e:
		print("攻击脚本出错！出错脚本为【%s】"%method)
		#raise(e) #不需要抛出
	
	print("\n  [!] 攻击完毕，成功获取{}个，失败获取{}个".format(success_attack,fail_attack))
	
	return flags

'''
用所有payload攻击所有主机
攻击方法名需要手动指定
'''
def attack_all(target_list):

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

			flags = attack_one(method,target_list)
			all_round_flags.append(flags)

		except Exception as e:
			print("方法出错：" + method)
			raise(e)
		print("="*40)
	
	return all_round_flags

def put_backdoor_all(method,target_list):
	pass

def exp_backdoor_all(target_list):
	pass