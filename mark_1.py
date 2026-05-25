import streamlit as st
from api_calling import giving_hint, solve_with_code, bug_finder, ask_me_anything
from PIL import Image

st.title("AI Code Debugger App")
st.text("Upload upto 5 photos or Code or Problem Link")
st.divider()


# for code
with st.container(border=True):
    code = st.text_area("sumbit you code")
    code_pressed = st.button("Debug Code", type="primary")
    if code:
        if code_pressed:
            with st.spinner("Processing..."):
                st.markdown(bug_finder(code))

            pressed = st.button("Click to clean the page", type="primary")
            if pressed:
                st.session_state.clear()
                st.rerun()


with st.sidebar:
    st.header("Upload at max 5 photos")
    images = st.file_uploader(
        "Upload", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

    # for images
    if images:
        pil_images = []
        for img in images:
            pil_images.append(Image.open(img))

        if len(images) > 5:
            st.error("You can upload at max 5 images")

        else:
            col = st.columns(len(images))

            for i, img in enumerate(images):
                with col[i]:
                    st.image(img)

    option = st.selectbox("Select an option", [
                          "Hints", "Solution with code"], index=None, placeholder="select an option")
    pressed = st.button("Press to initiate AI", type="primary")

if pressed:
    if not images:
        st.error("You must upload a image")
    elif not option:
        st.error("You must select an option")

    elif option == "Hints" and images:
        with st.container(border=True):
            with st.spinner("Processing"):
                st.markdown(giving_hint(pil_images))
    elif option == "Solution with code" and images:
        with st.spinner("Processiong..."):
            st.markdown(solve_with_code(pil_images))


with st.container(border=True):
    ask_input = st.text_area("Ask me anything", key="ask_area")
    if st.button("Get Answer", type="primary", key="ask_btn"):
        if ask_input:
            with st.spinner("Processing..."):
                st.markdown(ask_me_anything(ask_input))
        else:
            st.warning("Please ask a question.")



