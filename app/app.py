import seaborn as sns  # For creating plots
from faicons import icon_svg  # Provides access to icon assets for UI
from shiny import reactive  # Enables reactive programming
from shiny.express import input, render, ui  # Simplifies Shiny UI and server definitions
import palmerpenguins  # Dataset for visualizations and analysis
from pathlib import Path  # For working with file system paths

# Loading the data into an initial Pandas DataFrame
df = palmerpenguins.load_penguins()

# Creating a page title
ui.page_opts(title="Elen Tesfai's Penguins Dashboard", fillable=True)

# Sidebar for filter controls
with ui.sidebar(title="Filter controls"):
    # Slider input to filter by mass (body mass)
    ui.input_slider(
        "mass", 
        "Mass (g)", 
        min=2000, 
        max=6000, 
        value=6000  # Initial value
    )

    # Checkbox Group to filter by penguin species
    ui.input_checkbox_group(
        "species", 
        "Species", 
        choices=["Adelie", "Gentoo", "Chinstrap"], 
        selected=["Adelie", "Gentoo", "Chinstrap"]
    )
    
    # Horizontal line for separation
    ui.hr()
    
    # Links Section in Sidebar
    ui.h6("Links")
    ui.a("GitHub Source", href="https://github.com/denisecase/cintel-07-tdash", target="_blank")
    ui.a("GitHub App", href="https://denisecase.github.io/cintel-07-tdash/", target="_blank")
    ui.a("GitHub Issues", href="https://github.com/denisecase/cintel-07-tdash/issues", target="_blank")
    ui.a("PyShiny", href="https://shiny.posit.co/py/", target="_blank")
    ui.a("Template: Basic Dashboard", href="https://shiny.posit.co/py/templates/dashboard/", target="_blank")
    ui.a("See also", href="https://github.com/denisecase/pyshiny-penguins-dashboard-express", target="_blank")

# Main content area (outputs)
with ui.layout_column_wrap(fill=False):
    # Value box showing number of penguins in the filtered dataset
    with ui.value_box(showcase=icon_svg("earlybirds")):
        "Number of penguins"
        
        # Reactive function to return the count of penguins
        @render.text
        def count():
            return f"{filtered_df().shape[0]} penguins"

    # Value box showing average bill length of penguins in the filtered dataset
    with ui.value_box(showcase=icon_svg("ruler-horizontal")):
        "Average bill length"
        
        # Reactive function to return the average bill length
        @render.text
        def bill_length():
            return f"{filtered_df()['bill_length_mm'].mean():.1f} mm"

    # Value box showing average bill depth of penguins in the filtered dataset
    with ui.value_box(showcase=icon_svg("ruler-vertical")):
        "Average bill depth"
        
        # Reactive function to return the average bill depth
        @render.text
        def bill_depth():
            return f"{filtered_df()['bill_depth_mm'].mean():.1f} mm"

# Visualizations and data display section
with ui.layout_column_wrap():
    # Card showing Seaborn scatterplot: Bill length vs. Bill depth
    with ui.card(full_screen=True):
        ui.card_header("Bill length and depth")
        
        @render.plot
        def length_depth():
            return sns.scatterplot(
                data=filtered_df(),
                x="bill_length_mm",
                y="bill_depth_mm",
                hue="species",  # Color datapoints by species
            )

    # Card showing summary statistics (Data Grid)
    with ui.card(full_screen=True):
        ui.card_header("Penguin Data")
        
        @render.data_frame
        def summary_statistics():
            cols = [
                "species",
                "island",
                "bill_length_mm",
                "bill_depth_mm",
                "body_mass_g",
            ]
            return render.DataGrid(filtered_df()[cols], filters=True)

# Optional: Include external CSS for styling (Make sure `styles.css` exists in the correct directory)
# ui.include_css(app_dir / "styles.css")

# Reactive function to filter dataset based on user inputs
@reactive.calc
def filtered_df():
    # Filtering by selected species
    filt_df = df[df["species"].isin(input.species())]
    
    # Filtering by body mass (based on the slider value)
    filt_df = filt_df.loc[filt_df["body_mass_g"] < input.mass()]
    
    return filt_df