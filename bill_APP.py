import streamlit as st

st.set_page_config(page_title="T-Mobile Bill Calculator", layout="centered")

st.title("📱 T-Mobile Group Bill Calculator (Replacement Of Varshan)")

# Month List
months_list = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
]

# Select Months
selected_months = st.multiselect(
    "Select Months",
    months_list,
    default=[]
)

# Only continue if months selected
if len(selected_months) > 0:

    # Number of Months
    months = len(selected_months)

    st.write(f"## Number of Months: {months}")

    # Selected Month Display
    month_names = "/".join(selected_months)

    st.write(f"## Selected Months: {month_names}")

    # Constants
    total_bill = 265
    members = 9
    base_per_month = total_bill / members

    # People
    people = [
        "Varshan",
        "Mahesh Kanala",
        "Sujith",
        "Mahesh Dirisala",
        "Prasad"
    ]

    # Extra Charges
    extra_charges = {
        "Mahesh Dirisala": 4.16,
        "Prasad": 22.09
    }

    # Payment Status Section
    st.subheader("💰 Payment Status")

    # Store unpaid months count
    unpaid_months_count = {}

    for person in people:

        # Initial Amount
        pending_months = months

        base_total = base_per_month * pending_months
        extra_total = extra_charges.get(person, 0) * pending_months

        final_amount = round(base_total + extra_total, 2)

        # Name + Amount
        st.markdown(
            f"<h4 style='margin-bottom:5px;'>{person} - $ {final_amount}</h4>",
            unsafe_allow_html=True
        )

        cols = st.columns(len(selected_months))

        unpaid_count = 0

        for idx, month in enumerate(selected_months):

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

        # Pending Amount
        base_total = base_per_month * unpaid_count
        extra_total = extra_charges.get(person, 0) * unpaid_count

        pending_amount = round(base_total + extra_total, 2)

        st.markdown(
            f"##### Pending Amount: $ {pending_amount}"
        )

        st.divider()

    # Pending Summary
    st.subheader("📄 Pending Bill Summary")

    for person in people:

        unpaid_months = unpaid_months_count[person]

        base_total = base_per_month * unpaid_months
        extra_total = extra_charges.get(person, 0) * unpaid_months

        final_amount = round(base_total + extra_total, 2)

        pending_month_names = []

        for month in selected_months:

            paid = st.session_state.get(f"{person}_{month}", False)

            if not paid:
                pending_month_names.append(month)

        pending_months_display = "/".join(pending_month_names)

        st.text(
            f"{person} ----- {pending_months_display} ----- Due Amount: $ {final_amount}"
        )

else:
    st.info("Please select month(s) to calculate the bill.")
