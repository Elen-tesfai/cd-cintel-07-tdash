import pyshiny as shiny
import pandas as pd
import plotly.express as px
import logging

# Set up logging for the app
logging.basicConfig(level=logging.INFO)

# Step 1: Load and process the data
def load_data():
    """
    Loads and processes the dataset for display and visualization.
    The data source here is a CSV file, but it can be replaced with any other data source.
    """
    try:
        df = pd.read_csv("data.csv")  # Replace with your actual data path
        df['Date'] = pd.to_datetime(df['Date'])  # Convert date columns to datetime type
        logging.info("Data loaded successfully.")
        return df
    except Exception as e:
        logging.error(f"Error loading data: {e}")
        return pd.DataFrame()  # Return an empty dataframe on error

# Step 2: Create a line chart plot (Plotly)
def create_line_chart(df):
    """
    Generates a line chart for visualizing time series data.
    """
    fig = px.line(df, x='Date', y='Value', title='Time Series Data')
    return fig

# Step 3: Create a bar chart plot (Plotly)
def create_bar_chart(df):
    """
    Generates a bar chart for visualizing category-wise data.
    """
    fig = px.bar(df, x='Category', y='Amount', title='Category-wise Bar Chart')
    return fig

# Step 4: Create a table for displaying raw data
def create_data_table(df):
    """
    Creates a table to display the data in tabular format.
    """
    return shiny.DataTable(df)

# Step 5: Create the layout for the dashboard
def create_layout():
    """
    Defines the layout of the interactive dashboard.
    This layout includes the main title, dropdowns, sliders, and output sections.
    """
    layout = shiny.div(
        shiny.h1("Interactive Analytics Dashboard"),
        shiny.div(id="intro", children="Welcome to the interactive analytics dashboard!"),
        
        # Dropdown for chart selection
        shiny.div(
            shiny.selectInput("chart_type", label="Choose Chart Type", 
                             choices=["Line Chart", "Bar Chart"], 
                             selected="Line Chart")
        ),
        
        # Slider for time range selection (for example)
        shiny.div(
            shiny.sliderInput("time_range", "Select Time Range", 
                             min=2020, max=2024, value=(2020, 2024), step=1)
        ),
        
        # Row for the charts
        shiny.row(
            shiny.column(6, shiny.plotlyOutput("plot1")),  # Chart 1
            shiny.column(6, shiny.plotlyOutput("plot2"))   # Chart 2
        ),
        
        # Row for the data table
        shiny.row(
            shiny.column(12, shiny.dataTableOutput("data_table"))  # Data Table
        )
    )
    return layout

# Step 6: Set up the interactivity for the dashboard
def update_plots(input, output, session):
    """
    Updates the plots and data table dynamically based on user input.
    """
    # Render plot 1 based on chart type selection
    @output(id="plot1")
    def plot1():
        df = load_data()
        chart_type = input["chart_type"]
        
        if chart_type == "Line Chart":
            return create_line_chart(df)
        else:
            return create_bar_chart(df)

    # Render plot 2 (could be another type of chart or the same)
    @output(id="plot2")
    def plot2():
        df = load_data()
        return create_bar_chart(df)  # For simplicity, returning bar chart for plot 2
    
    # Render the data table
    @output(id="data_table")
    def data_table():
        df = load_data()
        return create_data_table(df)

# Step 7: Define the main function to run the app
def main():
    """
    The main function that runs the PyShiny app.
    """
    # Load the data (could be used in multiple parts of the app)
    df = load_data()
    
    # Create the dashboard layout
    layout = create_layout()
    
    # Set up the interactivity using callback functions
    shiny.App(layout=layout, server=update_plots)

if __name__ == "__main__":
    main()