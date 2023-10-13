from socket import socket, AF_INET, SOCK_STREAM, gethostname, gethostbyname
from json import loads, dumps

class mercury:
    def __init__(self, ip = gethostbyname(gethostname()), port = 55000): 
        self.__server_unit = socket(AF_INET, SOCK_STREAM)
        self.__server_unit.bind((ip, port))
        self.__server_unit.listen(1)
    def start(self, funcs : dict):
        while True:
            client_unit, address = self.__server_unit.accept()
            data = loads(client_unit.recv(1024).decode("utf-8"))

            if data["name"] not in funcs: client_unit.send(dumps({"family" : 9, "error" : 2, "info" : f"function name - \"{data['name']}\""}).encode("utf-8"))
            elif len(data["args"]) != funcs[data["name"]][1]: client_unit.send(dumps({"family" : 9, "error" : 2, "info" : f"function name - \"{data['name']}\", provided parameters count - {len(data['args'])}, function parameters count - {funcs[data['name']][1]}"}).encode("utf-8"))
            else:
                res = funcs[data["name"]][0](data["args"]) 
                if res == None: res = {"target" : "int", "value" : 0}
                client_unit.send(dumps(res).encode("utf-8"))

def from_chars_to_string(chars : list):
    res = ''
    for char in chars: res += char["value"]
    return res
def from_arr_to_string(arr : list):
    res = []
    for el in arr: 
        if el["target"].endswith("[]"): el["value"] = from_arr_to_string(el["value"])
        res.append(str(el["value"]))
    return '{' + ", ".join(res) + '}'