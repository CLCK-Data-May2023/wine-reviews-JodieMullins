import pandas as pd

reviews_df = pd.read_csv(r'data\winemag-data-130k-v2.csv.zip') # reads raw file from zip

country_count = reviews_df.country.value_counts() # creates list of countries and respective value counts

av_pts_per_country = reviews_df.groupby('country').points.mean() # average points of wine reviews per country
rounded_av_pts_per_country = round(av_pts_per_country, 1) # rounds point mean of reviews to one decimal place

output = pd.DataFrame.merge(country_count, rounded_av_pts_per_country, on='country') # Requested Data Frame

print(output)

output.to_csv('data/reviews-per-country.csv') # write requested DataFrame to file in specified folder