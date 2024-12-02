import streamlit as st
import pandas as pd

def render_experience(heading, data_source, is_startup = True):
    st.header(f":blue[{heading}]", divider='gray')
    df = pd.read_csv(data_source)
    for index, row in df.iterrows():
        col1, col2 = st.columns([0.3, 2])
        with col1:
            st.image(f"images/{row['company']}.png")
        with col2:
            st.subheader(row['title'])
            st.write(f"**{row['company']}** ({row['start_date']} - {row['end_date']})")
            st.write(row['description'])
            st.write("**Achievements:**")
            achievements = row['achievements'].split('•')
            achievements_appended = ''
            for a in achievements[1:]:
                achievements_appended += f"• {a}  \n"
            st.write(achievements_appended)
            if is_startup == False:
                st.write("**:red[Reasons for Failure]:**")
                reason_for_failure = row['reason_for_failure'].split('•')
                for r in reason_for_failure[1:]:
                    st.write(f"• {r}")    

# Page heading
col1_heading, col2_heading = st.columns([1.5,2])

with col1_heading:
    st.image("images/profile_picture.jpeg")

with col2_heading:
    st.title("Dimas Radityo")
    st.write("Product Manager; Aspiring Solopreneur; Lifelong Learner.")
    st.write(":email:: dimasradityo.b@gmail.com")
    st.write(":iphone:: (+62)81802000307")
    st.write(f":memo:: [https://www.linkedin.com/in/dimasradityo/](https://www.linkedin.com/in/dimasradityo/)")

# About Section
st.header(":blue[About]", divider='gray')
content = '''
Zero to one product manager specialized in driving product innovation from conception to market launch. Recognized for meticulous planning, execution, and technical expertise, setting the standard for other teams. Leveraged technical knowledge in engineering and data analysis to seamlessly facilitate collaboration for efficient product discovery and delivery, with no fear of diving in to the gritty details.

Currently a PM at TipTip (Series A), a leading content creator marketplace. Responsible for end-to-end product solutions for communities, including onboarding, monetization, and engagement features.

Previous roles in both early-stage (AdaKerja) and established startups (Ruangguru, Gojek) across diverse industries.

Academically accomplished with honors, and have led an organization in the United States. I have also completed a full-stack developer coding bootcamp and currently pursuing online courses in data analytics and product design.
'''
st.write(content)

# Work Experience Section
render_experience('Full Time Experiences', 'data/full_time.csv')
render_experience('Part Time Experiences', 'data/part_time.csv')
render_experience('Failed Startups', 'data/startups.csv', False)

# Education Section
st.header(f":blue[Education]", divider='gray')
st.write("**Business Management, Finance and Financial Management Services**  \nPPM School of Management - Bachelor's Degree  \n2015 - 2018")
st.write("**Business**  \nShoreline Community College - Associate's Degree  \n2013 - 2015")


# Others Section
col_1_others, col_2_others, col_3_others = st.columns(3)

# Skills Section
with col_1_others:
    st.header(f":blue[Skills]", divider='gray')

    st.write('**Product Management**  \nAdvanced')
    st.write('**User Research**  \nAdvanced')
    st.write('**SQL**  \nAdvanced')
    st.write('**Product Analytics**  \nAdvanced')
    st.write('**Product Strategy**  \nIntermediate')
    st.write('**Python**  \nIntermediate')

# Certifications Section
with col_2_others:
    st.header(f":blue[Certifications]", divider='gray')
    
    st.write('**Quantitative Research**  \nCoursera (2019)')
    st.write('**Data Wrangling, Analysis and AB Testing with SQL**  \nCoursera (2019)')
    st.write('**Certification of Software Engineering**  \nPurwadhika Startup and Coding School (2017)')

# Languages Section
with col_3_others:
    st.header(f":blue[Languages]", divider='gray')
    st.write("**Indonesian**  \nNative")
    st.write("**English**:  \nProfessional")
    st.write("**Chinese**:  \nBasic")
