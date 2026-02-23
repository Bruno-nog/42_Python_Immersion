def list_of_names(persons: dict[str, str]) -> list[str]:
    """String capitalized"""
    full_names = []
    for first, last in persons.items():
        first_cap = first.capitalize()
        last_cap = last.capitalize()
        full_names.append(first_cap + ' ' + last_cap)
    return full_names

if __name__ == "__main__":
    persons = {
        "jean": "valjean",
        "grace": "hopper",
        "xavier": "niel",
        "fifi": "brindacier"
    }
    print(list_of_names(persons))
