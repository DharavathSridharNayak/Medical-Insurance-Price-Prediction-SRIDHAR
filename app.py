import streamlit as st
import pickle
import numpy as np
from streamlit_extras.colored_header import colored_header
from streamlit_extras.stylable_container import stylable_container

# Load the trained model
try:
    with open('MIPML.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
except Exception as e:
    st.error(f"Failed to load the model: {e}")

# App configuration
st.set_page_config(
    page_title="MEDICAL INSURANCE PRICE PREDICTION 🩺💰📊",
    page_icon="🏥",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Custom CSS with vibrant theme
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
    }
    
    .stApp {
        background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
        color: white;
    }
    
    /* Rainbow gradient title effect */
    .rainbow-title {
        font-family: 'Montserrat', sans-serif;
        background: linear-gradient(90deg, 
            #FF5252 0%, 
            #FF4081 15%, 
            #E040FB 30%, 
            #7C4DFF 45%, 
            #536DFE 60%, 
            #40C4FF 75%, 
            #64FFDA 90%);
        -webkit-background-clip: text;
        background-clip: text;
        color: transparent;
        font-weight: 800;
        font-size: 2.8rem;
        text-align: center;
        margin-bottom: 0.5rem;
        text-shadow: 0 0 10px rgba(255,255,255,0.3);
        animation: rainbow 8s ease infinite;
        background-size: 400% 400%;
    }
    
    @keyframes rainbow {
        0% { background-position: 0% 50% }
        50% { background-position: 100% 50% }
        100% { background-position: 0% 50% }
    }
    
    /* Glass card styling */
    .glass-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
        padding: 2rem;
        transition: all 0.3s ease;
    }
    
    .glass-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 40px rgba(0, 0, 0, 0.4);
    }
    
    /* Rainbow button styling */
    .stButton>button {
        background: linear-gradient(90deg, 
            #FF5252 0%, 
            #FF4081 25%, 
            #E040FB 50%, 
            #7C4DFF 75%, 
            #536DFE 100%);
        color: white;
        border: none;
        padding: 0.75rem 1.5rem;
        border-radius: 50px;
        font-weight: 700;
        font-size: 1rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(123, 31, 162, 0.3);
        text-transform: uppercase;
        letter-spacing: 1px;
        background-size: 200% auto;
    }
    
    .stButton>button:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(123, 31, 162, 0.5);
        background-position: right center;
    }
    
    /* Custom input styling */
    .stSlider>div>div>div>div {
        background: linear-gradient(90deg, #FF5252 0%, #536DFE 100%) !important;
    }
    
    .stSelectbox>div>div>div>div {
        background-color: rgba(15, 23, 42, 0.8);
        color: white;
        border: 1px solid rgba(255, 255, 255, 0.3);
    }
    
    /* Result highlight - Rainbow effect */
    .rainbow-highlight {
        font-size: 3.5rem;
        font-weight: 800;
        background: linear-gradient(90deg, 
            #FF5252 0%, 
            #FF4081 25%, 
            #E040FB 50%, 
            #7C4DFF 75%, 
            #536DFE 100%);
        -webkit-background-clip: text;
        background-clip: text;
        color: transparent;
        margin: 1rem 0;
        text-align: center;
        text-shadow: 0 0 10px rgba(255,255,255,0.3);
        animation: rainbow 8s ease infinite;
        background-size: 400% 400%;
    }
    
    /* Health tip cards - Glass with gradient border */
    .health-tip-card {
        background: rgba(255, 255, 255, 0.08);
        border-radius: 12px;
        padding: 1.2rem;
        margin: 0.8rem 0;
        border-left: 4px solid;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .health-tip-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, 
            #FF5252 0%, 
            #FF4081 25%, 
            #E040FB 50%, 
            #7C4DFF 75%, 
            #536DFE 100%);
    }
    
    .health-tip-card:hover {
        transform: translateX(5px);
        background: rgba(255, 255, 255, 0.15);
    }
    
    /* Floating animation for emojis */
    .floating {
        animation: floating 3s ease-in-out infinite;
    }
    
    @keyframes floating {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
        100% { transform: translateY(0px); }
    }
    
    /* Pulse animation for important elements */
    .pulse {
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    
    /* Custom section headers */
    .section-header {
        font-size: 1.5rem;
        font-weight: 700;
        margin-bottom: 1.5rem;
        position: relative;
        display: inline-block;
    }
    
    .section-header::after {
        content: '';
        position: absolute;
        bottom: -8px;
        left: 0;
        width: 100%;
        height: 4px;
        background: linear-gradient(90deg, 
            #FF5252 0%, 
            #FF4081 25%, 
            #E040FB 50%, 
            #7C4DFF 75%, 
            #536DFE 100%);
        border-radius: 2px;
    }
    
    /* Badge styling */
    .badge {
        display: inline-block;
        padding: 0.25rem 0.75rem;
        border-radius: 50px;
        font-weight: 600;
        font-size: 0.75rem;
        margin-right: 0.5rem;
        margin-bottom: 0.5rem;
    }
    
    /* Progress bar styling */
    .progress-container {
        width: 100%;
        background-color: rgba(255,255,255,0.1);
        border-radius: 10px;
        margin: 0.5rem 0;
    }
    
    .progress-bar {
        height: 10px;
        border-radius: 10px;
        background: linear-gradient(90deg, 
            #FF5252 0%, 
            #FF4081 25%, 
            #E040FB 50%, 
            #7C4DFF 75%, 
            #536DFE 100%);
        transition: width 0.5s ease;
    }
</style>
""", unsafe_allow_html=True)

# Prediction function
def predict_charges(age, sex, bmi, children, smoker, region):
    sex = 1 if sex.lower() == 'male' else 0
    smoker = 1 if smoker.lower() == 'yes' else 0
    region_mapping = {'southwest': 0, 'southeast': 1, 'northwest': 2, 'northeast': 3}
    region = region_mapping.get(region.lower(), -1)
    if region == -1:
        st.error("Invalid region selected.")
        return None
    try:
        features = np.array([[age, bmi, children, smoker]], dtype=np.float32)
        prediction = model.predict(features)[0]
        return prediction
    except Exception as e:
        st.error(f"Prediction Error: {e}")
        return None

# Main app
def main():
    # Header section with rainbow gradient title
    with st.container():
        st.markdown("""
        <div style="text-align: center; padding: 2rem 0 1rem;">
            <h1 class="rainbow-title">MEDICAL INSURANCE PRICE PREDICTION 🩺💰📊</h1>
            <p style="font-size: 1.2rem; color: rgba(255,255,255,0.8); max-width: 700px; margin: 0 auto;">
                The Medical Insurance Price Prediction with <span style="font-weight:700;background:linear-gradient(90deg, #64FFDA 0%, #536DFE 100%);-webkit-background-clip:text;background-clip:text;color:transparent;">85%</span> Accuracy
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    # Split layout into two columns
    col1, col2 = st.columns([1, 1], gap="large")
    
    with col1:
        # Input form in glass card
        with stylable_container(
            key="input_form",
            css_styles="""
            {
                background: rgba(255, 255, 255, 0.1);
                backdrop-filter: blur(12px);
                border-radius: 20px;
                border: 1px solid rgba(255, 255, 255, 0.2);
                padding: 2rem;
                box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
                margin-bottom: 2rem;
            }
            """
        ):
            st.markdown("""
            <h3 class="section-header">
                <span class="floating">🧑‍💻</span> Your Profile Details
            </h3>
            """, unsafe_allow_html=True)
            
            age = st.slider('Age', 1, 100, 30, 
                          help="Your current age significantly impacts your premium")
            sex = st.selectbox('Gender', ['Male', 'Female'])
            bmi = st.slider('BMI', 15.0, 40.0, 22.0, 0.1,
                           help="Body Mass Index (18.5-24.9 is considered healthy)")
            children = st.select_slider('Number of Childrens', 
                                      options=[0, 1, 2, 3, 4, 5],
                                      help="Children or other dependents covered by your plan")
            smoker = st.radio('Do you smoke?', ['No', 'Yes'], 
                            horizontal=True,
                            help="Smoking status greatly affects insurance costs")
            region = st.selectbox('Region', 
                                ['Southwest', 'Southeast', 'Northwest', 'Northeast'],
                                help="Medical costs vary by geographic region")
            
            predict_btn = st.button("✨  ESTIMATED INSURANCE CHARGES", 
                                   type="primary", 
                                   use_container_width=True)
    
    with col2:
        # Results and info section
        if predict_btn:
            with st.spinner("🔮 Analyzing your profile with AI..."):
                prediction = predict_charges(age, sex, bmi, children, smoker, region)
                
                if prediction is not None:
                    with stylable_container(
                        key="result_card",
                        css_styles="""
                        {
                            background: rgba(255, 255, 255, 0.1);
                            backdrop-filter: blur(12px);
                            border-radius: 20px;
                            border: 1px solid rgba(255, 255, 255, 0.2);
                            padding: 2rem;
                            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
                            margin-bottom: 2rem;
                            text-align: center;
                        }
                        """
                    ):
                        st.markdown(f"""
                        <h3 class="section-header">
                            <span class="floating">💵</span> Your Estimated Annual Premium
                        </h3>
                        <div class="rainbow-highlight">{prediction:,.2f}</div>
                        <p style='color: rgba(255,255,255,0.8); font-size: 0.9rem;'>
                            Based on your unique profile characteristics
                        </p>
                        """, unsafe_allow_html=True)
                    
                    # Health recommendations
                    with stylable_container(
                        key="recommendations",
                        css_styles="""
                        {
                            background: rgba(255, 255, 255, 0.1);
                            backdrop-filter: blur(12px);
                            border-radius: 20px;
                            border: 1px solid rgba(255, 255, 255, 0.2);
                            padding: 1.5rem;
                            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.2);
                        }
                        """
                    ):
                        st.markdown("""
                        <h3 class="section-header">
                            <span class="floating">🌈</span> Personalized Health Insights
                        </h3>
                        """, unsafe_allow_html=True)
                        
                        # BMI Analysis
                        bmi_status = ""
                        if bmi < 18.5:
                            bmi_status = "Underweight"
                            bmi_color = "#FF5252"
                            bmi_percent = 30
                        elif 18.5 <= bmi <= 24.9:
                            bmi_status = "Healthy"
                            bmi_color = "#64FFDA"
                            bmi_percent = 70
                        elif 25 <= bmi <= 29.9:
                            bmi_status = "Overweight"
                            bmi_color = "#FFAB40"
                            bmi_percent = 40
                        else:
                            bmi_status = "Obese"
                            bmi_color = "#FF5252"
                            bmi_percent = 20
                            
                        st.markdown(f"""
                        <div class="health-tip-card">
                            <div style="display: flex; justify-content: space-between; align-items: center;">
                                <strong style="font-size:1.1rem; color: {bmi_color};">📊 BMI Analysis</strong>
                                <span class="badge" style="background: {bmi_color};">{bmi_status}</span>
                            </div>
                            <p style="margin: 0.5rem 0 0.2rem 0; color: rgba(255,255,255,0.9);">
                                Your BMI: <strong>{bmi:.1f}</strong> ({bmi_status})
                            </p>
                            <div class="progress-container">
                                <div class="progress-bar" style="width: {bmi_percent}%; background: {bmi_color};"></div>
                            </div>
                            <p style="margin: 0.5rem 0 0 0; color: rgba(255,255,255,0.9); font-size: 0.9rem;">
                                {f"Great job! Maintain your healthy weight." if bmi_status == "Healthy" 
                                else "Consider dietary changes and regular exercise to improve your BMI."}
                            </p>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        # Smoking Analysis
                        if smoker == 'Yes':
                            st.markdown("""
                            <div class="health-tip-card">
                                <div style="display: flex; justify-content: space-between; align-items: center;">
                                    <strong style="font-size:1.1rem; color: #FF4081;">🚭 Smoking Impact</strong>
                                    <span class="badge" style="background: #FF4081;">High Risk</span>
                                </div>
                                <p style="margin: 0.5rem 0 0 0; color: rgba(255,255,255,0.9);">
                                    Quitting smoking could lower your premium by up to <strong>50%</strong>.
                                </p>
                                <div style="margin-top: 0.8rem;">
                                    <span class="badge" style="background: #7C4DFF;">Quitline: 1-800-QUIT-NOW</span>
                                    <span class="badge" style="background: #40C4FF;">Nicotine Replacement</span>
                                    <span class="badge" style="background: #64FFDA;">Support Groups</span>
                                </div>
                            </div>
                            """, unsafe_allow_html=True)
                        
                        # Age Analysis
                        age_risk = ""
                        if age < 30:
                            age_risk = "Low Risk"
                            age_color = "#64FFDA"
                        elif 30 <= age < 50:
                            age_risk = "Moderate Risk"
                            age_color = "#FFAB40"
                        else:
                            age_risk = "Higher Risk"
                            age_color = "#FF5252"
                            
                        st.markdown(f"""
                        <div class="health-tip-card">
                            <div style="display: flex; justify-content: space-between; align-items: center;">
                                <strong style="font-size:1.1rem; color: {age_color};">👵 Age Factor</strong>
                                <span class="badge" style="background: {age_color};">{age_risk}</span>
                            </div>
                            <p style="margin: 0.5rem 0 0 0; color: rgba(255,255,255,0.9);">
                                At <strong>{age} years</strong>, consider these preventive measures:
                            </p>
                            <div style="margin-top: 0.8rem;">
                                <span class="badge" style="background: #536DFE;">Annual Physical</span>
                                <span class="badge" style="background: #E040FB;">Cancer Screenings</span>
                                {f'<span class="badge" style="background: #FF4081;">Cardio Checkup</span>' if age >= 40 else ''}
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        # General Wellness Tips
                        st.markdown("""
                        <div class="health-tip-card">
                            <strong style="font-size:1.1rem; color: #40C4FF;">🌟 Wellness Boosters</strong>
                            <p style="margin: 0.5rem 0 0 0; color: rgba(255,255,255,0.9);">
                                These habits can improve your health and potentially lower rates:
                            </p>
                            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.5rem; margin-top: 0.8rem;">
                                <span class="badge" style="background: #7C4DFF;">🏋️ 150min Exercise/Week</span>
                                <span class="badge" style="background: #FF4081;">🍎 5+ Fruits/Veggies Daily</span>
                                <span class="badge" style="background: #64FFDA;">💤 7-9 Hours Sleep</span>
                                <span class="badge" style="background: #FFAB40;">🧘 Stress Management</span>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
        
        else:
            # Default info display
            with stylable_container(
                key="info_card",
                css_styles="""
                {
                    background: rgba(255, 255, 255, 0.1);
                    backdrop-filter: blur(12px);
                    border-radius: 20px;
                    border: 1px solid rgba(255, 255, 255, 0.2);
                    padding: 2rem;
                    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
                }
                """
            ):
                st.markdown("""
                <h3 class="section-header">
                    <span class="floating">💡</span> How Medical Insurance Price Predictor App Works
                </h3>
                <p style='color: rgba(255,255,255,0.9); margin-bottom: 1.5rem;'>
                    This App analyzes thousands of data points to provide accurate premium estimates 
                    and personalized health recommendations to help you save on insurance costs.
                </p>
                
                <div style='background: rgba(255, 255, 255, 0.1);
                    border-radius: 15px;
                    padding: 1.5rem;
                    margin-top: 1.5rem;
                    border: 1px solid rgba(255, 255, 255, 0.2);'>
                    <h3 class="section-header">
                        <span class="floating">📊</span> Premium Impact Factors
                    </h3>
                    
                    <div class="health-tip-card" style="border-left-color: #FF5252;">
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <strong style="color: #FF5252;">🔼 Major Cost Increases</strong>
                            <span class="badge" style="background: #FF5252;">High Impact</span>
                        </div>
                        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.5rem; margin-top: 0.8rem;">
                            <span class="badge" style="background: rgba(255,82,82,0.2); color: #FF5252;">Smoking (+50-300%)</span>
                            <span class="badge" style="background: rgba(255,82,82,0.2); color: #FF5252;">Obesity (+20-100%)</span>
                            <span class="badge" style="background: rgba(255,82,82,0.2); color: #FF5252;">Chronic Conditions</span>
                            <span class="badge" style="background: rgba(255,82,82,0.2); color: #FF5252;">Older Age</span>
                        </div>
                    </div>
                    
                    <div class="health-tip-card" style="border-left-color: #64FFDA;">
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <strong style="color: #64FFDA;">🔽 Potential Savings</strong>
                            <span class="badge" style="background: #64FFDA; color: #0f0c29;">Up to 40%</span>
                        </div>
                        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.5rem; margin-top: 0.8rem;">
                            <span class="badge" style="background: rgba(100,255,218,0.2); color: #64FFDA;">Non-Smoker Discount</span>
                            <span class="badge" style="background: rgba(100,255,218,0.2); color: #64FFDA;">Healthy BMI</span>
                            <span class="badge" style="background: rgba(100,255,218,0.2); color: #64FFDA;">Preventive Care</span>
                            <span class="badge" style="background: rgba(100,255,218,0.2); color: #64FFDA;">Wellness Programs</span>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
    
    # Footer with gradient border
    st.markdown("""
    <div style="
        background: rgba(15, 23, 42, 0.7);
        color: white;
        padding: 1.5rem;
        text-align: center;
        border-radius: 20px 20px 0 0;
        margin-top: 3rem;
        border-top: 1px solid transparent;
        border-image: linear-gradient(90deg, 
            #FF5252 0%, 
            #FF4081 25%, 
            #E040FB 50%, 
            #7C4DFF 75%, 
            #536DFE 100%);
        border-image-slice: 1;
    ">
        <p style="margin: 0; color: rgba(255,255,255,0.9); font-size: 0.9rem;">
            This estimate is generated by Medical Insurance Price Predictor App and should not be considered an actual insurance quote.
        </p>
        <p style="margin: 0.5rem 0 0 0; color: rgba(255,255,255,0.7); font-size: 0.8rem;">
            © 2025 Medical Insurance Price Predictor | Built with ❤ using Streamlit | Deployed on Hugging Face
        </p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
