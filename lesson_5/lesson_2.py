import json

data = {
    'one': 'HELLO',
    'TWO': [1, 2, 3, 'a'],
    1: False,
    2: True,
    3: None,
    4: "ТЕКСТ",
    5: (22, 33),
    # 6: {1, 2, 3, 4} - сет не конвертируемый
}

j_data = json.dumps(data)
print(type(j_data))
print(j_data)

j_data = json.dumps(data, ensure_ascii=False)
with open('test.json', 'w') as file:
    json.dump(data, file)
print(j_data)

enc_data = json.loads(j_data)
print(type(enc_data))
print(enc_data)