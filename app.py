import streamlit as st
import google.generativeai as genai

# Page config
st.set_page_config(page_title="Women's Care Package Vault", page_icon="🛡️", layout="wide")

# Custom CSS
st.markdown("""
<style>
body { background-color: #000000; color: #ffffff; }
.main { background-color: #000000; }
.stButton > button { 
    background-color: #fbbf24 !important;
    color: #000000 !important;
    font-weight: bold;
    border-radius: 8px;
    width: 100%;
    padding: 15px !important;
}
h1, h2, h3 { color: #fbbf24; }
</style>
""", unsafe_allow_html=True)

# Configure Google AI
api_key = st.secrets.get("GOOGLE_API_KEY")
if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')
else:
    st.error("⚠️ Google API Key not found. Please add GOOGLE_API_KEY to Streamlit Secrets.")

# Resources Data
RESOURCES = {
    "YWCA Baton Rouge": {
        "phone": "(225) 336-5869",
        "description": "Emergency shelter, counseling, legal advocacy, support groups",
        "url": "https://www.ywcabr.org"
    },
    "National Serenity House Care Group": {
        "phone": "225-521-7611",
        "hotline": "1-877-319-1133",
        "description": "Emergency shelter, relocation services, safety planning",
        "founder": "Quinta D. Smith",
        "url": "https://thenationalserenityhousecaregrp.org"
    },
    "One Breath Project": {
        "phone": "(225) 555-0123",
        "description": "Yoga, art therapy, painting, chat support, community connections",
    },
    "Church of the King": {
        "phone": "(225) 555-0456",
        "description": "Furniture assistance, emergency aid, community support",
    },
    "Mending the Soul RMBS": {
        "url": "https://www.mendingthesoulrmbs.com/healing-services",
        "description": "PTSD, Sexual Assault Therapy, Anxiety, Coping Skills, Family Support",
    },
    "Dr. Sandy Reed (OLOL)": {
        "phone": "(225) 555-1111",
        "description": "Child Pediatrician - OLOL Network",
    },
    "University of Phoenix": {
        "phone": "1-866-766-0766",
        "description": "Online education, flexible schedules, career advancement",
        "url": "https://www.phoenix.edu"
    }
}

# Header
st.markdown("""
<div style='text-align: center; padding: 20px; background: linear-gradient(to right, #581c87, #6b21a8); border-bottom: 4px solid #fbbf24;'>
    <h1 style='color: #fbbf24; margin: 0;'>Women's Care Package Vault</h1>
    <p style='color: #d1d5db;'>Your journey to safety, healing, and hope</p>
</div>
""", unsafe_allow_html=True)

# Initialize session state
if "current_step" not in st.session_state:
    st.session_state.current_step = 0
if "completed_steps" not in st.session_state:
    st.session_state.completed_steps = []

# Define steps
STEPS = [
    {
        "title": "Step 1: Acknowledge You Need Help",
        "description": "Taking this first step shows strength and courage. God sees your bravery.",
        "scripture": '"Come to me, all you who are weary and burdened, and I will give you rest." - Matthew 11:28',
        "action": "I Am Ready to Ask for Help",
        "resources": []
    },
    {
        "title": "Step 2: Scan Important Documents",
        "description": "Keep your ID, birth certificate, and legal documents safe and organized.",
        "scripture": '"The Lord is your protector." - Psalm 121:5',
        "action": "Documents Secured",
        "resources": []
    },
    {
        "title": "Step 3: Emergency Shelter & Safety",
        "description": "Reach out to emergency shelter services. They are ready to help.",
        "scripture": '"He will cover you with his feathers." - Psalm 91:4',
        "action": "Contacted Shelter",
        "resources": ["YWCA Baton Rouge", "National Serenity House Care Group"]
    },
    {
        "title": "Step 4: Mental Health Support",
        "description": "Connect with a therapist who specializes in trauma and healing.",
        "scripture": '"He heals the brokenhearted." - Psalm 147:3',
        "action": "Scheduled Therapy",
        "resources": ["Mending the Soul RMBS"]
    },
    {
        "title": "Step 5: Basic Needs & Wellness",
        "description": "Access to hygiene, clothing, and community support.",
        "scripture": '"God will provide for all your needs." - Philippians 4:19',
        "action": "Accessed Resources",
        "resources": ["One Breath Project", "Church of the King"]
    },
    {
        "title": "Step 6: Childcare & Health",
        "description": "Pediatric care and support for your children.",
        "scripture": '"Let the little children come to me." - Matthew 19:14',
        "action": "Scheduled Pediatrician",
        "resources": ["Dr. Sandy Reed (OLOL)"]
    },
    {
        "title": "Step 7: Housing & Stability",
        "description": "Work towards long-term housing and independence.",
        "scripture": '"Unless the Lord builds the house..." - Psalm 127:1',
        "action": "Applied for Housing",
        "resources": ["National Serenity House Care Group"]
    },
    {
        "title": "Step 8: Education & Future",
        "description": "Invest in your future through education and career growth.",
        "scripture": '"I have plans for you... plans for hope." - Jeremiah 29:11',
        "action": "Enrolled in School",
        "resources": ["University of Phoenix"]
    }
]

