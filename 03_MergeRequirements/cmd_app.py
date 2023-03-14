import cowsay
import shlex
import cmd

def parce(string):
	return shlex.split(string)
	

BASE_COWSAY = {'-c':'default',
	       '-e':cowsay.Option.eyes,
	       '-T':cowsay.Option.tongue}
	       
BASE_COWTHINK = {'-c':'default',
	       '-e':cowsay.Option.eyes,
	       '-T':cowsay.Option.tongue}
	       
BASE_BUBBLE = {'-b':'cowsay',
	       '-l':40,
	       '-w': True}	
	
def make_param(other_params,default):
	param = default
	i=0
	if not len(other_params):
		return param
	while True:
		if other_params[i] in param.keys():
			param[other_params[i]]=other_params[i+1]
			i+=2
		else:
			break
		if i>=len(other_params):
			break
	return param


class Cow(cmd.Cmd):
	def do_list_cows(self,string):
		arg = parce(string)[0] if len(parce(string)) else cowsay.COW_PEN
		print(cowsay.list_cows(arg))
		
	def do_cowsay(self,string):
		message, *other_params = parce(string)
		param = make_param(other_params,BASE_COWSAY)
		print(cowsay.cowsay(message, cow=param['-c'], eyes=param['-e'], tongue=param['-T']))
		
	def do_cowthink(self,string):
		message, *other_params = parce(string)
		param = make_param(other_params,BASE_COWTHINK)
		print(cowsay.cowthink(message, cow=param['-c'], eyes=param['-e'], tongue=param['-T']))
		
	def do_make_bubble(self,string):
		message,*other_params = parce(string)
		param = make_param(other_params, BASE_BUBBLE)
		print(cowsay.make_bubble(message, width=int(param['-l']), brackets=cowsay.THOUGHT_OPTIONS[param['-b']], wrap_text=param['-w']))
		
	def do_exit(self,string):
		return True
		
	def emptyline(self):
        	pass
		
	
	
if __name__ == "__main__":
    Cow().cmdloop()
