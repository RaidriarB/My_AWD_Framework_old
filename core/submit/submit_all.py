import requests
import time
from submit import submit


'''
提交所有flag的函数，该文件不需要更改。
'''
def submit_all(flagset):

	success_submit = 0
	fail_submit = 0

	for pair in flagset:
		time.sleep(0.1)
		target = pair[0]
		flag = pair[1]
		if submit.submit_flag(target=target,flag=flag) == True:
			print(" [√] 提交{}的{}成功！".format(target,flag))
			success_submit += 1
		else:
			print("[x] 提交{}的{}失败！".format(target,flag))
			fail_submit += 1

	print("本轮提交完成，成功提交{}个，失败提交{}个".format(success_submit,fail_submit))

