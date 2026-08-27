🤖 AI Prompt Generator

An interactive Streamlit-based AI Prompt Generator that creates high-quality prompts using different prompt-engineering techniques.

The application uses the Hugging Face Router API through the OpenAI Python SDK and allows users to customize the prompt-generation model and creativity level.

✨ Features
🧠 Multiple prompt-engineering techniques
✍️ Natural-language task description
📋 Additional context and requirements
🤖 Configurable AI model
🎨 Adjustable creativity/temperature
⚡ Real-time prompt generation
📄 Generated prompt displayed in the UI
⬇️ Download generated prompts as .txt
💾 Generated prompts persist in Streamlit session state
🎨 Clean, responsive Streamlit interface
🛠️ Tech Stack
Python
Streamlit — Web application framework
OpenAI Python SDK — API client
Hugging Face Router — Model inference
Prompt Engineering — Prompt-generation techniques
📁 Project Structure
AI-Prompt-Generator/
│
├── app.py
├── prompt.py
├── requirements.txt
├── README.md
└── .gitignore

app.py

Contains the Streamlit application, UI components, model configuration, API calls, and prompt-generation workflow.

prompt.py

Contains:

PROMPT_CATEGORIES
build_generator_prompt()

These define the available prompt-engineering techniques and construct the prompt sent to the AI model.

🚀 Getting Started
1. Clone the repository
git clone <your-repository-url>
cd AI-Prompt-Generator

2. Create a virtual environment
python -m venv venv


Activate it:

Windows

venv\Scripts\activate


macOS/Linux

source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt


If you don't have a requirements.txt yet, you can create one containing:

streamlit
openai

4. Configure your API key

Do not hard-code your Hugging Face API key in app.py.

For local development, set an environment variable.

Windows PowerShell:

$env:HF_TOKEN="your-huggingface-token"


macOS/Linux:

export HF_TOKEN="your-huggingface-token"


Then update the client configuration:

client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.environ["HF_TOKEN"]
)


For Streamlit deployment, you can alternatively use .streamlit/secrets.toml:

HF_TOKEN = "your-huggingface-token"


and:

client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=st.secrets["HF_TOKEN"]
)

5. Run the application
streamlit run app.py


The application will open in your browser.

⚙️ How It Works

The application follows a simple workflow:

User Input
    ↓
Select Prompt Technique
    ↓
Add Context & Requirements
    ↓
build_generator_prompt()
    ↓
Hugging Face Model
    ↓
Generated Prompt
    ↓
Display / Download

Step 1 — Select a technique

The sidebar allows the user to choose a prompt-engineering technique from PROMPT_CATEGORIES.

Step 2 — Describe the task

The user provides:

What the AI should do
Relevant context
Additional requirements
Step 3 — Configure generation

The user can select:

AI model
Creativity/temperature
Step 4 — Generate

The application sends the generated instruction to the selected Hugging Face model.

Step 5 — Use the result

The resulting prompt is displayed in a text area and can be downloaded as:

generated_prompt.txt

🎛️ Configuration

The default model is:

moonshotai/Kimi-K2-Instruct-0905


You can change the model from the sidebar as long as the selected model is available through the configured Hugging Face Router endpoint.

The Creativity slider controls the model's temperature:

0.0 → More deterministic
0.7 → Balanced creativity
1.0 → More creative/variable

🔐 Security

Never commit API keys to GitHub or another public repository.

If an API key has already been committed or exposed, revoke/rotate it immediately and replace it with a new key.

Add sensitive files to .gitignore:

.env
.streamlit/secrets.toml
venv/
__pycache__/
*.pyc


A safer production configuration is to retrieve the API key from an environment variable or Streamlit secrets rather than placing it directly in source code.

📌 Example
Input

Task

Build a modern e-commerce website using React and Tailwind CSS.


Context

The website is for a clothing brand targeting young customers.


Requirements

Use a dark theme, responsive design, and include authentication.


The application combines these inputs with the selected prompt-engineering technique and asks the AI model to produce a more structured, detailed prompt.

🔮 Future Improvements

Possible improvements include:

 Copy-to-clipboard button
 Prompt history
 Multiple generated variations
 Export to Markdown/PDF
 More prompt-engineering techniques
 Model presets
 Custom system instructions
 Prompt quality scoring
 Prompt editing after generation
 User authentication
 Deployment on Streamlit Community Cloud
 Support for additional AI providers
🐛 Error Handling

If generation fails, the application displays the returned exception in the Streamlit interface:

Error generating prompt: ...


Common causes include:

Invalid API key
Expired/revoked API key
Incorrect model name
Network/API availability issues
Missing Python dependencies
📄 License

Add your preferred license here, for example:

MIT License


If this project is intended for public use, adding a license file such as LICENSE is recommended.

⭐ Contributing

Contributions and improvements are welcome.

Fork the repository.
Create a feature branch.
Make your changes.
Test the application locally.
Submit a pull request.

Built with ❤️ using Python, Streamlit, and AI.
