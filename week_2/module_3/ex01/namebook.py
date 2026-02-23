

def format_names(persons: dict[str, str]) -> list[str]:
    """returns a list with the key and value together"""
    full_names = []
    for key, value in persons.items():
        key_start = key.capitalize()
        value_end = value.capitalize()
        full_names.append(key_start + " " + value_end)
    return full_names

# if __name__ == "__main__":
#     persons = {
#         "jean": "valjean",
#         "grace": "hopper",
#         "xavier": "brindacier"
#     }
#     print(format_names(persons))