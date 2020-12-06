import requests
import sys
import os
#print(os.getcwd())
#sys.path.append(os.getcwd().split("/attack")[0])

from utils import *
from payload import *
from submit import *
from attack import *


target_list = []
self_host = None
shell_pass = None

'''
初始化
读取待攻击的目标和自己的主机
'''
def init():
	global target_list
	global self_host
	global shell_pass

	try:
		target_list = Config.load_target_list()
	except Exception as e:
		print("读取被攻击主机列表失败！")
		raise(e)
		sys.exit("程序正在退出..")
	
	try:
		self_host = Config.load_self_host()
	except Exception as e:
		print("读取本机ip失败！")
		raise(e)
		sys.exit("程序正在退出..")

	try:
		shell_pass = Config.load_shell_pass()
	except Exception as e:
		print("读取shell密码失败！")
		raise(e)
		sys.exit("程序正在退出..")
	
	for target in target_list:
		if self_host in target:
			target_list.remove(target)
	
'''
去除重复的flag值，存入集合flagset
'''
def gather_flags(all_round_flags):
	flagset = set()
	for flags in all_round_flags:
		for pair in flags:
			flagset.add(pair)
	return flagset

'''
打印配置信息等
'''
def show_info():
	print("调试信息")
	print("自己的主机为%s"%self_host)
	print("待进攻的目标列表如下:")
	for target in target_list:
		print(target)
	print("shell的密码为:【%s】"%shell_pass)


def main():
	init()
	show_info()
	print("[!] 初始化完成，target_list为")
	all_round_flags = attack.attack_all(target_list)
	print("进攻完毕，flag汇总如下")
	flagset = gather_flags(all_round_flags)
	import pprint
	pprint.pprint(flagset)
	print("提交所有flag")
	submit_all.submit_all(flagset)



if __name__ == '__main__':
	main()