def analyze_project(user_input):

    user_input = user_input.lower()

    project = {
        "app_type": "General",
        "traffic": "Low",
        "database": False,
        "storage": False,
        "authentication": False
    }

    # ---------- Application Type ----------

    if "netflix" in user_input or "video" in user_input:
        project["app_type"] = "Streaming"

    elif "ecommerce" in user_input or "shopping" in user_input:
        project["app_type"] = "E-Commerce"

    elif "chat" in user_input:
        project["app_type"] = "Chat"

    # ---------- Database ----------

    if "user" in user_input or "login" in user_input:
        project["database"] = True

    # ---------- Storage ----------

    if "image" in user_input or "video" in user_input:
        project["storage"] = True

    # ---------- Authentication ----------

    if "login" in user_input or "signup" in user_input:
        project["authentication"] = True

    # ---------- Traffic ----------

    if "10000" in user_input or "50000" in user_input:
        project["traffic"] = "High"

    return project