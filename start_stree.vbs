Set WshShell = CreateObject("WScript.Shell")

WshShell.CurrentDirectory = "C:\Users\Arnav kumar\OneDrive\Desktop\AI-Voice-Assistant"

WshShell.Run """C:\Users\Arnav kumar\OneDrive\Desktop\AI-Voice-Assistant\venv\Scripts\pythonw.exe"" ""C:\Users\Arnav kumar\OneDrive\Desktop\AI-Voice-Assistant\stree.py""", 0, False

Set WshShell = Nothing