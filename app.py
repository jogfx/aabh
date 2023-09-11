import streamlit as st
import pandas as pd

# Define the URL of the Excel file in your GitHub repository
excel_url = "https://raw.githubusercontent.com/jogfx/aabh/main/Keyholders.csv"

# Load the Keyholders data
keyholders = pd.read_csv(excel_url, delimiter=';')

# links to Google Sheets
google_sheets_links = {
    "Middle building": "https://docs.google.com/spreadsheets/d/1Llcx4LW4mlAATx_uxBA3_ivGVlCLjdapP3P7rH0Y-H0/edit?usp=drive_link",
    "Cinema": "https://docs.google.com/spreadsheets/d/1ep7mylEB4FPKObVmXkCKXCS_BhZDdmc4j0S2GRoJdVo/edit?usp=drive_link",
    "Guest room": "https://docs.google.com/spreadsheets/d/1f0RcWtknJrpKKrE9OwLu95ggZukoRqtb6i6xy63oRZ4/edit?usp=drive_link"
}

# "Good to Know"
pdfs = {
    "A-Å Aalborghus Kollegiet (Dansk Version)": "https://docs.google.com/document/d/1nxmiXR1CwYFi2reFHk68avTHuwxWbAy1ipOgHYMYGvE/edit?usp=sharing",
    "A-Z Aalborghus Kollegiet (English Version)": "https://docs.google.com/document/d/11C5IFSq0dk6z219QEq_qq_pmCVNA22gYkmetussYTH8/edit?usp=sharing",
}

# Useful Links
useful_links = {
    "Aalborghus Kollegiet facebook group": "https://www.facebook.com/groups/8666890873",
}

# Streamlit App
st.title("Dashboard")

# Section 1: Keyholders
st.header("Keyholders")

# Get unique types of keys
unique_key_types = keyholders["Key"].unique()

# Iterate over each unique type of key and create an expander block
for key_type in unique_key_types:
    with st.expander(f"{key_type} Keyholders"):
        # Filter keyholders by the current key type
        keyholders_filtered = keyholders[keyholders["Key"] == key_type]
        
        # Display a list of people with clickable Facebook links and Room
        for index, row in keyholders_filtered.iterrows():
            st.write(f"{row['Name']} - [Facebook]({row['Facebook']}) | Room: {row['Room']}", unsafe_allow_html=True)

# Section 2: Links to Google Sheets
st.header("Links to booking calendars")

# Display all Google Sheets links as clickable hyperlinks
for sheet_name, sheet_link in google_sheets_links.items():
    st.markdown(f"[{sheet_name}]({sheet_link})", unsafe_allow_html=True)

# Section 3: Good to Know (PDFs)
st.header("Useful documents")

# Display all PDF links as clickable hyperlinks
for pdf_label, pdf_link in pdfs.items():
    st.markdown(f"[{pdf_label}]({pdf_link})", unsafe_allow_html=True)

# Display the "Useful Links" section with predefined links
st.header("Useful Links")

# Create 3 columns for displaying links
columns = st.columns(3)

# Display predefined links
for link_label, link_url in useful_links.items():
    columns[0].write(link_label)
    columns[1].write(":")
    columns[2].markdown(f"[{link_url}]({link_url})", unsafe_allow_html=True)
