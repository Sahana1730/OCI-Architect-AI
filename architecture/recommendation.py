def recommend_services(project):

    services = []

    # Compute
    services.append("OCI Compute")

    # Database
    if project["database"]:
        services.append("Oracle Autonomous Database")

    # Storage
    if project["storage"]:
        services.append("OCI Object Storage")

    # Authentication
    if project["authentication"]:
        services.append("OCI Identity & Access Management (IAM)")

    # High Traffic
    if project["traffic"] == "High":
        services.append("OCI Load Balancer")

    # Networking
    services.append("Virtual Cloud Network (VCN)")

    return services