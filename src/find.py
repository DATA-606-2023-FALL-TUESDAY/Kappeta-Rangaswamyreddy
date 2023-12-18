import numpy as np
import pandas as pd
import plotly.express as px

df1 = pd.read_csv('athlete_events.csv')
df2 = pd.read_csv('noc_regions.csv')

df = df1.merge(df2, on = 'NOC', how = 'left')

def medal_tally(df,year, country):
    df_medal = df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'Season', 'City', 'Sport', 'Event', 'Medal'])
    flag = 0
    if year == 'Overall' and country == 'Overall':
        temp_df = df_medal
    if year == 'Overall' and country != 'Overall':
        flag == 1
        temp_df = df_medal[df_medal['NOC'] == country]
    if year != 'Overall' and country == 'Overall':
        temp_df = df_medal[df_medal['Year'] == int(year)]
    if year != 'Overall' and country != 'Overall':
        temp_df = df_medal[(df_medal['Year'] == int(year)) & (df_medal['NOC'] == country)]
    if flag == 1:
        Y = temp_df.groupby('NOC').sum()[['Gold', 'Silver', 'Bronze']].sort_values('Year').reset_index()
    else:
        Y = temp_df.groupby('NOC').sum()[['Gold', 'Silver', 'Bronze']].sort_values('Gold',
                                                                                   ascending=False).reset_index()

    Y['Total'] = Y['Gold'] + Y['Silver'] + Y['Bronze']
    return Y

def df_New(df):
    df_New = df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'Season', 'City', 'Sport', 'Event', 'Medal'])
    df_New = df_New.groupby('NOC').sum()[['Gold', 'Silver', 'Bronze']].sort_values('Gold',
      ascending=False).reset_index()
    df_New['Total'] = df_New['Gold'] + df_New['Silver'] + df_New['Bronze']
    df_New['Gold'] = df_New['Gold'].astype('int')
    df_New['Silver'] = df_New['Silver'].astype('int')
    df_New['Bronze'] = df_New['Bronze'].astype('int')
    df_New['Total'] = df_New['Total'].astype('int')  # Corrected column name
    return df_New

def county_list(df):
    year = df['Year'].unique().tolist()
    year.sort()
    year.insert(0, 'Overall')

    counrty = np.unique(df['NOC'].dropna().values).tolist()
    counrty.sort()
    counrty.insert(0, 'Overall')
    return year, counrty

def successful(df, sport):
    temp_df = df.dropna(subset=['Medal'])

    if sport != 'Overall':
        temp_df = temp_df[temp_df['Sport'] == sport]
    x = temp_df['Name'].value_counts().reset_index().head(10).merge(df, left_on='Name', right_on='Name', how='left')[
        ['Name', 'Sport']].drop_duplicates('Name').rename(columns={'Name': 'Medal'})
    return x


def yearwise(df,country):
    temp_df = df.dropna(subset=['Medal'])
    temp_df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'], inplace=True)

    new_df = temp_df[temp_df['NOC'] == country]
    final_df = new_df.groupby('Year').count()['Medal'].reset_index()

    return final_df

def country(df,country):
    temp_df = df.dropna(subset=['Medal'])
    temp_df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'], inplace=True)

    new_df = temp_df[temp_df['NOC'] == country]

    pt = new_df.pivot_table(index='Sport', columns='Year', values='Medal', aggfunc='count').fillna(0)
    return pt


def countrywise(df, country):
    temp_df = df.dropna(subset=['Medal'])
    temp_df = temp_df[temp_df['NOC'] == country]

    x = temp_df['Name'].value_counts().reset_index().head(10).merge(df, left_on='Name', right_on='Name', how='left')[
        ['Name', 'Sport']].drop_duplicates('Name').rename(columns={'Name': 'Athlete'})

    return x

def weight_v_height(df,sport):
    athlete_df = df.drop_duplicates(subset=['Name', 'NOC'])
    athlete_df['Medal'].fillna('No Medal', inplace=True)

    if sport != 'Overall':
        temp_df = athlete_df[athlete_df['Sport'] == sport]
        return temp_df
    else:
        return athlete_df

def men_vs_women(df):
    athlete_df = df.drop_duplicates(subset=['Name', 'NOC'])
    men = athlete_df[athlete_df['Sex'] == 'M'].groupby('Year').count()['Name'].reset_index()
    women = athlete_df[athlete_df['Sex'] == 'F'].groupby('Year').count()['Name'].reset_index()

    final = men.merge(women, on='Year', how='left')
    final.rename(columns={'Name_x': 'Male', 'Name_y': 'Female'}, inplace=True)

    final.fillna(0, inplace=True)
    return final