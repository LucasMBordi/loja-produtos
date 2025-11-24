import datetime

def registrar_log(msg: str):
    agora = datetime.datetime.now().strftime("%Y-%M-%D %H:%M:%S")
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(f"[{agora} {msg} \n]")