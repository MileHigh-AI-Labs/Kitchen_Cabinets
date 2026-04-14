' Launches email_server.py silently (no terminal window) in the background.
' Used by the Windows Startup shortcut so the server starts automatically on login.
Set WshShell = CreateObject("WScript.Shell")
WshShell.CurrentDirectory = "C:\Users\ravit\Desktop\Staging\Kitchen_Cabinets"
WshShell.Run "pythonw email_server.py", 0, False
