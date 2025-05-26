
# Energetic Compatibility Dowser

This Streamlit app simulates energetic compatibility testing based on intuitive pendulum dowsing. It evaluates the resonance of items (food, substances, environments, etc.) based on the user's name, date of birth, and a specific intention.

## Features
- Input a single item or upload a list of items
- Calculates compatibility using a deterministic algorithm
- Outputs resonance value and compatibility level
- Download results as CSV or Excel
- Ready for deployment on Streamlit Cloud

## How to Use
1. Fill in your name, date of birth, and intention.
2. Enter an item to test, or upload a file with a list.
3. Click "Run Dowsing" to view results.
4. Download the results if needed.

## Deployment
To deploy on Streamlit Cloud:
1. Fork or clone this repo to your GitHub account.
2. Visit [Streamlit Cloud](https://streamlit.io/cloud) and sign in.
3. Click “New app”, select this repo, choose `main` branch and `app.py` file.
4. Deploy and share the generated link.

## Requirements
- streamlit
- pandas
- xlsxwriter
