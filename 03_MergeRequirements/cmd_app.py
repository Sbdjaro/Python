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
	
def complete(prefix, line, beg, end):

	#print(prefix, line, beg, end)
	arg,command = shlex.split(line)[-1] if beg == end else shlex.split(line)[-2], shlex.split(line)[0]
	if command == 'cowsay':
		words = {'-c':cowsay.list_cows(),
	                 '-e':['OO','$$','GG'],
	                 '-T':['U','u','g','gg']}
	if command == 'cowthink':
		words = {'-c':cowsay.list_cows(),
	                 '-e':['OO','$$','GG'],
	                 '-T':['U','u','g','gg']}
	if command == 'make_bubble':
		words = {'-b':cowsay.list_cows()}  
	if arg in words.keys():               
		return [s for s in words[arg] if s.startswith(prefix)]
	else:
		return prefix


class Cow(cmd.Cmd):
	def do_list_cows(self,string):
		"""
		List all spicies
		list_cows [cow_path]
		
        	cow_path: path to the dir with spicies
		"""
		arg = parce(string)[0] if len(parce(string)) else cowsay.COW_PEN
		print(cowsay.list_cows(arg))
		
	def complete_list_cows(self,prefix, line, beg, end):
		return complete(prefix, line, beg, end)
		
	def do_cowsay(self,string):
		"""
		Print cow dialog
		cowsay message [-e eye_type] [-T tongue_type] [-c cow_type]
		
		message: message to say
		eye_type: string of cow eyes
		tongue_type: string of cow tongue
		cow_type: name of prepared cow (use list_cows to gett all name)
		"""
		message, *other_params = parce(string)
		param = make_param(other_params,BASE_COWSAY)
		print(cowsay.cowsay(message, cow=param['-c'], eyes=param['-e'], tongue=param['-T']))
		
	def complete_cowsay(self,prefix, line, beg, end):
		return complete(prefix, line, beg, end)
		
	def do_cowthink(self,string):
		"""
		Print cow thoughts
		cowthink message [-e eye_type] [-T tongue_type] [-c cow_type]
		
		message: message to think
		eye_type: string of cow eyes
		tongue_type: string of cow tongue
		cow_type: name of prepared cow (use list_cows to gett all name)
		"""
		message, *other_params = parce(string)
		param = make_param(other_params,BASE_COWTHINK)
		print(cowsay.cowthink(message, cow=param['-c'], eyes=param['-e'], tongue=param['-T']))
		
	def complete_cowthink(self,prefix, line, beg, end):
		return complete(prefix, line, beg, end)
		
	def do_make_bubble(self,string):
		"""
		Print just bubble with text
		make_bubble message [-b bubble_type] [-l message_lenght] [-w wrap_text]
		
		message: message to show
		bubble_type: 'cowsay' or 'cowthink'
		message_lenght: max lenght of text row
		wrap_text: IDK True or False
		"""
		message,*other_params = parce(string)
		param = make_param(other_params, BASE_BUBBLE)
		print(cowsay.make_bubble(message, width=int(param['-l']), brackets=cowsay.THOUGHT_OPTIONS[param['-b']], wrap_text=param['-w']))
		
	def complete_make_bubble(self,prefix, line, beg, end):
		return complete(prefix, line, beg, end)
		
	def do_exit(self,string):
		return True
		
	def emptyline(self):
        	pass
		
	
	
if __name__ == "__main__":
    Cow().cmdloop()
