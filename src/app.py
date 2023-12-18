import streamlit as st
import pandas as pd
import pre_processor,find
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.figure_factory as ff


df1 = pd.read_csv('athlete_events.csv')
df2 = pd.read_csv('noc_regions.csv')

df = pre_processor.preprocess()

st.sidebar.title("Olympic_Analysis")
df_menu = st.sidebar.radio(
    'select option',
    ('Medal Tally', 'Overall Analysis', 'Country_wise', 'Athletes Analysis')
)
if df_menu == 'Medal Tally':
    st.sidebar.header("Medals")
    years, country= find.county_list(df)

    Year = st.sidebar.selectbox("Year", years)
    Country = st.sidebar.selectbox("Country", country)

    df_New = find.medal_tally(df,Year,Country)
    st.table(df_New)

if df_menu == 'Overall Analysis':
    edition = df['Year'].unique().shape[0]-1
    city = df['City'].unique().shape[0]
    sports = df['Sport'].unique().shape[0]
    events = df['Event'].unique().shape[0]
    athlets = df['Name'].unique().shape[0]
    nation = df['NOC'].unique().shape[0]

    st.title("Total Statistics")
    col1,col2,col3 =st.columns(3)
    with col1:
        st.header('Edition')
        st.title(edition)
    with col2:
        st.header('Nations')
        st.title(nation)
    with col3:
        st.header('Athlets')
        st.title(athlets)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.header('Cities')
        st.title(city)
    with col2:
        st.header('Sports')
        st.title(sports)
    with col3:
        st.header('Events')
        st.title(events)

    st.title("Number of Events")
    fig ,ax = plt.subplots(figsize=(20,20))
    df_x = df.drop_duplicates(['Year', 'Sport', 'Event'])
    ax = sns.heatmap(df_x.pivot_table(index ='Sport',columns='Year',values='Event',aggfunc ='count').fillna(0).astype('int'),annot=True)
    st.pyplot(fig)

    st.title("Most successful Athletes")
    sport_list = df['Sport'].unique().tolist()
    sport_list.sort()
    sport_list.insert(0,'Overall')

    selected_sport = st.selectbox('Select a Sport',sport_list)
    x = find.successful(df,selected_sport)
    st.table(x)


if df_menu == 'Country_wise':
    st.sidebar.title('Country_wise')

    country_list = df['NOC'].dropna().unique().tolist()
    country_list.sort()

    selected_country = st.sidebar.selectbox('Select a Country',country_list)

    country_df = find.yearwise(df,selected_country)
    fig = px.line(country_df, x="Year", y="Medal")
    st.title(selected_country + " Medal Tally over the years")
    st.plotly_chart(fig)

    st.title(selected_country + " excels in the following sports")
    pt = find.country(df,selected_country)
    if not pt.empty:
        fig, ax = plt.subplots(figsize=(20, 20))
        ax = sns.heatmap(pt, annot=True)
        st.pyplot(fig)
    else:
        st.warning("No data available for heatmap.")

    st.title("Top 10 athletes of " + selected_country)
    top10_df = find.countrywise(df,selected_country)
    st.table(top10_df)

if df_menu == 'Athletes Analysis':
    athlete_df = df.drop_duplicates(subset=['Name', 'NOC'])

    x1 = athlete_df['Age'].dropna()
    x2 = athlete_df[athlete_df['Medal'] == 'Gold']['Age'].dropna()
    x3 = athlete_df[athlete_df['Medal'] == 'Silver']['Age'].dropna()
    x4 = athlete_df[athlete_df['Medal'] == 'Bronze']['Age'].dropna()

    fig = ff.create_distplot([x1, x2, x3, x4], ['Overall Age', 'Gold Medalist', 'Silver Medalist', 'Bronze Medalist'],show_hist=False, show_rug=False)
    fig.update_layout(autosize=False,width=1000,height=600)
    st.title("Distribution of Age")
    st.plotly_chart(fig)

    x = []
    name = []
    famous_sports = ['Basketball', 'Judo', 'Football', 'Tug-Of-War', 'Athletics',
                     'Swimming', 'Badminton', 'Sailing', 'Gymnastics',
                     'Art Competitions', 'Handball', 'Weightlifting', 'Wrestling',
                     'Water Polo', 'Hockey', 'Rowing', 'Fencing',
                     'Shooting', 'Boxing', 'Taekwondo', 'Cycling', 'Diving', 'Canoeing',
                     'Tennis', 'Golf', 'Softball', 'Archery',
                     'Volleyball', 'Synchronized Swimming', 'Table Tennis', 'Baseball',
                     'Rhythmic Gymnastics', 'Rugby Sevens',
                     'Beach Volleyball', 'Triathlon', 'Rugby', 'Polo', 'Ice Hockey']
    for sport in famous_sports:
        temp_df = athlete_df[athlete_df['Sport'] == sport]
        x.append(temp_df[temp_df['Medal'] == 'Gold']['Age'].dropna())
        name.append(sport)

    fig = ff.create_distplot(x, name, show_hist=False, show_rug=False)
    fig.update_layout(autosize=False, width=1000, height=600)
    st.title("Distribution of Age wrt Sports(Gold Medalist)")
    st.plotly_chart(fig)

    sport_list = df['Sport'].unique().tolist()
    sport_list.sort()
    sport_list.insert(0, 'Overall')

    st.title('Height Vs Weight')
    selected_sport = st.selectbox('Select a Sport', sport_list)
    temp_df = find.weight_v_height(df,selected_sport)
    fig,ax = plt.subplots()
    ax = sns.scatterplot(x=temp_df['Weight'], y=temp_df['Height'], hue=temp_df['Medal'], style=temp_df['Sex'], s=60)
    st.pyplot(fig)

    st.title("Men Vs Women Participation Over the Years")
    final = find.men_vs_women(df)
    fig = px.line(final, x="Year", y=["Male", "Female"])
    fig.update_layout(autosize=False, width=1000, height=600)
    st.plotly_chart(fig)