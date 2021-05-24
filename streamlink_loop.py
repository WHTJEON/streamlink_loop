import argparse
import os
import shutil

parser=argparse.ArgumentParser()
parser.add_argument('-url', required=True)
parser.add_argument('-cam', required=True)
parser.add_argument('-max', required=False,default=0)
args = parser.parse_args()

M3U8 = args.url
CAM = args.cam
MAX_RETRIES = int(args.max)

def divider():
	count = int(shutil.get_terminal_size().columns)
	count = count - 1
	print ('-' * count)
	
def create_command(i):
	global STREAMLINK_COMMAND
	FILENAME_ = "%s-%s.ts"%(CAM,i)
	STREAMLINK_COMMAND = "streamlink -o '%s' %s best"%(FILENAME_,M3U8)
	return STREAMLINK_COMMAND

def download_stream():	
	print("커맨드 실행중: %s"%STREAMLINK_COMMAND)	
	os.system(STREAMLINK_COMMAND)
	
i = 1

while True:
	create_command(i)
	divider()
	download_stream()
	print("Restarting..")
	i = i + 1
	if MAX_RETRIES != 0:		
		if i > MAX_RETRIES:
			divider()
			print("Max Retries Limit Reached")
			break
		else:
			continue
	else: 
		continue