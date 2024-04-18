import time
import joblib
from streamlit_option_menu import option_menu
import pandas as pd
import altair as alt
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="Djessy",
    page_icon="chart_with_upwards_trend",
    layout="wide",
)

with open(r'train_model/models/random_forest_model.sav', 'rb') as file:
    heart_disease_model = joblib.load(file)

with st.sidebar:
    selected = option_menu('Main Menu',
                           ['Acasă', 'Predicția apariției atacului de cord', 'Analiza datelor'],
                           icons=['house', 'magic', 'clipboard-data'], menu_icon='cast',
                           default_index=0)


def display_home_page():
    st.title('_Bine ați venit pe Portalul Djessy_')
    st.write('', )

    st.subheader('Sănătatea Cardiovasculară: O Privire de Ansamblu', divider='red')

    st.write(
        'Pe parcursul ultimelor decenii, cercetările în domeniul sănătății cardiovasculare au evoluat considerabil, '
        'beneficiind de avansurile tehnologice și de accesul sporit la date relevante. Cu toate acestea, există încă '
        'lacune semnificative în înțelegerea complexă a interacțiunilor dintre factorii de risc, precum _vârsta, sexul,'
        'nivelurile de colesterol și presiunea arterială_, care contribuie la apariția atacurilor de cord.'
    )

    st.subheader('Problema Atacurilor de Cord', divider='red')
    st.write(
        '_Atacul de cord (infarctul miocardic)_ rămâne una dintre cele mai presante probleme de sănătate la nivel '
        'mondial, exercitând o presiune semnificativă asupra sistemelor de sănătate și având consecințe serioase '
        'asupra calității vieții și a longevității populației.'
    )

    st.subheader('Statistici și Impact Economic', divider='red')
    st.write(
        'Bolile de inimă au costat Statele Unite aproximativ _239,9 miliarde de dolari în fiecare an_, în perioada '
        '2018-2019. Acest lucru include costul serviciilor de asistență medicală, al medicamentelor și al '
        'productivității pierdute din cauza decesului.'
    )

    st.subheader('Impactul Atacurilor de Cord', divider='red')
    st.write(
        'Dacă ne axăm pe atacuri de cord, în Statele Unite, cineva suferă un atac de cord la fiecare _40 de secunde_.'
        ' În fiecare an, aproximativ _805.000 de persoane_ din Statele Unite suferă un atac de cord.'
    )


