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

def init():
	global iplist
	try:
		iplist = Config.load_ip_list(config)
	except Exception as e:
		print("读取被攻击主机列表失败！")
		raise(e)
		sys.exit("程序正在退出..")

def main():
	init()
	print("[!] 初始化完成，iplist为")
	print(iplist)
	print("准备进攻全场")
	all_round_flags = attack.attack_all(iplist)
	print("进攻完毕，flag汇总如下")
	import pprint
	pprint.pprint(all_round_flags)
	print("提交所有flag")
	submit_all.submit_all(all_round_flags)



if __name__ == '__main__':
	main()