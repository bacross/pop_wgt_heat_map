import cfg
import csv
import pandas as pd
import pickle

def load_brews():
    craft_brew_directory_df = pd.read_csv(cfg.brewery_csv_path,encoding='iso-8859-1', header=None,names=['Breweries'])
    return craft_brew_directory_df

def build_brew_address_dict(ndf):
    brewAddressDict ={}
    for i in range(3,len(ndf.Breweries)):
        if ndf.Breweries.iloc[i][0:5]=='Phone':
            brewAddressDict[ndf.Breweries.iloc[i-3]]={'Address':str(ndf.Breweries.iloc[i-2])+', '+str(ndf.Breweries.iloc[i-1]).replace(' | Map','')}
    return brewAddressDict

def save_brewery_dict_pickle(ndict):
    with open(cfg.brewery_pickle_path,'wb') as brew_pickle_handle:
        pickle.dump(ndict,brew_pickle_handle)