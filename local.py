import requests
import time
import random
import psutil
import numpy as np
import os
import subprocess

ip_address_port = 'http://127.0.0.1:5000/'
headers = {'Content-Type': 'application/json'}

#Load the following from JSON
if os.path.exists(f"{os.getcwd()}"+"/config.json"):
		with open(f"{os.getcwd()}"+"/config.json", "r") as f:
			config = json.load(f)	
	wanted_used_percent = config["volumes"]["set_used_space_%"]
	minimum_change_rate_percent = config["volumes"]["min_change_%"]
	maximum_change_rate_percent = config["volumes"]["max_change_%"]
	minimum_add_rate_percent = config["volumes"]["min_add_%"]
	maximum_add_rate_percent = config["volumes"]["max_add_%"]
	minimum_cpu_load_percent = config["system"]["min_cpu_load"]
	maximum_cpu_load_percent = config["system"]["max_cpu_load"]
	minimum_ram_load_percent = config["system"]["min_ram_load"]
	maximum_ram_load_percent = config["system"]["max_ram_load"]
	number_of_change_profiles = config["preferences"]["number_of_change_profiles"]
	change_every_x_hours = config["preferences"]["change_every_x_hours"]
	skip_drives = config["volumes"]["skip_drives"]
	#startup = config["preferences"]["startup"]
else:
	print("No config.json file available")
	print("Closing in 10 seconds...")
	time.sleep(10)
	quit()

#detect if data_generator in location
if os.path.exists(f"{os.getcwd()}"+"/Binary/data-generator.exe"):
	print("Found Binary... running.")
	subprocess.call([f"{os.getcwd()}"+"/Binary/data-generator.exe"], shell=True)
else:
	print("Missing Generator!")

#Generic Profile
profile = {"id": 1, "jsonrpc": "2.0","method":"update_config","params":{"allow_windows_updates": false, "log_level": "INFO", "agent_version": "latest", "cpu_load": 1, "dtc_config": {}, "agent_install_args": [], "volumes": {"C": {"data_churn_rate": 0.1, "path": "apogee_data", "max_fragment_blocks": 512, "initial_usage": 1, "data_growth_rate": 1, "min_fragment_blocks": 128, "static_io_load": 1, "fragment": false, "database": {"updates_per_hour": 0, "queries_per_hour": 0, "inserts_per_hour": 0}}}, "ram_load": 1, "extra_ca_cert": "", "database_version": "", "agent_config": {}, "agent_type": "", "dtc_rmm_token": "", "format_volumes": [], "agent_auto_upgrade": false}}

#Check disks and populate profile
for disk in psutil.disk_partitions():
	if 'cdrom' in disk.opts:
		continue
	elif disk.mountpoint in skip_drives:
		continue
	else:
		#Fill Value
		disk_total = psutil.disk_usage(disk.mountpoint)[0]
		disk_used = psutil.disk_usage(disk.mountpoint)[1]
		set_used_space = ((wanted_used_percent / 100) * disk_total) / (1024 ** 3)
		#Change Value
		list_of_change_rates = np.linspace(minimum_change_rate_percent, maximum_change_rate_percent, number_of_profiles)
		new_change_rate_percent = random.choice(list_of_change_rates)
		new_change = ((new_change_rate_percent / 100) * disk_used) / (1024 ** 3)
		#Add Value
		list_of_add_rates = np.linspace(minimum_add_rate_percent, maximum_add_rate_percent, number_of_profiles)
		new_add_rate_percent = random.choice(list_of_add_rates)
		new_add = ((new_change_rate_percent / 100) * disk_used) / (1024 ** 3)
		#Volume Values
		''' THIS NEEDS SYNTHETIC DICT'''
		mount = f"{psutil.disk_partitions()[0].mountpoint}"[0]
		volume_data = {}
		volume_data.update({f'{mount}':''})
		volume_data["mount"] =  {"data_churn_rate": 0.1, "path": "scratch", "max_fragment_blocks": 512, "initial_usage": 1, "data_growth_rate": 1, "min_fragment_blocks": 128, "static_io_load": 1, "fragment": false, "database": {"updates_per_hour": 0, "queries_per_hour": 0, "inserts_per_hour": 0}}}
		volume_data["mount"]["data_churn_rate"] = new_change
		volume_data["mount"]["initial_usage"] = set_used_space
		volume_data["mount"]["data_growth_rate"] = new_add
		
		profile["params"]["volumes"] = volume_data
		#CPU Load Value
		list_of_cpu_load = np.linspace(minimum_cpu_load_percent, maximum_cpu_load_percent, number_of_profiles)
		new_cpu_load = random.choice(list_of_cpu_load)
		profile["params"]["cpu_load"] = new_cpu_load
		#RAM Load Value
		list_of_ram_load = np.linspace(minimum_ram_load_percent, maximum_ram_load_percent, number_of_profiles)
		new_ram_load = random.choice(list_of_ram_load)
		profile["params"]["ram_load"] = new_ram_load
		#Create scratch directory per volume
		if os.path.exists(f"{mount}"+"/scratch"):
			continue
		else:
			os.mkdir(f"{mount}"+"/scratch")

##Startup launcher
''' CREATE A SCHEDULED TASK TO LAUNCH AT STARTUP '''

while True:
	try:

		print("Changing Usage Profile!")
		response = requests.post(f"{ip_address_port}", headers=headers, data=str(profile))
		time.sleep(1)
		get = '{"id":1,"jsonrpc":"2.0","method":"get_config","params":{}}'
		response = requests.post(f"{ip_address_port}", headers=headers, data=get)
		if response.ok:
			print("Success :)")
		time.sleep(change_every_x_hours*60*60)
	except requests.RequestException as e:
		print("Request Failed: %s" % e)
		continue
	except KeyboardInterrupt:
		print("User Exit")
		exit()
	except OSError as e:  
    	print("Folder Creation failed" % e) 
	except:
		print("General Error - Retrying in 3 Seconds")
		time.sleep(3)
		continue