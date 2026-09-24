from voice import listen, speak
from ai_brain import understand_command
from commands import execute_action


def main():

    speak("Hello. I am ready.")

    while True:

        command = listen()

        if not command:
            continue

        # Stop assistant
        if (
            "stop assistant" in command
            or "close assistant" in command
            or "exit assistant" in command
        ):
            speak("Goodbye.")
            break

        print("\nYou:", command)

        # Send command to Gemini
        result = understand_command(command)

        print("AI:", result)

        action = result.get("action")
        target = result.get("target", "")

        # Unknown command
        if action == "unknown":
            speak("I don't know how to do that yet.")
            continue

        # Execute action
        response = execute_action(action, target)

        print("Assistant:", response)

        # Speak result
        speak(response)


if __name__ == "__main__":
    main()