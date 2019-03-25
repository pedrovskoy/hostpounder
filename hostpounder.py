import ctypes
import fileinput
import sys

query = 'spclient.wg.spotify.com'

# Detect platform
if sys.platform.startswith('win32'):
    def is_admin():
        """Check whether program is running with admin privileges"""
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

    if is_admin():
        path = 'C:\\Windows\\System32\\Drivers\\etc\\hosts'
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)

elif sys.platform.startswith('linux'):
    path = '/etc/hosts'

# Open hosts file
with open(path, "r") as hosts_file:
    data = hosts_file.readlines()

# Define functions to locate query and toggle hash character
def find(data, query):
    """Return index of query in the file"""
    for line in data:
        if query in line:
            query_index = data.index(line)
            break
    return query_index

def toggle(data, target_index):
    """ Add or remove hash character
    as first character in the line """
    target = data[target_index]
    if target.startswith('#'):
        target_update = target[1:]
        data[target_index] = target_update
        print("Toggled off.\n")
    else:
        target_update = '#' + target
        data[target_index] = target_update
        print("Toggled on.\n")
    return data

# Call find() to retrieve the target index
target_index = find(data, query)

# Write changes to hosts file
with open(path, "w") as hosts_file:
    toggle(data, target_index)
    hosts_file.writelines(data)
