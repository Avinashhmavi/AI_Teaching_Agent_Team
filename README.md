## 🧑‍🏫🧑‍🎓AI Teaching Agent Team

Welcome to the **AI Teaching Agent Team** project! This Streamlit app simulates a team of AI agents (Professor, Academic Advisor, Research Librarian, and Teaching Assistant) that help you learn any topic by generating a knowledge base, learning roadmap, resources, and practice materials.

---
## 🥇Live Demo
You can try the app live by clicking the link below:
 👉 [**AI Teaching Agent Team App**](https://aiteachingagentteam-yakvkt9gfdf6zgj4ugkud2.streamlit.app/)

---
## 🔥Features

- **Professor**: Creates a comprehensive knowledge base on the given topic.
- **Academic Advisor**: Designs a detailed learning roadmap with subtopics and time estimates.
- **Research Librarian**: Finds quality learning resources, including books, articles, and online courses.
- **Teaching Assistant**: Creates practice materials, including progressive exercises and real-world applications.

---

## ⚙️⚙️Technologies Used

- **Streamlit**: For building the web app interface.
- **Groq API**: For interacting with the `mixtral-8x7b-32768` LLM to generate responses.
- **Python**: The programming language used for the backend logic.

---

## **Pre-Installation Steps**

Before running the app, ensure you have the following installed:

### **1. Python**
Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

### **2. Virtual Environment (Optional but Recommended)**
Create a virtual environment to isolate the project dependencies:
```bash
python -m venv venv
```
Activate the virtual environment:
- On Windows:
  ```bash
  .\venv\Scripts\activate
  ```
- On macOS/Linux:
  ```bash
  source venv/bin/activate
  ```

### **3. Install Required Libraries**
Install the required Python libraries using `pip`:
```bash
pip install streamlit groq
```

---

## **How to Run the App Locally**

1. Clone the repository or download the `teaching_agent_team.py` file.
2. Navigate to the project directory:
   ```bash
   cd path/to/project
   ```
3. Run the Streamlit app:
   ```bash
   streamlit run teaching_agent_team.py
   ```
4. Open your browser and go to the URL provided in the terminal (usually `http://localhost:8501`).

---

## **How to Deploy on Streamlit Cloud**

1. **Push Your Code to GitHub**:
   - Create a new repository on GitHub.
   - Push the `teaching_agent_team.py` file and the `requirements.txt` file to the repository.

2. **Create a `requirements.txt` File**:
   Add the following content to the `requirements.txt` file:
   ```
   streamlit
   groq
   ```

3. **Deploy on Streamlit Cloud**:
   - Go to [Streamlit Cloud](https://share.streamlit.io/).
   - Log in with your GitHub account.
   - Click on "New App".
   - Select the repository and branch where your code is located.
   - Specify the path to your Streamlit app file (`teaching_agent_team.py`).
   - Click "Deploy".

4. **Set Up Secrets (Environment Variables)**:
   - In your Streamlit Cloud app settings, go to the "Secrets" section.
   - Add your Groq API key as a secret:
     ```

5. **Access Your App**:
   - Once deployed, Streamlit Cloud will provide you with a public URL for your app.
   - Share this URL with others or embed it in your website.

---

## **Project Structure**
```
AI-Teaching-Agent-Team/
├── teaching_agent_team.py  # Main Streamlit app file
├── requirements.txt        # List of dependencies
├── README.md               # Project documentation
```

---

## **Customization**
- **Groq API Key**: Replace the placeholder Groq API key in the code with your own key.
- **LLM Model**: You can switch the model in the `ask_groq` function to another Groq-supported model (e.g., `llama2-70b-4096`).

---

## **Contributing**
Contributions are welcome! If you'd like to contribute to this project, please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes.
4. Submit a pull request.

---


Enjoy using the **AI Teaching Agent Team**! 🚀
