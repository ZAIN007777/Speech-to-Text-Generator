import streamlit as st
import whisper
import numpy as np
from pydub import AudioSegment
from io import BytesIO


# Load Whisper model
@st.cache_resource
def load_whisper_model():
    model = whisper.load_model("base")  # You can use "small", "medium", or "large" for better accuracy
    return model


# Convert UploadedFile to a format Whisper can process
def process_uploaded_file(uploaded_file):
    # Load the audio file using pydub
    audio_bytes = uploaded_file.read()
    audio = AudioSegment.from_file(BytesIO(audio_bytes))
    # Convert to mono and resample to 16kHz
    audio = audio.set_channels(1).set_frame_rate(16000)
    # Convert to a NumPy array
    audio_array = np.array(audio.get_array_of_samples(), dtype=np.float32)
    # Normalize to the range [-1.0, 1.0]
    audio_array /= 32768.0
    return audio_array


# Streamlit App
st.title("🎤 Whisper AI: Real-Time Speech-to-Text App")
st.write("Upload an audio file, and Whisper AI will transcribe it for you!")

# Upload audio file
audio_file = st.file_uploader("Upload an audio file", type=["wav", "mp3", "m4a"])

if audio_file is not None:
    st.audio(audio_file, format="audio/wav")

    # Load Whisper model
    model = load_whisper_model()

    # Transcribe audio
    if st.button("Transcribe Audio"):
        with st.spinner("Transcribing..."):
            # Process the uploaded file
            audio_array = process_uploaded_file(audio_file)
            # Transcribe the audio
            result = model.transcribe(audio_array)
            transcription = result["text"]
            st.success("Transcription Complete!")
            st.text_area("Transcription", transcription, height=200)

            # Download transcription as a text file
            st.download_button(
                label="Download Transcription",
                data=transcription,
                file_name="transcription.txt",
                mime="text/plain"
            )
