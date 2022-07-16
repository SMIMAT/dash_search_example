import dash_html_components as html    # Dash HTML page elements
import dash_bootstrap_components as dbc   # Dash bootstrap elements - same as dcc but looks better

from ui_elements.style_dicts import * # Our predefined style dictionaries used to keep everything looking consistent

def make_layout(app):
    """Creates the layout for the application"""
    # Layout contained here. Your layout always starts with a Div, which is just an empty container on the page
    layout = html.Div(
        [
            # Navigation bar is stored here
            dbc.Navbar(
                [
                    dbc.NavItem(dbc.NavbarBrand(
                        app.title
                        ,className="ml-2"
                        ,style={
                            'color':'white'
                        }
                    ))
                    # To put stuff in the bar, you have to store it as follows to get it working right
                    ,dbc.Nav([
                        dbc.NavItem(
                            dbc.NavLink(
                                children='Developer Notes'
                                ,id='dev_notes'
                                ,n_clicks=None
                                ,href="#"
                            )
                        )
                    ])
                ]
                # Changes the color of the navbar. "Light" "dark" and "primary" are your options
                ,color='primary'
            )
            # Popup window for developer notes
            ,dbc.Modal(
                [
                    dbc.ModalHeader("Developer Notes")
                    ,dbc.ModalBody(
                        html.Div(
                            html.P(
                                [
                                    "This application is built using Flask/Dash."
                                    ,html.Br()
                                    ,html.A(
                                        children="The GitHub repository for this application can be found here."
                                        ,href="https://github.com/SMIMAT/dash_search_example",
                                    )
                                ]
                            )
                        )
                    )
                ]
                ,id="dev_notes_modal"
                ,size="lg"
            )
            # Our search input box and trigger button.
            ,html.Div(
                style=divstyle
                ,children=[
                    dbc.Input(
                        id="search_input"
                        ,type='text'
                        ,style={
                            "margin": 10
                            ,"width": 400
                            ,"height": 50
                        }
                        ,placeholder="Enter search terms here. EX: 'V8', 'ford', 'sedan', etc."
                    )
                    ,dbc.Button(
                        id="search_button"
                        ,children="Search"
                        ,disabled=True
                        ,style=button
                        ,color="dark"
                    )
                ]
            )
            # Line dividing the page
            ,html.Hr()
            # Empty div used to contain our search results.
            ,html.Div(
                id='search_results'
            )
        ]
    )

    return layout