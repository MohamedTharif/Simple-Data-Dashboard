"""
Created on Thu Aug  8 19:13:57 2024

@author: Mohamed Tharif
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def set_heading():
    #set the header    
    st.title("Simple Data Dashboard For Your Files")
    
    st.sidebar.title("Operations")

def set_sidebar():
    sidebar_value=st.sidebar.selectbox("Information about the Data",["Info","Calculations","Visualize"]) 
def file_upload():
    try:
        #accepting csv file as input
        uploaded_file=st.file_uploader("Enter Your CSV File",type="csv")
        return uploaded_file
    except:
        st.warning("Error While Loading File")

def file_info(df) -> None:
     
   
        #thie first five columns and values were printed
        st.subheader("Data Preview")
        st.write(df.head())    
        #st.write("Types of Data Present In the File",df.dtypes)     
    
        #row size and column size were displayed
        st.subheader("File Info")
        
        #finding size of the File
        rows=df.shape[0]
        column=df.shape[1]
        st.write("Columns Present in the File ", column)
        st.write("Rows Present in the File ",rows)

def fill_missing(df) -> pd.DataFrame:
    #filling missing values
    st.write("Has Missing Values")
    if st.button("Fill Missing Values"):
        st.write("Filling With 0")
        df=df.fillna(0)
        return df
    else :
        return df

def filter_data(df) -> None:
    #Columns are displayed
    st.subheader("Filter Data")  
    columns=df.columns.tolist()
    
    selected_column=st.selectbox("Select Column to filter by",columns)
    
    #Values In the Column were displayed
    unique_values=df[selected_column].unique()
    selected_value=st.selectbox("Select Values",unique_values)
    
    #selecting the column values which has been choosen by user
    filtered_df=df[df[selected_column]== selected_value]
    st.write(filtered_df)
    
    
def categorizing_columns(df) -> pd.DataFrame:
    #catogorizng the columns which is in type of Numerical values
    numerical_column = df.select_dtypes(include=['int64' , 'float64'])
    return numerical_column

#calculations has been done 
def Calculations(df,value,operation) -> float :
    if operation == "MAX":
        return df[value].max()    
    elif operation == "MIN":
        return df[value].min()
    elif operation == "MEAN":
        return df[value].mean()
    elif operation == "MEDIAN":
        return df[value].median()
    elif operation == "MODE":
        return df[value].mode()
    elif operation == "SUM":
        return df[value].sum()
    
def performing_calculations(df,operating_column) -> None:
    #performing Calculations 
    st.subheader("Calculations that can be Performed In the Below Columns")
    if operating_column is not None:
        
        calculating_value=st.selectbox("Columns",operating_column.columns.tolist())
   
        #type of operations 
        operations=["MIN","MAX","MEAN","MEDIAN","MODE","SUM"]    
        mode_of_operation=st.selectbox("Mode Of Operation",operations)
        
        #calculate results
        result=Calculations(df,calculating_value,mode_of_operation)
        
        display_result=f"{mode_of_operation} is {result} "
        if st.button("Enter"):
            st.write(display_result)
    else :
        st.write("No Calculations Can be Done Here")

#plot using matplotlib
def plot_data(df,columns) -> None:   
     
    st.subheader("Visualizing the Data")
   
    x_column=st.selectbox("Select x-axis Column",columns.columns.tolist())
    y_column=st.selectbox("Select y-axis Column",columns.columns.tolist())
    
    sort_x=sorted(df[x_column])
    sort_y=sorted(df[y_column])
    
    line_chart=plt.figure()
    #sorting columns for plotting
    plt.plot(sort_x,sort_y)
    
    bar_chart=plt.figure()
    plt.bar(sort_x,sort_y)    
    
    tab1,tab2=st.tabs(["Line Chart","Bar_chart"])
       
    #adding button for generating chart
    if st.button("Generate Chart"):
        #adding to the page
        tab1.subheader("Plotted Line Chart")
        tab1.pyplot(line_chart) 
        
        tab2.subheader("PLotted Bar Chart")
        tab2.pyplot(bar_chart)
         
        
        
if __name__ == "__main__":
    
   
    set_heading()

    set_sidebar()
    
    uploaded_file=file_upload()

    if uploaded_file is not None:
        #read through the pandas 
        df=pd.read_csv(uploaded_file)    
                
        #filling null values
        if df.isnull :           
            df=fill_missing(df)
            
                 
        file_info(df)
        
        filter_data(df)
          
                                           
        #calculations only performed with only numerical values
        #checking what are the columns can be used to calculate             
        operating_column=categorizing_columns(df)
      
        #adding to page
        performing_calculations(df,operating_column)
       
        #plotting the visual in the Page
        plot_data(df,operating_column)      
        
        
    else :
        st.write("Upload File......")    



