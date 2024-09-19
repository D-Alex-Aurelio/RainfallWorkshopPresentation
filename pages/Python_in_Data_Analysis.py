import streamlit as st


st.title("Python in Data Analysis")
st.header("Significance of Python in Data Analysis")
st.write("- Simple syntax")
st.write("- Wide range of libraries")

st.divider()

st.header("Integrated Development Environment (IDEs)")
st.write("### PyCharm")
st.write("- From JetBrains, used to create Python applications")
st.image("images/pycharm.png")
st.page_link("https://www.jetbrains.com/pycharm/",
             label="Download PyCharm")
st.write("### Google Colab")
st.write("- Uses cells to separate code into parts")
st.write("- Optimal for step-by-step applications")
st.image("images/google colab.png")
st.page_link("https://colab.research.google.com/",
             label="Try out Google Colab")
st.divider()

st.header("Python Libraries for Dashboard Creation")
st.write("### Pandas")
st.write("- Used for reading data files")
st.write("### Seaborn")
st.write("- Used for plotting data")
st.write("- Creates static plots")
st.write("### Plotly")
st.write("- Used to create interactive plots")
st.write("### Streamlit")
st.write("- Used to create web applications")