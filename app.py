import streamlit as st

from architecture.analyzer import analyze_project
from architecture.recommendation import recommend_services
from architecture.diagram import generate_diagram
from architecture.cost import estimate_cost
from ai.gemini import explain_architecture

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="OCI Architect",
    page_icon="☁️",
    layout="wide"
)

# ==========================================
# HEADER
# ==========================================

st.title("☁️ OCI Architect")

st.markdown("""
### Intelligent Oracle Cloud Architecture Planner

Describe your application and receive a recommended Oracle Cloud Infrastructure architecture.
""")

st.divider()

# ==========================================
# USER INPUT
# ==========================================

st.subheader("📝 Describe Your Application")

user_input = st.text_area(
    "Project Description",
    height=180,
    placeholder="""
Example:

I want an ecommerce website with
50000 users,
online payments,
image uploads,
and user login.
"""
)

generate = st.button("🚀 Generate Architecture")

st.divider()

# ==========================================
# MAIN
# ==========================================

if generate:

    if user_input.strip() == "":
        st.warning("Please enter your project description.")

    else:

        st.success("✅ Project analyzed successfully!")

        # ======================================
        # ANALYZE PROJECT
        # ======================================

        project = analyze_project(user_input)

        # ======================================
        # RECOMMEND SERVICES
        # ======================================

        services = recommend_services(project)

        # ======================================
        # COST ESTIMATION
        # ======================================

        costs, total_cost = estimate_cost(services)

        col1, col2 = st.columns(2)

        # ======================================
        # PROJECT ANALYSIS
        # ======================================

        with col1:

            st.subheader("📋 Project Analysis")

            st.markdown(f"""
### Application Type

**{project["app_type"]}**

---

### Traffic

**{project["traffic"]}**

---

### Database

{"✅ Enabled" if project["database"] else "❌ Disabled"}

---

### Storage

{"✅ Enabled" if project["storage"] else "❌ Disabled"}

---

### Authentication

{"✅ Enabled" if project["authentication"] else "❌ Disabled"}
""")

        # ======================================
        # OCI SERVICES
        # ======================================

        with col2:

            st.subheader("☁️ Recommended OCI Services")

            for service in services:

                st.markdown(
                    f"""
<div style="
background:#1f2937;
padding:18px;
border-radius:12px;
margin-bottom:12px;
border-left:6px solid #00C853;
box-shadow:0px 0px 10px rgba(0,0,0,0.3);
">

<h4 style="margin:0;color:white;">
☁️ {service}
</h4>

</div>
""",
                    unsafe_allow_html=True,
                )

        # ======================================
        # ARCHITECTURE
        # ======================================

        st.divider()

        st.subheader("🏗 Suggested Architecture")

        diagram = generate_diagram(services)

        st.code(diagram)

        # ======================================
        # COST ESTIMATION
        # ======================================

        st.divider()

        st.subheader("💰 Estimated Monthly OCI Cost")

        for item in costs:

            c1, c2 = st.columns([4, 1])

            with c1:
                st.write(item["service"])

            with c2:
                st.write(f"₹ {item['price']}")

        st.success(f"### 💵 Estimated Monthly Cost : ₹ {total_cost}")

        st.caption("⚠️ This is an estimated cost for demonstration purposes only.")

        # ======================================
        # INFORMATION
        # ======================================

        st.divider()

        st.info("""
This architecture recommendation is generated using the built-in Oracle Cloud recommendation engine.

The cost estimation shown above is an approximate value intended for educational purposes.
""")

        # ======================================
        # AI CLOUD ARCHITECT
        # ======================================

        st.divider()
        if st.button("✨ Explain Architecture with AI"):
            if "ai_response" not in st.session_state or st.session_state["ai_response"] == "":
                with st.spinner("Generating AI explanation..."):
                    st.session_state["ai_response"] = explain_architecture(
                        user_input,
                        st.session_state["services"]
            )

        st.markdown(st.session_state.get("ai_response", ""))