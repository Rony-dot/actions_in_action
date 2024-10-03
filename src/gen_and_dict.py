
def func_1_v():
  print("from func_1_v")

def func_2_v():
  print("from func_2_v")

def func_3_v():
  print("from func_3_v")

dict_func = {
  "func_1_k" : func_1_v,
  "func_2_k" : func_2_v,
  "func_3_k" : func_3_v,
}

print(dict_func.get("func_1_k"))
# for i in range(len(dict_func)):
#   print(dict_func[i])

for k,v in dict_func.items():
  print(f"key: {k},and val: {v}\n")
  print(dir(dict_func.get(k)))
  dict_func.get(k)

