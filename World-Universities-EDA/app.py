import numpy as np 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st


# Set up page configurations
st.set_page_config(page_title='World Universities Interactive Dashboard', page_icon='🎓', layout='wide')

world_uni_df = pd.read_csv('./world-uni-rankings.csv', encoding='latin1')

st.title('🎓World Universities Dashboard')

year = st.slider('Year Selected', 2016, 2024)

col_1, col_2, col_3, col_4, col_5 = st.columns(5, gap='large')

with col_1:
    st.header('Best Overall Score')
    def best_overall(year=year):
        sorted_by_year = world_uni_df[world_uni_df['Year'] == year]
        sort_desc = sorted_by_year.sort_values('Overall Score', ascending=False)
        school_name = sort_desc['Name'].iloc[0]
        score = sort_desc['Overall Score'].iloc[0]
        return school_name, round(score,1)
    
    best_overall_school, best_overall_score = best_overall()

    st.write(f"{best_overall_school}")
    st.write(f"Score: {best_overall_score}")

with col_2:
    st.header('Best Teaching Score')
    def best_teaching(year=year):
        sorted_by_year = world_uni_df[world_uni_df['Year'] == year]
        sort_desc = sorted_by_year.sort_values('Teaching', ascending=False)
        school_name = sort_desc['Name'].iloc[0]
        score = sort_desc['Teaching'].iloc[0]
        return school_name, round(score,1)
    
    best_teaching_school, best_teaching_score = best_teaching()

    st.write(f"{best_teaching_school}")
    st.write(f"Score: {best_teaching_score}")

with col_3:
    st.header('Best Research Environment')
    def best_research_env(year=year):
        sorted_by_year = world_uni_df[world_uni_df['Year'] == year]
        sort_desc = sorted_by_year.sort_values('Research Environment', ascending=False)
        school_name = sort_desc['Name'].iloc[0]
        score = sort_desc['Research Environment'].iloc[0]
        return school_name, round(score,1)
    
    best_res_env_school, best_res_env_score = best_research_env()

    st.write(f"{best_res_env_school}")
    st.write(f"Score: {best_res_env_score}")

with col_4:
    st.header('Best Research Quality')
    def best_research_qual(year=year):
        sorted_by_year = world_uni_df[world_uni_df['Year'] == year]
        sort_desc = sorted_by_year.sort_values('Research Quality', ascending=False)
        school_name = sort_desc['Name'].iloc[0]
        score = sort_desc['Research Quality'].iloc[0]
        return school_name, round(score,1)
    
    best_res_qual_school, best_res_qual_score = best_research_qual()

    st.write(f"{best_res_qual_school}")
    st.write(f"Score: {best_res_qual_score}")

with col_5:
    st.header('Most Industry Impact')
    def most_industry_imp(year=year):
        sorted_by_year = world_uni_df[world_uni_df['Year'] == year]
        sort_desc = sorted_by_year.sort_values('Industry Impact', ascending=False)
        school_name = sort_desc['Name'].iloc[0]
        score = sort_desc['Industry Impact'].iloc[0]
        return school_name, round(score,1)
    
    most_ind_imp_school, most_ind_imp_score = most_industry_imp()

    st.write(f"{most_ind_imp_school}")
    st.write(f"Score: {most_ind_imp_score}")

st.divider()

st.header(f'Overall Top 10 Universities In The World In {year}')
def top_ten_tbl(year=year):
    sorted_by_year = world_uni_df[world_uni_df['Year'] == year]
    sort_desc = sorted_by_year.sort_values('Overall Score', ascending=False)
    top_ten_uni = sort_desc[:10].reset_index(drop=True).set_index('Rank')
    return top_ten_uni[['Name', 'Overall Score']]

st.write(top_ten_tbl())

st.divider()

st.header(f'Trend In Overall Scores')
uni_names_array = world_uni_df.Name.unique()
uni_selection = st.selectbox(label='University Selected', options=uni_names_array)

def uni_ovr_score_trend(uni=uni_selection):
    # Filter by specified Uni
    filter_by_uni = world_uni_df[world_uni_df['Name'] == uni]
    year = filter_by_uni['Year']

    # Get scores
    ovr_score = filter_by_uni['Overall Score']
    teach_score = filter_by_uni['Teaching']
    res_env_score = filter_by_uni['Research Environment']
    res_qual_score = filter_by_uni['Research Quality']
    ind_impact_score = filter_by_uni['Industry Impact']

    # Plot
    plt.figure(figsize=(10,6))
    plt.plot(year, ovr_score, label='Overall Score')
    plt.plot(year, teach_score, label='Teaching')
    plt.plot(year, res_env_score, label='Research Environment')
    plt.plot(year, res_qual_score, label='Research Quality')
    plt.plot(year, ind_impact_score, label='Industry Impact')
    
    # plot customizations
    plt.title(f"Trend In Scores For {uni}")
    plt.ylabel("Score (out of 100)")
    plt.xlabel("Year")
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid()

    return plt.gcf()

st.pyplot(uni_ovr_score_trend())