# Main app flow
def display_step(step_idx):
    step = STEPS[step_idx]
    
    st.markdown(f"### {step['title']}")
    st.write(step['description'])
    st.info(step['scripture'])
    
    # Progress
    progress = (step_idx + 1) / len(STEPS)
    st.progress(progress)
    st.caption(f"Step {step_idx + 1} of {len(STEPS)}")
    
    st.markdown("---")
    
    # Show resources for this step
    if step['resources']:
        st.markdown("#### Resources for This Step:")
        for resource_name in step['resources']:
            resource = RESOURCES[resource_name]
            st.markdown(f"**{resource_name}**")
            st.write(resource['description'])
            
            if 'phone' in resource:
                st.write(f"📞 {resource['phone']}")
            if 'hotline' in resource:
                st.write(f"🚨 Hotline: {resource['hotline']}")
            if 'url' in resource:
                st.write(f"[Visit Website]({resource['url']})")
            if 'founder' in resource:
                st.write(f"*Founded by: {resource['founder']}*")
            
            st.write("")
    
    # AI Guidance
    with st.expander("💬 Get AI Guidance"):
        if st.button("Ask for Spiritual Guidance", key=f"guidance_{step_idx}"):
            with st.spinner("Thinking..."):
                try:
                    prompt = f"A woman is on: {step['title']}. Provide brief spiritual encouragement under 100 words based on Scripture and this step. Be compassionate and faith-based."
                    
                    response = model.generate_content(prompt)
                    st.write(response.text)
                except Exception as e:
                    st.warning(f"Unable to connect to AI. Please check your API key.")
    
    st.markdown("---")
    
    # Action buttons
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button(f"✓ {step['action']}", key=f"action_{step_idx}", use_container_width=True):
            st.session_state.completed_steps.append(step_idx)
            if step_idx < len(STEPS) - 1:
                st.session_state.current_step = step_idx + 1
            st.rerun()
    
    with col2:
        if step_idx > 0:
            if st.button("← Back", key=f"back_{step_idx}", use_container_width=True):
                st.session_state.current_step = step_idx - 1
                st.rerun()
    
    # Completion message
    if len(st.session_state.completed_steps) == len(STEPS):
        st.success("🌟 You Have Completed Your Journey!")
        st.write("You are strong, worthy, and loved. Continue to trust in God's plan for your life.")

# Main navigation
tab1, tab2, tab3 = st.tabs(["Your Journey", "All Resources", "About"])

with tab1:
    display_step(st.session_state.current_step)

with tab2:
    st.markdown("### All Available Resources")
    
    for name, resource in RESOURCES.items():
        st.markdown(f"#### {name}")
        st.write(resource['description'])
        
        if 'phone' in resource:
            st.write(f"📞 {resource['phone']}")
        if 'hotline' in resource:
            st.write(f"🚨 Hotline: {resource['hotline']}")
        if 'url' in resource:
            st.write(f"[Visit Website]({resource['url']})")
        if 'founder' in resource:
            st.write(f"*Founded by: {resource['founder']}*")
        
        st.write("")

with tab3:
    st.markdown("### About This App")
    st.write("""
    This is a faith-based, step-by-step guide for women seeking help from domestic violence.
    
    **Core Resources:**
    - Emergency Shelter (YWCA, National Serenity House)
    - Mental Health (Mending the Soul RMBS)
    - Wellness (One Breath Project)
    - Community Support (Church of the King)
    - Child Care (Dr. Sandy Reed)
    - Education (University of Phoenix)
    
    **Emergency Numbers:**
    - 988: National Crisis Hotline
    - 225-382-3636: Local Support
    - 911: Immediate Danger
    
    **Scripture-Based Approach:**
    This app is grounded in faith and God's love for you. Every step reflects God's compassion and healing power.
    """)

# Footer
st.markdown("""
<hr style='border: 2px solid #fbbf24;'>
<p style='text-align: center; color: #d1d5db; font-size: 11px;'>
"For God has not given us a spirit of fear, but of power and of love and of a sound mind." - 2 Timothy 1:7<br>
All resources are confidential and free. You are not alone.
</p>
""", unsafe_allow_html=True)
