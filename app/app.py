import seaborn as sns  # For creating plots
from faicons import icon_svg  # Provides access to icon assets for UI

from shiny import reactive  # Enables reactive programming
from shiny.express import input, render, ui  # Simplifies Shiny UI and server definitions
import palmerpenguins  # Dataset for visualizations and analysis
from pathlib import Path  # For working with file system paths


#Loading the data into an initial Pandas DataFrame
df = palmerpenguins.load_penguins()

#Creating a page title
ui.page_opts(title="Elen Tesfai's Penguins dashboard", fillable=True)

#This is needed for selecting the category
with ui.sidebar(title="Filter controls"):

    # Slider input to filter by mass
    ui.input_slider("mass", "Mass", 2000, 6000, 6000)

    # Checkbox Group to filter by penguin species
    ui.input_checkbox_group(
        "species",
        "Species",
        ["Adelie", "Gentoo", "Chinstrap"],
        selected=["Adelie", "Gentoo", "Chinstrap"],
    )
    ui.hr()
    ui.h6("Links") # Header for Links section

    # Clickable links to resources
    ui.a(
        "GitHub Source",
        href="https://github.com/denisecase/cintel-07-tdash",
        target="_blank",
    )
    ui.a(
        "GitHub App",
        href="https://denisecase.github.io/cintel-07-tdash/",
        target="_blank",
    )
    ui.a(
        "GitHub Issues",
        href="https://github.com/denisecase/cintel-07-tdash/issues",
        target="_blank",
    )
    ui.a("PyShiny", href="https://shiny.posit.co/py/", target="_blank")
    ui.a(
        "Template: Basic Dashboard",
        href="https://shiny.posit.co/py/templates/dashboard/",
        target="_blank",
    )
    ui.a(
        "See also",
        href="https://github.com/denisecase/pyshiny-penguins-dashboard-express",
        target="_blank",
    )

# Main content area (outputs)
with ui.layout_column_wrap(fill=False):

    # Value box showing number of penguins in the filtered dataset
    with ui.value_box(showcase=icon_svg("earlybirds")):
        "Number of penguins"

        @render.text
        def count():
            return filtered_df().shape[0]
    # Value box showing avg bill length of penguins in the filtered dataset
    with ui.value_box(showcase=icon_svg("ruler-horizontal")):
        "Average bill length"

        @render.text
        def bill_length():
            return f"{filtered_df()['bill_length_mm'].mean():.1f} mm"

     # Value box showing avg bill depth of penguins in the filtered dataset
    with ui.value_box(showcase=icon_svg("ruler-vertical")):
        "Average bill depth"

        @render.text
        def bill_depth():
            return f"{filtered_df()['bill_depth_mm'].mean():.1f} mm"


with ui.layout_columns():
    with ui.card(full_screen=True):

        # Seaborn scatterplot showing Bill length vs. depth
        ui.card_header("Bill length and depth")

        @render.plot
        def length_depth():
            return sns.scatterplot(
                data=filtered_df(),
                x="bill_length_mm",
                y="bill_depth_mm",
                hue="species",    # Color datapoints by species
            )

    with ui.card(full_screen=True):

        # Data Grid showing summary stats of filtered dataset
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


#ui.include_css(app_dir / "styles.css")

# Reactive function to filter dataset based on user inputs
@reactive.calc
def filtered_df():
    filt_df = df[df["species"].isin(input.species())]
    filt_df = filt_df.loc[filt_df["body_mass_g"] < input.mass()]
    return filt_df