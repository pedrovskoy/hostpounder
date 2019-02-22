query = 'spclient.wg.spotify.com'
        
def find(hosts, query):
    for line in hosts:
        if query in line:
            q_index = hosts.index(line)
            break
    return(q_index)

t_index = find(hosts, query)

def toggle(hosts, t_index):
    target = hosts[t_index]
    if target.startswith('#'):
        target_update = target[1:]
        hosts[t_index] = target_update
        print("Toggled off.\n")
    elif target.startswith('0') or target.startswith('1'):
        target_update = '#' + target
        hosts[t_index] = target_update
        print("Toggled on.\n")
    return(hosts)

def toggle_caller(hosts):
    run = input("Enter 'q' to quit\n")
    while run.lower() != 'q':
        toggle(hosts, t_index)
        print("Control: {}".format(hosts[0]))
        run = input("Enter 'q' to quit.\n")

toggle_caller(hosts)
