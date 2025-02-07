#!python3.13
import streamlit as st

st.write("Hello, World")
st.title("Title")
st.header("Header")
st.subheader("Subtitle")

st.markdown("this is _Markdown_")

st.caption("some text")

st.code("""def say(name):
    return f"hello, {name}"
""", language="python")

st.button("Press")