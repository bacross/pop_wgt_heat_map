import cfg

from etl.run_etl import run_etl
from models import get_lat_longs as gll
from models import calc_pop_weighted_dist as cpwd

### load and munge breweries
craft_brew_directory_df, pop_centers = run_etl()

### get lat longs
craft_brew_directory_df = gll.get_lat_longs(craft_brew_directory_df)

### do some munging for specific breweries
craft_brew_directory_df.set_value('Bellport Brewing Company','BBL',250)
craft_brew_directory_df.set_value('New Province Brewing Company','BBL',750)
craft_brew_directory_df.set_value('Ladyface Ale Companie','BBL',731)
craft_brew_directory_df = craft_brew_directory_df.drop(['Eola School Restaurant'])

### calculate population weighted distances
craft_brew_directory_df = cpwd.calc_pop_weighted_dist_frame(craft_brew_directory_df,pop_centers)

### calculate magnitude metric
craft_brew_directory_df['Magnitude'] = craft_brew_directory_df.apply(
    lambda row: float(row['BBL'])/float(row['PopWgtDist']) if float(row['PopWgtDist'])!=float(0) else 0.0,axis=1)


