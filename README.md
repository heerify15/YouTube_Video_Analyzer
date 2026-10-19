# TubeNotes 🎬
### AI-Powered YouTube Video Analyzer

**Turn YouTube videos into structured insights with AI.**

TubeNotes is an AI-powered application that analyzes YouTube videos and generates structured reports to help users understand video content more efficiently. Built with Python, Streamlit, Agno, and the Groq API, it provides a simple interface for submitting videos and exploring AI-generated analysis.

## ✨ Features

- **AI-Powered Analysis:** Analyze YouTube videos using an AI agent.
- **Structured Reports:** Generate organized, readable analysis of video content.
- **Timestamp Navigation:** Jump to relevant moments in a video using clickable timestamps when available in the report.
- **Expandable Sections:** Explore report sections without overwhelming the interface.
- **Markdown Export:** Download generated analysis reports for future reference.
- **Video Preview:** View the submitted YouTube video within the application.
- **Analysis History:** Access previous analyses during the current session.
- **Interactive Interface:** A custom dark-themed interface with crimson accents, built using Streamlit and CSS.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core application logic |
| Streamlit | Interactive web interface |
| Agno | AI agent orchestration |
| Groq API | Large language model inference |
| YouTubeTools | YouTube video analysis tools |
| CSS | Custom interface styling |

## 📁 Project Structure

```text
├── ui.py                       # Streamlit user interface
├── youtube_video_analyzer.py   # AI agent and analysis logic
├── .gitignore (.env # API credentials (not committed))
└── README.md
```

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or a compatible version supported by your dependencies
- A Groq API key
- Internet access

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd TubeNotes
```

Replace the placeholder with your actual repository URL.

### 2. Create a virtual environment

**Windows:**

```powershell
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

Install the packages required by your project:

```bash
pip install streamlit agno groq python-dotenv
```

If your implementation requires additional packages or specific versions, install those as well. For reproducible setup, use a `requirements.txt` generated from your tested environment.

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
```

Use the exact environment variable name expected by your backend. Never commit API keys or other secrets to GitHub.

### 5. Run the application

```bash
python -m streamlit run ui.py
```

Open the local URL displayed in the terminal, usually:

`http://localhost:8501`

## 📖 How to Use

1. Launch TubeNotes in your browser.
2. Paste a valid YouTube video URL.
3. Start the analysis.
4. Wait for the AI agent to process the video and generate a report.
5. Explore the report sections and use available timestamps to navigate the video.
6. Download the report in Markdown format if you want to save it.

## ⚙️ How It Works

```text
YouTube Video URL
        |
        v
URL Validation
        |
        v
Streamlit Interface
        |
        v
Agno AI Agent
        |
        v
Groq LLM + YouTube Tools
        |
        v
Video Analysis
        |
        v
Structured Report
        |
        v
Explore, Navigate & Export
```

## 🔐 Security

- Store API credentials in environment variables.
- Keep `.env` out of version control.
- Do not expose API keys in source code, logs, or screenshots.
- Follow the usage policies and access restrictions of the services and tools you integrate.

## ⚠️ Limitations

- Analysis quality depends on the underlying model, available video information, and tool capabilities.
- Some videos may be inaccessible because of privacy settings, regional restrictions, or unavailable transcripts.
- Generated reports may contain inaccuracies and should be checked against the original video when precision matters.
- Analysis history is session-based and is not permanently stored by the current implementation.
- Processing time depends on video accessibility, tool execution, and model response time.

## 🔮 Future Improvements

- Video summarization with customizable detail levels.
- Topic extraction and automatic key-point generation.
- Question answering over video content.
- Persistent analysis history.
- Support for exporting reports in additional formats.
- Improved source references and transcript-based navigation.

## 👨‍💻 Built With

TubeNotes is a mini project exploring AI agents, large language models, tool integration, and the development of practical AI-powered applications.

**TubeNotes — Watch less. Understand more.**
