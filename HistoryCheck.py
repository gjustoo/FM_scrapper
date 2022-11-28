def check_uid(uid):
    lines = None
    with open('uids.txt','r') as f:
        lines = f.readlines()
        lines = [line[:-1] for line in lines]
    if uid in lines:
        return True
    else:
        return False

def save_uid(uid):
    with open('uids.txt', 'a') as f:
        f.write(uid + '\n')
