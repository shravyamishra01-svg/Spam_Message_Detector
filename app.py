import streamlit as st

from src.predictor import predict_message
from src.utils import format_prediction, get_prediction_message
from src.history import add_prediction, get_history, clear_history
from src.validation import validate_message



st.set_page_config(
    page_title="Spam Message Detector",
    page_icon="📩",
    layout="centered"
)


st.title("📩 Spam Message Detector")

st.write(
    "Enter a message below and the system will predict "
    "whether it is Spam or Not Spam."
)


message = st.text_area(
    "Enter your message:",
    height=150,
    placeholder="Type or paste your message here..."
)


if st.button("Check Message"):

    valid, validation_message = validate_message(message)

    if not valid:
        st.warning(validation_message)

    else:
        try:
            prediction, confidence = predict_message(message)

            add_prediction(
                message,
                prediction,
                confidence
            )

            result = format_prediction(prediction)

            if prediction == "spam":
                st.error(f"🚨 {result}")
            else:
                st.success(f"✅ {result}")

            st.write(
                f"Confidence: **{confidence:.2f}%**"
            )

            st.info(
                get_prediction_message(prediction)
            )

        except ValueError as error:
            st.warning(str(error))

            result = format_prediction(prediction)

            if prediction == "spam":
                st.error(f"🚨 {result}")
            else:
                st.success(f"✅ {result}")

            st.write(
                f"Confidence: **{confidence:.2f}%**"
            )

            st.info(
                get_prediction_message(prediction)
            )

        except ValueError as error:
            st.warning(str(error))


st.divider()

st.subheader("📋 Prediction History")


history = get_history()


if history:

    for item in reversed(history):

        st.write(
            f"**Time:** {item['time']}"
        )

        st.write(
            f"**Message:** {item['message']}"
        )

        st.write(
            f"**Prediction:** {format_prediction(item['prediction'])}"
        )

        st.write(
            f"**Confidence:** {item['confidence']:.2f}%"
        )

        st.divider()

    if st.button("Clear History"):
        clear_history()
        st.rerun()

else:

    st.info("No predictions have been made yet.")