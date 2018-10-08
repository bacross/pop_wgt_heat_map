import cfg
import pandas as pd
def load_pop_centers():
    pop_centers = pd.read_csv(cfg.pop_centers_path)
    return pop_centers