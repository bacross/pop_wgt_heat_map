from etl import load_breweries_from_csv as lbfc
from etl import load_pop_centers as lpc
from etl import load_brew_control_gr as lbcg
import  cfg
import pandas as pd

def run_etl():
    #load breweries
    craft_brew_directory_df = lbfc.load_brews()

    # build brewery dictionary
    brewAddressDict = lbfc.build_brew_address_dict(craft_brew_directory_df)

    # create brewery dataframe
    brewery_address_df = pd.DataFrame.from_dict(brewAddressDict, orient='index')

    #load census pop centers

    pop_centers = lpc.load_pop_centers()

    # load brewery control group info

    brew_control_group = lbcg.load_brew_control_group()

    # join addresses and control group
    brewery_df = brewery_address_df.join(brew_control_group, how='left')

    print("data has been loaded")
    return brewery_df, pop_centers
