import streamlit as st

st.set_page_config(page_title="T-Mobile Bill Calculator", layout="centered")

st.title("📱 T-Mobile Group Bill Calculator (Replacement Of Varshan)")

# All months
months_list = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
               "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# Session state to store selected months permanently
if "saved_months" not in st.session_state:
    st.session_state.saved_months = []

# Month selection
selected_months = st.multiselect(
    "Select Months",
    months_list,
    default=st.session_state.saved_months
)

# Save previous selections
for month in selected_months:
    if month not in st.session_state.saved_months:
        st.session_state.saved_months.append(month)

# Keep order same as months_list
st.session_state.saved_months = [
    m for m in months_list if m in st.session_state.saved_months
]

# Final months
final_months = st.session_state.saved_months

# Auto-calculate months
months = len(final_months)

st.write(f"Number of Months: {months}")

month_names = "/".join(final_months)

st.write(f"Selected Months: {month_names}")

# Constants
total_bill = 265
members = 9
base_per_month = total_bill / members

# People
people = ["Varshan", "Mahesh Kanala", "Sujith", "Mahesh Dirisala", "Prasad"]

# Extra charges
extra_charges = {
    "Mahesh Dirisala": 4.16,
    "Prasad": 22.09
}

# Payment Tracker
st.subheader("💰 Payment Status")

for person in people:

    st.markdown(f"### {person}")

    cols = st.columns(len(final_months))

    for idx, month in enumerate(final_months):

        paid = cols[idx].checkbox(
            f"{month}",
            key=f"{person}_{month}"
        )

        if paid:
            cols[idx].success("PAID")
        else:
            cols[idx].error("NOT PAID")

    st.divider()

# Bill Summary
if months > 0:

    st.subheader("📄 Bill Summary")

    for person in people:

        base_total = base_per_month * months
        extra_total = extra_charges.get(person, 0) * months

        final_amount = round(base_total + extra_total, 2)

        st.text(f"{person} ----- {month_names} ----- {final_amount}")

else:
    st.warning("Please select at least one month")
