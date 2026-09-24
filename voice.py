import speech_recognition as sr
import subprocess


recognizer = sr.Recognizer()

recognizer.energy_threshold = 300
recognizer.dynamic_energy_threshold = True
recognizer.pause_threshold = 0.5
recognizer.non_speaking_duration = 0.5


def speak(text):

    print("Stree:", text)

    safe_text = text.replace("'", "''")

    powershell_command = f"""
Add-Type -AssemblyName System.Speech
$speaker = New-Object System.Speech.Synthesis.SpeechSynthesizer
$speaker.Volume = 100
$speaker.Rate = 0
$speaker.Speak('{safe_text}')
$speaker.Dispose()
"""

    try:

        subprocess.run(
            [
                "powershell.exe",
                "-NoProfile",
                "-Command",
                powershell_command
            ],
            creationflags=subprocess.CREATE_NO_WINDOW
        )

    except Exception as e:

        print("Speech error:", e)


def listen(timeout=None, phrase_time_limit=4):

    with sr.Microphone() as source:

        print("🎤 Listening...")

        try:

            audio = recognizer.listen(
                source,
                timeout=timeout,
                phrase_time_limit=phrase_time_limit
            )

        except sr.WaitTimeoutError:

            print("Timeout - no speech.")

            return ""

    try:

        command = recognizer.recognize_google(audio)

        print("Recognized:", command)

        return command.lower().strip()

    except sr.UnknownValueError:

        print("Could not understand speech.")

        return ""

    except sr.RequestError as e:

        print("Speech recognition error:", e)

        return ""