import streamlit as st
import qrcode
from datetime import datetime


print("QR Code Generator Program")
data = st.text_input("Please enter your QR Code data : ", key="input")
if st.button("Generate QR Code"):
    if data:
        img = qrcode.make(f'{data}')
        img_path = f"QRcodeimg/{datetime.today().strftime('%Y-%m-%d-%H-%M-%S')}.png"
        img.save(img_path)
        st.image(img_path, width=300)
        st.success("QR Code image saved")

        # clear data

        # data = ""

        # st.text_input("Please input your QR Code data : ", value=data)

    else:
        st.warning("Please enter your data before generate QR Code")
