import streamlit as st
import json
from pathlib import Path

st.set_page_config(page_title="The Survey Forge", layout="wide")
st.title("📐 The Survey Forge")

# Load survey types
survey_template_dir = Path("data/survey_templates")
survey_types = [f.stem for f in survey_template_dir.glob("*.json")]

with st.form("create_project"):
    st.subheader("Create New Project")
    client_name = st.text_input("Client Name")
    client_email = st.text_input("Client Email")
    client_phone = st.text_input("Client Phone")
    client_address = st.text_input("Client Address")
    survey_address = st.text_input("Survey Property Address")
    survey_type = st.selectbox("Type of Survey", survey_types)
    pm_assigned = st.text_input("Project Manager Assigned")
    status = st.selectbox("Status", ["Draft", "Scheduled", "Field Complete", "Delivered"])

    submitted = st.form_submit_button("Create Project")
    if submitted:
        project_data = {
            "client_name": client_name,
            "client_email": client_email,
            "client_phone": client_phone,
            "client_address": client_address,
            "survey_address": survey_address,
            "survey_type": survey_type,
            "pm_assigned": pm_assigned,
            "status": status
        }
        projects_file = Path("data/projects.json")
        if projects_file.exists():
            projects = json.loads(projects_file.read_text())
        else:
            projects = []
        projects.append(project_data)
        projects_file.write_text(json.dumps(projects, indent=2))
        st.success("Project created successfully!")
