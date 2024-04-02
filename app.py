import openai
import streamlit as st
from streamlit_chat import message

# Setting page title and header
st.set_page_config(page_title="The SEO Works OptiBot", page_icon="https://www.seoworks.co.uk/wp-content/themes/seoworks/assets/images/fav.png", layout="wide",    menu_items={
        'Get Help': 'https://www.seoworks.co.uk',
        'Report a bug': "mailto:james@seoworks.co.uk",
        'About': "Let us know what you think of the app?"
    })
st.markdown("<h2 style='text-align: left;'>The SEO Works OptiBot</h2>", unsafe_allow_html=True)

# Help tips

use_prompts_help = "If you want to use the templates select yes, otherwise select no"
category_help = "Select which category of prompts you would like to use"
help_generic = "Add something useful"

user_prompts=st.radio("Use prompts",['Yes', 'No'],help= use_prompts_help)

tone_options = ['Default', 'Authoritative', 'Caring', 'Casual', 'Cheerful', 'Coarse', 'Conservative', 'Conversational', 'Creative', 'Dry', 'Edgy', 
'Enthusiastic', 'Expository', 'Formal', 'Frank', 'Friendly', 'Fun', 'Funny', 'Humorous', 'Informative', 'Irreverent', 'Journalistic', 'Matter of fact', 
'Nostalgic', 'Objective', 'Passionate', 'Poetic', 'Playful', 'Professional', 'Provocative', 'Quirky', 'Respectful', 'Romantic', 'Sarcastic', 'Serious', 
'Smart', 'Snarky', 'Subjective', 'Sympathetic', 'Trendy', 'Trustworthy', 'Unapologetic', 'Upbeat', 'Witty']

style_options = ['Default', 'Academic', 'Analytical', 'Argumentative', 'Conversational', 'Creative', 'Critical', 'Descriptive', 'Epigrammatic', 'Epistolary', 
                 'Expository', 'Informative', 'Instructive', 'Journalistic', 'Metaphorical', 'Narrative', 'Persuasive', 'Poetic', 'Satirical', 'Technical']

