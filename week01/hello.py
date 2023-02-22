#%%
import altair as alt
import pandas as pd

alt.data_transformers.enable('json')
#> DataTransformerRegistry.enable('json')

url = "https://github.com/byuidatascience/data4python4ds/raw/master/data-raw/mpg/mpg.csv"
mpg = pd.read_csv(url)


chart = (alt.Chart(mpg)
  .encode(
    x='displ',
    y='hwy')
  .mark_circle()
)

chart

# %%
