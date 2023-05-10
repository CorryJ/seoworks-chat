import openai
import streamlit as st
from streamlit_chat import message

# Setting page title and header
st.set_page_config(page_title="The SEO Works chat robot", page_icon="https://www.seoworks.co.uk/wp-content/themes/seoworks/assets/images/fav.png", layout="wide",    menu_items={
        'Get Help': 'https://www.seoworks.co.uk',
        'Report a bug': "mailto:james@seoworks.co.uk",
        'About': "Let us know what you think of the app?"
    })
st.markdown("<h2 style='text-align: left;'>The SEO Works chat robot</h2>", unsafe_allow_html=True)


option1 = st.selectbox(
    'Category ',
    ('Copy writing', 'SEO'))

if option1 == 'Copy writing':
    option2 = st.selectbox('Sub Category',('Blog writing', 'Content writing'))

if option1 == 'SEO':
    option2 = st.selectbox('Sub Category',('Keyword research', 'Local SEO', 'On page optimisation'))

if option2 == "Blog writing":
    option3 = st.selectbox('Select a template',('Generate blog post titles', 'Generate blog post descriptions', 'Generate complete blog post from topic'))

if option2 == "Content writing":
    option3 = st.selectbox('Select a template',('Content titles generator', 'Content rewriter (paste content)', 'Content brief generator', 
                                                'Content outline generator', 'Monthly content calendar','FAQ generator'))

if option2 == "Keyword research":
    option3 = st.selectbox('Select a template',('Keyword strategy', 'Get search intent for keyword'))

if option2 == 'Blog writing' or option2 == "Keyword research":
    language = st.selectbox('Select a language',('english', 'spanish', 'welsh'))

if option2 == 'Blog writing':
    tone = st.selectbox('Select tone',('informative', 'trustworthy', 'professional'))
    style = st.selectbox('Writing style',('academic', 'analytical', 'creative'))
    topic = st.text_input('Topic:', 'add',  type='default')

if option3 == 'Generate blog post titles' or option3 == 'Generate blog post descriptions':
    number_of_titles = st.text_input('Total titles (Add number):', '',  type='default')

if option3 == 'Keyword strategy':
    seed_keyword = st.text_input('Seed keyword:', '',  type='default')
    keyword_number_total= st.text_input('Total no of keywords:', '',  type='default')

if option3 == 'Generate complete blog post from topic':
    headings_number_total= st.text_input('Total no of headings', '',  type='default')

# Initialise session state variables
if 'generated' not in st.session_state:
    st.session_state['generated'] = []
if 'past' not in st.session_state:
    st.session_state['past'] = []
if 'messages' not in st.session_state:
    st.session_state['messages'] = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]
if 'model_name' not in st.session_state:
    st.session_state['model_name'] = []
if 'cost' not in st.session_state:
    st.session_state['cost'] = []
if 'total_tokens' not in st.session_state:
    st.session_state['total_tokens'] = []
if 'total_cost' not in st.session_state:
    st.session_state['total_cost'] = 0.0

# Sidebar - let user choose model, show total cost of current conversation, and let user clear the current conversation
st.sidebar.image("https://www.seoworks.co.uk/wp-content/themes/seoworks/assets/logos/Seoworks-Logo-Light.svg")
st.sidebar.title("Options and info:")
model_name = st.sidebar.radio("Choose a model:", ("GPT-3.5", "GPT-4 (Not released yet)"))
counter_placeholder = st.sidebar.empty()
counter_placeholder.write(f"Total cost of this conversation: ${st.session_state['total_cost']:.5f}")
api_key = st.sidebar.text_input('API key:', 'Add your api key',  type='password')
temperature_setting = st.sidebar.slider("Set the temperature of the response (Higher = more random, lower = more focussed):",min_value=0.0, max_value=1.0, step=0.1)
clear_button = st.sidebar.button("Clear Conversation", key="clear")

# Set org ID and API key
# openai.organization = "org-UhxonLlzrkpFpzI10Q4q9aAE"
openai.api_key = api_key

# Map model names to OpenAI model IDs
if model_name == "GPT-3.5":
    model = "gpt-3.5-turbo"
else:
    model = "gpt-4"

# reset everything
if clear_button:
    st.session_state['generated'] = []
    st.session_state['past'] = []
    st.session_state['messages'] = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]
    st.session_state['number_tokens'] = []
    st.session_state['model_name'] = []
    st.session_state['cost'] = []
    st.session_state['total_cost'] = 0.0
    st.session_state['total_tokens'] = []
    counter_placeholder.write(f"Total cost of this conversation: ${st.session_state['total_cost']:.5f}")