if user_prompts == "Yes":

    option1 = st.selectbox(
        'Category ',
        ('Copy writing', 'SEO', 'Marketing'), help= category_help)

    if option1 == 'Copy writing':
        option2 = st.selectbox('Sub Category',('Blog writing', 'Content writing'), help=help_generic)

    if option1 == 'SEO':
        option2 = st.selectbox('Sub Category',('Keyword research', 'Ecommerce SEO', 'On page optimisation'),help=help_generic)

    if option1 == 'Marketing':
        # option2 = st.selectbox('Sub Category',('Default','Miscellaneous'))
        option2 = 'Miscellaneous'

    if option2 == "Blog writing":
        option3 = st.selectbox('Select a template',('Generate blog post titles', 'Generate blog post descriptions', 
                                                    'Generate blog post outline','Generate complete blog post from outline', 
                                                    'Generate complete blog post from topic','Generate introduction using framework','Generate paragraph of text'),help=help_generic)

    if option2 == "Content writing":
        option3 = st.selectbox('Select a template',('Content titles generator', 'Content rewriter (paste content)', 'Content brief generator', 
                                                    'Content outline generator', 'Monthly content calendar','FAQ generator'),help=help_generic)

    if option2 == "Keyword research":
        option3 = st.selectbox('Select a template',('Keyword strategy', 'Get search intent for keywords', 'Related keywords generator',
                                                    'Long tail keywords generator', 'Keyword categorisation'),help=help_generic)
        
    if option2 == "Ecommerce SEO":
        option3 = st.selectbox('Select a template',('Product description generator', 'Category description generator', 'Landing page generator', 'Bulk titles and descriptions'),help=help_generic)

    if option2 == "On page optimisation":
        option3 = st.selectbox('Select a template',('Meta title and description generator', 'Create silo structure'),help=help_generic)

    if option2 == "Miscellaneous":
        option3 = st.selectbox('Select a template',('Create buyer persona','Market research', 'Subreddit research'),help=help_generic)

    if option2 == 'Blog writing' or option2 == "Keyword research" or option2 == "Get search intent for keywords":
        language = st.selectbox('Select a language',('english', 'spanish', 'welsh'),help=help_generic)

    if option2 == 'Blog writing':
        tone = st.selectbox('Select tone',(tone_options),help=help_generic)
        style = st.selectbox('Writing style',(style_options),help=help_generic)
        topic = st.text_input('Topic:',  type='default', placeholder='add your topic or title',help=help_generic)

    if option2 == 'Content writing':
        content_writing_tone = st.selectbox('Select tone',(tone_options),help=help_generic)
        content_writing_style = st.selectbox('Writing style',(style_options),help=help_generic)
        content_writing_topic = st.text_input('Topic:',  type='default', placeholder='add your topic or title',help=help_generic)


    if option2 == 'Ecommerce SEO':
        Ecommerce_writing_tone = st.selectbox('Select tone',(tone_options),help=help_generic)
        Ecommerce_writing_style = st.selectbox('Writing style',(style_options),help=help_generic)
        Ecommerce_writing_topic = st.text_input('Topic:',  type='default', placeholder='add your topic or title',help=help_generic)


    if option3 == 'Generate blog post titles' or option3 == 'Generate blog post descriptions' or option3 == 'Generate blog post outline':
        number_of_titles = st.text_input('Total titles (Add number):', '',  type='default', help=help_generic)

    if option3 == 'Keyword strategy':
        seed_keyword = st.text_input('Seed keyword:', '',  type='default', help=help_generic)
        keyword_number_total= st.text_input('Total no of keywords:', '',  type='default', help=help_generic)

    if option3 == 'Generate complete blog post from topic':
        headings_number_total= st.text_input('Total no of headings', '',  type='default', help=help_generic)

    if option3 == 'Generate complete blog post from outline':
        blog_post_outline = st.text_area('Blog post outline',  value='', placeholder='add your detailed outline', height=200, help=help_generic)

    if option3 == 'Generate introduction using framework':
        # framework_topic = st.text_input('Topic:', type='default', placeholder='Add topic')
        framework_total_words = st.text_input('Number of keywords:', type='default', placeholder='Add number of words (must be a number)', help=help_generic)
        framework_keywords = st.text_area('Keywords',  value='', placeholder='add your keywords', help=help_generic, height=200)
        framework = st.selectbox('Framework',('AIDA (Attention, Interest Desire Attention)','PAS (Problem Agitate Solution)', 'BAB (Before After Bridge)', 'FAB (Features Advantages Benefits)'), help=help_generic)
        
    if option3 == 'Generate paragraph of text':
        # framework_topic = st.text_input('Topic:', type='default', placeholder='Add topic')
        paragraph_total_words = st.text_input('Number of words:', type='default', placeholder='Add number of words (must be a number)', help=help_generic)
        paragraph_keywords = st.text_area('Keywords',  value='', placeholder='add your keywords',help=help_generic, height=200)
        

    if option3 == 'Content titles generator':
        # framework_topic = st.text_input('Topic:', type='default', placeholder='Add topic')
        content_titles_total_titles = st.text_input('Total titles:', type='default', placeholder='Add number of titles (must be a number)', help=help_generic)

    if option3 == 'Content rewriter (paste content)':
        rewrite_content = st.text_area('Content',  value='', placeholder='Add your content', height=250, help=help_generic)

    if option3 == 'Content brief generator':
        content_brief_main_keyword = st.text_input('Main keyword:', type='default', placeholder='Main keyword', help=help_generic)
        content_brief_total_keywords = st.text_input('Total keywords:', type='default', placeholder='Add number of keywords', help=help_generic)
        content_brief_total_questions = st.text_input('Total questions:', type='default', placeholder='Add number of questions', help=help_generic)

    if option3 == 'Monthly content calendar':
        content_calendar_artitles_per_week = st.text_input('Articles per week:', type='default', placeholder='1', help=help_generic)
        content_brief_number_of_months = st.text_input('Number of months:', type='default', placeholder='3', help=help_generic)

    if option3 == 'FAQ generator':
        faq_number = st.text_input('Number of FAQs:', type='default', placeholder='5', help=help_generic)

    if option3 == 'Get search intent for keywords':
        search_intent_keywords = st.text_area('Your keywords:', value='' , height=200, help=help_generic)

    if option3 == 'Related keywords generator' or option3=='Long tail keywords generator':
        related_keywords_generator_seed = st.text_input('Seed keyword:', type = 'default', placeholder='Seed keyword', help=help_generic)
        related_keywords_total = st.text_input('Total keywords:', type = 'default', placeholder='Add number', help=help_generic)

    if option3 == 'Keyword categorisation' or option3=='Long tail keywords generator':
        keyword_categorisation_list = st.text_area('List of keywords:', value='' , height=150, help=help_generic)
        keyword_categorisation_search_volumn = st.text_area('List of keyword volumes:', value='' , height=150, help=help_generic)
        keyword_categorisation_difficulty = st.text_area('List of associated keyword difficulties:', value='' , height=150, help=help_generic)

    if option3 == 'Product description generator':
        product_description = st.text_area('Product description:', value='' , height=200, help=help_generic)
        product_description_total_words = st.text_input('Total words:', type = 'default', placeholder='Add number', help=help_generic)
        product_description_total_headings = st.text_input('Total headings:', type = 'default', placeholder='Add number', help=help_generic)
        product_description_total_keywords = st.text_input('Total total keywords:', type = 'default', placeholder='Add number', help=help_generic)

    if option3 == 'Category description generator':
        category = st.text_input('Category:', type = 'default', placeholder='Category', help=help_generic)
        category_total_words = st.text_input('Total words:', type = 'default', placeholder='Add number', help=help_generic)

    if option3 == 'Landing page generator':
        landing_page_generator_product = st.text_input('Product:', type = 'default', placeholder='Product', help=help_generic)
        landing_page_total_word = st.text_input('Total words:', type = 'default', placeholder='Add number', help=help_generic)
        landing_page_call_to_action = st.text_input('Call to action:', type = 'default', placeholder='Click to purchase product', help=help_generic)

    if option3 == 'Bulk titles and descriptions':
        bulk_titles_and_descriptions_products = st.text_area('Products:', value='' , height=250, help=help_generic)

    if option3 == 'Meta title and description generator':
        meta_writing_tone = st.selectbox('Select tone',(tone_options))
        meta__writing_style = st.selectbox('Writing style',(style_options))
        meta_titles_and_descriptions_keywords = st.text_area('Your keywords:', value='' , height=250, help=help_generic)

    if option3 == 'Create silo structure':
        silo_keywords = st.text_area('Your keyword:', value='' , height=150, placeholder='Add ONE keyword', help=help_generic)

    if option3 == 'Create buyer persona':
        persona_writing_tone = st.selectbox('Select tone',(tone_options), help=help_generic)
        persona__writing_style = st.selectbox('Writing style',(style_options), help=help_generic)
        persona_sell_question = st.text_input('What do you sell:', value='' , type = 'default', placeholder= 'What do you sell', help=help_generic)
        persona_location_question = st.text_input('Where do you sell:', value='' , type = 'default', placeholder= 'Where do you sell', help=help_generic)

    if option3 == 'Market research':
        market_research_topic = st.text_input('What is the topic:', value='' , type = 'default', placeholder= 'Add topic area', help=help_generic)

    if option3 == 'Subreddit research':
        subreddits_research_topic = st.text_input('What is the topic:', value='' , type = 'default', placeholder= 'Add topic area', help=help_generic)

