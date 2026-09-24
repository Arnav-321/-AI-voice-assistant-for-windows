# Stree - AI Voice Assistant

Stree is a Windows-based AI voice assistant built with Python. It combines voice recognition, Gemini AI, Windows automation, and browser automation to provide a hands-free desktop assistant experience inspired by assistants such as Alexa and JARVIS.

## Γ£¿ Features

### ≡ƒÄÖ∩╕Å Voice Assistant
- Wake word detection using **"Hello"**
- Speech-to-text using Google Speech Recognition
- Text-to-speech using Windows PowerShell `System.Speech`
- Continuous listening mode
- Natural-language command processing

### ≡ƒºá AI Brain
- Uses Google's Gemini API to understand user commands
- Converts natural-language instructions into structured actions
- Supports multiple actions in a single request
- Includes retry handling for temporary Gemini service errors
- Falls back to another Gemini model when required

### ≡ƒ¬ƒ Windows Control
Stree can perform several desktop operations, including:

- Open applications
- Close applications
- Open folders
- Create folders
- Create files
- Search for files
- Rename files
- Copy files
- Move files
- Delete files
- Keyboard shortcuts
- Mouse control
- Window switching
- Minimize/maximize windows
- Show desktop
- Volume and mute controls
- Open Windows Settings
- Open Task Manager
- Open Control Panel
- Take screenshots
- Lock Windows

### ≡ƒîÉ Chrome Browser Automation
Stree uses browser automation to control a dedicated Chrome session.

Supported operations include:

- Open Chrome
- Search Google
- Open URLs
- Open new tabs
- Close tabs
- Switch between tabs
- Go back/forward
- Refresh pages
- Open Chrome Downloads
- Open Chrome History
- Open Chrome Bookmarks
- Open Chrome Settings
- Click search results
- Click links/buttons by visible text
- Scroll pages
- Zoom in/out/reset
- Type into the active browser page

Stree can also understand multi-step commands such as:

> "Search Google for Python tutorials and click the first result."

The AI can convert this into a sequence of browser actions.

## ≡ƒÅù∩╕Å Project Structure

```text
AI-Voice-Assistant/
Γöé
Γö£ΓöÇΓöÇ venv/
Γö£ΓöÇΓöÇ .env
Γö£ΓöÇΓöÇ ai_brain.py
Γö£ΓöÇΓöÇ browser_controller.py
Γö£ΓöÇΓöÇ commands.py
Γö£ΓöÇΓöÇ requirements.txt
Γö£ΓöÇΓöÇ stree.py
Γö£ΓöÇΓöÇ voice.py
ΓööΓöÇΓöÇ start_stree.vbs
```

### File Description

| File | Purpose |
|---|---|
| `stree.py` | Main assistant loop and wake-word handling |
| `voice.py` | Speech recognition and text-to-speech |
| `ai_brain.py` | Gemini AI command interpretation |
| `commands.py` | Windows and assistant actions |
| `browser_controller.py` | Chrome browser automation |
| `requirements.txt` | Python dependencies |
| `.env` | Stores the Gemini API key |
| `start_stree.vbs` | Starts Stree automatically with Windows |

## ΓÜÖ∩╕Å Requirements

- Windows 10/11
- Python 3.10+
- Google Chrome
- Working microphone
- Internet connection
- Gemini API key
- Python virtual environment

## ≡ƒÜÇ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Voice-Assistant.git
cd AI-Voice-Assistant
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

If Playwright is not already installed:

```bash
pip install playwright
```

## ≡ƒöæ Gemini API Configuration

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

**Never commit your `.env` file or API key to GitHub.**

Add this to `.gitignore`:

```gitignore
.env
venv/
__pycache__/
*.pyc
```

## Γû╢∩╕Å Run Stree

Activate the virtual environment:

```bash
venv\Scripts\activate
```

Then run:

```bash
python stree.py
```

Stree will start and say:

> "Stree is ready."

Say:

> "Hello"

Then give your command.

## ≡ƒùú∩╕Å Example Commands

### Windows

```text
Hello
Open Notepad
```

```text
Hello
Open Downloads folder
```

```text
Hello
Open Calculator
```

```text
Hello
Take a screenshot
```

```text
Hello
Create a folder called Projects
```

### Chrome

```text
Hello
Open Chrome
```

```text
Hello
Search Google for Python tutorials
```

```text
Hello
Search Google for React tutorials and click the first result
```

```text
Hello
Open Chrome Downloads
```

```text
Hello
Open Chrome History
```

```text
Hello
Go back
```

```text
Hello
Open a new tab
```

```text
Hello
Search Google for GitHub and click the result containing GitHub
```

## ≡ƒîÉ Chrome Automation Architecture

Stree uses Playwright to communicate with a Chrome instance through the Chrome DevTools Protocol.

For reliability, Stree can use a dedicated Chrome profile:

```text
Stree
  Γöé
  Γö£ΓöÇΓöÇ Voice Recognition
  Γöé
  Γö£ΓöÇΓöÇ Gemini AI
  Γöé     ΓööΓöÇΓöÇ Converts speech ΓåÆ structured actions
  Γöé
  Γö£ΓöÇΓöÇ Windows Controller
  Γöé     ΓööΓöÇΓöÇ Desktop operations
  Γöé
  ΓööΓöÇΓöÇ Chrome Controller
        ΓööΓöÇΓöÇ Playwright + Chrome DevTools Protocol
```

Using a dedicated browser profile helps prevent Stree's automation from interfering with your normal Chrome session.

## ≡ƒöÉ Security

This project requires access to:

- Microphone
- Gemini API
- Windows desktop controls
- Chrome browser automation

Keep your Gemini API key private.

Do not upload:

```text
.env
```

to GitHub.

A recommended `.gitignore` is:

```gitignore
.env
venv/
__pycache__/
*.pyc
```

##  Development Status

Stree is an actively developing personal AI assistant.

### Current stage

- [x] Voice input
- [x] Wake-word detection
- [x] Gemini AI integration
- [x] Windows automation
- [x] File operations
- [x] Chrome automation
- [x] Multi-action commands
- [x] Automatic Windows startup
- [ ] More advanced website interaction
- [ ] More natural conversations
- [ ] Offline speech recognition
- [ ] Custom GUI
- [ ] Memory system
- [ ] Plugin/skill system

## Future Improvements

Planned improvements may include:

- Offline speech recognition
- Better wake-word detection
- Context-aware conversations
- Personal memory
- Application-specific skills
- More advanced website automation
- WhatsApp and email integration
- Calendar integration
- Smart home integration
- Custom animated GUI
- System performance monitoring
- Local AI model support
- Voice-controlled coding assistance
   Author

**Arnav Kumar**

B.E. Computer Science and Engineering

 License

This project can be used for learning, experimentation, and personal development.

Choose and add an appropriate open-source license before distributing the project publicly.

---

Γ¡É If you find this project useful, consider starring the repository.
