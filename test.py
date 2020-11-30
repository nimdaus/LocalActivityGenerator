import requests
import pprint
import time
import random

#make up the post
ip_address_port = 'http://127.0.0.1:5000/'
pp = pprint.PrettyPrinter()
headers = {'Content-Type': 'application/json'}
profile_change_hours = 4
heartbeat_uuid = "20d9f9c4-64a4-47f5-9194-0c30409aabd4"

load_list = ['{"id": 1, "jsonrpc": "2.0","method":"update_config","params":{"allow_windows_updates": false, "log_level": "INFO", "agent_version": "latest", "cpu_load": 15, "dtc_config": {}, "agent_install_args": [], "volumes": {"C": {"data_churn_rate": 0.02538, "path": "apogee_data", "max_fragment_blocks": 512, "initial_usage": 22.0, "data_growth_rate": 0.00282, "min_fragment_blocks": 128, "static_io_load": 3.0, "fragment": false, "database": {"updates_per_hour": 0, "queries_per_hour": 0, "inserts_per_hour": 0}}}, "ram_load": 15, "extra_ca_cert": "", "database_version": "", "agent_config": {}, "agent_type": "", "dtc_rmm_token": "", "format_volumes": [], "agent_auto_upgrade": false}}','{"id": 1, "jsonrpc": "2.0","method":"update_config","params":{"allow_windows_updates": false, "log_level": "INFO", "agent_version": "latest", "cpu_load": 25, "dtc_config": {}, "agent_install_args": [], "volumes": {"C": {"data_churn_rate": 0.02256, "path": "apogee_data", "max_fragment_blocks": 512, "initial_usage": 22.0, "data_growth_rate": 0.00564, "min_fragment_blocks": 128, "static_io_load": 5.0, "fragment": false, "database": {"updates_per_hour": 0, "queries_per_hour": 0, "inserts_per_hour": 0}}}, "ram_load": 25, "extra_ca_cert": "", "database_version": "", "agent_config": {}, "agent_type": "", "dtc_rmm_token": "", "format_volumes": [], "agent_auto_upgrade": false}}','{"id": 1, "jsonrpc": "2.0","method":"update_config","params":{"allow_windows_updates": false, "log_level": "INFO", "agent_version": "latest", "cpu_load": 35, "dtc_config": {}, "agent_install_args": [], "volumes": {"C": {"data_churn_rate": 0.01974, "path": "apogee_data", "max_fragment_blocks": 512, "initial_usage": 22.0, "data_growth_rate": 0.00846, "min_fragment_blocks": 128, "static_io_load": 5.0, "fragment": false, "database": {"updates_per_hour": 0, "queries_per_hour": 0, "inserts_per_hour": 0}}}, "ram_load": 35, "extra_ca_cert": "", "database_version": "", "agent_config": {}, "agent_type": "", "dtc_rmm_token": "", "format_volumes": [], "agent_auto_upgrade": false}}']

while True:
	try:
		data = random.choice(load_list)
		response = requests.post(f"{ip_address_port}", headers=headers, data=data)
		pp.pprint(response)
		time.sleep(1)
		data = '{"id":1,"jsonrpc":"2.0","method":"get_config","params":{}}'
		response = requests.post(f"{ip_address_port}", headers=headers, data=data)
		pp.pprint(response.json())
		requests.get(f"https://hc-ping.com/{heartbeat_uuid}", timeout=10)
		time.sleep(profile_change_hours*60*60)
	except requests.RequestException as e:
		print("Ping failed: %s" % e)
		continue
	except KeyboardInterrupt:
		exit()
	except:
		print("An error has occured")
		continue
