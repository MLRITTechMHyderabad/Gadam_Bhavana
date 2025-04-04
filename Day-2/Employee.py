employees = [
    {"name": "Alice", "salary": 50000, "rating": 5},
    {"name": "Bob", "salary": 40000, "rating": 3},
    {"name": "Charlie", "salary": 35000, "rating": 2}
]
# Using map and lambda to modify salaries based on ratings
x= list(map(lambda employee: {
    "name": employee["name"],
    "salary": (
        employee["salary"] * 1.10 
        if employee["rating"] in [4, 5] #10% increase for ratings 4 & 5
        else
        employee["salary"] * 1.05 
        if employee["rating"] == 3 # 5% increase for rating 3
        else
        employee["salary"] * 0.97 
        if employee["rating"] in [1, 2] #3% decrease for ratings 1 & 2
        else
        employee["salary"] #No change for other ratings 
    ),
    "rating": employee["rating"]
}, employees))

print(x)