from preswald import text, plotly, connect, get_df, table, query
import pandas as pd
import plotly.express as px

#Title
text("World Happiness Analysis: Insights across countries")

#Intro
text("""
The World Happiness Report evaluates well-being across nations based on factors like GDP, social support, freedom, and more.  
Understanding what makes countries happier can guide better policy-making and societal development.
""")

#Load the CSV
connect()
df = get_df('WH_csv')

#Show the data
text("Full Dataset View")
table(df)


from preswald import slider

# Add a slider to filter by Happiness Score
threshold = slider("Happiness Score Threshold", min_val=0, max_val=10, default=6)
table(df[df['Happiness Score'] > threshold], title="Countries Above Happiness Threshold")



#Exploratory Data Analysis (EDA)


#Top 10 Happiest Countries
text("Top 10 Happiest Countries")

top10 = df.sort_values('Happiness Score', ascending=False).head(10)
fig = px.bar(top10, x='Country', y='Happiness Score',
             title='Top 10 Happiest Countries',
             labels={'Country': 'Country', 'Happiness Score': 'Happiness Score'})
plotly(fig)


#GDP vs Happiness Score
text("Relationship Between GDP and Happiness Score")

fig = px.scatter(df, x='Economy (GDP per Capita)', y='Happiness Score',
                 text='Country',
                 title='GDP vs Happiness Score',
                 labels={'Economy (GDP per Capita)': 'GDP per Capita', 'Happiness Score': 'Happiness Score'})
fig.update_traces(textposition='top center')
plotly(fig)

#Freedom vs Happiness Score
text("Relationship Between Freedom and Happiness Score")

fig = px.scatter(df, x='Freedom', y='Happiness Score',
                 text='Country',
                 title='Freedom vs Happiness Score',
                 labels={'Freedom': 'Freedom to Make Life Choices', 'Happiness Score': 'Happiness Score'})
fig.update_traces(textposition='top center')
plotly(fig)

#Region-wise Average Happiness
text("Average Happiness Score by Region")

region_avg = df.groupby('Region')['Happiness Score'].mean().sort_values(ascending=False)
fig = px.bar(x=region_avg.index, y=region_avg.values,
             title='Average Happiness Score by Region',
             labels={'x': 'Region', 'y': 'Average Happiness Score'})
plotly(fig) 