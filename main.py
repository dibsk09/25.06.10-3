import streamlit as st
st.title("첫 app")
st.write("hello")
name=st.text_input("이름 입력")
if name:
  if name=="연우":
    st.success("반갑습니다 ,name,님")
  else:
    st.warning("누구니????")

  
