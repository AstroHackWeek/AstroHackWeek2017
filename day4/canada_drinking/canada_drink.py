import matplotlib.pyplot as plt
import geopandas as gpd

# Census map of Canada provided by Statistics Canada
# http://www12.statcan.gc.ca/census-recensement/2011/geo/bound-limit/bound-limit-2011-eng.cfm
canada = gpd.read_file('map_data/gpr_000b11a_e.shp')

canada_drinking = {
    'Alberta': 18,
    'British Columbia': 19,
    'Manitoba': 18,
    'New Brunswick': 19,
    'Newfoundland and Labrador': 19,
    'Northwest Territories': 19,
    'Nova Scotia': 19,
    'Nunavut': 19,
    'Ontario': 19,
    'Prince Edward Island': 19,
    'Quebec': 18,
    'Saskatchewan': 19,
    'Yukon': 19}

canada['drink'] = ''

for num, state in enumerate(canada['PRENAME']):
    canada['drink'][num] = canada_drinking[state]

canada.plot('drink', cmap='jet', legend=True)
plt.axis('off')
plt.title('Drinking age remained 19 in Saskatchewan')
plt.savefig('after_figure.png')
