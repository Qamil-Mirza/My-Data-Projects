import numpy as np 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import sys
import path

dir = path.Path(__file__).abspath()
sys.path.append(dir.parent.parent)

file_path = './world-uni-rankings.csv'


# Set up page configurations
st.set_page_config(page_title='World Universities Interactive Dashboard', page_icon='🎓', layout='wide')

world_uni_df = pd.read_csv(file_path, encoding='latin1')

st.title('🎓World Universities Dashboard')

year = st.slider('Year Selected', 2016, 2024, key='summary')

col_1, col_2, col_3, col_4, col_5, col_6 = st.columns(6, gap='large')

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

with col_6:
    st.header('Best International Outlook')
    def best_international_outlook(year=year):
        sorted_by_year = world_uni_df[world_uni_df['Year'] == year]
        sort_desc = sorted_by_year.sort_values('International Outlook', ascending=False)
        school_name = sort_desc['Name'].iloc[0]
        score = sort_desc['International Outlook'].iloc[0]
        return school_name, round(score,1)
    
    best_int_out_school, most_int_out_score = best_international_outlook()

    st.write(f"{best_int_out_school}")
    st.write(f"Score: {most_int_out_score}")

st.divider()

top_ten_year = st.slider('Year Selected', 2016, 2024, key='top-ten-year')

st.header(f'Overall Top 10 Universities In The World In {top_ten_year}')
def top_ten_tbl(year=top_ten_year):
    sorted_by_year = world_uni_df[world_uni_df['Year'] == year]
    sort_desc = sorted_by_year.sort_values('Overall Score', ascending=False)
    top_ten_uni = sort_desc[:10].reset_index(drop=True).set_index('Rank')
    return top_ten_uni[['Name', 'Overall Score']]

st.write(top_ten_tbl())

st.divider()

st.header(f'Trend In Overall Scores')
uni_names_array = world_uni_df.Name.unique()
uni_selection = st.selectbox(label='University Selected', options=uni_names_array, key='top-ten-tbl')

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
    int_out_score = filter_by_uni['International Outlook']

    # Plot
    plt.figure(figsize=(10,6))
    plt.plot(year, ovr_score, label='Overall Score')
    plt.plot(year, teach_score, label='Teaching')
    plt.plot(year, res_env_score, label='Research Environment')
    plt.plot(year, res_qual_score, label='Research Quality')
    plt.plot(year, ind_impact_score, label='Industry Impact')
    plt.plot(year, int_out_score, label='International Outlook')
    
    # plot customizations
    plt.title(f"Trend In Scores For {uni}")
    plt.ylabel("Score (out of 100)")
    plt.xlabel("Year")
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid()

    return plt.gcf()

st.pyplot(uni_ovr_score_trend())

st.divider()

st.header('University Student And Staff Population')

pie_col_1, pie_col_2 = st.columns(2)

with pie_col_1:
    pie_year = st.slider('Year Selected', 2016, 2024, key='pie-chart-year')

with pie_col_2:
    pie_uni = st.selectbox(label='University Selected', options=uni_names_array, key='pie-chart-uni')

# Feature engineering to get student and staff population
def get_staff_pop():
    staff_pop_df = world_uni_df
    staff_pop_df['Staff Population'] = world_uni_df['Student Population'] * (1/world_uni_df['Students to Staff Ratio'])
    return staff_pop_df

staff_pop_df = get_staff_pop()

def pie_chart(uni=pie_uni, year=pie_year):
    # Data wrangling
    data = []
    filtered_data = staff_pop_df[(staff_pop_df['Year'] == year) & (staff_pop_df['Name'] == uni)]
    student_pop = filtered_data['Student Population'].iloc[0]
    staff_pop = filtered_data['Staff Population'].iloc[0]
    student_ratio = student_pop / (student_pop + staff_pop)
    staff_ratio = staff_pop / (student_pop + staff_pop)
    data.append(round(student_ratio, 2))
    data.append(round(staff_ratio, 2))

    # Initialize figure
    fig, ax = plt.subplots(figsize=(7,3))
    ax.pie(data, labels=['Student', 'Staff'], autopct='%1.1f%%', colors=['#003262', '#C4820E'], textprops=dict(color='w', weight='bold', size=10))
    ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    ax.set_title(f'{year} Student & Staff Population Percentage For {uni}')
    
    return fig

# Display the plot in Streamlit
st.pyplot(pie_chart())

st.divider()

st.header("Gender Ratio Over Time")

gender_uni = st.selectbox(label='University Selected', options=uni_names_array, key='gender-uni')


def get_female_male_pop_df():
    male_female_pop_df = world_uni_df.copy()
    boolean_mask = male_female_pop_df['Female to Male Ratio'].str.len() > 5
    male_female_pop_df.loc[boolean_mask, 'Female to Male Ratio'] = male_female_pop_df.loc[boolean_mask, 'Female to Male Ratio'].str[:-3]
    
    # Now we split the ratios into two columns
    male_female_pop_df['Female Population Percentage'] = male_female_pop_df['Female to Male Ratio'].str[:2]
    male_female_pop_df['Female Population Percentage'] = pd.to_numeric(male_female_pop_df['Female Population Percentage'],
                                                                        errors='coerce').astype('Int64')
    
    male_female_pop_df['Male Population Percentage'] = male_female_pop_df['Female to Male Ratio'].str[3:]
    male_female_pop_df['Male Population Percentage'] = pd.to_numeric(male_female_pop_df['Male Population Percentage'],
                                                                        errors='coerce').astype('Int64')
    
    # drop the Female to Male Ratio column
    male_female_pop_df.drop('Female to Male Ratio', inplace=True, axis=1)

    # drop the rows with null values
    male_female_pop_df.dropna(inplace=True)
    return male_female_pop_df

df_male_female = get_female_male_pop_df()

# Create a function to plot the bar chart Over time
def gender_ratio_over_time(uni=gender_uni):
    plt.figure(figsize=(10,6))
    filter_by_uni = df_male_female[df_male_female['Name'] == uni]

    year = filter_by_uni['Year']
    female = filter_by_uni['Female Population Percentage']
    male = filter_by_uni['Male Population Percentage']

    # initialize the plot
    plt.figure(figsize=(10,6))
    # calculate the width of each bar
    bar_width = 0.35

    # calculate the x positions for the bars
    bar_positions_female = np.arange(len(year))
    bar_positions_male = bar_positions_female + bar_width

    # plot the female and male population percentage side by side
    plt.bar(year, female, width=bar_width, color='pink', label='Female')
    plt.bar(year+bar_width, male, width=bar_width, color='blue', label='Male')

    # plot customizations
    plt.title(f'Distribution Of Gender Ratio Over Time: {uni}')
    plt.xlabel('Year')
    plt.xticks(year+bar_width/2, year)
    plt.ylabel('Percentage')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid()
    return plt.gcf()

st.pyplot(gender_ratio_over_time())

st.markdown("If graph is not showing, it means the data isn't available for that university. Please select another university.")