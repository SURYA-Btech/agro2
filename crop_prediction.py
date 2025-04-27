import pandas as pd
import streamlit as st
import time

# Page setup
st.set_page_config(page_title="Crop Price Prediction", layout="wide")

# Data
data = {
    'Rainfall (mm)': [200, 150, 300, 400, 250, 100, 500, 350, 275, 180],
    'Temperature (°C)': [25, 23, 30, 32, 28, 22, 35, 29, 27, 24],
    'Price': [1500, 1300, 1800, 2100, 1700, 1200, 2500, 2000, 1600, 1400]
}
df = pd.DataFrame(data)

# Simple manual prediction function
def predict_price(rainfall, temperature):
    avg_price = 1000 + (rainfall * 2.5) + (temperature * 8.5)
    return avg_price

# Home Page
st.title("🌾 Crop Price Prediction Platform")

st.header("Welcome to Smart Farming Solutions ")
col1, col2 = st.columns(2)
with col1:
    st.subheader("Empowering Farmers:")
    st.write("""
    - 📈 Predict crop selling prices easily  
    - 🌦️ Rainfall and temperature based prediction  
    - 🖥️ Fast, Secure & Easy-to-use
    """)
    st.metric(label="Happy Farmers", value="120+")
    st.metric(label="Supported Crops", value="50+")

st.divider()

st.subheader("Why Farmers Trust Us:")
features = [
    "⚡ Instant Price Predictions",
    "📊 Simple User Interface",
    "🔒 Safe and Private",
    "🌎 Works Across India",
    "🤖 AI-Ready Platform",
]
for feature in features:
    st.success(feature)

st.divider()

# Prediction Section
st.subheader(" Predict Your Crop Price")

with st.form(key="predict_form"):
    rainfall = st.number_input("Enter Rainfall (mm)", min_value=0, max_value=1000, value=300)
    temperature = st.number_input("Enter Temperature (°C)", min_value=0, max_value=50, value=25)
    submit_button = st.form_submit_button("Predict Price")
    if submit_button:
        price = predict_price(rainfall, temperature)
        st.success(f" Predicted Crop Price: ₹{price:.2f}")

st.divider()

# Testimonials Auto-Change
st.subheader("💬 What Our Farmers Say")

testimonials = [
    "“My profits increased by 30% thanks to this app! - Rajesh Kumar, Tamil Nadu”",
    "“Finally I know the right time to sell my crops! - Ayesha Patel, Gujarat”",
    "“Super easy to use and very helpful! - Sunil Verma, Punjab”",
]

testimonial_placeholder = st.empty()
i = 0
for _ in range(5):  # Loop 5 times to display auto-moving testimonials
    testimonial_placeholder.info(testimonials[i % len(testimonials)])
    time.sleep(3)
    i += 1

st.divider()

# Growth Chart
st.subheader("📈 Our Growth Journey")

growth_data = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'Users': [50, 100, 250, 400, 600, 900]
})
st.line_chart(growth_data.set_index('Month'))

st.divider()

# About and Contact
st.subheader(" About Us")
st.write("""
We are passionate about empowering Indian farmers using digital tools.
Our goal is to make crop pricing simple, predictable, and profitable for all.
""")

st.subheader("📬 Contact Us")
st.write("📧 Email: support@croppricepredict.com")
st.write("📞 Phone: +91 9876543210")
st.write("[🔗 Connect on LinkedIn](https://linkedin.com/company/crop-price-predict)")
