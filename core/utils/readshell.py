

SHELL_PATH = "../backdoor/"

def read_shell(shell_name,shell_pass):
	shell_str = open(SHELL_PATH + shell_name , 'r').read()
	shell_str.replace('[passwd]',shell_pass)
	return shell_str
