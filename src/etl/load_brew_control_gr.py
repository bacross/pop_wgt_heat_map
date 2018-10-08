import cfg
import pandas as pd

def load_brew_control_group():
    with open(cfg.brew_control_group_path) as brew_control_group_file:
        brew_control_group = csv.reader(brew_control_group_file)
        brew_control_group_list = [','.join(row) for row in brew_control_group]

    brewContGrList = [strg.split(',') for strg in brew_control_group_list]

    brewContDf = pd.DataFrame(brewContGrList[1:len(brewContGrList)])
    brewContDf = brewContDf.iloc[:, 0:4]
    brewContDf.columns = brewContGrList[0]
    brewContDf.index = brewContDf.iloc[:, 0]
    brewContDf.head()

    controlGrBBL = pd.DataFrame(brewContDf['2016 Barrels (Control Group)'])

    return controlGrBBL