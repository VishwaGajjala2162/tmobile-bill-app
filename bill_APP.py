import streamlit as st

st.set_page_config(page_title="T-Mobile Bill Calculator", layout="centered")

st.title("📱 T-Mobile Group Bill Calculator (Replacement Of Varshan)")

# Month dropdown FIRST
months_list = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
               "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

selected_months = st.multiselect(
    "Select Months",
    months_list,
    default=["Jan", "Feb"]
)

# Auto-calculate number of months
months = len(selected_months)

st.write(f"Number of Months: {months}")

# Convert months to format
month_names = "/".join(selected_months)

st.write(f"Selected Months: {month_names}")

# Constants
total_bill = 265
members = 9
base_per_month = total_bill / members

# People required
people = ["Varshan", "Mahesh Kanala", "Sujith", "Mahesh Dirisala", "Prasad"]

# Extra charges
extra_charges = {
    "Mahesh Dirisala": 4.16,
    "Prasad": 22.09
}

# Calculate only if at least 1 month selected
if months > 0:
    st.subheader("📄 Bill Summary")

    for person in people:
        base_total = base_per_month * months
        extra_total = extra_charges.get(person, 0) * months
        final_amount = round(base_total + extra_total, 2)

        st.text(f"{person} ----- {month_names} ----- {final_amount}")
else:
    st.warning("Please select at least one month")