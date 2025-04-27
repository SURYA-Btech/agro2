import time
import pandas as pd
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Page settings
st.set_page_config(page_title="Crop Price Prediction", layout="wide")

# Data directly inside
data = {
    'Rainfall (mm)': [200, 150, 300, 400, 250, 100, 500, 350, 275, 180],
    'Temperature (°C)': [25, 23, 30, 32, 28, 22, 35, 29, 27, 24],
    'Price': [1500, 1300, 1800, 2100, 1700, 1200, 2500, 2000, 1600, 1400]
}
df = pd.DataFrame(data)

# ML Model
X = df[['Rainfall (mm)', 'Temperature (°C)']]
y = df['Price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
predicted = model.predict(X_test)

# Sidebar Navigation
menu = st.sidebar.selectbox("Navigation", ["Home", "Predict Price", "About Us", "Contact Us"])

# Home Page
if menu == "Home":
    st.title("🏡 Welcome to Crop Price Prediction Platform")

    col1, col2 = st.columns(2)
    with col1:
        st.header("Empowering Farmers with ML 🌾")
        st.write("""
        - ✅ Accurate Crop Price Predictions  
        - 🚀 Boost your profits with informed decisions  
        - 🌦️ Analyze weather patterns, soil, and market trends
        """)
        st.metric(label=" Happy Customers", value="120+")
        st.metric(label="🌱 Crops Supported", value="50+")
    
    st.divider()

    st.subheader("🔥 Why Choose Us?")
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
    
    # Display moving testimonials
    testimonial_placeholder = st.empty()  # Create a placeholder to update the testimonial
    i = 0
    while True:
        testimonial_placeholder.info(testimonials[i])  # Show the current testimonial
        i = (i + 1) % len(testimonials)  # Move to the next testimonial
        time.sleep(3)  # Wait for 3 seconds before moving to the next testimonial

    st.divider()

    st.subheader("📈 Our Growth")
    growth_data = pd.DataFrame({
        'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
        'Users': [50, 100, 250, 400, 600, 900]
    })
    st.line_chart(growth_data.set_index('Month'))

# Prediction Page
elif menu == "Predict Price":
    st.title("🌾 Predict Your Crop Price")

    # User input system for rainfall and temperature
    with st.form(key="predict_form"):
        rainfall = st.number_input("Enter Rainfall (mm)", min_value=0, max_value=1000, value=300)
        temperature = st.number_input("Enter Temperature (°C)", min_value=0, max_value=50, value=25)

        submit_button = st.form_submit_button("Predict Price")
        if submit_button:
            user_data = pd.DataFrame({'Rainfall (mm)': [rainfall], 'Temperature (°C)': [temperature]})
            price_pred = model.predict(user_data)
            st.success(f"Predicted Crop Price: ₹{price_pred[0]:.2f}")

    st.divider()

    st.subheader("📊 See Model Performance")
    mse = mean_squared_error(y_test, predicted)
    st.write(f"Mean Squared Error (MSE): {mse:.2f}")

    st.subheader("📈 Actual vs Predicted Prices")
    comparison_df = pd.DataFrame({'Actual Price': y_test, 'Predicted Price': predicted})
    st.line_chart(comparison_df)

# About Us Page
elif menu == "About Us":
    st.title("👩‍💻 About Our Platform")
    st.write("""
    We are a team of passionate engineers dedicated to empowering Indian farmers.  
    Our AI-powered platform predicts crop prices based on rainfall and temperature to maximize your profits.
    """)

    st.subheader("🚀 Mission")
    st.info("Farmers often face significant challenges due to unpredictable crop prices and limited diversification options. \n AgroVision addresses these issues by predicting crop prices at harvest and suggesting alternative crops to reduce risks. Using advanced algorithms, the app provides farmers with simple, actionable insights to safeguard their income and improve their livelihoods. Additionally, it supports government buffer stock decisions by offering accurate supply and demand predictions, ensuring a stable and profitable farming experience.")

    st.subheader("🌍 Vision")
    st.info("The agriculture sector serves millions of small-scale farmers globally. With increasing digital adoption, there is a significant opportunity to provide affordable and accessible tools for price prediction and crop diversification.\n  Advancements in AI and data analytics enable scalable solutions for both farmers and governments to improve decision-making and resource management.")

    st.subheader(" Technologies We Use")
    techs = ["Python", "Scikit-learn", "Pandas", "Plotly"]
    st.write(techs)

# Contact Us Page
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
