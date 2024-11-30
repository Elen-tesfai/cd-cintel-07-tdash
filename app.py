import pyshiny

# Create a simple PyShiny application
def app():
    return pyshiny.render.text("Hello, PyShiny World!")

# Run the app
if __name__ == "__main__":
    pyshiny.run_app(app)