# generate a response
def generate_response(prompt):
    st.session_state['messages'].append({"role": "user", "content": prompt})

    completion = openai.ChatCompletion.create(
        model=model,
        temperature= temperature_setting,
        messages=st.session_state['messages'],
        
    )
    response = completion.choices[0].message.content
    st.session_state['messages'].append({"role": "assistant", "content": response})

    # print(st.session_state['messages'])
    total_tokens = completion.usage.total_tokens
    prompt_tokens = completion.usage.prompt_tokens
    completion_tokens = completion.usage.completion_tokens
    return response, total_tokens, prompt_tokens, completion_tokens


# container for chat history
response_container = st.container()
# container for text box
container = st.container()

if option3 == "Generate blog post titles":

    with container:
        with st.form(key='my_form', clear_on_submit=True):
            user_input = st.text_area("Add your prompt:", key='input', value="Please ignore all previous instructions. You are an expert copywriter \
who writes catchy titles for blog posts. You have a " +tone + " tone of voice. "+"You have a "+ style +" writing style. "+"Write "+ number_of_titles \
+ " catchy blog post titles with a hook for the topic " + "'"+ topic + "'" + ". The titles should be written in the " + language + ". The titles should be less than 75 characters. " \
+ "The titles should include the words from the topic " +"'" + topic + "'"+ ". Do not use single quotes, double quotes or any other enclosing characters. Do not self reference. Do not explain what you are doing.",height=100)

            submit_button = st.form_submit_button(label='Generate response')        
            
        if submit_button and user_input:
            output, total_tokens, prompt_tokens, completion_tokens = generate_response(user_input)
            st.session_state['past'].append(user_input)
            st.session_state['generated'].append(output)
            st.session_state['model_name'].append(model_name)
            st.session_state['total_tokens'].append(total_tokens)

        # from https://openai.com/pricing#language-models
            if model_name == "GPT-3.5":
                cost = total_tokens * 0.002 / 1000
            else:
                cost = (prompt_tokens * 0.03 + completion_tokens * 0.06) / 1000

            st.session_state['cost'].append(cost)
            st.session_state['total_cost'] += cost

if option3 == "Generate blog post descriptions":

    with container:
        with st.form(key='my_form_1', clear_on_submit=True):
            user_input = st.text_area("Add your prompt:", key='input', value="Please ignore all previous instructions. You are an expert copywriter \
who writes catchy titles for blog posts. You have a " +tone + " tone of voice. "+"You have a "+ style +" writing style. " +"Write "+ number_of_titles \
+ " catchy blog post descriptions with a hook for the blog post titled " + "'"+ topic + "'" + ". The titles should be written in the " + language + ". The titles should be less than 160 characters. " \
+ "The descriptions should include the words from the topic " +"'" + topic + "'"+ ". Do not use single quotes, double quotes or any other enclosing characters. Do not self reference. Do not explain what you are doing.",height=100)

            submit_button = st.form_submit_button(label='Generate response')        
            
        if submit_button and user_input:
            output, total_tokens, prompt_tokens, completion_tokens = generate_response(user_input)
            st.session_state['past'].append(user_input)
            st.session_state['generated'].append(output)
            st.session_state['model_name'].append(model_name)
            st.session_state['total_tokens'].append(total_tokens)

        # from https://openai.com/pricing#language-models
            if model_name == "GPT-3.5":
                cost = total_tokens * 0.002 / 1000
            else:
                cost = (prompt_tokens * 0.03 + completion_tokens * 0.06) / 1000

            st.session_state['cost'].append(cost)
            st.session_state['total_cost'] += cost

