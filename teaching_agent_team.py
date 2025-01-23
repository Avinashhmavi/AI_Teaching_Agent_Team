import streamlit as st
import groq

# Set up Groq API key
groq_api_key = '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'
client = groq.Client(api_key=groq_api_key)

# Define a function to interact with Groq's LLM
def ask_groq(prompt, role="You are a helpful assistant.", model="mixtral-8x7b-32768"):
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": role},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

# Define roles for each agent
PROFESSOR_ROLE = "You are a Professor. Your role is to create comprehensive knowledge bases, explain concepts from first principles, and include key terminology."
ACADEMIC_ADVISOR_ROLE = "You are an Academic Advisor. Your role is to create detailed learning roadmaps, break topics into subtopics, and include time estimates."
RESEARCH_LIBRARIAN_ROLE = "You are a Research Librarian. Your role is to find quality learning resources, including books, articles, and online courses."
TEACHING_ASSISTANT_ROLE = "You are a Teaching Assistant. Your role is to create practice materials, including progressive exercises and real-world applications."

# Set up Streamlit interface
st.set_page_config(page_title="👨‍🏫 AI Teaching Agent Team", layout="wide")

# Add a title and description
st.title("👨‍🏫 AI Teaching Agent Team")
st.write("Enter a topic below, and the AI agents will generate a knowledge base, learning roadmap, resources, and practice materials for you.")

# Initialize session state
if 'responses' not in st.session_state:
    st.session_state['responses'] = {}

# Input for the topic
topic = st.text_input(
    "Enter topic:",
    placeholder="e.g., Machine Learning"
)

# Button to start the process
if st.button("Start"):
    if not topic:
        st.error("Please enter a topic.")
    else:
        # Generate responses from each agent
        with st.spinner("Generating Knowledge Base..."):
            professor_response = ask_groq(
                f"Create a comprehensive knowledge base on {topic}. Include key terminology and first principles.",
                role=PROFESSOR_ROLE
            )
            st.session_state['responses']['professor'] = professor_response

        with st.spinner("Creating Learning Roadmap..."):
            academic_advisor_response = ask_groq(
                f"Create a detailed learning roadmap for {topic}. Break it down into subtopics and include time estimates.",
                role=ACADEMIC_ADVISOR_ROLE
            )
            st.session_state['responses']['academic_advisor'] = academic_advisor_response

        with st.spinner("Finding Learning Resources..."):
            research_librarian_response = ask_groq(
                f"Find quality learning resources for {topic}. Include books, articles, and online courses.",
                role=RESEARCH_LIBRARIAN_ROLE
            )
            st.session_state['responses']['research_librarian'] = research_librarian_response

        with st.spinner("Creating Practice Materials..."):
            teaching_assistant_response = ask_groq(
                f"Create practice materials for {topic}. Include progressive exercises and real-world applications.",
                role=TEACHING_ASSISTANT_ROLE
            )
            st.session_state['responses']['teaching_assistant'] = teaching_assistant_response

# Display agent responses
if st.session_state['responses']:
    st.markdown("---")
    st.markdown("### 📚 Professor Response: Knowledge Base")
    st.markdown(st.session_state['responses']['professor'])

    st.markdown("---")
    st.markdown("### 🗺️ Academic Advisor Response: Learning Roadmap")
    st.markdown(st.session_state['responses']['academic_advisor'])

    st.markdown("---")
    st.markdown("### 📖 Research Librarian Response: Learning Resources")
    st.markdown(st.session_state['responses']['research_librarian'])

    st.markdown("---")
    st.markdown("### 📝 Teaching Assistant Response: Practice Materials")
    st.markdown(st.session_state['responses']['teaching_assistant'])