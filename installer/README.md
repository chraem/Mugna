# Creating Your Own Installer With auto-py-to-exe
1. Install `auto-py-to-exe`.

`pipenv install auto-py-to-exe`

2. Run auto-py-to-exe.
`pipenv run auto-py-to-exe`
> This will prompt a UI to help you convert the `main.py` into executable file much easier.

3. Fill the form based on your preference or you may as well do what I did.

| Action | Input |
| ------- | ------- |
| Scipt Location: | path/to/mugna_raw/main.py |
| (--onedir / --onefile) | One Directory |
| (--console / --windowed) | Window Based |
| Icon | path/to/mugna_raw/cat.ico |
| General Options --name | mugna_setup |

4. Convert `.py` to `.exe`.

6. Open the mugna_setup folder.

8. From mugna_raw directory, copy the mugna folder inside mugna_setup.

10. You may now run the executable file.

 > If you want to keep things more organized, try [inno setup](https://jrsoftware.org/isdl.php).

# Provided Installer
To cut the hassle I provided the installer [here](https://github.com/chraem/Mugna/blob/main/installer/Mugna%20Setup.exe).

# Trigerring Anti-Virus 
You may want to read this:
- [My Antivirus Detected the exe as a Virus](https://nitratine.net/blog/post/issues-when-using-auto-py-to-exe/#my-antivirus-detected-the-exe-as-a-virus)
- [Direct issue on pyinstaller github repository](https://github.com/pyinstaller/pyinstaller/issues/2501#issuecomment-286230354)
- [Community score from virustotal.com](https://www.virustotal.com/gui/file/f94140a95bb613c79e66e01b430acd2eab8c27af4e3a9b280b061b916f79cf81/detection)
