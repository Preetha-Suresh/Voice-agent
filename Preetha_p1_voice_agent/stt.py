from faster_whisper import WhisperModel

model = WhisperModel(
    "base",
    device="cpu",
    compute_type="int8"
)

segments, info = model.transcribe("test.wav")

print("Detected language:", info.language)

print("\nTranscription:")

for segment in segments:
    print(segment.text)