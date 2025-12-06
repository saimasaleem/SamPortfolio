import streamlit as st

st.title("🧩 Projects & Frameworks")

st.header("1. ADA-DR: Adversarial Domain Adaptation for Disaster Response")
st.write("""
A robust ADA framework using **Vision Transformers** to handle the *cold-start problem* 
in new disaster events. Achieved **4% improvement in F1 score** over DDA models.
""")

st.header("2. DeLTran15: Lightweight Transformer for Humanitarian Classification")
st.write("""
Built using the OSEMN methodology, this system fine-tunes lightweight transformer models 
and applies **post-training quantization** to enable real-time disaster response.
""")

st.header("3. BERTopic + Self-training Domain Adaptation")
st.write("""
A unified approach that performs **topic modelling** and **domain adaptation** 
for new disaster events, addressing both textual and image-based shifts.
""")

st.header("4. Vision Transformer + Adversarial DA")
st.write("""
Applied ViT with adversarial adaptation for **disaster imagery**, particularly 
cross-domain transfer between typhoons, hurricanes, and earthquakes.
""")

st.header("5. ForgeDisaster Dataset")
st.write("""
A unique dataset for **image forgery detection**, enabling early identification 
of manipulated disaster images.
""")
