# REPORT

## Project Title

Voice Input Interface for a Terminal Coding Agent

---

## Motivation

Terminal-based AI coding agents are becoming increasingly powerful for developers who prefer working entirely inside the terminal. However, most coding agents still rely heavily on keyboard input, making the workflow less accessible and less hands-free.

The goal of this project was to reduce keyboard and mouse interaction by enabling voice-driven interaction with a terminal coding agent. Instead of manually typing prompts, users can speak commands naturally, which are then transcribed and forwarded to the coding agent.

I wanted the system to feel lightweight, simple to run, and practical for real-world developer workflows.

---

## Chosen Coding Agent

For this project, I selected Aider as the terminal coding agent.

Reasons for choosing Aider:

- Open source and terminal-based
- Easy CLI integration
- Can execute coding-related prompts directly
- Works with multiple LLM providers
- Lightweight setup compared to larger IDE-based systems

Aider already supports interaction through terminal prompts, which made it suitable for wrapping with a voice interface.

---

## High-Level Architecture

The system consists of three main components:

1. Speech Capture
2. Speech-to-Text Transcription
3. Command Routing and Agent Execution

Workflow:

User Speech → Audio Recording → Whisper Transcription → Command Router → Aider CLI → Terminal Output

---

## Speech Recognition Design

### Selected STT Engine

I used Faster-Whisper for speech-to-text transcription.

Reasons for choosing Faster-Whisper:

- Fully local execution
- No cloud dependency
- Fast inference
- Good transcription accuracy
- Lightweight enough for CPU usage

The transcription model runs locally on the user's machine using CPU inference with int8 quantization.

---

## Alternatives Considered

### Google Speech API

Pros:
- High accuracy
- Simple integration

Cons:
- Requires internet connection
- API cost and quota limits
- External dependency

### OpenAI Whisper API

Pros:
- Strong transcription quality

Cons:
- Paid API usage
- Cloud dependency
- Higher latency

### Vosk

Pros:
- Offline support

Cons:
- Lower transcription accuracy compared to Whisper

After evaluation, Faster-Whisper provided the best balance between accuracy, performance, offline capability, and simplicity.

---

## Voice Command System

A command router was implemented to recognize spoken shortcuts and execute terminal actions.

Examples:

- "clear screen"
- "list files"
- "open VS Code"
- "exit"

The system uses RapidFuzz for approximate string matching instead of exact matching.

This improves usability because speech recognition may slightly vary spoken phrases.

Example:

"clear screen" may be transcribed as:
- "clear screen"
- "clear scream"
- "clear"

RapidFuzz allows flexible matching for such cases.

---

## AI Agent Integration

When the spoken text does not match a built-in command, it is forwarded directly to Aider.

Example:

User says:
"create a simple python calculator"

The system transcribes the speech and forwards the prompt to Aider automatically.

Aider then generates the requested code inside the terminal.

This creates a voice-driven coding workflow.

---

## External Services Used

### OpenRouter

Used as the LLM provider for Aider.

Reason:
- Access to multiple LLMs through one API
- Simple integration
- Free-tier models available

### Models Tested

- Gemini 2.0 Flash
- DeepSeek Chat
- Llama 3
- GPT-3.5 Turbo

Final stable model used:
- GPT-3.5 Turbo through OpenRouter

---

## Cost Considerations

The system was designed with low cost in mind.

### Speech Recognition

- Fully local
- No API cost

### LLM Usage

- OpenRouter free/low-cost models
- Minimal token usage during testing

This architecture avoids expensive continuous cloud transcription costs.

---

## Challenges Faced

### 1. Windows Terminal Command Issues

Commands like:
- clear screen
- list files

initially did not execute correctly due to PowerShell behavior differences.

This was solved using:
- os.system("cls")
- subprocess.run(..., shell=True)

---

### 2. Whisper CUDA Errors

The initial Faster-Whisper setup attempted GPU execution and failed due to missing CUDA libraries.

Solution:
- Forced CPU mode
- Used compute_type="int8"

---

### 3. Speech Recognition Variability

Speech transcription was sometimes inconsistent.

Example:
- "clear screen" became "clear scream"

Solution:
- Added fuzzy matching using RapidFuzz

---

### 4. API Rate Limits

Gemini free-tier quotas caused repeated rate limit failures during testing.

Solution:
- Switched to OpenRouter GPT-3.5 Turbo model

---

## Current Limitations

- No wake-word detection
- Continuous listening is not implemented
- Some commands still depend on platform-specific terminal behavior
- Background noise can reduce transcription quality

---

## Possible Future Improvements

- Add wake-word support
- Add conversation memory/context tracking
- Add fully continuous voice mode
- Add cross-platform shell abstraction

---

## Final Outcome

The final system successfully demonstrates a voice-driven terminal coding workflow.

Users can:
- Speak coding prompts
- Execute terminal shortcuts
- Trigger AI-assisted code generation
- Interact with a terminal coding agent with reduced keyboard usage

The project satisfies the assignment goal of creating a voice input interface for a terminal coding agent while minimizing manual interaction.
