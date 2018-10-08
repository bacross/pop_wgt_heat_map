import cfg
import googlemaps
import pickle

def get_lat_longs(address_dict):
    googmaps = googlemaps.Client(cfg.api_key)
    if cfg.get_lat_long_test_flag == True:
        key_list = list(address_dict.keys())[0:10]
    else:
        key_list = list(address_dict.keys())

    for key in key_list:
        address_dict[key].update(
            {'lat/lng': googmaps.geocode(address_dict[key])[0]['geometry']['location']})

    with open(cfg.address_dict_path, 'wb') as brew_address_dict_path:
        pickle.dump(address_dict, brew_address_dict_path)

    return address_dict