import pickle
import streamlit as st
# loading the trained model
pickle_in = open('AI_DrugClassifier.pkl', 'rb') 
classifier = pickle.load(pickle_in)
@st.cache()
# defining the function which will make the prediction using the data which the user inputs
def self_prediction(Age, Sex, BP, Cholesterol, Na_to_K):
    # Pre-processing user input
    if Sex == "MALE":
        Sex = 0
    else:
        Sex = 1
    if BP == "LOW":
        BP = 0
    elif BP == "NORMAL":
         BP = 1
    else :
        BP = 2
    if Cholesterol == "NORMAL":
        Cholesterol = 0
    else:
        Cholesterol = 1
   
    # Making predictions
    self_prediction = classifier.predict([[Age, Sex, BP, Cholesterol, Na_to_K]])
    
    if self_prediction == 0:
        pred = 'drugA'
    elif self_prediction == 1:
        pred = 'drugB'
    elif self_prediction == 2:
        pred = 'drugC'
    elif self_prediction == 3:
        pred = 'drugX'
    else :
        pred = 'DrugY'
    return pred
# this is the main function in which we define our webpage
def main():
    # front end elements of the web page
        html_temp = """
        <div style ="background-color:yellow;padding:13px">
        <h1 style ="color:black;text-align:center;">Prediksi Narkoba (PN App)</h1>
        </div>
        """
    # display the front end aspect
        st.markdown(html_temp, unsafe_allow_html = True)
    # following lines create boxes in which user can enter data required to make prediction
        Age = st.number_input("Masukan Umur",min_value=15, max_value=74, value=15, step=1)
        Sex = st.selectbox('Gender',("MALE","FEMALE"))
        BP = st.selectbox('BP Status',("LOW","NORMAL","HIGH"))
        Cholesterol = st.selectbox('Cholesterol',("NORMAL","HIGH"))
        Na_to_K = st.number_input("Masukan NatoK",min_value=6, max_value=38, value=6, step=1)
        result =""
    # when 'Predict' is clicked, make the prediction and store it
        if st.button("Predict"):
            result = self_prediction(Age, Sex, BP, Cholesterol, Na_to_K)
            st.success('Jenis Narkoba {}'.format(result))
            print(Na_to_K)
if __name__=='__main__':
    main()
