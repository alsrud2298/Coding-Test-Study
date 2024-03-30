import re

def solution(new_id):
    clean_id = new_id
    clean_id = clean_id.lower()
    clean_id = re.sub('[^a-z0-9\-_.]','',clean_id)
    clean_id = re.sub('\.+','.',clean_id)
    clean_id = re.sub('^[.]|[.]$','',clean_id)
    clean_id = 'a' if len(clean_id) == 0 else clean_id[:15]
    clean_id = re.sub('^[.]|[.]$','',clean_id)
    clean_id = clean_id if len(clean_id) > 2 else clean_id + "".join([clean_id[-1] for i in range(3-len(clean_id))])
    return clean_id