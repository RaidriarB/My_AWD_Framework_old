import requests
from submit import submit

'''
提交所有flag的函数，该文件不需要更改。
'''
def submit_all(all_round_flags):
	success_submit = 0
	fail_submit = 0
	for flags in all_round_flags:
		for pair in flags:
			host = pair[0]
			flag = pair[1]
			#print("host:{},flag:{}".format(host,flag))
			if submit.submit_flag(host=host,flag=flag) == True:
				print("[√] 主机{}的flag提交成功！".format(host))
				success_submit += 1

			else:
				print("[x] 主机{}的flag提交失败！".format(host))
				fail_submit += 1
	print("本轮提交完成，成功提交{}个，失败提交{}个".format(success_submit,fail_submit))
