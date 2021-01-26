import requests
import pprint
import time
import random


ip_address_port = 'http://127.0.0.1:5000/'
pp = pprint.PrettyPrinter()
headers = {'Content-Type': 'application/json'}
profile_change_hours = 2

profile_1 = '{"id": 1, "jsonrpc": "2.0","method":"update_config","params":{"allow_windows_updates": false, "log_level": "INFO", "agent_version": "latest", "cpu_load": 10, "dtc_config": {}, "agent_install_args": [], "volumes": {"C": {"data_churn_rate": 0.1, "path": "apogee_data", "max_fragment_blocks": 512, "initial_usage": 22.0, "data_growth_rate": 0.01, "min_fragment_blocks": 128, "static_io_load": 2.0, "fragment": false, "database": {"updates_per_hour": 0, "queries_per_hour": 0, "inserts_per_hour": 0}}}, "ram_load": 5, "extra_ca_cert": "", "database_version": "", "agent_config": {}, "agent_type": "", "dtc_rmm_token": "", "format_volumes": [], "agent_auto_upgrade": false}}'

profile_2 = '{"id": 1, "jsonrpc": "2.0","method":"update_config","params":{"allow_windows_updates": false, "log_level": "INFO", "agent_version": "latest", "cpu_load": 14, "dtc_config": {}, "agent_install_args": [], "volumes": {"C": {"data_churn_rate": 0.2, "path": "apogee_data", "max_fragment_blocks": 512, "initial_usage": 22.0, "data_growth_rate": 0.02, "min_fragment_blocks": 128, "static_io_load": 3.0, "fragment": false, "database": {"updates_per_hour": 0, "queries_per_hour": 0, "inserts_per_hour": 0}}}, "ram_load": 8, "extra_ca_cert": "", "database_version": "", "agent_config": {}, "agent_type": "", "dtc_rmm_token": "", "format_volumes": [], "agent_auto_upgrade": false}}'

profile_3 =  '{"id": 1, "jsonrpc": "2.0","method":"update_config","params":{"allow_windows_updates": false, "log_level": "INFO", "agent_version": "latest", "cpu_load": 18, "dtc_config": {}, "agent_install_args": [], "volumes": {"C": {"data_churn_rate": 0.3, "path": "apogee_data", "max_fragment_blocks": 512, "initial_usage": 22.0, "data_growth_rate": 0.03, "min_fragment_blocks": 128, "static_io_load": 4.0, "fragment": false, "database": {"updates_per_hour": 0, "queries_per_hour": 0, "inserts_per_hour": 0}}}, "ram_load": 11, "extra_ca_cert": "", "database_version": "", "agent_config": {}, "agent_type": "", "dtc_rmm_token": "", "format_volumes": [], "agent_auto_upgrade": false}}'

profile_4 =  '{"id": 1, "jsonrpc": "2.0","method":"update_config","params":{"allow_windows_updates": false, "log_level": "INFO", "agent_version": "latest", "cpu_load": 22, "dtc_config": {}, "agent_install_args": [], "volumes": {"C": {"data_churn_rate": 0.4, "path": "apogee_data", "max_fragment_blocks": 512, "initial_usage": 22.0, "data_growth_rate": 0.04, "min_fragment_blocks": 128, "static_io_load": 5.0, "fragment": false, "database": {"updates_per_hour": 0, "queries_per_hour": 0, "inserts_per_hour": 0}}}, "ram_load": 14, "extra_ca_cert": "", "database_version": "", "agent_config": {}, "agent_type": "", "dtc_rmm_token": "", "format_volumes": [], "agent_auto_upgrade": false}}'

profile_5 =  '{"id": 1, "jsonrpc": "2.0","method":"update_config","params":{"allow_windows_updates": false, "log_level": "INFO", "agent_version": "latest", "cpu_load": 26, "dtc_config": {}, "agent_install_args": [], "volumes": {"C": {"data_churn_rate": 0.5, "path": "apogee_data", "max_fragment_blocks": 512, "initial_usage": 22.0, "data_growth_rate": 0.05, "min_fragment_blocks": 128, "static_io_load": 6.0, "fragment": false, "database": {"updates_per_hour": 0, "queries_per_hour": 0, "inserts_per_hour": 0}}}, "ram_load": 17, "extra_ca_cert": "", "database_version": "", "agent_config": {}, "agent_type": "", "dtc_rmm_token": "", "format_volumes": [], "agent_auto_upgrade": false}}'

profile_6 =  '{"id": 1, "jsonrpc": "2.0","method":"update_config","params":{"allow_windows_updates": false, "log_level": "INFO", "agent_version": "latest", "cpu_load": 30, "dtc_config": {}, "agent_install_args": [], "volumes": {"C": {"data_churn_rate": 0.6, "path": "apogee_data", "max_fragment_blocks": 512, "initial_usage": 22.0, "data_growth_rate": 0.06, "min_fragment_blocks": 128, "static_io_load": 7.0, "fragment": false, "database": {"updates_per_hour": 0, "queries_per_hour": 0, "inserts_per_hour": 0}}}, "ram_load": 20, "extra_ca_cert": "", "database_version": "", "agent_config": {}, "agent_type": "", "dtc_rmm_token": "", "format_volumes": [], "agent_auto_upgrade": false}}'

profile_7 =  '{"id": 1, "jsonrpc": "2.0","method":"update_config","params":{"allow_windows_updates": false, "log_level": "INFO", "agent_version": "latest", "cpu_load": 34, "dtc_config": {}, "agent_install_args": [], "volumes": {"C": {"data_churn_rate": 0.7, "path": "apogee_data", "max_fragment_blocks": 512, "initial_usage": 22.0, "data_growth_rate": 0.07, "min_fragment_blocks": 128, "static_io_load": 8.0, "fragment": false, "database": {"updates_per_hour": 0, "queries_per_hour": 0, "inserts_per_hour": 0}}}, "ram_load": 23, "extra_ca_cert": "", "database_version": "", "agent_config": {}, "agent_type": "", "dtc_rmm_token": "", "format_volumes": [], "agent_auto_upgrade": false}}'

profile_8 =  '{"id": 1, "jsonrpc": "2.0","method":"update_config","params":{"allow_windows_updates": false, "log_level": "INFO", "agent_version": "latest", "cpu_load": 38, "dtc_config": {}, "agent_install_args": [], "volumes": {"C": {"data_churn_rate": 0.8, "path": "apogee_data", "max_fragment_blocks": 512, "initial_usage": 22.0, "data_growth_rate": 0.08, "min_fragment_blocks": 128, "static_io_load": 9.0, "fragment": false, "database": {"updates_per_hour": 0, "queries_per_hour": 0, "inserts_per_hour": 0}}}, "ram_load": 26, "extra_ca_cert": "", "database_version": "", "agent_config": {}, "agent_type": "", "dtc_rmm_token": "", "format_volumes": [], "agent_auto_upgrade": false}}'

profile_list = [profile_1, profile_2, profile_3, profile_4, profile_5, profile_6, profile_7, profile_8]

while True:
	try:
		profile = random.choice(profile_list)
		response = requests.post(f"{ip_address_port}", headers=headers, data=profile)
		pp.pprint(response)
		time.sleep(1)
		get = '{"id":1,"jsonrpc":"2.0","method":"get_config","params":{}}'
		response = requests.post(f"{ip_address_port}", headers=headers, data=get)
		pp.pprint(response.json())
		time.sleep(profile_change_hours*60*60)
	except requests.RequestException as e:
		print("Ping failed: %s" % e)
		continue
	except KeyboardInterrupt:
		exit()
	except:
		print("An error has occured")
		continue
