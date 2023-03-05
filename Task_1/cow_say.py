
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-e",'--eye_string', type=str, help="Change eye string")
parser.add_argument("-f",'--cowfile', type=str, help="Change cow")
parser.add_argument("-l",action="store_true")
parser.add_argument("-n",action="store_true")    
parser.add_argument("-T",'--tongue_string', type=str, help="Change cow")      
parser.add_argument("-W", '--column', type=int,help='Change width')          
parser.add_argument('message')
args = parser.parse_args()
params={}
if args.eye_string is not None:
	params['eyes'] = args.eye_string
if args.cowfile is not None:
	params['cow'] = args.cowfile
if args.tongue_string is not None:
	params['tongue'] = args.tongue_string
if args.column is not None:
	params['width'] = args.column
params['message']=args.message
from cowsay import cowsay
from cowsay import list_cows
if not args.l :
	print(cowsay(**params))
else:
	print(str(list_cows()))
