#!/usr/bin/env python3

def array_of_names(name_dict):
    full_names = []
    for first, last in name_dict.items():
        full_name = first.capitalize() + ' ' + last.capitalize()
        full_names.append(full_name)
    return full_names

# Example usage
persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_names(persons))
