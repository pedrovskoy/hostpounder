path = 'C:\\Windows\\System32\\Drivers\\etc\\hosts'
query = 'spclient.wg.spotify.com'

with open(path, "r") as hosts_file:
    data = hosts_file.readlines()
    
def find(data, query):
    """Returns query's index in the file"""
    for line in data:
        if query in line:
            q_index = data.index(line)
    return(q_index)

t_index = find(data, query)

def toggle(data, t_index):
    """ Adds or remove hash character
    as first character in the line """
    target = data[t_index]
    if target.startswith('#'):
        target_update = target[1:]
        data[t_index] = target_update
        print("Toggled off.\n")
    else:
        target_update = '#' + target
        data[t_index] = target_update
        print("Toggled on.\n")
    return(data)

with open(path, "w") as hosts_file:
    toggle(data, t_index)
    hosts_file.writelines(data)
