import pickle
import streamlit as st

heart_disease_model = pickle.load(open(r'C:\Sophi\model\heart_disease_model.sav', 'rb'))

# Sidebar navigation
st.sidebar.markdown("## Menu")
selected = st.sidebar.selectbox('Select Page', [
    'Home',
    'Heart Disease Prediction'
])


# Function to display Home page content
def display_home_page():
    st.title("_Bine ați venit pe Portalul Sophi_")
    st.write("", )

    # Titlu pagină
    st.subheader("Sănătatea Cardiovasculară: O Privire de Ansamblu", divider='red')

    # Introducere
    st.write(
        "Pe parcursul ultimelor decenii, cercetările în domeniul sănătății cardiovasculare au evoluat considerabil, "
        "beneficiind de avansurile tehnologice și de accesul sporit la date relevante. Cu toate acestea, există încă "
        "lacune semnificative în înțelegerea complexă a interacțiunilor dintre factorii de risc, precum _vârsta, sexul,"
        "nivelurile de colesterol și presiunea arterială_, care contribuie la apariția atacurilor de cord."
    )

    # Problema atacurilor de cord
    st.subheader("Problema Atacurilor de Cord", divider='red')
    st.write(
        "_Atacul de cord (infarctul miocardic)_ rămâne una dintre cele mai presante probleme de sănătate la nivel "
        "mondial, exercitând o presiune semnificativă asupra sistemelor de sănătate și având consecințe serioase "
        "asupra calității vieții și a longevității populației."
    )

    # Statistici
    st.subheader("Statistici și Impact Economic", divider='red')
    st.write(
        "Bolile de inimă au costat Statele Unite aproximativ _239,9 miliarde de dolari în fiecare an_, în perioada "
        "2018-2019. Acest lucru include costul serviciilor de asistență medicală, al medicamentelor și al "
        "productivității pierdute din cauza decesului."
    )

    # Impactul atacurilor de cord
    st.subheader("Impactul Atacurilor de Cord", divider='red')
    st.write(
        "Dacă ne axăm pe atacuri de cord, în Statele Unite, cineva suferă un atac de cord la fiecare _40 de secunde_."
        " În fiecare an, aproximativ _805.000 de persoane_ din Statele Unite suferă un atac de cord."
    )


# Function to display Heart Disease Prediction page content
def display_heart_disease_prediction():
    st.title('Heart Disease Prediction')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input('Age')

    with col2:
        sex_category = st.selectbox('Sex',
                                    ['Male', 'Female'])
        sex_numeric = convert_cp_to_numeric(sex_category)

    with col3:
        cp_category = st.selectbox('Chest Pain types',
                                   ['typical angina', 'atypical angina', 'non-anginal pain', 'asymptomatic'])
        cp_numeric = convert_cp_to_numeric(cp_category)

    with col1:
        trestbps = st.number_input('Resting Blood Pressure')

    with col2:
        chol = st.number_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs_category = st.selectbox('Fasting Blood Sugar > 120 mg/dl',
                                    ['True', 'False'])
        fbs_numeric = convert_cp_to_numeric(fbs_category)

    with col1:
        restecg_category = st.selectbox('Resting Electrocardiographic results',
                                        ['Normal', 'Having ST-T wave abnormality',
                                         'Left ventricular hypertrophy by Estes '
                                         'criteria'])
        restecg_numeric = convert_cp_to_numeric(restecg_category)

    with col2:
        thalach = st.number_input('Maximum Heart Rate achieved')

    with col3:
        exang_category = st.selectbox('Exercise Induced Angina', ['Yes', 'No'])
        exang_numeric = convert_cp_to_numeric(exang_category)

    with col1:
        oldpeak = st.number_input('ST depression induced by exercise')

    with col2:
        slope_category = st.selectbox('Slope of the peak exercise ST segment', ['Upsloping', 'Flat', 'Downsloping'])
        slope_numeric = convert_cp_to_numeric(slope_category)

    with col3:
        ca_category = st.selectbox('Major vessels colored by flourosopy',
                                   ['A major vessel coloured by flouroscopy',
                                    'Two major vessels coloured by flouroscopy',
                                    'Three major vessels coloured by flouroscopy'])
        ca_numeric = convert_cp_to_numeric(ca_category)

    with col1:
        thal_category = st.selectbox('Thalassemia',
                                     ['Normal',
                                      'Fixed defect',
                                      'Reversable defect'])
        thal_numeric = convert_cp_to_numeric(thal_category)

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict(
            [[age, sex_numeric, cp_numeric, trestbps, chol, fbs_numeric, restecg_numeric, thalach,
              exang_numeric, oldpeak, slope_numeric, ca_numeric, thal_numeric]])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)


def convert_sex_to_numeric(sex_category):
    if sex_category == 'Female':
        return 0
    elif sex_category == 'Male':
        return 1
    else:
        return 2


def convert_cp_to_numeric(cp_category):
    if cp_category == 'typical angina':
        return 0
    elif cp_category == 'atypical angina':
        return 1
    elif cp_category == 'non-anginal pain':
        return 2
    elif cp_category == 'asymptomatic':
        return 3
    else:
        return 4


def convert_fbs_to_numeric(fbs_category):
    if fbs_category == 'False':
        return 0
    elif fbs_category == 'True':
        return 1
    else:
        return 2


def convert_restecg_to_numeric(restecg_category):
    if restecg_category == 'Normal':
        return 0
    elif restecg_category == 'Having ST-T wave abnormality':
        return 1
    elif restecg_category == 'Left ventricular hypertrophy by Estes criteria':
        return 2
    else:
        return 3


def convert_exang_to_numeric(exang_category):
    if exang_category == 'No':
        return 0
    elif exang_category == 'Yes':
        return 1
    else:
        return 2


def convert_slope_to_numeric(slope_category):
    if slope_category == 'Upsloping':
        return 0
    elif slope_category == 'Flat':
        return 1
    elif slope_category == 'Downsloping':
        return 2
    else:
        return 3


def convert_ca_to_numeric(ca_category):
    if ca_category == 'A major vessel coloured by flouroscopy':
        return 1
    elif ca_category == 'Two major vessels coloured by flouroscopy':
        return 2
    elif ca_category == 'Three major vessels coloured by flouroscopy':
        return 3
    else:
        return 4


def convert_thal_to_numeric(thal_category):
    if thal_category == 'Normal':
        return 1
    elif thal_category == 'Fixed defect':
        return 2
    elif thal_category == 'Reversable defect':
        return 3
    else:
        return 0


# Display content based on selected page
if selected == 'Home':
    display_home_page()
elif selected == 'Heart Disease Prediction':
    display_heart_disease_prediction()
