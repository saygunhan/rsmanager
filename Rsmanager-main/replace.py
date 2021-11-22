from pathlib2 import Path

def replace(rep_path,ip,port):
    path = Path("{}".format(rep_path))
    text1 = path.read_text()
    text1 = text1.replace("x", "{}".format(ip))
    path.write_text(text1)
    text2 = path.read_text()
    text2 = text2.replace("y", "{}".format(port))
    path.write_text(text2)

