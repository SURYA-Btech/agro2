import pandas as pd
import streamlit as st
from itertools import cycle

# Page settings
st.set_page_config(page_title="LearnChain - Decentralized Course Platform", layout="wide")

# Sample course data
course_data = pd.DataFrame({
    "Course Name": ["Intro to Blockchain", "Smart Contracts 101", "IPFS & Filecoin Basics", "DAO Governance"],
    "Instructor": ["Alice", "Bob", "Charlie", "Diana"],
    "Fee (MATIC)": [50, 75, 60, 90],
    "IPFS Link": ["ipfs://abc", "ipfs://def", "ipfs://ghi", "ipfs://jkl"]
})

# Sample user progress data
user_progress = pd.DataFrame({
    "Course": ["Intro to Blockchain", "Smart Contracts 101"],
    "Progress (%)": [100, 45]
})

# Sidebar Menu
menu = st.sidebar.selectbox("Navigation", ["Home", "Courses", "Certifications", "Progress", "Payments", "About Us", "Contact Us"])

# --------------- Home Page ---------------
if menu == "Home":
    st.title("🏛️ Welcome to LearnChain")

    col1, col2 = st.columns(2)
    with col1:
        st.header("Revolutionizing Learning with Blockchain 🌐")
        st.write("""
        -  Decentralized Ownership of Your Learning  
        -  Verifiable NFT Certificates  
        -  Direct Payments without Middlemen  
        -  Full Privacy and Security  
        - 🛠 Govern the platform via DAO  
        """)
        st.metric(label="Active Learners", value="5,000+")
        st.metric(label="Verified Certificates", value="1,200+")

    # Updated local image display
with col2:
    st.image("C:/Users/surya/ren/some_image.jpg", caption="Learning on Blockchain", use_container_width=True)

    st.divider()

    st.subheader("🚀 Why learnchain?")
    benefits = [
        " Wallet-based Identity (No usernames/passwords)",
        " Courses Stored on IPFS",
        "🛡 Immutable Certificates",
        " Transparent Learning Records",
        " Global Access 24/7",
        " DAO-based Platform Governance"
    ]
    for benefit in benefits:
        st.success(benefit)

    st.divider()

    st.subheader("📢 Learner Testimonials")
    testimonials = [
        "“Finally, a platform where my certificates are truly mine!” - Neha, India",
        "“Seamless learning experience with full transparency.” - Marcus, USA",
        "“DAO governance gave me a voice in shaping courses!” - Amina, Kenya"
    ]
    selected = st.selectbox("What our learners say", testimonials)
    st.info(selected)

    st.divider()

    st.subheader("📊 Our Growth Journey")
    growth_data = pd.DataFrame({
        "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        "Users": [500, 800, 1500, 3000, 4000, 5000]
    })
    st.line_chart(growth_data.set_index("Month"))

# --------------- Courses Page ---------------
elif menu == "Courses":
    st.title("📚 Explore Courses")

    st.dataframe(course_data)

    st.divider()

    st.subheader("📝 Enroll Now")
    course_choice = st.selectbox("Select Course", course_data["Course Name"])
    enroll = st.button("Enroll")

    if enroll:
        st.success(f"You have enrolled in {course_choice}! Complete the course to earn your NFT certificate.")

# --------------- Certifications Page ---------------
elif menu == "Certifications":
    st.title("🎓 Your Certifications")

    sample_certificates = [
        {"Course": "Intro to Blockchain", "Certificate Link": "https://polygonscan.com/token/0x..."},
        {"Course": "Smart Contracts 101", "Certificate Link": "https://polygonscan.com/token/0x..."}
    ]

    for cert in sample_certificates:
        st.write(f" {cert['Course']}: [View Certificate]({cert['Certificate Link']})")

    st.divider()
    st.info("All certificates are minted as NFTs on the Polygon blockchain. Publicly verifiable!")

# --------------- Progress Page ---------------
elif menu == "Progress":
    st.title("📈 Your Learning Progress")

    st.dataframe(user_progress)

    st.divider()

    st.subheader("🔎 Track by Wallet")
    wallet_address = st.text_input("Enter Your Wallet Address")
    if wallet_address:
        st.success(f"Progress data for wallet {wallet_address} fetched (simulation).")

# --------------- Payments Page ---------------
elif menu == "Payments":
    st.title("💸 Payments")

    st.write("""
    We support:
    - 🔹 Crypto (MATIC, USDT, ETH)
    - 🔹 Traditional (UPI, Bank Transfer)

    All payment records are stored on-chain for transparency.
    """)

    method = st.selectbox("Choose Payment Method", ["Crypto Wallet", "UPI", "Bank Transfer"])
    if method == "Crypto Wallet":
        st.success("Connect Wallet: Coming Soon (MetaMask, WalletConnect)")
    elif method == "UPI":
        st.write("Pay to UPI ID: `web3learn@upi`")
    else:
        st.write("Bank Transfer Details:\n\nAccount Name: Web3Learn\nIFSC: ABCD0123456\nAccount No: 9876543210")

    st.divider()
    st.info("After payment, access will be unlocked automatically via your wallet.")

# --------------- About Us Page ---------------
elif menu == "About Us":
    st.title("👨‍💻 About Web3Learn")

    st.write("""
    Web3Learn is a fully decentralized e-learning platform powered by blockchain.  
    We eliminate central control and give power back to learners.
    """)
    st.subheader("🌟 Our Vision")
    st.info("Enable true ownership of learning credentials, accessible globally.")

    st.subheader("🔧 Technologies Used")
    tech_stack = ["Python", "Streamlit", "Blockchain (Polygon)", "IPFS", "Web3Auth", "NFTs", "DAO Frameworks"]
    for tech in tech_stack:
        st.success(tech)

    st.divider()
    st.subheader("🌎 Join the Revolution!")
    st.write("[Visit our GitHub](https://github.com/web3learn)")

# --------------- Contact Us Page ---------------
elif menu == "Contact Us":
    st.title("📬 Contact Us")

    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submit = st.form_submit_button("Send")

        if submit:
            st.success(f"Thank you {name}! We'll get back to you shortly.")

    st.divider()
    st.write("📧 Email: support@web3learn.com")
    st.write("🌐 Website: [https://web3learn.com](https://web3learn.com)")
    st.write("🔗 LinkedIn: [Web3Learn LinkedIn](https://linkedin.com/company/web3learn)")
