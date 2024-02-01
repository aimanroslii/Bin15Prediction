import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import streamlit.components.v1 as components
import seaborn as sns
#import pygwalker as pyg

def addValue(row):
    if row['% Bin 15'] >= 2.0:
       return 'Bad'
    else:
        return 'Good'



def load_data():
    #Acquire data
    train_df = pd.read_csv('../Data/train_data.csv')
    test_df = pd.read_csv('../Data/test_data.csv')
    combine = [train_df, test_df]

    train_df = train_df.drop("Unnamed: 8", axis=1)
    train_df = train_df.drop("Unnamed: 9", axis=1)
    train_df = train_df.drop("Unnamed: 10", axis=1)
    train_df = train_df.drop("Unnamed: 11", axis=1)
    train_df = train_df.drop("Unnamed: 12", axis=1)
    train_df = train_df.drop("Unnamed: 13", axis=1)
    train_df = train_df.drop("Unnamed: 14", axis=1)
    train_df = train_df.drop("Unnamed: 15", axis=1)
    train_df = train_df.drop("Unnamed: 16", axis=1)
    train_df = train_df.drop("Unnamed: 17", axis=1)
    train_df = train_df.drop("Fab WW", axis=1)
    train_df = train_df.drop("Wafer Coat MT", axis=1)

    test_df = test_df.drop("Unnamed: 9", axis=1)
    test_df = test_df.drop("Unnamed: 10", axis=1)
    test_df = test_df.drop("Unnamed: 11", axis=1)
    test_df = test_df.drop("Unnamed: 12", axis=1)
    test_df = test_df.drop("Unnamed: 13", axis=1)
    test_df = test_df.drop("Unnamed: 14", axis=1)
    test_df = test_df.drop("Unnamed: 15", axis=1)
    test_df = test_df.drop("Unnamed: 16", axis=1)
    test_df = test_df.drop("Unnamed: 17", axis=1)
    test_df = test_df.drop("Unnamed: 8", axis=1)
    test_df = test_df.drop("Fab WW", axis=1)
    test_df = test_df.drop("Wafer Coat MT", axis=1)

    train_df['Status Bin15'] = train_df.apply(addValue, axis=1)

    return train_df

df = load_data()
@st.cache_data
def show_explore_page():
    st.title("Explore Bin15 Percentage Information")

    st.write(""" """)
    st.write("""#### Bin15 Status vs Wafer Coat Tool""")
    # Create a FacetGrid using Seaborn
    g = sns.FacetGrid(df, col='Status Bin15')
    g.map(plt.hist, 'Wafer Coat Tool', bins=20)
    # Convert the Matplotlib plot to a Streamlit-friendly format
    fig, ax1 = plt.subplots()
    sns.histplot(df, x='Wafer Coat Tool', bins=20, hue='Status Bin15', multiple='stack', ax=ax1)
    st.pyplot(fig)

    st.write(""" """)
    st.write("""#### Bin15 Status vs Fab""")
    g = sns.FacetGrid(df, col='Status Bin15')
    g.map(plt.hist, 'Fab Plant', bins=20)
    # Convert the Matplotlib plot to a Streamlit-friendly format
    fig2, ax1 = plt.subplots()
    sns.histplot(df, x='Fab Plant', bins=20, hue='Status Bin15', multiple='stack', ax=ax1)
    st.pyplot(fig2)

    st.write(""" """)
    st.write("""#### Bin15 Status vs Supplier""")
    g = sns.FacetGrid(df, col='Status Bin15')
    g.map(plt.hist, 'Supplier', bins=20)
    # Convert the Matplotlib plot to a Streamlit-friendly format
    fig1, ax1 = plt.subplots()
    sns.histplot(df, x='Supplier', bins=20, hue='Status Bin15', multiple='stack', ax=ax1)
    st.pyplot(fig1)