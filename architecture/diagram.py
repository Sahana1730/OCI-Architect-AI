def generate_diagram(services):

    diagram = []

    diagram.append("🌐 Internet")

    if "OCI Load Balancer" in services:
        diagram.append("      │")
        diagram.append("⚖ OCI Load Balancer")

    diagram.append("      │")
    diagram.append("💻 OCI Compute")

    if "Oracle Autonomous Database" in services:
        diagram.append("      │")
        diagram.append("🗄 Oracle Autonomous Database")

    if "OCI Object Storage" in services:
        diagram.append("      │")
        diagram.append("📦 OCI Object Storage")

    return "\n".join(diagram)