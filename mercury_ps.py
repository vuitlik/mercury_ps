from pyautogui import typewrite

from mercury import mercury, from_chars_to_string, from_arr_to_string

def __uni_print(data, end : str): 
    if data["target"] == "char[]": data["value"] = from_chars_to_string(data["value"])
    elif data["target"].endswith("[]"): data["value"] = from_arr_to_string(data["value"])
    print(data["value"], end = end)
    
__println = lambda params: __uni_print(params[0], '\n')
__print = lambda params: __uni_print(params[0], '')
def __input(params : list): 
    res = {"target" : "char[]", "value" : []}
    for char in input(): res["value"].append({"target" : "char", "value" : char})
    return res

#PyAutoGUI
def __typewrite(params : list): typewrite(params[0]["value"], params[1]["value"])

funcs = {
    "println" : [__println, 1],
    "print" : [__print, 1],
    "input" : [__input, 0],
    "typewrite" : [__typewrite, 2]
}

if __name__ == "__main__": mercury().start(funcs)