def display_heart_disease_prediction():
    st.subheader('Predicția apariției atacului de cord')
    tab1, tab2 = st.tabs(['📈Predicția riscului apariției atacului de cord',
                          '📝Recomandări pentru a preveni apariția atacului de cord'])

    with tab1:
        col1, col2, col3 = st.columns(3)

        with col1:
            age = st.number_input('Vârsta')

        with col2:
            sex_category = st.selectbox('Sex',
                                        ['Bărbat', 'Femeie'])
            sex_numeric = convert_sex_to_numeric(sex_category)

        with col3:
            cp_category = st.selectbox('Tipuri de dureri toracice',
                                       ['angină pectorală tipică', 'angina atipică', 'durere non-anginoasă',
                                        'asimptomatic'])
            cp_numeric = convert_cp_to_numeric(cp_category)

        with col1:
            trestbps = st.number_input('Tensiunea arterială în repaus')

        with col2:
            chol = st.number_input('Colestoral seric în mg/dl')

        with col3:
            fbs_category = st.selectbox('Zahărul din sânge în stare de repaus > 120 mg/dl',
                                        ['Adevărat', 'Fals'])
            fbs_numeric = convert_fbs_to_numeric(fbs_category)

        with col1:
            restecg_category = st.selectbox('Rezultate electrocardiografice în repaus',
                                            ['Normal', 'Anomalie a undei ST-T',
                                             'Hipertrofia ventriculară stângă după criteriile Estes'])
            restecg_numeric = convert_restecg_to_numeric(restecg_category)

        with col2:
            thalach = st.number_input('Ritmul cardiac maxim atins')

        with col3:
            exang_category = st.selectbox('Angina indusă de exercițiu', ['Da', 'Nu'])
            exang_numeric = convert_exang_to_numeric(exang_category)

        with col1:
            oldpeak = st.number_input('Depresia ST indusă de exercițiu')

        with col2:
            slope_category = st.selectbox('Panta segmentului ST de vârf de exercițiu',
                                          ['Înclinată ascendentă', 'Plată', 'Înclinație descendentă'])
            slope_numeric = convert_slope_to_numeric(slope_category)

        with col3:
            ca_category = st.selectbox('Vasele majore colorate prin flouroscopie',
                                       ['Niciun vas major colorat prin flouroscopie',
                                        'Un vas major colorat prin flouroscopie',
                                        'Două vase majore colorate prin flouroscopie',
                                        'Trei vase majore colorate prin flouroscopie'])
            ca_numeric = convert_ca_to_numeric(ca_category)

        with col1:
            thal_category = st.selectbox('Talasemie',
                                         ['Normal',
                                          'Defect fixat',
                                          'Defect reversibil'])
            thal_numeric = convert_thal_to_numeric(thal_category)

        if st.button('Rezultatul testului predicției atacului de cord'):
            progres_text = "Se prelucrează datele furnizate. Așteptați puțin."
            bar = st.progress(0)

            for procent_complet in range(100):
                time.sleep(0.03)
                bar.progress(procent_complet + 1, text=f"{procent_complet + 1}% - {progres_text}")
            bar.empty()
            heart_prediction = heart_disease_model.predict(
                [[age, sex_numeric, cp_numeric, trestbps, chol, fbs_numeric, restecg_numeric, thalach,
                  exang_numeric, oldpeak, slope_numeric, ca_numeric, thal_numeric]])

            if heart_prediction[0] == 1:
                heart_diagnosis = 'Persoana poate suferi un atac de cord'
                st.warning(heart_diagnosis)
                st.toast('Ai grijă de inima ta! Cineva drag te așteaptă acasă mereu.', icon='😢')
                time.sleep(2)
                st.toast('Îți place să te joci cu viața?', icon='🤨')
                time.sleep(2)
                st.toast('Consultă imediat un medic cardiolog!', icon='⚠')
                time.sleep(2)

            else:
                heart_diagnosis = 'Persoana nu poate suferi un atac de cord'
                st.success(heart_diagnosis)
                st.toast('Ești o sursă de inspirație!', icon='🎉')
                time.sleep(2)
                st.toast('Respect!', icon='😎')
                time.sleep(2)
                st.toast('Un train_model de disciplină și responsabilitate admirabil!', icon='😍')
                time.sleep(2)
                st.toast('Un exemplu viu de dedicare și preocupare pentru sănătate sa!', icon='😁')
                time.sleep(2)
                st.toast('Disciplina și responsabilitatea prelungesc viața.', icon='😉')
                time.sleep(2)
                st.toast('Exemplu viu de dedicare și preocupare pentru inima sa.', icon='🥇')
                time.sleep(2)
    with tab2:
        if cp_numeric == 0:
            st.write('**Angină pectorală tipică poate apărea din cauza unei activități fizice intense. Iată câteva '
                     'recomandări:**')
            st.write('1. Consultați un medic pentru evaluarea și diagnosticarea corectă a anginei pectorale și pentru '
                     'a elabora un plan de tratament adecvat.')
            st.write('2. Urmăriți modificările stilului de viață, care includ o alimentație echilibrată, activitate '
                     'fizică regulată și renunțarea la fumat.')
            st.write('3. Luați medicamentele prescrise de medic pentru controlul durerii, a tensiunii arteriale și a '
                     'altor factori de risc cardiovascular.')
            st.write('4. Fiți atent la simptomele anginei pectorale și notați orice schimbare a acestora pentru a '
                     'discuta cu medicul dumneavoastră.')
            st.write('5. Dacă este recomandat de medic, participați la un program de reabilitare cardiacă pentru a vă '
                     'ajuta să vă recăpătați și să vă îmbunătățiți starea de sănătate cardiovasculară.')
            st.write('6. Gestionarea eficientă a stresului poate contribui la reducerea episoadelor de angină '
                     'pectorală. Exercițiile de respirație, meditația și alte tehnici de relaxare pot fi benefice.')

        elif cp_numeric == 1:
            st.write('**Angina atipică poate apărea, de exemplu, din cauza unor spasme coronariene. Iată câteva '
                     'recomandări:**')
            st.write('1. Consultați un medic pentru evaluarea și diagnosticarea corectă a simptomelor dumneavoastră.')
            st.write('2. Monitorizați simptomele și notificați medicul despre orice schimbare sau exacerbare a '
                     'acestora.')
            st.write('3. Respectați cu strictețe instrucțiunile și recomandările medicului pentru gestionarea '
                     'simptomelor anginei atipice.')

        elif cp_numeric == 2:
            st.write('**Durerea non-anginoasă poate apărea, de exemplu, din cauza anxietății și stresului. Iată câteva '
                     'recomandări:**')
            st.write('1. Identificați cauza durerii și consultați un medic pentru evaluare și tratament adecvat.')
            st.write('2. Evitați auto-diagnosticul și auto-medicația, și cereți sfatul unui specialist în caz de '
                     'durere în piept.')
            st.write('3. Urmați recomandările medicului și participați la investigații suplimentare pentru '
                     'clarificarea diagnosticului.')

        elif cp_numeric == 3:
            st.write('**Angina atipică poate să nu prezinte simptome evidente. Iată câteva recomandări pentru '
                     'gestionarea acestei forme asimptomatice:**')
            st.write('1. Chiar dacă nu prezentați simptome, efectuați examene medicale regulate pentru evaluarea '
                     'stării dumneavoastră de sănătate cardiovasculară.')
            st.write('2. Discutați cu medicul despre factorii de risc și despre măsurile preventive pentru prevenirea '
                     'problemelor cardiace.')
            st.write('3. Adoptați un stil de viață sănătos, care include alimentație echilibrată, activitate fizică '
                     'regulată și renunțarea la fumat.')

        if trestbps < 90:
            st.write('**Presiunea arterială este scăzută (hipotensiune). Iată câteva recomandări:**')
            st.write('1. Consumă mai multe lichide pentru a menține hidratarea.')
            st.write('2. Evită pozițiile brusc schimbate, care ar putea determina amețeli.')
            st.write('3. Consumă alimente bogate în săruri și electroliți.')
            st.write('4. Poziționează-te într-un mod confortabil când te ridici sau stai jos.')
            st.write('5. Consultă medicul pentru o evaluare și sfaturi suplimentare.')

        elif trestbps > 140:
            st.write('**Presiunea arterială este ridicată (hipertensiune). Iată câteva recomandări:**')
            st.write('1. Adoptă o dietă sănătoasă, bogată în fructe și legume și săracă în sare și grăsimi saturate.')
            st.write('2. Faci exerciții fizice regulat pentru a menține o greutate sănătoasă.')
            st.write('3. Evită consumul excesiv de alcool și renunță la fumat.')
            st.write('4. Gestionează stresul prin tehnici de relaxare sau meditație.')
            st.write('5. Monitorizează regulat presiunea arterială și consultă medicul pentru evaluare și tratament.')

        else:
            st.write('**Presiunea arterială este în intervalul normal (100-140 mmHg). Totuși, este recomandabil să '
                     'consulți periodic medicul specialist.**')

        if chol < 200:
            st.write('**Nivelul de colesterol este scăzut. Iată câteva recomandări:**')
            st.write('1. Adoptă o dietă sănătoasă și echilibrată.')
            st.write('2. Faci exerciții fizice regulat.')
            st.write('3. Consultă medicul pentru evaluare și tratament.')

        elif chol > 239:
            st.write('**Nivelul de colesterol este ridicat. Iată câteva recomandări:**')
            st.write('1. Adoptă o dietă sănătoasă și echilibrată.')
            st.write('2. Faci exerciții fizice regulat.')
            st.write('3. Consultă medicul pentru evaluare și tratament.')
        else:
            st.write('**Nivelul de colesterol este în limitele normale. Totuși, este recomandabil să consulți periodic '
                     'medicul specialist.**')

        if fbs_numeric == 0:
            st.write('**Nivelul de zahăr în sânge este în normă sau puțin scăzut de normele admisibile. De aceia, iată '
                     'câteva recomandări:**')
            st.write('1. Beți multă apă pentru a ajuta la diluarea nivelului de zahăr din sânge.')
            st.write('2. Consumați alimente sănătoase, bogate în fibre și proteine, și evitați alimentele bogate în '
                     'zahăr și carbohidrați simpli.')
            st.write('3. Faceți exerciții fizice regulate pentru a ajuta la reducerea nivelului de zahăr din sânge.')
            st.write('4. Folosiți un dispozitiv de monitorizare a glicemiei și consultați un medic pentru recomandări '
                     'specifice.')
            st.write('5. Redu și consumul de alcool, deoarece acesta poate afecta nivelul de zahăr din sânge.')
            st.write('6. Este recomandabil să consulți periodic medicul specialist.')
        elif fbs_numeric == 1:
            st.write('**Nivelul de zahăr în sânge este ridicat. Iată câteva recomandări:**')
            st.write('1. Consumați rapid carbohidrați simpli, cum ar fi suc de fructe sau bomboane, pentru a crește '
                     'nivelul de zahăr din sânge.')
            st.write('2. Monitorizați nivelul de zahăr și asigurați-vă că revine la normal.')
            st.write('3. Mâncați mese regulate și evitați perioadele prelungite fără alimente.')
            st.write('4. Evitați exercițiile fizice intense până când nivelul de zahăr revine la normal.')
            st.write('5. Consultați un medic pentru evaluare și recomandări specifice, dacă hipoglicemia este o '
                     'problemă frecventă sau severă.')

        result_thalach = 220 - age

        if result_thalach < thalach:
            st.write('**Nivelul de bătăi a inimii este ridicat. Iată câteva recomandări:**')
            st.write('1. Consultați un medic pentru evaluare **_cât mai urgent_**.')
            st.write('2. Evitați activitățile fizice intense fără recomandarea medicului.')

        else:
            abnormal_thalach = result_thalach - 15
            if abnormal_thalach < thalach:
                st.write('**Nivelul de bătăi a inimii este scăzut. Iată câteva recomandări:.**')
                st.write('1. Consultați un medic pentru evaluare și investigații suplimentare.')
                st.write('2. Faceți mișcare ușoară și monitorizați simptomele.')
                st.write('3. Discutați cu medicul despre eventualele cauze și tratament.')
            else:
                st.write('**Valorile pentru ritmul cardiac și frecvența maximă a inimii sunt într-o gamă sănătoasă.**')

        if exang_numeric == 0:
            st.write('**Faptul că simțiți durere la efort fizic nu indică o situație favorabilă. Iată câteva '
                     'recomandări:**')
            st.write('1. Opriți imediat efortul fizic și odihniți-vă dacă apare durerea.')
            st.write('2. Consultați un medic pentru evaluare și diagnosticare precisă.')
            st.write('3. Evitați eforturile fizice intense până când obțineți recomandări medicale.')
            st.write('4. Monitorizați simptomele și raportați orice schimbare medicului.')
            st.write('5. Respectați cu strictețe instrucțiunile și tratamentul prescris de medic.')

        else:
            st.write('**Cu toate că nu prezentați durere la efectuarea eforutului fizic este vital să mențineți '
                     'această stare. Iată câteva recomandări:**')
            st.write('1. Continuați exercițiile fizice regulate.')
            st.write('2. Monitorizați simptomele și semnalele corpului.')
            st.write('3. Asigurați-vă că sunteți bine hidratat și odihniți.')
            st.write('4. Consultați un medic sau specialist pentru orice îngrijorare sau întrebare.')


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
    if exang_category == 'Da':
        return 0
    elif exang_category == 'Nu':
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
        return 4