if user_prompts == "No":
    option3 = "Manual"

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
# api_key = st.sidebar.text_input('API key:', 'Add your api key',  type='password') # **commented out for ease of development**
temperature_setting = st.sidebar.slider("Set the temperature of the response (Higher = more random, lower = more focussed):",min_value=0.0, max_value=1.0, step=0.1)
clear_button = st.sidebar.button("Clear Conversation", key="clear")


# openai.api_key = api_key

# openai.api_key = st.secrets.api_key
openai.api_key = st.secrets.api_key

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

if option3 == "Manual":

    with container:
        with st.form(key='my_form', clear_on_submit=False):
            user_input = st.text_area("Add your prompt:", key='input', value="",height=150, placeholder='Write away')

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

if option3 == "Generate blog post titles":

    with container:
        with st.form(key='my_form', clear_on_submit=True):
            user_input = st.text_area("Add your prompt:", key='input', value="Please ignore all previous instructions. You are an expert copywriter \
who writes catchy titles for blog posts. You have a " +tone + " tone of voice. "+"You have a "+ style +" writing style. "+"Write "+ number_of_titles \
+ " catchy blog post titles with a hook for the topic " + "'"+ topic + "'" + ". The titles should be written in the " + language + ". The titles should be less than 75 characters. " \
+ "The titles should include the words from the topic " +"'" + topic + "'"+ ". Do not use single quotes, double quotes or any other enclosing characters. Do not self reference. Do not explain what you are doing.",height=150)

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

