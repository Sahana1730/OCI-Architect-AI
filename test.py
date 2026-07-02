from ai.requirement_analyzer import analyze_requirements

data = analyze_requirements("""
Build an ecommerce application.

50000 users.

Payments.

Login.

Image uploads.

Order tracking.
""")

print(data)