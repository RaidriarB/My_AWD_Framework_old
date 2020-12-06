import requests
import sys
import os
#print(os.getcwd())
#sys.path.append(os.getcwd().split("/attack")[0])

from utils import *
from payload import *
from submit import *
from attack import *


config = "../conf/config"
iplist = []
self_ip = None

def init():
	global iplist
	global self_ip

	try:
		iplist = Config.load_ip_list(config)
	except Exception as e:
		print("读取被攻击主机列表失败！")
		raise(e)
		sys.exit("程序正在退出..")
	
	try:
		self_ip = Config.load_self_ip(config)
	except Exception as e:
		print("读取被攻击主机列表失败！")
		raise(e)
		sys.exit("程序正在退出..")
	
	for ip in iplist:
		if self_ip in ip:
			iplist.remove(ip)
	

def gather_flags(all_round_flags):
	flagset = set()
	for flags in all_round_flags:
		for pair in flags:
			flagset.add(pair)
	return flagset

def show_info():
	print("调试信息")
	print("自己的ip为{}"%self_ip)
	print("待进攻的ip列表如下:")
	for ip in iplist:
		print(ip)


def main():
	init()
	print("[!] 初始化完成，iplist为")
	all_round_flags = attack.attack_all(iplist)
	print("进攻完毕，flag汇总如下")
	flagset = gather_flags(all_round_flags)
	import pprint
	pprint.pprint(flagset)
	print("提交所有flag")
	submit_all.submit_all(flagset)



if __name__ == '__main__':
	main()