import streamlit as st
import pandas as pd
import plotly.express as px

# Function to load data
@st.cache_data
def load_data(file_path):
    """Loads and preprocesses the electric vehicle population data."""
    try:
        df = pd.read_csv(file_path)
        # No 'Sale Date' column, using 'Model Year' for time-based analysis
        # Ensure 'Model Year' is integer type
        df['Model Year'] = df['Model Year'].astype(int)
        return df
    except FileNotFoundError:
        st.error(f"Error: The file '{file_path}' was not found.")
        return None
    except Exception as e:
        st.error(f"An error occurred while loading the data: {e}")
        return None

# Function to create sidebar filters
def create_sidebar_filters(df):
    """Creates sidebar filters and returns the filtered dataframe."""
    st.sidebar.header("Filter Options")

    # Model Year slider
    min_year = int(df['Model Year'].min())
    max_year = int(df['Model Year'].max())
    selected_year_range = st.sidebar.slider(
        "Select Model Year Range",
        min_value=min_year,
        max_value=max_year,
        value=(min_year, max_year)
    )
    start_year, end_year = selected_year_range
    filtered_df = df[(df['Model Year'] >= start_year) & (df['Model Year'] <= end_year)]

    # Manufacturer filter
    all_manufacturers = sorted(filtered_df['Make'].unique())
    selected_manufacturers = st.sidebar.multiselect(
        "Select Manufacturer(s)",
        all_manufacturers,
        default=all_manufacturers
    )
    if selected_manufacturers:
        filtered_df = filtered_df[filtered_df['Make'].isin(selected_manufacturers)]

    # Electric Vehicle Type filter
    all_ev_types = sorted(filtered_df['Electric Vehicle Type'].unique())
    selected_ev_types = st.sidebar.multiselect(
        "Select EV Type(s)",
        all_ev_types,
        default=all_ev_types
    )
    if selected_ev_types:
        filtered_df = filtered_df[filtered_df['Electric Vehicle Type'].isin(selected_ev_types)]

    return filtered_df

# Visualization functions
def plot_sales_over_time(df):
    """Plots electric vehicle registrations over model year."""
    # Group by 'Model Year' and count registrations
    registrations_by_year = df.groupby('Model Year').size().reset_index(name='Count')
    fig = px.bar(registrations_by_year, x='Model Year', y='Count', title='Electric Vehicle Registrations by Model Year', color='Count', color_continuous_scale=px.colors.sequential.Viridis)
    st.plotly_chart(fig, use_container_width=True)

def plot_top_manufacturers(df):
    """Plots the top electric vehicle manufacturers."""
    top_manufacturers = df['Make'].value_counts().nlargest(10).reset_index()
    top_manufacturers.columns = ['Make', 'Count']
    fig = px.bar(top_manufacturers, x='Make', y='Count', title='Top 10 Electric Vehicle Manufacturers', color='Count', color_continuous_scale=px.colors.sequential.Viridis)
    st.plotly_chart(fig, use_container_width=True)

def plot_vehicle_types(df):
    """Plots the distribution of electric vehicle types."""
    ev_type_counts = df['Electric Vehicle Type'].value_counts().reset_index()
    ev_type_counts.columns = ['Electric Vehicle Type', 'Count']
    fig = px.pie(ev_type_counts, names='Electric Vehicle Type', values='Count', title='Electric Vehicle Type Distribution', color='Count', color_discrete_sequence=px.colors.sequential.Viridis)
    st.plotly_chart(fig, use_container_width=True)

def plot_electric_range_distribution(df):
    """Plots the distribution of electric ranges."""
    fig = px.histogram(df, x='Electric Range', nbins=50, title='Distribution of Electric Range' ,color='Electric Range')
    st.plotly_chart(fig, use_container_width=True)

def plot_county_distribution(df):
    """Plots the distribution of vehicles by county."""
    county_counts = df['County'].value_counts().nlargest(10).reset_index()
    county_counts.columns = ['County', 'Count']
    fig = px.bar(county_counts, x='County', y='Count', title='Top 10 Counties by EV Registrations', color='Count', color_continuous_scale=px.colors.sequential.Viridis)
    st.plotly_chart(fig, use_container_width=True)

# Main dashboard function
def main():
    st.set_page_config(layout="wide")
    st.title("Electric Vehicle Sales Analysis")

    df = load_data("Electric_Vehicle_Population_Data.csv")

    if df is not None:
        filtered_df = create_sidebar_filters(df)

        st.header("Key Performance Indicators")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Vehicles", f"{len(filtered_df):,}")
        with col2:
            st.metric("Unique Manufacturers", f"{filtered_df['Make'].nunique():,}")
        with col3:
            st.metric("Average Electric Range (miles)", f"{filtered_df['Electric Range'].mean():,.0f}")

        st.header("Sales Trends")
        plot_sales_over_time(filtered_df)

        st.header("Vehicle Demographics")
        col1, col2 = st.columns(2)
        with col1:
            plot_top_manufacturers(filtered_df)
        with col2:
            plot_vehicle_types(filtered_df)

        st.header("Electric Range and County Distribution")
        plot_electric_range_distribution(filtered_df)

        st.header("County Distribution")
        plot_county_distribution(filtered_df)

if __name__ == "__main__":
    main()