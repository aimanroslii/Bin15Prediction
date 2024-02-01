import streamlit as st
import pickle
import numpy as np

def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

dec_tree_reg_loaded = data["model"]
le_supplier = data["le_supplier"]
le_fabPlant = data["le_fabPlant"]
le_WaferCoatTool = data["le_WaferCoatTool"]
le_WaferLot = data["le_WaferLot"]

def show_predict_page():
    st.title("Bin 15 Percentage Prediction")
    st.write("""#### Please fill up the information to predict Bin15 Percentage""")

    supplier = (
        "Supp1",
        "Supp2"
    )

    fab = (
        "Fab 1",
        "Fab 2",
        "Fab 3"
    )

    waferCoatTool = (
        "WC 1",
        "WC 2",
        "WC 3"
    )

    waferCoatLot = (
        "1603111",
        "1603222",
        "1603333"
    )

    supplier = st.selectbox("Supplier", supplier)
    fab = st.selectbox("Fab Number", fab)
    waferCoatTool = st.selectbox("Wafer Coat Tool Number", waferCoatTool)
    waferCoatLot = st.selectbox("Wafer Coat Lot", waferCoatLot)
    waferCoatThickness = st.number_input("Enter Wafer Coat Thickness <Range from 50 - 150>", placeholder="Range from 50 - 150")

    #Add button to start prediction
    ok = st.button("Calculate Bin15 Percentage")
    if ok:
        X = np.array([[supplier, fab, waferCoatTool, waferCoatLot, waferCoatThickness]])
        X[:,0] = le_supplier.transform(X[:,0])
        X[:,1] = le_fabPlant.transform(X[:,1])
        X[:,2] = le_WaferCoatTool.transform(X[:,2])
        X[:,3] = le_WaferLot.transform(X[:,3])
        X = X.astype(float)

        bin15Prediction = dec_tree_reg_loaded.predict(X)

        if(waferCoatThickness < 50 or waferCoatThickness >150 ):
            st.subheader("Please Enter Valid Wafer Coat Thickness")
        else:
            st.subheader(f"The estimated Bin15 Percentage is {bin15Prediction[0]:.2f}")
