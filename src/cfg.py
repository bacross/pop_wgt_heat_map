# Todo: organize config file by grouping items associated with similar processes
import json

repo_path = '..'
data_path = repo_path + '/data'
proc_data_path = data_path + '/processed'
raw_data_path = data_path + '/raw'
api_cfg_path = repo_path + '/src/api_cfg.json'

with open(api_cfg_path) as api_cfg_file:
    api_cfg = json.load(api_cfg_file)

api_key = api_cfg['API_KEY']

brewery_csv_path = raw_data_path + '/Craft Brewery Directory.csv'

address_dict_path = proc_data_path + '/brew_address_dict.pkl'

get_lat_long_test_flag = True

pop_centers_path = raw_data_path + '/census population centers.txt'

brew_control_group_path = raw_data_path + '/breweryControlGroup.csv'

