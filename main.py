import sounddevice as sd
from scipy.io.wavfile import write
from faster_whisper import WhisperModel
from command_router import handle_command
from agent import send_to_aider

model = WhisperModel(
    "base",
    device="cpu",
    compute_type="int8"
)

sample_rate = 44100
duration = 5

while True:

    print("\n→ Listening... Speak now.")

    audio = sd.rec(
        int(duration * sample_rate),
        samplerate=sample_rate,
        channels=1
    )

    sd.wait()

    write("temp.wav", sample_rate, audio)

    print("✓ Transcribing...")

    segments, info = model.transcribe("temp.wav")

    text = ""

    for segment in segments:
        text += segment.text

    text = text.strip()

    if not text:
        continue

    print(f"\nYou said: {text}")

    running = handle_command(text)

    if running is False:
        break

    if len(text.strip()) > 0:
        send_to_aider(text)