if option3 == "Keyword categorisation":

    with container:
        with st.form(key='my_form_2', clear_on_submit=True):
            user_input = st.text_area("Add your prompt:", key='input', value="Please ignore all previous instructions. Filter the below list of keywords \
into categories, target persona, search intent, search volume and add information to a six-column table: List of keywords – " + "["+ keyword_categorisation_list + "]" + ", Keyword \
Search Volume ["+keyword_categorisation_search_volumn+"]"+" and Keyword Difficulties ["+keyword_categorisation_difficulty+"]. Do not self reference. Do not explain what \
you are doing.", height=200)

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


if option3 == "Generate blog post outline":

    with container:
        with st.form(key='my_form_4', clear_on_submit=True):
            user_input = st.text_area("Add your prompt:", key='input', value="Please ignore all previous instructions. You are an expert copywriter who creates content outlines. You have a "+ tone +" tone of voice. You have a "+ style + " Analytical writing style. \
Create a long form content outline in the " + language + " language for the blog post titled " +"'"+ topic + "'"+".  The content outline should include a minimum of " + number_of_titles +" headings and subheadings. The outline should \
be extensive and it should cover the entire topic. Create detailed subheadings that are engaging and catchy. Do not write the blog post, please only write the outline of the blog post. \
Please do not number the headings. Please add a newline space between headings and subheadings. Do not self reference. Do not explain what you are doing.", height=250)

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

if option3 == "Generate complete blog post from outline":

    with container:
        with st.form(key='my_form_5', clear_on_submit=True):
            user_input = st.text_area("Add your prompt:", key='input', value="Please ignore all previous instructions. You are an expert \
copywriter who writes detailed and thoughtful blog articles. You have a " + tone + " tone of voice. You have a " + style + " writing style. I will \
give you a title and an outline for an article and I want you to expand in the " + language + " language on each of the subheadings to create a complete article \
from it. Please intersperse short and long sentences. Utilize uncommon terminology to enhance the originality of the content. Please format \
the content in a professional format. Do not self reference. Do not explain what you are doing. The blog title is " + topic +" . The blog article outline is - " + "'" + blog_post_outline + "'." , height=250)

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

if option3 == "Generate introduction using framework":

    with container:
        with st.form(key='my_form_6', clear_on_submit=True):
            user_input = st.text_area("Add your prompt:", key='input', value="Please ignore all previous instructions. You are an expert copywriter \
who writes detailed and compelling blog articles. You have a " + tone + " tone of voice. You have a " + style + " writing style. I want you to write a compelling \
blog introduction paragraph of around " + framework_total_words + " words on " + topic +" in the " + language + " language. Please use the " + framework +
" copywriting framework to hook and grab the attention of the blog readers. Please intersperse short and long sentences. Utilize uncommon \
terminology to enhance the originality of the content. Please format the content in a professional format. Do not self reference. Do not \
explain what you are doing. I will give you a list of keywords below and it would be great if you can add them into the text wherever \
appropriate. Please do highlight these keywords in bold in the text using markdown if you have them in the text. Here are the keywords - " "\n" + framework_keywords + "\n" "\n" " Remember that the topic is " + topic +".", height=250)

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

if option3 == "Generate paragraph of text":

    with container:
        with st.form(key='my_form_7', clear_on_submit=True):
            user_input = st.text_area("Add your prompt:", key='input', value="Please ignore all previous instructions. You are an expert copywriter who writes detailed and thoughtful blog articles. \
You have a" + tone + " tone of voice. You have a " + style + " writing style. I want you to write around " + paragraph_total_words + " words on " + topic + " in the english language. I will give you a list of keywords that need to be in the  \
text that you create. Please intersperse short and long sentences. Utilize uncommon terminology to enhance the originality of the content. Please format the content in a professional format. Do not \
self reference. Do not explain what you are doing. Here are the keywords - " "\n" + paragraph_keywords + "\n" + "Please highlight these keywords in bold in the text using markdown.", height=250)

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

if option3 == "Content titles generator":

    with container:
        with st.form(key='my_form_8', clear_on_submit=True):
            user_input = st.text_area("Add your prompt:", key='input', value="Please ignore all previous instructions. You are an \
expert copywriter who writes catchy titles for articles. You have a " + content_writing_tone +  " tone of voice. You have a " + content_writing_style + " writing style. \
Write " + content_titles_total_titles +" catchy article titles with a hook for the topic " + "'" + content_writing_topic + "'" +". The titles should be in the english language. Do not self reference. \
Do not explain what you are doing.", height=250)

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


