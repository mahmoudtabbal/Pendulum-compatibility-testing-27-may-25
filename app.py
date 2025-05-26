
import streamlit as st
import hashlib
import pandas as pd
import io
import datetime
dob = st.date_input("Date of Birth", min_value=datetime.date(1900, 1, 1), max_value=datetime.date.today())
# Dowsing algorithm
def calculate_resonance(name, dob, intention, item):
    signature = f"{name}|{dob}|{intention}|{item}"
    hash_value = hashlib.sha256(signature.encode()).hexdigest()
    numeric_value = int(hash_value[:12], 16)
    scaled = (numeric_value % 200001) - 100000
    return scaled

def interpret_resonance(value):
    if value < -70000:
        return "D (Dangerous)"
    elif value < -51000:
        return "VH (Very Harmful)"
    elif value < -31000:
        return "MH (Moderately Harmful)"
    elif value < 0:
        return "mH (Mildly Harmful)"
    elif value <= 30000:
        return "OK"
    elif value <= 50000:
        return "G (Good)"
    elif value <= 70000:
        return "VG (Very Good)"
    else:
        return "N (Necessary)"

st.title("Energetic Compatibility Dowser")

name = st.text_input("Full Name")
dob = st.date_input("Date of Birth", min_value=datetime.date(1900, 1, 1), max_value=datetime.date.today(), key="dob_input")
intention = st.text_input("Intention (e.g., emotional balance, focus)")

item_input = st.text_input("Single Item to Test")
uploaded_file = st.file_uploader("Or upload a file with items (one item per line)", type=["txt", "csv"])

results = []

if st.button("Run Dowsing"):
    if not name or not intention:
        st.error("Please enter name and intention.")
    else:
        items = []
        if item_input:
            items.append(item_input.strip())
        if uploaded_file:
            items.extend([line.strip() for line in uploaded_file.read().decode("utf-8").splitlines() if line.strip()])

        for item in items:
            val = calculate_resonance(name, dob, intention, item)
            level = interpret_resonance(val)
            results.append({"Item": item, "Resonance Value": val, "Compatibility Level": level})

        df = pd.DataFrame(results)
        st.dataframe(df)

        # Export options
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button("Download as CSV", csv, "dowsing_results.csv")

        excel_buffer = io.BytesIO()
        with pd.ExcelWriter(excel_buffer, engine='xlsxwriter') as writer:
            df.to_excel(writer, index=False)
        st.download_button("Download as Excel", excel_buffer.getvalue(), "dowsing_results.xlsx")
