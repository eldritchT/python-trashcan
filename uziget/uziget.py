import requests
import html2text
from connect.utils.terminal.markdown import render
import shlex
import playsound

print("UziGet | версия 1.01")

while True:
    cmd, *args = shlex.split(input("> "))

    if cmd == "":
        pass

    if cmd == "check":
        print("[?] Проверка ya.ru")
        r = requests.get("https://ya.ru")
        if r.status_code == 200:
            print(f"[+] Получено 200 (SUCCESS)\n")
        print("[?] Проверка google.ru..")
        r = requests.get("https://google.ru")
        if r.status_code == 200:
            print(f"[+] Получено 200 (SUCCESS)\n")
        print("[?] Проверка httpbin.org..")
        r = requests.get("https://httpbin.org")
        if r.status_code == 200:
            print(f"[+] Получено 200 (SUCCESS)\n")
        print("[?] Проверка kod.ru..")
        r = requests.get("https://kod.ru")
        if r.status_code == 200:
            print(f"[+] Получено 200 (SUCCESS)\n")

    elif cmd == "get":
        if args is not None:
            url = args[0]
            r = requests.get(f"https://{url}")
            print(render(html2text.html2text(r.text)))
        else:
            print(f"Использование: get <url>")

    elif cmd == "exit":
        break
