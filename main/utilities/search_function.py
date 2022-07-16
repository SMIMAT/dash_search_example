"""Contains the primary search function. Rudimentary but illustrates the point."""

from utilities.base_data import base_data


def primary_search(input):
    """Scans all elements of our data and returns a filtered list of items that match our criteria."""
    final_list = []
    input = input.lower()
    for item in base_data:
        for key in item.keys():
            if input in item[key].lower():
                final_list.append(item)
    
    return final_list