if option3 == "Content rewriter (paste content)":

    with container:
        with st.form(key='my_form_10', clear_on_submit=True):
            user_input = st.text_area("Prompt template:", key='input', value="Please ignore all previous instructions. \
You are an expert copywriter who can rewrite content in your own voice and style. You have a " + content_writing_tone + " tone of \
voice. You have a " + content_writing_style + " writing style. Please rewrite content that I will give you. Please rewrite the \
content in the english language. Please intersperse short and long sentences. Utilize uncommon terminology \
to enhance the originality of the content. Please format the content in a professional format. Do not self \
reference. Do not explain what you are doing. Rewrite the following content - " +"'"+ rewrite_content +"'" , height=250)

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


if option3 == "Content brief generator":

    with container:
        with st.form(key='my_form_11', clear_on_submit=True):
            user_input = st.text_area("Prompt template:", key='input', value="Please ignore all previous instructions. You are an expert copywriter who creates content briefs. \
You have a " + content_writing_tone + " Casual tone of voice. You have a " + content_writing_style + " writing style. Please write only in the english language.The article title \
is "  + "'" + content_writing_topic + "'." + "First print out 'Content Brief for " + content_brief_main_keyword + " as a heading. Then print a heading 'Content Overview'. Then \
print 'Title' and write the article title. After this print 'Meta Description'. Now generate a meta description for the article title that is less than 160 characters. The \
description should contain the keyword " + content_brief_main_keyword +". After this table print out the following 'Outline / What is this content about'. Generate a content \
outline for the article " + content_writing_topic + " here. After this print the following 'What keywords and topics are recommended or required?' as a heading. Now list \
down " + content_brief_total_keywords + " keywords that are closely related to " + content_brief_main_keyword + ". After this print the following 'What key questions do \
readers have that need to be answered?' as a heading. Now generate " + content_brief_total_questions + " questions that the reader may have related to the " + content_writing_topic + \
"and " + content_brief_main_keyword + "  and print them out. Do not self reference. Do not explain what you are doing." , height=250)

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

if option3 == "Content outline generator":

    with container:
        with st.form(key='my_form_12', clear_on_submit=True):
            user_input = st.text_area("Prompt template:", key='input', value="Please ignore all previous instructions. \
You are an expert copywriter who creates content outlines. You have a " + content_writing_tone +" tone of voice. You have a " + content_writing_style + " Analytical \
writing style. Create a long form content outline in the english language for the article titled "+"'"+ content_writing_topic +"'" +".  The content \
outline should include a minimum of 20 headings and subheadings. The outline should be extensive and it should cover \
the entire topic. Create detailed subheadings that are engaging and catchy. Do not write the article, please only write  \
the outline of the article. Do not self reference. Do not explain what you are doing." , height=150)

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

if option3 == "Monthly content calendar":

    with container:
        with st.form(key='my_form_13', clear_on_submit=True):
            user_input = st.text_area("Prompt template:", key='input', value="Please ignore all previous instructions. \
Please respond only in the english language. You are a copywriter who is an expert in creating content calendars. \
You have a " + content_writing_tone +" tone of voice. You have a " + content_writing_style +" writing style. Please create a content calendar for " + content_brief_number_of_months + " months \
using long tail keywords related to my topic. There should be " + content_calendar_artitles_per_week + " blog posts scheduled each week of the month. Every blog \
post should have a catchy & click-bait title. The table should have actual dates in the future. Please organize each blog \
post in the table so that it looks like a calendar. My topic is " +"'"+content_writing_topic+"'" + ". Do not self reference. Do not explain what you are doing. Reply back only with the table." , height=150)

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

if option3 == "FAQ generator":

    with container:
        with st.form(key='my_form_14', clear_on_submit=True):
            user_input = st.text_area("Prompt template:", key='input', value="Please ignore all previous instructions. \
Please respond only in the english language. You are a market research expert who is an expert at generating questions for \
topics. You have a " + content_writing_tone +" tone of voice. You have a " + content_writing_style + " writing style. Please generate " + faq_number + " most frequently asked questions \
on the topic " + "'"+ content_writing_topic+"'" + ". Do not self reference. Do not explain what you are doing. Reply back only with the table." , height=150)

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

