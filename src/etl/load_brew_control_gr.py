import cfg
import pandas as pd
import csv

def load_brew_control_group():
    brewContDf = pd.read_csv(cfg.brew_control_group_path, encoding = "iso-8859-1")
    brewContDf = brewContDf.iloc[:, 0:4]
    brewContDf.columns = brewContGrList[0]
    brewContDf.index = brewContDf.iloc[:, 0]
    
    controlGrBBL = pd.DataFrame(brewContDf['2016 Barrels (Control Group)'])

    return controlGrBBL