def display_statistics_heart_disease():
    st.subheader('_Analiza exploratorie a datelor de învățare a modelului_')
    tab1, tab2, tab3, tab4 = st.tabs(["🩺Presiunea arterială", "📈Ritmul cardiac în raport cu vârsta",
                                      "🤕Tipuri de durere pe gen", "💔Atacuri de cord pe gen"])

    data = pd.read_csv('train_model/data/heart_disease_data.csv')

    with tab1:
        st.write('O presupunere care persistă de mult timp, anume dacă există o asociere semnificativă între sex și '
                 'nivelurile tensiunii arteriale, cu o posibilă tendință de a observa niveluri mai ridicate la femei '
                 'în comparație cu bărbații.')
        summary_data = data.groupby('sex')['trestbps'].mean().reset_index()
        summary_data['sex'] = summary_data['sex'].map({0: 'Femei', 1: 'Bărbați'})

        st.write('**Presiune arterială medie pe sex**')
        st.bar_chart(summary_data.set_index('sex').rename(columns={'trestbps': 'Presiune arterială medie'}),
                     use_container_width=True, width=800)
        st.markdown("<hr style='border: 1px solid red;'>", unsafe_allow_html=True)
        st.write('În urma analiza acestei presupuneri, am optat pentru vizualizarea cu '
                 'ajutorul unui grafic de tip bar pentru a compara distribuțiile tensiunii arteriale în '
                 'funcție de sex. Dar, spre surprindere presupunerea nu s-a adeverit, fiind depistată o diferență '
                 'minoră în setul de date analizat. De aceia, la antrenarea unui train_model de **Machine Learning** '
                 'nu este atât de important acest parametru.')
    with tab2:
        media_thalach = data['thalach'].mean()

        chart = alt.Chart(data).mark_line().encode(
            x=alt.X('age', type='quantitative', title='Vârstă'),
            y=alt.Y('thalach', type='quantitative', title='Număr bătăi/minut'),
        )

        media_line = alt.Chart(pd.DataFrame({'media_thalach': [media_thalach]})).mark_rule(color='red').encode(
            y='media_thalach:Q'
        )

        combined_chart = (chart + media_line).properties(
            width=700,
        )

        st.write('Variația numărului maxim de bătăi a inimii în funcție de vârstă poate influența riscul de apariție '
                 'a atacului de cord în mai multe moduri.')
        st.write('**Statistica valorilor personale cu linie pentru media numărului bătăi/minut**')
        st.altair_chart(combined_chart, use_container_width=True)

        st.markdown("<hr style='border: 1px solid red;'>", unsafe_allow_html=True)
        st.write('Cu cât o persoană este mai tânără, cu atât frecvența '
                 'cardiacă maximă (FCmax) este mai mare. FCmax este de obicei calculată aproximativ ca 220 minus '
                 'vârsta în ani. Rezerva cardiacă, care reprezintă diferența între frecvența cardiacă în repaus și '
                 'cea maximă, este un indicator al capacității de adaptare a inimii la efort. La persoanele mai în '
                 'vârstă, care au o FCmax mai mică, eforturile fizice intense pot pune o presiune mai mare asupra '
                 'inimii și a sistemului cardiovascular, crescând riscul de complicații cardiace, inclusiv riscul de '
                 'atac de cord. Alți factori de risc asociati varstei, cum ar fi creșterea tensiunii arteriale, '
                 'nivelurile crescute de colesterol și diabetul, contribuie la această vulnerabilitate. Monitorizarea '
                 'frecvenței cardiace și a răspunsului inimii la activitatea fizică este esențială pentru evaluarea '
                 'riscului cardiovascular și pentru stabilirea unui plan de exerciții adecvat în funcție de vârstă și '
                 'starea de sănătate a individului. Este important să se acorde atenție acestor aspecte și să se '
                 'urmeze recomandările medicului pentru menținerea sănătății cardiovasculare.')
    with tab3:
        summary_data = data.groupby(['sex', 'cp']).size().reset_index(name='count')

        summary_data['sex'] = summary_data['sex'].map({0: 'Femei', 1: 'Bărbați'})
        summary_data['cp'] = summary_data['cp'].map({
            0: 'Angină pectorală tipică',
            1: 'Angina atipică',
            2: 'Durere non-anginoasă',
            3: 'Asimptomatic'
        })

        male_data = summary_data[summary_data['sex'] == 'Bărbați']
        male_bars = alt.Chart(male_data).mark_bar().encode(
            x=alt.X('cp:N', title='Tipul de durere'),
            y=alt.Y('count:Q', title='Numărul de observații'),
            color=alt.Color('sex:N', title='Gen'),
        ).properties(
            width=1000,
            height=400,
            title='Numărul de observații pentru fiecare tip de durere - Bărbați',
        )
        st.write('O altă presupunere pe care am cercetat-o este dacă există vreo asociere semnificativă între gen '
                 'și prevalența anumitor tipuri de durere, sugerând posibile schimbări în raportarea la gen.')

        female_data = summary_data[summary_data['sex'] == 'Femei']
        female_bars = alt.Chart(female_data).mark_bar().encode(
            x=alt.X('cp:N', title='Tipul de durere'),
            y=alt.Y('count:Q', title='Numărul de observații'),
            color=alt.Color('sex:N', title='Gen'),
        ).properties(
            width=300,
            height=400,
            title='Numărul de observații pentru fiecare tip de durere - Femei'
        )

        st.altair_chart(male_bars, use_container_width=True)
        st.write('Pentru a evidenția acestă potențială corelație, am focalizat atenția asupra variabilelor relevante.'
                 'Folosind un grafic de tip bar, am intenționat să evidențiem frecvența '
                 'diferitelor tipuri de durere în dependență de gen. Astfel, putem observa că '
                 'bărbații prezintă un randament de dureri mai înalt, iar la sexul opus, putem observa în plotul de '
                 'mai jos, diapazonul fiind cu mult mai mic. Meditând asupra acestei analize apare o întrebare simplă, '
                 'dar care poate aduce lumină în acest subiect: **de ce apar diferențe în modul în care bărbații și '
                 'femeile raportează și percep durerile?**')
        st.markdown("<hr style='border: 1px solid red;'>", unsafe_allow_html=True)
        st.altair_chart(female_bars, use_container_width=True)
        st.write('Hormonii sexuali au o influență semnificativă asupra variabilității legate de durere, având un '
                 'impact diferit asupra bărbaților și femeilor. Această influență nu este surprinzătoare, '
                 'deoarece hormonii sexuali și receptorii lor sunt distribuiți în zonele sistemelor nervoase '
                 'periferice și centrale care sunt implicate în transmiterea senzațiilor de durere. Capacitatea '
                 'organismului de a se adapta la durere poate varia, similar cu cum oamenii se obișnuiesc cu '
                 'temperaturile extreme după o perioadă de expunere constantă. Un aspect interesant este legat de '
                 'beta-endorfine, analgezice naturale eliberate de organism în timpul stresului sau al durerii. '
                 'Studiile arată că organismul femeilor eliberează în mod obișnuit mai puține beta-endorfine decât '
                 'cel al bărbaților, ceea ce poate influența modul în care acestea percep și gestionează durerea. '
                 'Beta-endorfinele au un rol important în reducerea senzațiilor de durere, fiind eliberate în fluxul '
                 'sanguin în timpul rănilor sau al altor situații dureroase.'
                 'Totuși, este important să se sublinieze că diferențele individuale și alte factori, '
                 'cum ar fi comportamentul și experiențele personale, pot juca, de asemenea, un rol semnificativ în '
                 'modul în care fiecare persoană resimte și raportează durerile cardiace.')
    with tab4:
        num_cases_by_sex = data['sex'].value_counts()
        num_cases_by_sex = num_cases_by_sex.rename({0: 'Femei', 1: 'Bărbați'})

        num_heart_attacks_by_sex = data[data['target'] == 1]['sex'].value_counts()
        num_heart_attacks_by_sex = num_heart_attacks_by_sex.rename({0: 'Femei', 1: 'Bărbați'})

        df = pd.DataFrame({
            'Sex': num_cases_by_sex.index.tolist() * 2,
            'Număr cazuri': num_cases_by_sex.tolist() + num_heart_attacks_by_sex.tolist(),
            'Tip cazuri': ['Total'] * 2 + ['Atac de cord'] * 2,
            'Base': [0, 0, 0, 0]
        })

        fig = px.bar(df, x='Sex', y='Număr cazuri', color='Tip cazuri', base='Base',
                     labels={'Sex': 'Sex', 'Număr cazuri': 'Număr cazuri de atac de cord'},
                     title='Numărul de cazuri de atac de cord în funcție de sex')

        st.write('Datele medicale arată că, în general, bărbații au o incidență mai mare de atacuri de cord decât '
                 'femeile. Factori precum diferențele biologice, hormonale și comportamentale pot influența acest '
                 'fenomen. Este esențial să subliniem că aceste concluzii se bazează pe tendințe generale și că fiecare'
                 'individ poate prezenta riscuri specifice în funcție de istoricul său medical, stilul de viață și alți'
                 'factori.')
        st.plotly_chart(fig, use_container_width=True)
        st.markdown("<hr style='border: 1px solid red;'>", unsafe_allow_html=True)
        st.write('Similar cu presupunirile precedente, vom utiliza un grafic de tip bar pentru a compara numărul de '
                 'cazuri de atacuri de cord între sexe. Astfel, putem observa că din 207 bărbați și 96 '
                 'femei, 114 bărbați și 24 de femei nu au suferit un atac de cord, pe când 93 de bărbați și 72 de '
                 'femei au suferit un atac de cord. Putem concluziona că doar 25% din femei nu au suferit atact de '
                 'cord, spre deosebire de bărbați unde raportul este 55%.')


if selected == 'Acasă':
    display_home_page()
elif selected == 'Predicția apariției atacului de cord':
    display_heart_disease_prediction()
elif selected == 'Analiza datelor':
    display_statistics_heart_disease()
