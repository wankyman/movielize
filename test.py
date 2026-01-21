import streamlit



def writer():
    f = streamlit.session_state.area
    streamlit.write(f"you typed {f}")

k = streamlit.text_area("Input Box",placeholder="Enter your question",key="area",on_change=writer)
