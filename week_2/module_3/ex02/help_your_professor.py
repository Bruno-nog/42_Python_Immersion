

def average(grade: dict[str, int]) -> float:
    """add the values and divide by the quantity"""
    if not grade:
        return 0.0
    total = sum(grade.values())        
    return total / len(grade)

# if __name__ == "__main__":
#     class_3b = {
#         "marine": 18, 
#         "jean": 15, 
#         "coline": 8
#     }
#     print(average(class_3b))