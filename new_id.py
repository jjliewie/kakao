import re

def solution(new_id):
#     first step
    new_id = new_id.lower()
#     second step
    new_id = re.sub('[^a-z0-9-_.]', '', new_id)
#     third step
    new_id = re.sub('\.+', '.', new_id)
#     fourth step
    new_id = re.sub('^[.]|[.]$', '', new_id)
#     fifth step
    if not new_id:
        new_id = 'a'
#     sixth step
    if len(new_id) > 15:
        new_id = new_id[:15]
    new_id = re.sub('^[.]|[.]$', '', new_id)
#     seventh step
    while len(new_id) < 3:
        new_id += new_id[len(new_id)-1]

    answer = new_id
    return answer