if option3 == "Keyword strategy":

    with container:
        with st.form(key='my_form_2', clear_on_submit=True):
            user_input = st.text_area("Add your prompt:", key='input', value="Please ignore all previous instructions. Please respond only in the" + language \
+" language." + " You are a market research expert that speaks and writes fluent english. You are an expert in keyword research and can develop a full SEO content plan \
in fluent english. " + "'"+seed_keyword + "'" +" is the target keyword for which you need to create a Keyword Strategy & Content Plan. Create a markdown table with a list of " + keyword_number_total +" closely \
related keywords for an SEO strategy plan for the main " + "'"+seed_keyword + "'" + ". Cluster the keywords according to the top 10 super categories and name the super category in the \
first column as 'Category'. There should be a maximum of 6 keywords in a super category. The second column should be called 'Keyword' and contain the suggested keyword. \
The third column will be called 'search Intent' and will show the search intent of the suggested keyword from the following list of intents (commercial, transactional, \
navigational, informational, local or investigational). The fourth column will be called 'Title' and will be catchy and click-bait title to use for an article or blog post\
about that keyword. The fifth column will be called Description: and will be a catchy meta description with a maximum length of 160 words. The meta description should ideally \
have a call to action. Do not use single quotes, double quotes or any other enclosing characters in any of the columns you fill in. Do not self reference. Do not explain what \
you are doing. Just return your suggestions in the table.", height=400)

            submit_button = st.form_submit_button(label='Generate response')        
            
        if submit_button and user_input:
            output, total_tokens, prompt_tokens, completion_tokens = generate_response(user_input)
            st.session_state['past'].append(user_input)
            st.session_state['generated'].append(output)
            st.session_state['model_name'].append(model_name)
            st.session_state['total_tokens'].append(total_tokens)

        # from https://openai.com/pricing#language-models
            if model_name == "GPT-3.5":
                cost = total_tokens * 0.002 / 1000
            else:
                cost = (prompt_tokens * 0.03 + completion_tokens * 0.06) / 1000

            st.session_state['cost'].append(cost)
            st.session_state['total_cost'] += cost

if option3 == "Generate complete blog post from topic":

    with container:
        with st.form(key='my_form_3', clear_on_submit=True):
            user_input = st.text_area("Add your prompt:", key='input', value="Please ignore all previous instructions. You are an expert \
copywriter who writes detailed and thoughtful blog articles. You have a " + tone + " tone of voice. You You have a " + style+" writing style. \
I will give you a topic for an article and I want you to create an outline for the topic with a minimum of " + headings_number_total +" headings and subheadings.\
I then want you to expand in the "+ language+ " language on each of the individual subheadings in the outline to create a complete article from it. Please intersperse \
short and long sentences. Utilize uncommon terminology to enhance the originality of the content. Please format the content in a professional format. Do not self \
reference. Do not explain what you are doing. Send me the outline and then immediately start writing the complete article. The blog article topic is - " + "'"+ topic +"'. ", height=250)

            submit_button = st.form_submit_button(label='Generate response')        
            
        if submit_button and user_input:
            output, total_tokens, prompt_tokens, completion_tokens = generate_response(user_input)
            st.session_state['past'].append(user_input)
            st.session_state['generated'].append(output)
            st.session_state['model_name'].append(model_name)
            st.session_state['total_tokens'].append(total_tokens)

        # from https://openai.com/pricing#language-models
            if model_name == "GPT-3.5":
                cost = total_tokens * 0.002 / 1000
            else:
                cost = (prompt_tokens * 0.03 + completion_tokens * 0.06) / 1000

            st.session_state['cost'].append(cost)
            st.session_state['total_cost'] += cost

else:

    with container:
        with st.form(key='my_form_3', clear_on_submit=True):
       # user_input = st.text_area("Add your prompt:", key='input', height=100)
            user_input = st.text_area("Add your prompt:", value="Write your own prompt ",height=100)
            submit_button = st.form_submit_button(label='Generate response')
    

        if submit_button and user_input:
            output, total_tokens, prompt_tokens, completion_tokens = generate_response(user_input)
            st.session_state['past'].append(user_input)
            st.session_state['generated'].append(output)
            st.session_state['model_name'].append(model_name)
            st.session_state['total_tokens'].append(total_tokens)

        # from https://openai.com/pricing#language-models
            if model_name == "GPT-3.5":
                cost = total_tokens * 0.002 / 1000
            else:
                cost = (prompt_tokens * 0.03 + completion_tokens * 0.06) / 1000

            st.session_state['cost'].append(cost)
            st.session_state['total_cost'] += cost

if st.session_state['generated']:
    with response_container:
        for i in range(len(st.session_state['generated'])):
            message(st.session_state["past"][i], is_user=True, key=str(i) + '_user')
            message(st.session_state["generated"][i], key=str(i))
            st.write(
                f"Model used: {st.session_state['model_name'][i]}; Number of tokens: {st.session_state['total_tokens'][i]}; Cost: ${st.session_state['cost'][i]:.5f}")
            counter_placeholder.write(f"Total cost of this conversation: ${st.session_state['total_cost']:.5f}")


