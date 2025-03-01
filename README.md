# Whisper AI with Streamlit

This project integrates OpenAI's Whisper AI with Streamlit for speech recognition.

## Installation

To run this project, install the required dependencies:

```sh
pip install streamlit openai-whisper numpy pydub
```

### Additional Dependencies

Ensure you have `ffmpeg` installed, as `pydub` requires it to process audio files.

#### Install `ffmpeg`:
- **Windows**: Download and install from [FFmpeg website](https://ffmpeg.org/download.html)
- **MacOS**: Install via Homebrew:
  ```sh
  brew install ffmpeg
  ```
- **Linux**: Install via package manager:
  ```sh
  sudo apt update && sudo apt install ffmpeg
  ```

## Usage

Run the Streamlit app with:

```sh
streamlit run app.py
```

## Dependencies

- `streamlit`: For creating the web interface
- `whisper`: OpenAI’s speech recognition model
- `numpy`: For numerical operations
- `pydub`: For handling audio files

## License

This project is open-source and available under the MIT License.