if option3 == "Get search intent for keywords":

    with container:
        with st.form(key='my_form_14', clear_on_submit=True):
            user_input = st.text_area("Prompt template:", key='input', value="Please ignore all previous instructions. Please respond only in the english \
language. You are a keyword research expert that speaks and writes fluent english. I will give you a long list of keywords, and I want you to classify them \
by the search intent, whether commercial, transactional, navigational, informational, local or investigational. Once done, please print them out in a markdown \
table with 'Keyword' as the first column, and 'Search Intent' as the second. Here are the keywords - \n" + search_intent_keywords , height=150)

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

if option3 == "Related keywords generator":

    with container:
        with st.form(key='my_form_15', clear_on_submit=True):
            user_input = st.text_area("Prompt template:", key='input', value="Please ignore all previous instructions. Please respond only in the english language. \
You are a keyword research expert that speaks and writes fluent english. I want you to generate a list of " + related_keywords_total + " keywords closely related to " + related_keywords_generator_seed + " without duplicating any \
words. Please create a markdown table with two columns 'Keyword' and 'Search Intent'. The first column should be the keyword you generated, and the second column \
should be the search intent of the keyword (commercial, transactional, navigational, informational, local or investigational). After the table, please print 'List \
of same keywords separated by commas:'. On the next line print the same list of keywords at the bottom separated by commas. Do not repeat yourself. Do not self \
reference. Do not explain what you are doing." , height=200)

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

if option3 == "Long tail keywords generator":

    with container:
        with st.form(key='my_form_16', clear_on_submit=True):
            user_input = st.text_area("Prompt template:", key='input', value="Please ignore all previous instructions. Please respond only in the english language. \
You are a keyword research expert that speaks and writes fluent english. I want you to generate a list of " + related_keywords_total + " long tail keywords for " + related_keywords_generator_seed + " without duplicating any \
words. Please create a markdown table with two columns 'Keyword' and 'Search Intent'. The first column should be the keyword you generated, and the second column \
should be the search intent of the keyword (commercial, transactional, navigational, informational, local or investigational). After the table, please print 'List \
of same keywords separated by commas:'. On the next line print the same list of keywords at the bottom separated by commas. Do not repeat yourself. Do not self \
reference. Do not explain what you are doing." , height=200)

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

if option3 == "Product description generator":

    with container:
        with st.form(key='my_form_17', clear_on_submit=True):
            user_input = st.text_area("Prompt template:", key='input', value="Please ignore all previous instructions. Please respond only in the english language. \
You are an E-commerce SEO expert copywriter who writes product descriptions that compel users to purchase the products. You have a " + Ecommerce_writing_tone +" tone of voice. \
You have a " + Ecommerce_writing_style +" writing style. Do not self reference. Do not explain what you are doing. In this task, you will craft a compelling product description for an e-commerce \
item that I will provide. Your goal is to create three unique content sections for the product description, each focusing on a different set of relevant keywords. \
Be sure to label each section with an eye-catching subheading that accurately summarizes its content. Your product description should be keyword-rich, informative, \
and engaging, with a word count of under " + product_description_total_keywords + " words. Your objective is to use emotional language and creative reasoning to persuade potential buyers to purchase the \
product. Once you have written the product description, please create a bulleted list of " + product_description_total_headings + " possible H1 headings for the product page. Provide a bulleted list of " + product_description_total_keywords \
+ " broad match keywords that you used to create the product description. To further enhance the product page marketing appeal, create a persuasive and professional sounding \
meta title and description that incorporates similar language to that of the new product summary. The meta title should be between 50 and 60 characters long. The meta \
description should be between 140 to 150 characters long. This is the e-commerce item - " + "'"+ product_description+"'"+".", height=250)

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

if option3 == "Category description generator":

    with container:
        with st.form(key='my_form_18', clear_on_submit=True):
            user_input = st.text_area("Prompt template:", key='input', value="Please ignore all previous instructions. Please respond only in the english language. \
You are an E-commerce SEO expert copywriter. You have a " + Ecommerce_writing_tone + " tone of voice. You have a "  + Ecommerce_writing_style + " writing style. Do not self reference. Do not explain what you are \
doing. your task is to create a compelling " + category_total_words + " word product category description in flawless english based on the category name that I provide. Your focus should be on \
highlighting the benefits of the products within the category, rather than just listing their features. Avoid using the passive voice and instead use active verbs to create a \
sense of urgency and excitement. Your goal is to create a category description that engages potential customers and inspires them to make a purchase. Make sure that your description \
flows smoothly and is easy to understand. It should be written in one line, which means you should avoid long paragraphs and instead break up your text with subheadings and bullet points. \
At the end of your category description, include a strong call to action that encourages customers to explore the products within the category and make a purchase. This will help to boost \
engagement and conversions. Overall, your objective is to create a category description that is informative, engaging, and persuasive. By highlighting the benefits of the products within the \
category and using active language to create a sense of urgency, you can attract and convert potential customers, driving sales and boosting the success of the e-commerce store. Category Name:" + "'"+category +"'" , height=275)

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

