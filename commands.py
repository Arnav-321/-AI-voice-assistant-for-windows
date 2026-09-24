import subprocess
import os
import webbrowser
import pyautogui
import time
import ctypes
import shutil
import glob


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def chrome_open():
    chrome_paths = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        os.path.expandvars(
            r"%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe"
        )
    ]

    for path in chrome_paths:
        if os.path.exists(path):
            subprocess.Popen([path])
            return True

    return False


def get_chrome_path():
    chrome_paths = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        os.path.expandvars(
            r"%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe"
        )
    ]

    for path in chrome_paths:
        if os.path.exists(path):
            return path

    return None


def get_user_folder(folder_name):
    home = os.path.expanduser("~")

    folders = {
        "desktop": os.path.join(home, "Desktop"),
        "downloads": os.path.join(home, "Downloads"),
        "documents": os.path.join(home, "Documents"),
        "pictures": os.path.join(home, "Pictures"),
        "videos": os.path.join(home, "Videos"),
        "music": os.path.join(home, "Music")
    }

    return folders.get(folder_name.lower().strip())


# ============================================================
# MAIN ACTION EXECUTOR
# ============================================================

def execute_action(action, target):

    action = action.lower().strip()
    target = target.strip()

    print(f"Action: {action}")
    print(f"Target: {target}")

    # ========================================================
    # OPEN APPLICATION
    # ========================================================

    if action == "open_app":

        app = target.lower().strip()

        if app == "notepad":
            subprocess.Popen("notepad.exe")
            return "Notepad opened."

        elif app == "calculator":
            subprocess.Popen("calc.exe")
            return "Calculator opened."

        elif app == "chrome":

            if chrome_open():
                return "Chrome opened."

            return "Chrome was not found."

        elif app in ["vs code", "visual studio code", "vscode"]:

            try:
                subprocess.Popen("code")
                return "Visual Studio Code opened."
            except:
                return "Visual Studio Code was not found."

        elif app == "paint":
            subprocess.Popen("mspaint.exe")
            return "Paint opened."

        elif app in ["file explorer", "explorer"]:
            subprocess.Popen("explorer.exe")
            return "File Explorer opened."

        elif app == "settings":
            subprocess.Popen("start ms-settings:", shell=True)
            return "Windows Settings opened."

        elif app == "task manager":
            subprocess.Popen("taskmgr.exe")
            return "Task Manager opened."

        elif app == "control panel":
            subprocess.Popen("control.exe")
            return "Control Panel opened."

        elif app in ["cmd", "command prompt"]:
            subprocess.Popen("cmd.exe")
            return "Command Prompt opened."

        elif app == "powershell":
            subprocess.Popen("powershell.exe")
            return "PowerShell opened."

        else:
            return f"I don't know how to open {target} yet."

    # ========================================================
    # CLOSE APPLICATION
    # ========================================================

    elif action == "close_app":

        app = target.lower().strip()

        processes = {
            "notepad": "notepad.exe",
            "calculator": "CalculatorApp.exe",
            "chrome": "chrome.exe",
            "paint": "mspaint.exe",
            "file explorer": "explorer.exe",
            "explorer": "explorer.exe",
            "task manager": "Taskmgr.exe",
            "cmd": "cmd.exe",
            "command prompt": "cmd.exe",
            "powershell": "powershell.exe"
        }

        process = processes.get(app)

        if not process:
            return f"I don't know how to close {target}."

        try:
            subprocess.run(
                ["taskkill", "/IM", process, "/F"],
                capture_output=True
            )

            return f"{target} closed."

        except Exception as e:
            print("Close error:", e)
            return f"I could not close {target}."

    # ========================================================
    # OPEN FOLDER
    # ========================================================

    elif action == "open_folder":

        folder = get_user_folder(target)

        if not folder:
            return f"I don't know that folder."

        if os.path.exists(folder):
            os.startfile(folder)
            return f"{target} folder opened."

        return f"{target} folder was not found."

    # ========================================================
    # CREATE FOLDER
    # ========================================================

    elif action == "create_folder":

        folder_name = target.strip()

        if not folder_name:
            return "No folder name was provided."

        desktop = get_user_folder("desktop")
        folder_path = os.path.join(desktop, folder_name)

        try:
            os.makedirs(folder_path, exist_ok=True)
            return f"Folder {folder_name} created on the desktop."

        except Exception as e:
            print("Folder error:", e)
            return "I could not create the folder."

    # ========================================================
    # CREATE TEXT FILE
    # ========================================================

    elif action == "create_file":

        filename = target.strip()

        if not filename:
            return "No file name was provided."

        if not filename.lower().endswith(".txt"):
            filename += ".txt"

        desktop = get_user_folder("desktop")
        file_path = os.path.join(desktop, filename)

        try:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write("")

            return f"{filename} created on the desktop."

        except Exception as e:
            print("File creation error:", e)
            return "I could not create the file."

    # ========================================================
    # SEARCH FILE
    # ========================================================

    elif action == "search_file":

        filename = target.strip()

        if not filename:
            return "No file name was provided."

        search_locations = [
            get_user_folder("desktop"),
            get_user_folder("downloads"),
            get_user_folder("documents"),
            get_user_folder("pictures")
        ]

        matches = []

        for location in search_locations:

            if not location or not os.path.exists(location):
                continue

            pattern = os.path.join(location, "**", f"*{filename}*")

            matches.extend(
                glob.glob(pattern, recursive=True)
            )

        if not matches:
            return f"I could not find {filename}."

        first_file = matches[0]

        os.startfile(first_file)

        return f"I found and opened {os.path.basename(first_file)}."

    # ========================================================
    # RENAME FILE
    # ========================================================

    elif action == "rename_file":

        # Target format:
        # old name | new name

        if "|" not in target:
            return "Please provide the old and new file names."

        old_name, new_name = target.split("|", 1)

        old_name = old_name.strip()
        new_name = new_name.strip()

        search_locations = [
            get_user_folder("desktop"),
            get_user_folder("downloads"),
            get_user_folder("documents")
        ]

        for location in search_locations:

            pattern = os.path.join(
                location,
                "**",
                old_name
            )

            matches = glob.glob(
                pattern,
                recursive=True
            )

            if matches:

                old_path = matches[0]
                new_path = os.path.join(
                    os.path.dirname(old_path),
                    new_name
                )

                try:
                    os.rename(old_path, new_path)

                    return f"{old_name} renamed to {new_name}."

                except Exception as e:
                    print("Rename error:", e)
                    return "I could not rename the file."

        return f"I could not find {old_name}."

    # ========================================================
    # COPY FILE
    # ========================================================

    elif action == "copy_file":

        # Format:
        # source | destination folder

        if "|" not in target:
            return "Please provide the file and destination."

        source, destination = target.split("|", 1)

        source = source.strip()
        destination = destination.strip()

        search_locations = [
            get_user_folder("desktop"),
            get_user_folder("downloads"),
            get_user_folder("documents")
        ]

        source_path = None

        for location in search_locations:

            pattern = os.path.join(
                location,
                "**",
                source
            )

            matches = glob.glob(
                pattern,
                recursive=True
            )

            if matches:
                source_path = matches[0]
                break

        destination_path = get_user_folder(destination)

        if not source_path:
            return f"I could not find {source}."

        if not destination_path:
            return f"I don't know the destination folder {destination}."

        try:

            shutil.copy2(
                source_path,
                destination_path
            )

            return f"{source} copied to {destination}."

        except Exception as e:

            print("Copy error:", e)
            return "I could not copy the file."

    # ========================================================
    # MOVE FILE
    # ========================================================

    elif action == "move_file":

        if "|" not in target:
            return "Please provide the file and destination."

        source, destination = target.split("|", 1)

        source = source.strip()
        destination = destination.strip()

        search_locations = [
            get_user_folder("desktop"),
            get_user_folder("downloads"),
            get_user_folder("documents")
        ]

        source_path = None

        for location in search_locations:

            pattern = os.path.join(
                location,
                "**",
                source
            )

            matches = glob.glob(
                pattern,
                recursive=True
            )

            if matches:
                source_path = matches[0]
                break

        destination_path = get_user_folder(destination)

        if not source_path:
            return f"I could not find {source}."

        if not destination_path:
            return f"I don't know the destination folder {destination}."

        try:

            shutil.move(
                source_path,
                destination_path
            )

            return f"{source} moved to {destination}."

        except Exception as e:

            print("Move error:", e)
            return "I could not move the file."

    # ========================================================
    # DELETE FILE
    # ========================================================

    elif action == "delete_file":

        filename = target.strip()

        if not filename:
            return "No file was specified."

        search_locations = [
            get_user_folder("desktop"),
            get_user_folder("downloads"),
            get_user_folder("documents")
        ]

        for location in search_locations:

            pattern = os.path.join(
                location,
                "**",
                filename
            )

            matches = glob.glob(
                pattern,
                recursive=True
            )

            if matches:

                file_path = matches[0]

                try:

                    # Move to Recycle Bin instead of permanent deletion.
                    import send2trash

                    send2trash.send2trash(file_path)

                    return f"{filename} moved to the Recycle Bin."

                except ImportError:

                    return (
                        "File deletion requires the send2trash package."
                    )

                except Exception as e:

                    print("Delete error:", e)
                    return "I could not delete the file."

        return f"I could not find {filename}."

    # ========================================================
    # SEARCH WEB
    # ========================================================

    elif action == "search_web":

        if not target:
            return "I don't know what to search for."

        url = (
            "https://www.google.com/search?q="
            + target.replace(" ", "+")
        )

        webbrowser.open(url)

        return f"Searching Google for {target}."

    # ========================================================
    # OPEN WEBSITE
    # ========================================================

    elif action == "open_website":

        if not target:
            return "No website was specified."

        if not target.startswith("http"):
            target = "https://" + target

        webbrowser.open(target)

        return "Website opened."

    # ========================================================
    # CHROME HOME
    # ========================================================

    elif action == "browser_home":

        if not chrome_open():
            return "Chrome was not found."

        return "Chrome opened."

    # ========================================================
    # CHROME NEW TAB
    # ========================================================

    elif action == "browser_new_tab":

        pyautogui.hotkey("ctrl", "l")
        pyautogui.hotkey("ctrl", "t")

        return "New Chrome tab opened."

    # ========================================================
    # CHROME CLOSE TAB
    # ========================================================

    elif action == "browser_close_tab":

        pyautogui.hotkey("ctrl", "w")

        return "Chrome tab closed."

    # ========================================================
    # CHROME NEXT TAB
    # ========================================================

    elif action == "browser_next_tab":

        pyautogui.hotkey("ctrl", "tab")

        return "Next Chrome tab selected."

    # ========================================================
    # CHROME PREVIOUS TAB
    # ========================================================

    elif action == "browser_previous_tab":

        pyautogui.hotkey("ctrl", "shift", "tab")

        return "Previous Chrome tab selected."

    # ========================================================
    # CHROME TAB NUMBER
    # ========================================================

    elif action == "browser_tab_number":

        try:

            number = int(target)

            if 1 <= number <= 8:

                pyautogui.hotkey(
                    "ctrl",
                    str(number)
                )

                return f"Chrome tab {number} selected."

            return "Chrome supports tab numbers from 1 to 8."

        except:

            return "Invalid tab number."

    # ========================================================
    # CHROME BACK
    # ========================================================

    elif action == "browser_back":

        pyautogui.hotkey("alt", "left")

        return "Going back."

    # ========================================================
    # CHROME FORWARD
    # ========================================================

    elif action == "browser_forward":

        pyautogui.hotkey("alt", "right")

        return "Going forward."

    # ========================================================
    # CHROME REFRESH
    # ========================================================

    elif action == "browser_refresh":

        pyautogui.press("f5")

        return "Page refreshed."

    # ========================================================
    # CHROME DOWNLOADS
    # ========================================================

    elif action == "browser_downloads":

        pyautogui.hotkey("ctrl", "l")

        pyautogui.write(
            "chrome://downloads/",
            interval=0.01
        )

        pyautogui.press("enter")

        return "Chrome Downloads opened."

    # ========================================================
    # CHROME HISTORY
    # ========================================================

    elif action == "browser_history":

        pyautogui.hotkey("ctrl", "l")

        pyautogui.write(
            "chrome://history/",
            interval=0.01
        )

        pyautogui.press("enter")

        return "Chrome History opened."

    # ========================================================
    # CHROME BOOKMARKS
    # ========================================================

    elif action == "browser_bookmarks":

        pyautogui.hotkey("ctrl", "l")

        pyautogui.write(
            "chrome://bookmarks/",
            interval=0.01
        )

        pyautogui.press("enter")

        return "Chrome Bookmarks opened."

    # ========================================================
    # CHROME SETTINGS
    # ========================================================

    elif action == "browser_settings":

        pyautogui.hotkey("ctrl", "l")

        pyautogui.write(
            "chrome://settings/",
            interval=0.01
        )

        pyautogui.press("enter")

        return "Chrome Settings opened."

    # ========================================================
    # CHROME SEARCH
    # ========================================================

    elif action == "browser_search":

        if not target:
            return "I don't know what to search for."

        pyautogui.hotkey("ctrl", "l")

        pyautogui.write(
            target,
            interval=0.02
        )

        pyautogui.press("enter")

        return f"Searching for {target}."

    # ========================================================
    # OPEN URL IN CHROME
    # ========================================================

    elif action == "browser_open_url":

        if not chrome_open():
            return "Chrome was not found."

        time.sleep(1)

        pyautogui.hotkey("ctrl", "l")

        pyautogui.write(
            target,
            interval=0.01
        )

        pyautogui.press("enter")

        return "Website opened in Chrome."

    # ========================================================
    # BROWSER SEARCH RESULT
    # ========================================================

    elif action == "browser_result":

        try:

            number = int(target)

            if number < 1:
                return "Invalid result number."

            # Give Google time to display the results.
            time.sleep(2)

            # Google search pages can be navigated
            # with the keyboard.
            pyautogui.press(
                "tab",
                presses=number,
                interval=0.2
            )

            pyautogui.press("enter")

            return f"Opened search result {number}."

        except Exception as e:

            print("Result selection error:", e)

            return "I could not select that search result."

    # ========================================================
    # BROWSER SCROLL
    # ========================================================

    elif action == "browser_scroll":

        try:

            amount = int(target)

            pyautogui.scroll(amount)

            if amount > 0:
                return "Scrolled up."

            return "Scrolled down."

        except:

            return "I could not scroll the page."

    # ========================================================
    # BROWSER ZOOM IN
    # ========================================================

    elif action == "browser_zoom_in":

        pyautogui.hotkey("ctrl", "+")

        return "Browser zoom increased."

    # ========================================================
    # BROWSER ZOOM OUT
    # ========================================================

    elif action == "browser_zoom_out":

        pyautogui.hotkey("ctrl", "-")

        return "Browser zoom decreased."

    # ========================================================
    # BROWSER RESET ZOOM
    # ========================================================

    elif action == "browser_zoom_reset":

        pyautogui.hotkey("ctrl", "0")

        return "Browser zoom reset."

    # ========================================================
    # TYPE TEXT
    # ========================================================

    elif action == "type_text":

        if not target:
            return "There is no text to type."

        pyautogui.write(
            target,
            interval=0.03
        )

        return "Text typed."

    # ========================================================
    # PRESS KEY
    # ========================================================

    elif action == "press_key":

        if not target:
            return "No key was specified."

        key = target.lower().strip()

        try:

            if "+" in key:

                keys = key.split("+")
                pyautogui.hotkey(*keys)

                return f"Pressed {target}."

            pyautogui.press(key)

            return f"Pressed {target}."

        except Exception as e:

            print("Keyboard error:", e)

            return f"I could not press {target}."

    # ========================================================
    # MOUSE CLICK
    # ========================================================

    elif action == "mouse_click":

        pyautogui.click()

        return "Clicked."

    # ========================================================
    # DOUBLE CLICK
    # ========================================================

    elif action == "mouse_double_click":

        pyautogui.doubleClick()

        return "Double clicked."

    # ========================================================
    # RIGHT CLICK
    # ========================================================

    elif action == "mouse_right_click":

        pyautogui.rightClick()

        return "Right clicked."

    # ========================================================
    # MOVE MOUSE
    # ========================================================

    elif action == "mouse_move":

        try:

            parts = (
                target
                .replace(",", " ")
                .split()
            )

            if len(parts) != 2:
                return "Please provide X and Y coordinates."

            x = int(parts[0])
            y = int(parts[1])

            pyautogui.moveTo(
                x,
                y,
                duration=0.3
            )

            return f"Mouse moved to {x}, {y}."

        except Exception as e:

            print("Mouse error:", e)

            return "I could not move the mouse."

    # ========================================================
    # MOUSE SCROLL
    # ========================================================

    elif action == "mouse_scroll":

        try:

            amount = int(target)

            pyautogui.scroll(amount)

            if amount > 0:
                return "Scrolled up."

            return "Scrolled down."

        except:

            return "I could not scroll."

    # ========================================================
    # MINIMIZE
    # ========================================================

    elif action == "minimize_window":

        pyautogui.hotkey(
            "alt",
            "space"
        )

        time.sleep(0.2)

        pyautogui.press("n")

        return "Window minimized."

    # ========================================================
    # MAXIMIZE
    # ========================================================

    elif action == "maximize_window":

        pyautogui.hotkey(
            "alt",
            "space"
        )

        time.sleep(0.2)

        pyautogui.press("x")

        return "Window maximized."

    # ========================================================
    # CLOSE CURRENT WINDOW
    # ========================================================

    elif action == "close_window":

        pyautogui.hotkey(
            "alt",
            "f4"
        )

        return "Window closed."

    # ========================================================
    # SWITCH WINDOW
    # ========================================================

    elif action == "switch_window":

        pyautogui.hotkey(
            "alt",
            "tab"
        )

        return "Window switched."

    # ========================================================
    # SHOW DESKTOP
    # ========================================================

    elif action == "show_desktop":

        pyautogui.hotkey(
            "win",
            "d"
        )

        return "Desktop shown."

    # ========================================================
    # VOLUME UP
    # ========================================================

    elif action == "volume_up":

        pyautogui.press(
            "volumeup",
            presses=3,
            interval=0.1
        )

        return "Volume increased."

    # ========================================================
    # VOLUME DOWN
    # ========================================================

    elif action == "volume_down":

        pyautogui.press(
            "volumedown",
            presses=3,
            interval=0.1
        )

        return "Volume decreased."

    # ========================================================
    # MUTE
    # ========================================================

    elif action == "mute":

        pyautogui.press("volumemute")

        return "Volume muted."

    # ========================================================
    # LOCK WINDOWS
    # ========================================================

    elif action == "lock_windows":

        ctypes.windll.user32.LockWorkStation()

        return "Windows locked."

    # ========================================================
    # SCREENSHOT
    # ========================================================

    elif action == "take_screenshot":

        try:

            filename = (
                f"screenshot_"
                f"{int(time.time())}.png"
            )

            pyautogui.screenshot(filename)

            return f"Screenshot saved as {filename}."

        except Exception as e:

            print("Screenshot error:", e)

            return "I could not take the screenshot."

    # ========================================================
    # UNKNOWN
    # ========================================================

    else:

        return "I don't know how to perform that action."