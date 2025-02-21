# import streamlit as st

# def accounts():
#     st.header("🏦 Accounts")
#     col1, col2 = st.columns (2)
#     selected_account = None
#     with col1:
#         if st.button('💵 Cash', key = 'cash_btn'):
#             selected_account = ('💵 Cash')
#         if st.button('💳 Card', key = 'card_btn'):
#             selected_account = ('💳 Card')

#     with col2:
#         if st.button('💸 Paypal', key = 'paypal_btn'):
#             selected_account = ('💸 Paypal')
#         if st.button('🏦 Bank Account', key = 'bank_acc_btn'):
#             selected_account = ('🏦 Bank Account')
    
#     return selected_account