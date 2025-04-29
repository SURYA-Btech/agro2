# --------------- Home Page ---------------
if menu == "Home":
    st.title("🏛️ Welcome to Web3Learn")

    col1, col2 = st.columns(2)
    with col1:
        st.header("Revolutionizing Learning with Blockchain 🌐")
        st.write("""
        - 🎓 Decentralized Ownership of Your Learning  
        - 📜 Verifiable NFT Certificates  
        - 💰 Direct Payments without Middlemen  
        - 🔒 Full Privacy and Security  
        - 🛠️ Govern the platform via DAO  
        """)
        st.metric(label="Active Learners", value="5,000+")
        st.metric(label="Verified Certificates", value="1,200+")

    with col2:
        # Loading the image from a local file
        st.image("C:/Users/surya/ren/some_image.jpg", caption="Learning on Blockchain", use_container_width=True)

    st.divider()

    st.subheader("🚀 Why Web3Learn?")
    benefits = [
        "🪙 Wallet-based Identity (No usernames/passwords)",
        "📦 Courses Stored on IPFS",
        "🛡️ Immutable Certificates",
        "📈 Transparent Learning Records",
        "🌍 Global Access 24/7",
        "🧑‍🤝‍🧑 DAO-based Platform Governance"
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
