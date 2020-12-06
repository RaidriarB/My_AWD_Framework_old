CONFIG_FILE = "./../conf/config"

def load_config():
	conf_dict = {}
	with open(CONFIG_FILE,"r") as config:
		text = config.read()
		lines = text.split("\n")

		for line in lines:
			# 跳过空行
			if line.strip() == "":
				continue

			# 解析key-value
			key,value = line.split("=")[0].strip(),line.split("=")[1].strip()
			#print(key,value)
			conf_dict[key] = value
	return conf_dict

def load_target_list():
	config_dict = load_config()
	
	# 列表生成式格式
	target_rules = config_dict["target_list"]
	target_list = eval(target_rules)
	return target_list

def load_self_host():
	config_dict = load_config()
	self_host = config_dict["self_host"]
	return self_host

def load_shell_pass():
	config_dict = load_config()
	shell_pass = config_dict["shell_pass"]
	return shell_pass