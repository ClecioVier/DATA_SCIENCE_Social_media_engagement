# Instagram's engagement
# What we want to answer?
# What type of content has more engagement on Instagram?
# We have the Instagram database since they started posting on March,27
# He also has given some instructions:
# You can ignore the visualization series, we need to know only likes, comments and interactions
# Null tags (please treat as empty)

# Import Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Import excel file
df = pd.read_excel(r'08. Analisando o engajamento no Instagram.xlsx')

# Seeing the first 5 lines
print(df.head())

# Erasing "visualizations series"
df = df.drop("Visualizações", axis=1)

# Seeing if "Visualization series" was deleted
df.head()

# Seeing only the last five lines
df.tail()

# Seeing df information
df.info()

# Counting values which had been shown in "carousel" series
df.Carrossel.value_counts()

# The null values are from non "carousel" posts. In this way, "null" should be none "N"
# Filtering values when "carousel" is null
df.loc[df.Carrossel.isnull()].head(10)

# Searching values which "NO" are null
df.loc[df.Carrossel.notnull()].head(10)

# Selecting only "carousel" series
df.loc[df.Carrossel.isnull(), 'Carrossel'].head(10)

# Giving "N" values for this series
df.loc[df.Carrossel.isnull(), 'Carrossel'] = "N"

# Descriptive statistics
print(df.describe())

# Building a graph to see data scatter
ax = df.plot(kind="scatter", x="Data", y="Curtidas",color="blue", label="Curtidas", figsize=(14,8));
df.plot(kind="scatter", x="Data", y="Comentários", color="red", label="Comentários", figsize=(14, 8), ax=ax);
# plt.show()

# We need to verify if there is a pattern when we observe others series of information

# Ordering the values
print(df.sort_values(by="Curtidas", ascending=False).head())
print(df.sort_values(by="Curtidas", ascending=False).tail())

# We can observe on Top 5 that all posts had people and were campaign photos
# On 5 worst posts, there weren't people neither campaign posts
# This could be a tip that people and campaign have relationship with likes

# To improve visualization, let's build a pattern on value formats
pd.options.display.float_format = '{:,.2f}'.format

# Cluster the information per type
df.groupby("Tipo")["Comentários"].count()

df.groupby(['Tipo', 'Pessoas', 'Campanhas'])[['Curtidas', 'Comentários']].mean()

# Analysing again about the video, it doesn't seem so bad anymore. When it had done in a campaign and there are people,
# it had a good result, near the result of the photos.
# What could have down the mean is only videos with people or campaign, or without both.
# We don't have any video with only one of both (people or campaign)
# In other way, IGTV, even having people, it didn't have a better result

print(df.groupby(['Pessoas', 'Campanhas', 'Tipo'])[['Curtidas', 'Comentários']].mean())

# Let's filter the base only where the type is "video" to understand the results better
print(df[df.Tipo == 'Vídeo'])

# In this way, we can see that they only had 2 campaigns with video, so we can suggest more campaigns with video
# Here we notice that the store try to post 4 videos showing its products (without any person)
# and they have a low result
# When the video was made with people making trends and commemorative dates the result was much better!

# Conclusions
# At first analysis, posts with people has better engagement than those with no one.
# Posts in campaign also had better engagement
# On this base, the carrossel had not made difference to improve the brand engagement

# Then, let's cluster by "Tags"
df.groupby("Tags")["Curtidas"].mean()

# Transforming a tag series in a tag list
df.Tags = df.Tags.str.split("/")
df.head()

# Separating a tag series in 1 line for each list element
df = df.explode('Tags')
df.head()

# Ordering by likes
df.groupby("Tags")[["Curtidas", "Comentários"]].mean().sort_values("Curtidas", ascending=False)

# Filtering values without tag
df[df.Tags.isnull()]
df.loc[df.Tags.isnull(), "Tags"]
df.loc[df.Tags.isnull(), "Tags"] = "Sem tag"
df.groupby("Tags")[["Curtidas", "Comentários"]].mean().sort_values("Curtidas", ascending=False)

# Ignoring these values as costumer orientation
df.loc[df.Tags == 'Sem tag', "Tags"] = np.nan
df[df.Tags.isnull()]

# Analysing data by people and tag
df.groupby(["Pessoas", "Tags"])[["Curtidas", "Comentários"]].mean()

# Analysing by like
df.groupby(["Pessoas", "Tags"])[["Curtidas", "Comentários"]].mean().sort_values("Curtidas", ascending=False)

# Analysing by campaign and tag
df.groupby(["Campanhas", "Tags"])[["Curtidas", "Comentários"]].mean().sort_values("Curtidas", ascending=False)

# Conclusions 02
# Having person's face in the post is a key to engagement.
# Build campaigns help a lot.
# The tag "Promotion" had a greater performance than any other tag.
# Use trend contents also can help, even the trend being of other area.
# The best manner to show a product is with other person using it,
# For new brand products it's more important, being almost the double.
