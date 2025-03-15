import streamlit as st

# Initialize inventory as a dictionary
if "inventory" not in st.session_state:
    st.session_state.inventory = {}

st.sidebar.title("📦 Inventory Management")

# Add new items
item_name = st.sidebar.text_input("Item Name")
item_quantity = st.sidebar.number_input("Quantity", min_value=1, step=1)
if st.sidebar.button("Add Item"):
    if item_name:
        st.session_state.inventory[item_name] = (
            st.session_state.inventory.get(item_name, 0) + item_quantity
        )
        st.sidebar.success(f"✅ Added {item_quantity} {item_name}(s) to inventory.")

# Display inventory in sidebar
st.sidebar.subheader("📋 Current Inventory")
for item, quantity in st.session_state.inventory.items():
    st.sidebar.write(f"📌 **{item}:** {quantity}")

# Sell items section
st.title("🎂 Welcome to Zee Bakery 📦")
st.subheader("🛒 Sell Items")
sell_item = st.selectbox("Select Item to Sell", list(st.session_state.inventory.keys()) if st.session_state.inventory else ["No items available"])
sell_quantity = st.number_input("Quantity to Sell", min_value=1, step=1)

if st.button("Sell Item"):
    if sell_item in st.session_state.inventory and st.session_state.inventory[sell_item] >= sell_quantity:
        st.session_state.inventory[sell_item] -= sell_quantity
        st.success(f"✅ Sold {sell_quantity} {sell_item}(s).")
        # Remove item if stock reaches zero
        if st.session_state.inventory[sell_item] == 0:
            del st.session_state.inventory[sell_item]
            st.warning(f"⚠️ {sell_item} is now out of stock!")
    else:
        st.error("❌ Not enough stock available!")


st.sidebar.markdown("---")

# Footer
st.sidebar.markdown("<p style='text-align: center; color: grey;'>Build with ❤️ By Ismail Ahmed Shah</p>", unsafe_allow_html=True)


# Add a 'Contact Us' section
st.sidebar.markdown("---")
st.sidebar.markdown("### 📬 Contact")

# Email Link
st.sidebar.write("📧 [Email Us](mailto:ismailahmedshahpk@gmail.com)")

# LinkedIn Link
st.sidebar.write("🔗 [Connect on LinkedIn](https://www.linkedin.com/in/ismail-ahmed-shah-2455b01ba/)")

# WhatsApp Link
st.sidebar.write("💬 [Chat on WhatsApp](https://wa.me/923322241405)")
