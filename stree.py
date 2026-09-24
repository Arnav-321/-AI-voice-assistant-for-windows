import time

from voice import listen, speak
from ai_brain import understand_command
from commands import execute_action


WAKE_PHRASE = "hello"


def wait_for_wake_word():

    print("\n================================")
    print("Waiting for 'Hello'...")
    print("================================")

    while True:

        speech = listen(
            timeout=None,
            phrase_time_limit=4
        )

        if not speech:
            continue

        print("Wake listener heard:", speech)

        if WAKE_PHRASE in speech:

            print(">>> WAKE WORD DETECTED <<<")

            return True

def get_command():
    speak("Yes?")
    time.sleep(0.2)

    print("\n================================")
    print("NOW LISTENING FOR COMMAND")
    print("================================")

    command = listen(timeout=5, phrase_time_limit=8)

    print("COMMAND HEARD:", command)

    return command



def process_command(command):

    if not command:

        speak("I didn't hear a command.")

        return True

    command = command.lower().strip()

    print("Processing:", command)

    # ==========================================
    # STOP STREE
    # ==========================================

    stop_commands = [
        "close assistant",
        "close assistance",
        "stop assistant",
        "stop assistance",
        "exit assistant",
        "exit assistance",
        "close stree",
        "stop stree",
        "exit stree"
    ]

    for stop_command in stop_commands:

        if stop_command in command:

            speak("Goodbye.")

            return False

    # ==========================================
    # GEMINI
    # ==========================================

    print("Sending command to Gemini...")

    result = understand_command(command)

    print("Gemini result:", result)

    action = result.get("action")
    target = result.get("target", "")

    # ==========================================
    # UNKNOWN
    # ==========================================

    if action == "unknown":

        speak("I don't know how to do that yet.")

        return True

    # ==========================================
    # EXECUTE
    # ==========================================

    print("Executing:", action, target)

    response = execute_action(
        action,
        target
    )

    print("Action result:", response)

    speak(response)

    return True


def main():

    speak("Stree is ready.")

    running = True

    while running:

        try:

            # ----------------------------------
            # WAIT FOR HELLO
            # ----------------------------------

            wait_for_wake_word()

            # ----------------------------------
            # LISTEN FOR COMMAND
            # ----------------------------------

            command = get_command()

            # ----------------------------------
            # PROCESS COMMAND
            # ----------------------------------

            running = process_command(command)

            time.sleep(0.5)

        except KeyboardInterrupt:

            print("\nStree stopped.")

            break

        except Exception as e:

            print("\nERROR:", e)

            speak("Something went wrong.")

            time.sleep(2)


if __name__ == "__main__":
    main()