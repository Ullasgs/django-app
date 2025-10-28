def users_above_18(users):
    return [user['name'] for user in users if user['age'] > 18]

users = [
    {"name": "Aarav Sharma", "age": 22},
    {"name": "Vivaan Gupta", "age": 17},
    {"name": "Aditya Singh", "age": 19},
    {"name": "Ishaan Patel", "age": 16},
    {"name": "Ananya Mehta", "age": 21},
    {"name": "Diya Reddy", "age": 15},
    {"name": "Saanvi Kapoor", "age": 20},
    {"name": "Rohan Joshi", "age": 18},
    {"name": "Myra Iyer", "age": 23},
    {"name": "Kiara Nair", "age": 17}
]

print("All users:", users)
print("Users above 18:", users_above_18(users))
