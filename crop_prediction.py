import pandas as pd
import streamlit as st
from itertools import cycle

# Page settings
st.set_page_config(page_title="Crop Price Prediction", layout="wide")

# Data
data = {
    'Rainfall (mm)': [200, 150, 300, 400, 250, 100, 500, 350, 275, 180],
    'Temperature (°C)': [25, 23, 30, 32, 28, 22, 35, 29, 27, 24],
    'Price': [1500, 1300, 1800, 2100, 1700, 1200, 2500, 2000, 1600, 1400]
}
df = pd.DataFrame(data)

# Price Prediction Function
def predict_price(rainfall, temperature):
    a = 2.5  # rainfall weight
    b = 30   # temperature weight
    c = 1000 # base price
    return a * rainfall + b * temperature + c

# Sidebar Menu
menu = st.sidebar.selectbox("Navigation", ["Home", "Predict Price", "About Us", "Contact Us"])

# ---------------- Home Page ----------------
if menu == "Home":
    st.title(" Welcome to Crop Price Prediction Platform")

    col1, col2 = st.columns(2)
    with col1:
        st.header("Empowering Farmers with ML 🌾")
        st.write("""
        - Accurate Crop Price Predictions  
        - Boost your profits with informed decisions  
        - 🌦 Analyze weather patterns, soil, and market trends
        """)
        st.metric(label="Happy Customers", value="120+")
        st.metric(label="Crops Supported", value="50+")

    st.divider()

    st.subheader("Why Choose Us?")
    features = [
        "⚡ Real-time Price Updates",
        "📈 Machine Learning Powered",
        "🌎 Works Across India",
        "📊 Upload your own Data",
        "🔒 Secure & Private",
        "🖥️ Easy-to-Use Interface"
    ]
    for feature in features:
        st.success(feature)

    st.divider()

    st.subheader("💬 What Our Customers Say")
    testimonials = [
        "“This app changed my farming business! - Rajesh Kumar, Tamil Nadu”",
        "“I can finally predict the best time to sell crops! - Ayesha Patel, Gujarat”",
        "“Very accurate predictions and simple to use. - Sunil Verma, Punjab”"
    ]
    selected_testimonial = st.selectbox("Testimonials", testimonials)
    st.info(selected_testimonial)

    st.divider()

    st.subheader("📈 Our Growth")
    growth_data = pd.DataFrame({
        'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
        'Users': [50, 100, 250, 400, 600, 900]
    })
    st.line_chart(growth_data.set_index('Month'))

# ---------------- Predict Price Page ----------------
elif menu == "Predict Price":
    st.title("Predict Your Crop Price")

    with st.form(key="predict_form"):
        rainfall = st.number_input("Enter Rainfall (mm)", min_value=0, max_value=1000, value=300)
        temperature = st.number_input("Enter Temperature (°C)", min_value=0, max_value=50, value=25)
        submit_button = st.form_submit_button("Predict Price")

        if submit_button:
            price_pred = predict_price(rainfall, temperature)
            st.success(f"Predicted Crop Price: ₹{price_pred:.2f}")

    st.divider()

    st.subheader("📊 Model Performance")
    predicted_prices = [
        predict_price(df['Rainfall (mm)'][i], df['Temperature (°C)'][i])
        for i in range(len(df))
    ]

    comparison_df = pd.DataFrame({
        'Actual Price': df['Price'],
        'Predicted Price': predicted_prices
    })

    st.line_chart(comparison_df)

# ---------------- About Us Page ----------------
elif menu == "About Us":
    st.title("👩‍💻 About Our Platform")
    st.write("""
    We are a team of passionate engineers dedicated to empowering Indian farmers.  
    Our platform predicts crop prices based on rainfall and temperature to maximize your profits.
    """)

    st.subheader("🚀 Mission")
    st.info("Farmers often face significant challenges due to unpredictable crop prices and limited diversification options. \nAgroVision addresses these issues by predicting crop prices at harvest and suggesting alternative crops to reduce risks.")

    st.subheader("🌍 Vision")
    st.info("With increasing digital adoption, there's an opportunity to provide affordable and accessible tools for price prediction. Our vision is to help small-scale farmers make informed decisions through data-driven solutions.")

    st.subheader("🛠️ Technologies We Use")
    techs = ["Python", "Pandas", "Streamlit"]
    st.write(techs)

# ---------------- Contact Us Page ----------------
elif menu == "Contact Us":
    st.title("📞 Contact Us")
    st.write("Feel free to connect with us!")

    with st.form(key="contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Your Message")
        submit_button = st.form_submit_button("Send Message")

        if submit_button:
            st.success(f"Thank you {name}! We have received your message and will contact you shortly.")

    st.divider()
    st.write("📧 Email: support@croppricepredict.com")
    st.write("📞 Phone: +91 9876543210")
    st.write("[🔗 LinkedIn](https://linkedin.com/company/crop-price-predict)")
