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
            for a in achievements[1:]:
                st.write(f"• {a}")
            if is_startup == False:
                st.write("**:red[Reasons for Failure]:**")
                reason_for_failure = row['reason_for_failure'].split('•')
                for r in reason_for_failure[1:]:
                    st.write(f"• {r}")    

# Page heading
col1, col2 = st.columns([1.5,2])

with col1:
    st.image("images/profile_picture.jpeg")

with col2:
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

# Full Time Experience Section
render_experience('Full Time Experiences', 'data/full_time.csv')
    

# Part Time Experience Section
render_experience('Part Time Experiences', 'data/part_time.csv')

# Failed Startups Section
render_experience('Failed Startups', 'data/startups.csv', False)
