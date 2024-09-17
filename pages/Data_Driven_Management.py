import streamlit as st

st.title("Data Driven Management")
st.header("Definition")
st.write("Decisions are based on gathered data.")

st.divider()

st.header("Data Analysis Process")

st.markdown("### 1. Define Objectives and Questions")
st.write("Sets the direction of the analysis.")
with st.expander("What is the objective of the Rainfall Dashboard?"):
     st.write("To analyze rainfall depth in terms of yearly, monthly, and daily time intervals")

st.markdown("### 2. Collection of Data")
st.write("Through interviews, surveys, observations, and existing databases.")
with st.expander("Where can we get rainfall data in the web?"):
    st.page_link("https://www.pagasa.dost.gov.ph/climate/climate-data",
                     label="PAGASA website")
    st.page_link("https://power.larc.nasa.gov/data-access-viewer/",
                     label="NASA Data Access Viewer")

st.markdown("### 3. Data Cleaning")
st.write("Checking for inconsistencies in the data and correcting them.")
with st.expander("What can we do with if there is missing data in the rainfall dataset?"):
    st.write("We can change the missing data to zero or equate it to the median or mean of the dataset.")

st.markdown("### 4. Data Analysis")
st.write("The application of statistical or mathematical techniques to discover patterns in the data.")
with st.expander("What techniques can we use for the rainfall analysis?"):
    st.write("Summary statistics such as the measures of central tendency (mean and median)")

st.markdown("### 5. Data Interpretation and Visualization")
st.write("Visual representation of data, makes it easier to understand complex data")
with st.expander("What graphs might one use for rainfall analysis?"):
    st.write("For time series analysis, a line graph is a common visualization to use.")

st.markdown("### 6. Data Presentation")
st.write("Presenting one's findings in a form that in easy to understand.")

st.divider()

st.header("Data Analysis Tools")

st.markdown("### MS Excel")
st.write("Simple and versatile with no programming skills needed")

st.markdown("### MS Power BI")
st.write("Transforms raw data into interactive visualizations")

st.markdown("### Structured Query Language (SQL)")
st.write("Managing and manipulating databases")

st.markdown("### R Programming")
st.write("Specifically designed for statistical computing and graphics")

st.markdown("### Python Programming")
st.write("General purpose programming language with wide range of libraries")

st.divider()

st.header("DataCamp Article")
st.write("All info presented is from the following article:")
st.page_link("https://www.datacamp.com/blog/what-is-data-analysis-expert-guide",
             label="What is Data Analysis? An Expert Guide With Examples")