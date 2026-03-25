def get_user(users, user_id):
    return users.get(user_id)

def update_user(users, user_id, data):
    if user_id not in users:
        return None
    if "name" in data:
        users[user_id]["name"] = data["name"]
    if "email" in data:
        users[user_id]["email"] = data["email"]
    return users[user_id]
