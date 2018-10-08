import cfg
import pandas as pd
import csv

def load_brew_control_group():
    brewContDf = pd.read_csv(cfg.brew_control_group_path, encoding = "iso-8859-1")
    controlGrBBL = pd.DataFrame(brewContDf['2016 Barrels (Control Group)'])

    return controlGrBBL