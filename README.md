# Dr. V² (Doctor V-Squared) - AI Medibot

## Overview
Dr. V² is an AI-powered medical assistant that helps users with:
- **Medical Image Analysis** 🏥
- **Voice-based Symptom Analysis** 🎙️
- **Text-based Medical Consultation** 💬
- **AI-Powered Doctor Responses** 🩺

It supports **both voice and text-based queries** and can analyze medical images for potential conditions.

## Features
- **Voice Interaction:** Uses **Groq's Whisper** for speech recognition.
- **Text-to-Speech:** Converts AI responses into voice using **gTTS**.
- **Medical Image Analysis:** Provides insights based on uploaded medical images.
- **Conversational AI:** Mimics a real doctor for natural interactions.

## Installation Guide
### 1. Clone the Repository
```sh
git clone https://github.com/yourusername/doctor-v2.git
cd doctor-v2
```

### 2. Set Up Virtual Environment
#### Using Conda
```sh
conda create --name myenv python=3.11
conda activate myenv
```
#### Using venv (Alternative)
```sh
python -m venv myenv
source myenv/bin/activate  # On Mac/Linux
myenv\Scripts\activate  # On Windows
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
Create a **.env** file and add your API keys:
```sh
GROQ_API_KEY = "your_groq_api_key"
ELEVENLABS_API_KEY = "your_elevenlabs_api_key"
```

### 5. Install FFmpeg (Windows Users Only)
Dr. V² requires **FFmpeg** for audio processing:
1. Download FFmpeg from [official site](https://ffmpeg.org/download.html).
2. Extract it to `C:\ffmpeg`.
3. Add `C:\ffmpeg\bin` to **System PATH**:
   - Search for "Environment Variables" in Start Menu.
   - Edit the `Path` variable under "System Variables".
   - Add `C:\ffmpeg\bin` and save.

### 6. Run the Application
```sh
python gradio_app.py
```

## Usage
1. Open the **Gradio UI**.
2. Speak or type your symptoms or medical questions.
3. Upload a medical image (optional).
4. Get AI-powered medical insights and voice responses!





