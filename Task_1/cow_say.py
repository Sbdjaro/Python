
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument("-e",'--eye_string', type=str, help="Change eye string")
parser.add_argument("-f",'--cowfile', type=str, help="Change cow")
#parser.add_argument("-h",'--help')
parser.add_argument("-l",action="store_true")
parser.add_argument("-n",action="store_true")                    
parser.add_argument('message')
args = parser.parse_args()
params={}
if args.eye_string is not None:
	params['eyes'] = args.eye_string
if args.cowfile is not None:
	params['cow'] = args.cowfile
params['message']=args.message
from cowsay import cowsay
from cowsay import list_cows
if args.l is None:
	print(cowsay(**params))
else:
	print(str(list_cows()))
message = """
The most remarkable thing about my mother is that for thirty years she served
the family nothing but leftovers.  The original meal has never been found.
		--
""".strip()
#print(cowsay(message))

#subprocess.run(['cowsay',message])