if option3 == "Landing page generator":

    with container:
        with st.form(key='my_form_19', clear_on_submit=True):
            user_input = st.text_area("Prompt template:", key='input', value="Please ignore all previous instructions. Please respond only in the english language. Do not self reference. \
Do not explain what you are doing. You are an E-commerce SEO expert copywriter. You have a " + Ecommerce_writing_tone +" tone of voice. You have a "+ Ecommerce_writing_style +" writing style. Your task is to generate a detailed \
USER PERSONA for a business that sells " + landing_page_generator_product +". First write 'User Persona creation for ' as the heading. Now create a subheading called 'Demographics'. Below, you need to create a table with \
the 2 columns and 7 rows with the following format: Column 1 = Data points (Name, Age, Occupation, Annual income, Marital status, Family situation, Location), Column 2 = Answers for each \
data point in Column 1. Now create a subheading called 'Landing page for selling  to the above persona'. Below this generate landing page text of around " + landing_page_total_word + " words using this persona. \
The landing page needs a headline that grabs attention, highlights the product's value proposition, and entices visitors to learn more. Use action-oriented language, such as 'Discover', \
'Transform' or 'Experience.'  The landing page copy should be persuasive and informative and highlight the product's benefits and features. Use short paragraphs, bullet points, and subheadings \
to make it easy to read and scan. Use persuasive language that speaks to your audience's emotions and desires. End the landing page with a clear and prominent CTA to " + landing_page_call_to_action , height=275)

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


if option3 == "Bulk titles and descriptions":

    with container:
        with st.form(key='my_form_20', clear_on_submit=True):
            user_input = st.text_area("Prompt template:", key='input', value="Please ignore all previous instructions. Please respond only in the english language. \
You are an E-commerce SEO expert copywriter. You have a " + Ecommerce_writing_tone +" tone of voice. You have a "+Ecommerce_writing_style +" writing style. Do not self reference. Do not explain what you are doing. \
Generate compelling meta titles and meta descriptions for a list of e-commerce products that I will give you. One meta title and one meta description should be generated for \
every product in the list that I give you. The meta title should not be more than 60 characters long. The meta descriptions should not be longer than 160 characters long. \
The meta title and meta description should have the product keywords in them. The meta title and meta description should use persuasive language that speaks to the audience's \
emotions and desires and makes them want to purchase the product. Here are the e-commerce products - \n" + bulk_titles_and_descriptions_products , height=275)

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

if option3 == "Meta title and description generator":

    with container:
        with st.form(key='my_form_21', clear_on_submit=True):
            user_input = st.text_area("Prompt template:", key='input', value="Please ignore all previous instructions. Please respond only in the english language. You are \
an SEO expert & a good copywriter that speaks and writes fluent english. You have a " + meta_writing_tone +" tone of voice. You have a " + meta__writing_style + " writing style. Do not self reference. Do not \
explain what you are doing. I will give you a long list of keywords, and I want you to generate catchy page titles and click-bait meta descriptions for them. The page titles \
should be between 70 and 80 characters. The meta descriptions should be between 140 and 160 characters. Both the page titles and the meta descriptions should contain the keyword. \
Please print this out in a markdown table with 'Keyword' as the first column, 'Title' as the second and 'Description' as the third column. Here are the keywords - \n" + meta_titles_and_descriptions_keywords, height=275)

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
   
if option3 == "Create silo structure":

    with container:
        with st.form(key='my_form_22', clear_on_submit=True):
            user_input = st.text_area("Prompt template:", key='input', value="Please ignore all previous instructions. Please respond only in the english language. \
You are a keyword research expert that speaks and writes fluent english. Create a detailed SILO structure for a website using the keyword: " + silo_keywords +".  \
Organize the page of the website in a hierarchical structure, with the Homepage at the top and the more specific pages at the bottom. You need to group, isolate, and \
interlink pages about a specific topic. Do not repeat yourself. Do not self reference. Do not explain what you are doing. Only write down the SILO pages in a nested structure." , height=275)

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

