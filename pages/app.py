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
    st.title('Predicția apariției atacului de cord')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input('Vârsta')

    with col2:
        sex_category = st.selectbox('Sex',
                                    ['Bărbat', 'Femeie'])
        sex_numeric = convert_cp_to_numeric(sex_category)

    with col3:
        cp_category = st.selectbox('Tipuri de dureri toracice',
                                   ['angină pectorală tipică', 'angina atipică', 'durere non-anginoasă', 'asimptomatic'])
        cp_numeric = convert_cp_to_numeric(cp_category)

    with col1:
        trestbps = st.number_input('Tensiunea arterială în repaus')

    with col2:
        chol = st.number_input('Colestoral seric în mg/dl')

    with col3:
        fbs_category = st.selectbox('Zahărul din sânge în stare de repaus > 120 mg/dl',
                                    ['Adevărat', 'Fals'])
        fbs_numeric = convert_cp_to_numeric(fbs_category)

    with col1:
        restecg_category = st.selectbox('Rezultate electrocardiografice în repaus',
                                        ['Normal', 'Anomalie a undei ST-T',
                                         'Hipertrofia ventriculară stângă după criteriile Estes'])
        restecg_numeric = convert_cp_to_numeric(restecg_category)

    with col2:
        thalach = st.number_input('Ritmul cardiac maxim atins')

    with col3:
        exang_category = st.selectbox('Angina indusă de exercițiu', ['Da', 'Nu'])
        exang_numeric = convert_cp_to_numeric(exang_category)

    with col1:
        oldpeak = st.number_input('Depresia ST indusă de exercițiu')

    with col2:
        slope_category = st.selectbox('Panta segmentului ST de vârf de exercițiu', ['Înclinată ascendentă', 'Plată', 'Înclinație descendentă'])
        slope_numeric = convert_cp_to_numeric(slope_category)

    with col3:
        ca_category = st.selectbox('Vasele majore colorate prin flouroscopie',
                                   ['Un vas major colorat prin flouroscopie',
                                    'Două vase majore colorate prin flouroscopie',
                                    'Trei vase majore colorate prin flouroscopie'])
        ca_numeric = convert_cp_to_numeric(ca_category)

    with col1:
        thal_category = st.selectbox('Talasemie',
                                     ['Normal',
                                      'Defect fixat',
                                      'Defect reversibil'])
        thal_numeric = convert_cp_to_numeric(thal_category)

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction
    if st.button('Rezultatul testului predicției atacului de cord'):
        heart_prediction = heart_disease_model.predict(
            [[age, sex_numeric, cp_numeric, trestbps, chol, fbs_numeric, restecg_numeric, thalach,
              exang_numeric, oldpeak, slope_numeric, ca_numeric, thal_numeric]])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'Persoana poate suferi un atac de cord'
        else:
            heart_diagnosis = 'Persoana nu poate suferi un atac de cord'

    st.success(heart_diagnosis)


def convert_sex_to_numeric(sex_category):
    if sex_category == 'Femeie':
        return 0
    elif sex_category == 'Bărbat':
        return 1
    else:
        return 2


def convert_cp_to_numeric(cp_category):
    if cp_category == 'angină pectorală tipică':
        return 0
    elif cp_category == 'angina atipică':
        return 1
    elif cp_category == 'durere non-anginoasă':
        return 2
    elif cp_category == 'asimptomatic':
        return 3
    else:
        return 4


def convert_fbs_to_numeric(fbs_category):
    if fbs_category == 'Fals':
        return 0
    elif fbs_category == 'Adevărat':
        return 1
    else:
        return 2


def convert_restecg_to_numeric(restecg_category):
    if restecg_category == 'Normal':
        return 0
    elif restecg_category == 'Anomalie a undei ST-T':
        return 1
    elif restecg_category == 'Hipertrofia ventriculară stângă după criteriile Estes':
        return 2
    else:
        return 3


def convert_exang_to_numeric(exang_category):
    if exang_category == 'Nu':
        return 0
    elif exang_category == 'Da':
        return 1
    else:
        return 2


def convert_slope_to_numeric(slope_category):
    if slope_category == 'Înclinată ascendentă':
        return 0
    elif slope_category == 'Plată':
        return 1
    elif slope_category == 'Înclinație descendentă':
        return 2
    else:
        return 3


def convert_ca_to_numeric(ca_category):
    if ca_category == 'Un vas major colorat prin flouroscopie':
        return 1
    elif ca_category == 'Două vase majore colorate prin flouroscopie':
        return 2
    elif ca_category == 'Trei vase majore colorate prin flouroscopie':
        return 3
    else:
        return 4


def convert_thal_to_numeric(thal_category):
    if thal_category == 'Normal':
        return 1
    elif thal_category == 'Defect fixat':
        return 2
    elif thal_category == 'Defect reversibil':
        return 3
    else:
        return 0


# Display content based on selected page
if selected == 'Acasă':
    display_home_page()
elif selected == 'Predicția apariției atacului de cord':
    display_heart_disease_prediction()
