import streamlit as st
from monday_api import get_board_items

st.title("Monday.com Business Intelligence Agent")

st.write("Ask business questions about deals or work orders.")

# Hardcoded board IDs
DEALS_BOARD_ID = "5027109133"
WORK_ORDERS_BOARD_ID = "5027109307"

question = st.text_input("Ask a business question")

if st.button("Run"):

    deals_df = get_board_items(DEALS_BOARD_ID)
    work_orders_df = get_board_items(WORK_ORDERS_BOARD_ID)

    if deals_df.empty and work_orders_df.empty:
        st.error("Could not fetch board data. Check API token.")
        st.stop()

    st.subheader("Deals Data")
    st.dataframe(deals_df)

    st.subheader("Work Orders Data")
    st.dataframe(work_orders_df)

    if question:

        st.subheader("Basic Insights")

        st.write("Total Deals:", len(deals_df))
        st.write("Total Work Orders:", len(work_orders_df))

        if "Deal Status" in deals_df.columns:
            st.write("Deal Status Distribution:")
            st.write(deals_df["Deal Status"].value_counts())