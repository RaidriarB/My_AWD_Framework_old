from payload import *

s = dir(getflag)

import operator

for k in s:
	if not k.startswith("__"):
		eval("getflag."+k)(["127.0.0.1","127.0.0.2"])
