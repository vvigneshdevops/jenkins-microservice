'''hosts = ['host1', 'host2', 'host3', 'host7', 'host8', 'host11', 'host12']
groups = []

current_group = []
for host in sorted(hosts):
    host_num = int(host[4:])  # extract the host number from the string
    if len(current_group) == 0:
        current_group.append(host)
    else:
        prev_host_num = int(current_group[-1][4:])
        if host_num == prev_host_num + 1:
            current_group.append(host)
        else:
            groups.append(current_group)
            current_group = [host]

# add the last group
groups.append(current_group)

output = '_'.join(['{}-{}'.format(group[0], group[-1]) for group in groups])
print(output)

hosts = ['host1', 'host2', 'host3', 'host7', 'host8', 'host11', 'host12']
groups = []

current_group = []
prev_host_num = None  # initialize to None for the first host
for host in sorted(hosts):
    host_num = int(host[4:])  # extract the host number from the string
    if len(current_group) == 0:
        current_group.append(host)
        prev_host_num = host_num  # update the previous host number
    else:
        if host_num == prev_host_num + 1:
            current_group.append(host)
            prev_host_num = host_num  # update the previous host number
        else:
            groups.append(current_group)
            current_group = [host]
            prev_host_num = host_num  # update the previous host number

# add the last group
groups.append(current_group)

output = '_'.join(['{}-{}'.format(group[0], group[-1]) for group in groups])
print(output)
'''

hosts = ['host1', 'host2', 'host3', 'host7', 'host8', 'host9', 'host12', 'host13']

ranges = []
start = None
prev = None

for host in sorted(hosts):
    num = int(host[4:])
    if start is None:
        start = num
    elif num != prev + 1:
        ranges.append((start, prev))
        start = num
    prev = num

ranges.append((start, prev))
result = '_'.join([f'host{start}-{end}' for start, end in ranges])

print(result)
