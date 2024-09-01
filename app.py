import streamlit as st
import datetime

from PIL import Image 
st.title('Hello All....')

st.write("hi I am streamlit by Amitava")

st.header("This is Header")
st.subheader("This is Sub-Header")

st.markdown("### This is Markdown")

st.success("This is success")

st.info("This is INFO...")

st.warning("This is Warning")

st.error("This is error")

q=ZeroDivisionError("Try 2 divide by 0")
st.exception(q)


st.write(range(10))


img=Image.open('abc.png')
st.image(img,width=300)

if st.checkbox("Show/Hide"):
    st.text("Showing the wizard....")


r=st.radio("Select Gender",('Male','Female'))

if r=='Male':
    st.success('You are a Male')
else:
    st.success('U are a Female!!!')


hobby=st.selectbox("Hobbies",['Cooking','Gardening','Travelling','Watching Movie'])
st.write('your hobbey is ',hobby)

hobby=st.multiselect("Hobbies",['Cooking','Gardening','Travelling','Watching Movie'])
st.write('your hobbies are ',len(hobby),'hobby')



st.button('Click me for no reason')
if st.button('About'):
    st.text('welcome to streamlit....')

n=st.text_input('enter name')

st.write('name is ',n.title())

t1=st.number_input("enter 1st no")
t2=st.number_input("enter 2nd no")
sum=t1+t2
st.write('sum is ',sum)

age=st.slider("enter age",min_value=0,max_value=100,value=10)
st.write('your age is ',age)

date=st.date_input("Whats your Birthday?",datetime.date(2024,1,1),datetime.date(1990,1,1),datetime.datetime.now())
st.write("your bday is ",date)

c1,c2=st.columns(2)
with c1:
    st.write("Column 1 content here")
with c2:
    st.write("Column 2 content here")

with st.expander("see details"):
    st.write("I am hidden")


options=st.sidebar.selectbox('Choose option',['A','B','C'])
st.write(f'You selected {options}')

st.markdown(
    '''
    <style>
    .mno{
    font-size:30px;
    }
    </style>
    ''',unsafe_allow_html=True)

st.markdown("<p class='mno'>I AM AMITAVA</p>",unsafe_allow_html=True)


if 'count' not in st.session_state:
    st.session_state['count']=0

if st.button('Click me!!!'):
    st.session_state['count']+=1

st.write('count is ',st.session_state['count'])







