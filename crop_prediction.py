import streamlit as st
import pandas as pd

# Page settings
st.set_page_config(page_title="Web3 E-Learning Platform", layout="wide")

# Sidebar navigation
menu = st.sidebar.selectbox("Navigation", [
    "Home", 
    "Course Marketplace", 
    "Certifications", 
    "Progress Tracker", 
    "Governance", 
    "Payments", 
    "Contact Us"
])

# ---------------- Home Page ----------------
if menu == "Home":
    st.title("🎓 Welcome to the Web3 E-Learning Revolution")

    col1, col2 = st.columns(2)
    with col1:
        st.header("📚 Learn. 👛 Own. 🧾 Verify.")
        st.markdown("""
        - ✅ Wallet-Backed Identity (Web3Auth)  
        - 📦 Content stored permanently on IPFS  
        - 🧾 Verifiable NFT Certifications  
        - 🔒 Fully Censorship-Resistant  
        - 🌍 Community-Driven DAO Governance  
        """)
        st.metric("Active Learners", "5,000+")
        st.metric("Courses On-Chain", "120+")
    with col2:
        st.image("https://gateway.pinata.cloud/ipfs/QmWeb3ExampleImage", caption="Decentralized Learning Powered by Blockchain")

    st.divider()

    st.subheader("✨ Key Features")
    features = [
        "👛 Easy Wallet Signup (Google/Email > Web3 Wallet)",
        "📚 Courses Stored & Tracked On-Chain",
        "🧾 Certificates Minted as NFTs",
        "📦 Course Materials on IPFS (Decentralized Storage)",
        "📊 Progress Tracking On Blockchain",
        "💸 UPI + Crypto Payments",
        "🗳️ DAO-Based Governance",
        "🔐 Fully Transparent, Open-Source Smart Contracts"
    ]
    for feature in features:
        st.success(feature)

    st.divider()

    st.subheader("💬 Testimonials")
    testimonials = [
        "“Love owning my learning records forever!” — Ayaan, Mumbai",
        "“This is the future of education!” — Priya, Hyderabad",
        "“I minted my course certificate to show employers!” — Karan, Bangalore"
    ]
    selected_testimonial = st.selectbox("User Feedback", testimonials)
    st.info(selected_testimonial)

    st.divider()

    st.subheader("📈 Platform Growth")
    growth_data = pd.DataFrame({
        'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
        'Users': [200, 500, 1200, 2500, 5000]
    })
    st.line_chart(growth_data.set_index('Month'))

# ---------------- Course Marketplace ----------------
elif menu == "Course Marketplace":
    st.title("🎯 Explore On-Chain Courses")

    st.info("🚀 All course metadata is stored via Smart Contracts. Content is hosted on IPFS.")

    courses = [
        {"Title": "Blockchain Basics", "Instructor": "0x123...abc", "Fee (MATIC)": 10, "IPFS Link": "ipfs://QmABC"},
        {"Title": "Solidity Development", "Instructor": "0x456...def", "Fee (MATIC)": 15, "IPFS Link": "ipfs://QmDEF"},
        {"Title": "Decentralized Storage Systems", "Instructor": "0x789...ghi", "Fee (MATIC)": 12, "IPFS Link": "ipfs://QmGHI"}
    ]
    df_courses = pd.DataFrame(courses)
    st.table(df_courses)

    st.success("🔗 After enrollment, your progress will be tracked on-chain!")

# ---------------- Certifications ----------------
elif menu == "Certifications":
    st.title("🧾 Verify Your NFT Certificate")

    nft_id = st.text_input("Enter NFT ID or Wallet Address")
    if nft_id:
        st.success(f"✅ Certificate for {nft_id} found!")
        st.json({
            "Course": "Blockchain Basics",
            "Issued To": nft_id,
            "Date": "2025-04-25",
            "IPFS Metadata": "https://ipfs.io/ipfs/QmCertificateHashExample"
        })

    st.divider()
    st.info("All certificates are minted directly to your wallet — fully verifiable on public blockchains.")

# ---------------- Progress Tracker ----------------
elif menu == "Progress Tracker":
    st.title("📊 Your On-Chain Learning Progress")

    wallet_address = st.text_input("Enter your Wallet Address")
    if wallet_address:
        st.info(f"Tracking Progress for Wallet: {wallet_address}")

        progress_data = pd.DataFrame({
            'Course': ['Blockchain Basics', 'Solidity Dev', 'IPFS Essentials'],
            'Progress (%)': [100, 65, 40]
        })
        st.bar_chart(progress_data.set_index('Course'))

# ---------------- Governance ----------------
elif menu == "Governance":
    st.title("🗳️ DAO Governance Panel")

    st.info("🚀 Use your $LEARN tokens to participate in governance!")

    proposals = [
        {"Proposal": "Add 'Web3 Security' Course", "Status": "Voting Open"},
        {"Proposal": "Move to Layer 2 Blockchain", "Status": "Approved"},
        {"Proposal": "Sponsor Hackathon for Learners", "Status": "Voting Open"}
    ]
    proposals_df = pd.DataFrame(proposals)
    st.table(proposals_df)

    st.success("🎯 Shape the future of the platform with your votes!")

# ---------------- Payments ----------------
elif menu == "Payments":
    st.title("💸 Payments")

    st.write("""
    We support:
    - 🔹 Crypto (MATIC, USDT, ETH)
    - 🔹 Traditional (UPI, Bank Transfer)
