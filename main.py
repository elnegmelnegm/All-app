import streamlit as st

# Display header
st.set_page_config(
    page_title="ُEDA AI Chat",
    page_icon="https://www.edaegypt.gov.eg/media/wc3lsydo/group-287.png",
    layout="wide",
)

st.markdown('''
<img src="https://www.edaegypt.gov.eg/media/wc3lsydo/group-287.png" width="250" height="100">''', unsafe_allow_html=True)

st.markdown('''
Powered by Google AI <img src="https://seeklogo.com/images/G/google-ai-logo-996E85F6FD-seeklogo.com.png" width="20" height="20"> Streamlit <img src="https://global.discourse-cdn.com/business7/uploads/streamlit/original/2X/f/f0d0d26db1f2d99da8472951c60e5a1b782eb6fe.png" width="22" height="22"> Python <img src="https://i.ibb.co/wwCs096/nn-1-removebg-preview-removebg-preview.png" width="22" height="22">''', unsafe_allow_html=True)

st.link_button("Drug Side Effects and Interactions App", "https://drug-drug-5qohebfrcptarhcj8niwgo.streamlit.app/",use_container_width= True, help="This application enables users to access comprehensive information about a specific drug by providing its name. Users can input the name of the drug, and the app will retrieve detailed information on various aspects, including but not limited to, indications, contraindications, potential side effects, and any known drug interactions. هذا التطبيق يمكّن المستخدمين من الوصول إلى معلومات شاملة حول دواء معين عن طريق تقديم اسمه. يُمكن المستخدمين من إدخال اسم الدواء، حيث سيقوم التطبيق بجلب معلومات مفصلة حول جوانب متنوعة، تشمل ولكن لا تقتصر على الدلالات، والتوجيهات، والتحذيرات، والآثار الجانبية المحتملة، وأي تفاعلات معروفة مع الأدوية الأخرى")
#st.markdown('''
#This application enables users to access comprehensive information about a specific drug by providing its name. Users can input the name of the drug, and the app will retrieve detailed information on various aspects, including but not limited to, indications, contraindications, potential side effects, and any known drug interactions''', unsafe_allow_html=True)


st.link_button("Drug Food Interactions App", "https://drug-drug-interaction-hyk3pkub6bayodgp2nnuya.streamlit.app/", use_container_width= True, help="This application empowers users to access comprehensive information about a specific food item and its potential interactions with drugs by providing its name. Users can input the name of the food, and the app will retrieve detailed information on various aspects, including but not limited to, potential interactions with specific medications.هذا التطبيق يمكن المستخدمين من الوصول إلى معلومات شاملة حول طعام معين وتفاعلاته المحتملة مع الأدوية عن طريق تقديم اسمه. يُمكن المستخدمين من إدخال اسم الطعام، حيث سيقوم التطبيق بجلب معلومات مفصلة حول جوانب متنوعة، تشمل ولكن لا تقتصر على تفاعلات محتملة مع أدوية معينة ")

st.link_button("Nutritional Guidance App for Egyptians with Diabetes, Hypertension, and Elevated Cholesterol Levels", "https://dpc-eda-iwjjdpb87qynvv5zjprgqb.streamlit.app/", use_container_width= True, help="This application empowers users to access comprehensive information about a specific food item and its potential effect on diabetes, hypertension and hypercholesterolemia by providing its picture. Users can input the picture of the food, and the app will retrieve detailed information on various aspects of potential effect on mentioned diseases.هذا التطبيق يمكن المستخدمين من الوصول إلى معلومات شاملة حول طعام معين وتاثيره على مرضى السكر او ضغط الدم او مرضى الذين يعانون من ارتفاع نسبة الكوليسترول عن تقديم صورة. يُمكن المستخدمين من إدخال صورة الطعام، حيث سيقوم التطبيق بجلب معلومات مفصلة حول تاثيره على الامراض المذكورة مسبقا ")
