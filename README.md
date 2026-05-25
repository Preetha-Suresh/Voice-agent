# Voice Agent for Terminal Coding Assistants

A lightweight voice-controlled interface for terminal-based AI coding agents.

This project enables developers to interact with coding assistants using voice commands and reducing keyboard/mouse usage during development workflows.

---

# Features

- Speech-to-text based voice input
- Voice command routing
- Terminal automation
- AI coding agent integration using Aider
- Context-aware command memory
- Fuzzy matching for flexible voice commands
- Hands-free developer workflow support

---

# Supported Voice Commands

Examples:

- "clear screen"
- "list files"
- "open vscode"
- "git status"
- "commit changes"
- "create simple python calculator"
- "exit"

General prompts can also be forwarded to the AI coding agent.

Example:

"create a flask app"

---

# Project Structure

```text
voice-agent/
│
├── README.md
├── REPORT.md
├── LICENSE
├── requirements.txt
├── main.py
├── stt.py
├── command_router.py
├── agent.py
├── memory.py
└── .gitignore
```

---

# Technologies Used

- Python 3.11
- Faster-Whisper
- SoundDevice
- RapidFuzz
- Aider
- OpenRouter API

---

# Setup Instructions

## 1. Clone the repository

```bash
git clone <https://github.com/Preetha-Suresh/Voice-agent.git>
cd voice-agent
```

---

## 2. Create virtual environment

### Windows

```powershell
python -m venv venv
```

Activate:

```powershell
venv\Scripts\activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Install Aider

```bash
pip install aider-chat
```

---

## 5. Configure OpenRouter API key

Windows PowerShell:

```powershell
$env:OPENROUTER_API_KEY="your_api_key_here"
```

No API keys are included in this repository.

---

# Running the Project

Run:

```bash
python main.py
```

Speak commands through your microphone.

---

# Demo Setup Time

Approximate setup time before demo:
5–10 minutes

---

# Design Overview

The system follows this workflow:

```text
Voice Input
    ↓
Speech-to-Text
    ↓
Context Memory
    ↓
Command Router
    ↓
Terminal Commands / AI Coding Agent
```
