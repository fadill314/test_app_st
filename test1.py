import streamlit as st

st.title("EMC2 / Cloud Module")
st.header("App pour test des AI app")
#st.video("https://youtu.be/YfZ0zk5Zzcw")

st.sidebar.image("https://seeklogo.com/images/E/ecole-hassania-des-travaux-publics-ehtp-logo-3D5770F217-seeklogo.com.png")
st.sidebar.header("Master Cloud Computing")
choix=st.sidebar.selectbox('Select app type :', ['---choose application ---', 'Image Analysis', 'OCR', 'Thumbnail Image', 'Face Analysis'])

if choix == 'Image Analysis':
  image_file=st.file_uploader('load an image', type= ['png', 'jpg', 'jpeg'])
