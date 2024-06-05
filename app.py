import streamlit as st 
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers


def getLLamaresponse(input_text , no_words , blog_style ):
    #  we are calling llama model 
    llm = CTransformers(model = 'models\llama-2-7b-chat.ggmlv3.q5_K_S.bin' ,
                        model_type = 'llama',
                        config = {'max_new_tokens' : 256 ,
                                  'temperature' : 0.3 } )
    
    # we are calling template
    template = """
    write a blog about {input_text} for {blog_style} in {no_words} words
    
    """
    
    prompt = PromptTemplate(input_variables = ["input_text" , "no_words" , "blog_style" ] ,
                            template = template )
    
    # generating response from the LLama model 
    response = llm( prompt.format(input_text = input_text , no_words = no_words , blog_style = blog_style))
    print( response )
    
    return response 
    

# function to get response from the llama 2 model

st.set_page_config(
    page_title = "Generate  blogs " ,
    page_icon = '🤖',
    layout = 'centered',
    initial_sidebar_state = 'collapsed'
)

st.header(" Generate blogs ")
# this is for blog topic
input_text = st.text_input("Enter the blog topic ")
# this are for number of words and fro whom we are writing
col1 , col2 = st.columns([5 , 5 ])
# here we are setting width 5 , 5 
with col1:
    no_words = st.text_input("number of words")
with col2 :
    blog_style = st.selectbox('Writing the blog for ' ,
                              ('data scientist' , 'student' , 'researchers'
                               ) , index = 1)
    
submit = st.button("Generate")

# if clicked submit 

if submit:
    st.write( getLLamaresponse(input_text , no_words , blog_style))
    