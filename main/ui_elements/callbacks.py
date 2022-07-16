"""Separate module for callbacks. As your application becomes larger, it can be useful to split these out."""

import dash_html_components as html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from utilities.search_function import primary_search
from ui_elements.style_dicts import *

'''


Callbacks are used to add dynamic page functions to your application. These are equivalent to onPress for a button in JavaScript.

Every callback needs at least one input and one output. The format for these always goes ('name_of_page_element', 'parameter_used')
The Input is the trigger. When this piece of its attached page component is changed, it will trigger the function.
The Output is what gets changed. The function needs to return one item for every output you have in your callback. 
    If you are returning a sentence to a text block and a new color to a button, you need to return those two things from your function in that order.
Each of your inputs needs to be listed as a parameter of the function defined under the callback.

You can use the State feature to take in another element on the page without necessarily triggering the function from that element.

'''


def add_callbacks(app):
    """Adds callbacks to your application."""

    # This callback opens up a modal window with developer notes.
    #
    # It takes in the number of clicks from the dev_notes link at the top of the page. 
    # It returns either true or false to the modal is_open component. Returning False will close it, returning True will open it.
    #
    @app.callback(
        Output('dev_notes_modal', 'is_open'),
        Input('dev_notes','n_clicks')
    )
    def open_dev_notes_modal(clicks):
        if not clicks:
            raise PreventUpdate
        return True
    

    # This callback disables the button if nothing is searched yet.
    # This is not really necessary for the app to work, but is helpful to illustrate that it's something you can do.
    @app.callback(
        Output('search_button','disabled'),
        Input('search_input','value')
    )
    def disable_search_button(inputs):
        if not inputs:
            return True
        if len(inputs) < 2:
            return True
        return False


    # This executes the search
    # It takes in the input text as a state - we don't want it to search every time they type a new letter. Only when the button is clicked.
    # For every item it finds, it will return a text block.
    # This is a good placeholder as you will find most APIs return a list of dicts fairly similar to this.
    @app.callback(
        Output('search_results','children'),
        Input('search_button','n_clicks'),
        State('search_input','value')
    )
    def execute_search(clicks, search_value):
        if not clicks:
            return None
        
        results_list = primary_search(search_value)

        if len(results_list) == 0:
            return html.P(
                "No results found - please try a new search term."
                ,style=readout_style
            )
        
        else:
            base_results = []
            for i in results_list:
                base_results.append(
                    html.P(
                        style=readout_style
                        ,children=[
                            html.Br()
                            ,"Make: {} ".format(i['make'])
                            ,html.Br()
                            ,"Model: {} ".format(i['model'])
                            ,html.Br()
                            ,"Engine: {} ".format(i['engine'])
                            ,html.Br()
                            ,"Style: {} ".format(i['style'])
                            ,html.Br()
                            ,"Description: {} ".format(i['desc'])
                            ,html.Br()
                            ,html.Br()
                        ]
                    )
                )
            return base_results


    return app