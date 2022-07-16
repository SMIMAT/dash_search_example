import dash
import dash_bootstrap_components as dbc

from ui_elements.callbacks import add_callbacks
from ui_elements.layout import make_layout

 
#Change the theme to another bootstrap theme if you'd like
#More themes can be found here https://bootswatch.com/
app = dash.Dash(__name__,external_stylesheets=[dbc.themes.FLATLY])

# Title your app here
app.title = "Search Engine Example"

# Leave dev tools on - this will let you know if something is wrong on the page
# If you are using scheduled jobs, change debug to False both here and at the end of the page
# Otherwise your scheduled jobs will run twice every time
app.enable_dev_tools(debug=True, dev_tools_hot_reload=False)


# Sets the layout of the app to match your layout file
app.layout = make_layout(app)

# Adds callbacks - these make the app actually do stuff
app = add_callbacks(app)


# Run function - spins it up on localhost at port 3000
if __name__ == "__main__":
    app.run_server(debug=True, use_reloader=False, host='0.0.0.0', port=3000)