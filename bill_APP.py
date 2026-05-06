import streamlit as st

st.set_page_config(page_title="T-Mobile Bill Calculator", layout="centered")

st.title("📱 T-Mobile Group Bill Calculator (Replacement Of Varshan)")

# Month List
months_list = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
               "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# Session state for saved months
if "saved_months" not in st.session_state:
    st.session_state.saved_months = ["Jan"]

# Month Selection
selected_months = st.multiselect(
    "Select Months",
    months_list,
    default=st.session_state.saved_months
)

# Ensure at least one month always selected
if len(selected_months) == 0:
    selected_months = ["Jan"]

# Save previous months
for month in selected_months:
    if month not in st.session_state.saved_months:
        st.session_state.saved_months.append(month)

# Maintain order
st.session_state.saved_months = [
    m for m in months_list if m in st.session_state.saved_months
]

final_months = st.session_state.saved_months

# Number of months
months = len(final_months)

st.write(f"### Number of Months: {months}")

month_names = "/".join(final_months)

st.write(f"### Selected Months: {month_names}")

# Constants
total_bill = 265
members = 9
base_per_month = total_bill / members

# People
people = ["Varshan", "Mahesh Kanala", "Sujith", "Mahesh Dirisala", "Prasad"]

# Extra Charges
extra_charges = {
    "Mahesh Dirisala": 4.16,
    "Prasad": 22.09
}

# Payment Status
st.subheader("💰 Payment Status")

# Store unpaid months count
unpaid_months_count = {}

for person in people:

    st.markdown(f"## {person}")

    cols = st.columns(len(final_months))

    unpaid_count = 0

    for idx, month in enumerate(final_months):

        paid = cols[idx].checkbox(
            f"{month}",
            key=f"{person}_{month}"
        )

        if paid:
            cols[idx].success("PAID")
        else:
            cols[idx].error("NOT PAID")
            unpaid_count += 1

    unpaid_months_count[person] = unpaid_count

    st.divider()

# Bill Summary
st.subheader("📄 Pending Bill Summary")

for person in people:

    unpaid_months = unpaid_months_count[person]

    base_total = base_per_month * unpaid_months

    extra_total = extra_charges.get(person, 0) * unpaid_months

    final_amount = round(base_total + extra_total, 2)

    st.text(
        f"{person} ----- Pending Months: {unpaid_months} ----- Due Amount: ${final_amount}"
    )