if option3 == "Create buyer persona":

    with container:
        with st.form(key='my_form_23', clear_on_submit=True):
            user_input = st.text_area("Prompt template:", key='input', value= "Please ignore all previous instructions. Please respond only in the english language. You are a marketing researcher \
that writes fluent english. You have a " + persona_writing_tone +" tone of voice. You have a " + persona__writing_style +" writing style. Your task is to generate a detailed USER PERSONA for a business \
that sells " + persona_sell_question + " in " + persona_location_question + ". First write 'User Persona creation for " + persona_sell_question + " in '" + persona_location_question +"' as the heading. Now create a subheading called 'Demographics'. \
Below, you need to create a table with the 2 columns and 7 rows with the following format: Column 1 = Data points (Name, Age, Occupation, Annual income, Marital status, Family situation, Location), \
Column 2 = Answers for each data point in Column 1 based on the specific market " + "'" + persona_sell_question + "'" + ". Now create a subheading called 'USER DESCRIPTION'. Below this generate a summary \
of the user persona in no more than 500 characters. Now create a subheading called 'PSYCHOGRAPHICS'. Below this you need to create a table with 2 columns and 9 rows with the following format: \
Column 1 = Data points (Personal characteristics, Hobbies, Interests, Personal aspirations, Professional goals, Pains, Main challenges, Needs, Dreams), Column 2 = Answers for each data point in Column \
1 based on the specific market " + persona_sell_question + ". Now create a subheading called 'SHOPPING BEHAVIORS'. Below this you need to create a table with 2 columns and 8 rows with the following \
format: Column 1 = Data points (Budget, Shopping frequency, Preferred channels, Online behavior, Search terms, Preferred brands, Triggers, Barriers), Column 2 = Answers for each data point in Column 1 \
based on the specific market " + persona_sell_question + ". Please make sure that your response is structured in 4 separate tables and has a separate row for each data point. Do not provide bullet points. Do not self \
reference. Do not explain what you are doing." , height=275)

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

if option3 == "Market research":

    with container:
        with st.form(key='my_form_24', clear_on_submit=True):
            user_input = st.text_area("Prompt template:", key='input', value= "Firstly, what are the most popular " +"'"+ market_research_topic +"'"+" websites? Please provide the URLs of these websites. \
Secondly, looking at all of those sites (and those sites only) if you had to break out all of the things they write about into 5-15 high level categories, what would those categories be? \
Give a brief description of each category, and a couple of specific examples of things they've written about that would fit into that category." , height=150)

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

if option3 == "Subreddit research":

    with container:
        with st.form(key='my_form_25', clear_on_submit=True):
            user_input = st.text_area("Prompt template:", key='input', value= "Firstly, what are the most popular subreddits about " +"'"+ subreddits_research_topic+"'"+". Secondly, what are \
the most popular topics those subreddits talk about? Thirdly, what are some specific titles to popular threads from the popular topics you just listed?" , height=150)

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


# else:
#       with container:
#           with st.form(key='my_form_3', clear_on_submit=True):
#          # user_input = st.text_area("Add your prompt:", key='input', height=100)
#               user_input = st.text_area("Add your prompt:", value="Write your own prompt ",height=100)
#               submit_button = st.form_submit_button(label='Generate response')
    
#           if submit_button and user_input:
#               output, total_tokens, prompt_tokens, completion_tokens = generate_response(user_input)
#               st.session_state['past'].append(user_input)
#               st.session_state['generated'].append(output)
#               st.session_state['model_name'].append(model_name)
#               st.session_state['total_tokens'].append(total_tokens)

#           # from https://openai.com/pricing#language-models
#               if model_name == "GPT-3.5":
#                   cost = total_tokens * 0.002 / 1000
#               else:
#                   cost = (prompt_tokens * 0.03 + completion_tokens * 0.06) / 1000

#               st.session_state['cost'].append(cost)
#               st.session_state['total_cost'] += cost

if st.session_state['generated']:
    with response_container:
        for i in range(len(st.session_state['generated'])):
            message(st.session_state["past"][i], is_user=True, key=str(i) + '_user')
            message(st.session_state["generated"][i], key=str(i))
            st.write(
                f"Model used: {st.session_state['model_name'][i]}; Number of tokens: {st.session_state['total_tokens'][i]}; Cost: ${st.session_state['cost'][i]:.5f}")
            counter_placeholder.write(f"Total cost of this conversation: ${st.session_state['total_cost']:.5f}")
        
