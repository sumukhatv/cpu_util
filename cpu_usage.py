import time
import string
import sys
import commands

cpu_time_p = 0.0
idle_time_p = 0.0

def get_cpu_usage():
	global cpu_time_p
	global idle_time_p

	text = commands.getoutput("cat /proc/stat | grep '^cpu '").split()
	idle_time = float(text[4])
	
	cpu_time = float(text[1])+float(text[2])+float(text[3])+float(text[4])
	
	idle_d = idle_time - idle_time_p
	cpu_time_d = cpu_time - cpu_time_p
	usage_d = (1000*(cpu_time_d-idle_d)/cpu_time_d+5)/10
	
	cpu_time_p = cpu_time
	idle_time_p = idle_time
	
	return usage_d


def get_proc_cpu_usage(proc):
        for entry in commands.getoutput("ps aux").split("\n"):
                if (proc in entry.split()[10]):
                        return float(entry.split()[2])
        return 0.0


def usage():
	print "usage: python cpu_uage.py -i <interval seconds> -p <process name>"
	return

if __name__ == '__main__':
	if (len(sys.argv) == 2):
		if (sys.argv[1] == "-h"):
			usage()
			exit(0)

	if (len(sys.argv) == 3):
		try:
			print "CPU"
			while (True):
				load = get_cpu_usage()
				load = round(load, 2)
				print load				
				time.sleep(float(sys.argv[2]))

		except KeyboardInterrupt:
			exit(0)

	if (len(sys.argv) == 5):
                try:
			print "CPU\tProcess"
                        while (True):
                                load = get_cpu_usage()
                                load = round(load, 2)
                                load_proc = get_proc_cpu_usage(sys.argv[4])
                                print str(load)+"\t"+str(load_proc)
                                time.sleep(float(sys.argv[2]))

                except KeyboardInterrupt:
                        exit(0)
	else:
		usage()
		
