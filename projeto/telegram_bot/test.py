answer = {'ok': True, 'result': [{'update_id': 800703034, 'message': {'message_id': 1, 'from': {'id': 6193395827, 'is_bot': False, 'first_name': 'Pavão', 'language_code': 'pt-br'}, 'chat': {'id': 6193395827, 'first_name': 'Pavão', 'type': 'private'}, 'date': 1700500167, 'text': '/start', 'entities': [{'offset': 0, 'length': 6, 'type': 'bot_command'}]}}, {'update_id': 800703035, 'message': {'message_id': 3, 'from': {'id': 6193395827, 'is_bot': False, 'first_name': 'Pavão', 'language_code': 'pt-br'}, 'chat': {'id': 6193395827, 'first_name': 'Pavão', 'type': 'private'}, 'date': 1700500214, 'text': 'Ajuda'}}]}

print("************************")
print(answer["result"][0])

print("************************")
print(answer["result"][-1]["message"]["from"]["first_name"])
print("************************")

print("************************")