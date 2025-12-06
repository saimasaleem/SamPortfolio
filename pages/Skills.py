import streamlit as st

st.title("💡 Skills")

skill_groups = {
    "Programming": ["Python", "Java", "C", "C++", "SQL/PLSQL"],
    "AI/ML": ["Deep Learning", "Transformers", "Domain Adaptation", "NLP", "CNNs"],
    "Tools": ["Streamlit", "OpenCV", "Scikit-Learn", "TensorFlow", "PyTorch"],
    "Research": ["Scientific Writing", "Reviewing (Scientific Reports Journal)", "Model Evaluation"]
}

for category, skills in skill_groups.items():
    st.subheader(f"🔹 {category}")
    st.write(", ".join(skills))
