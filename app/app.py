"""Streamlit web app"""

import numpy as np
import streamlit as st
import cv2
from fer_pytorch.fer import FER
import torch

st.set_option("deprecation.showfileUploaderEncoding", False)


@st.cache
def cached_fer():
    fer = FER()
    fer.get_pretrained_model("resnet34")
    return fer


def main():
    fer = cached_fer()

    st.title("Recognize emotions")

    uploaded_file = st.file_uploader("Choose an image...", type="jpg")

    if uploaded_file is not None:
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        image = cv2.imdecode(file_bytes, 1)

        st.image(image, caption="Before", use_column_width=True, channels="BGR")
        st.write("")
        st.write("Detecting faces...")

        with torch.no_grad():
            output = fer.predict_image(image, show_top=True)
        if not output:
            st.write("No faces detected")
        else:
            output_dict = output[0]
            box_coordinates = output_dict["box"]
            x, y, w, h = (
                box_coordinates[0],
                box_coordinates[1],
                box_coordinates[2],
                box_coordinates[3],
            )

            top_emotion = next(iter(output_dict["top_emotion"]))
            prob = round(float(next(iter(output_dict["top_emotion"].values()))), 2)

            cv2.rectangle(image, (int(x), int(y)), (int(w), int(h)), (255, 0, 0), 2)
            cv2.putText(
                image,
                f"{top_emotion}: {prob:.2f}",
                (int(x), int(y - 5)),
                cv2.FONT_HERSHEY_SIMPLEX,
                1.0,
                (0, 0, 255.0),
                2,
            )

            st.image(image, caption="After", use_column_width=True, channels="BGR")


if __name__ == "__main__":
    main()
