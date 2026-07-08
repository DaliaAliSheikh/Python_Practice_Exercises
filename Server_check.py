temps = [35, 42, 50, 28, 47]

def check_servers(temps):
    for temp in temps:
        if temp >= 45:
            print(temp, "warning high temp")
        else:
            print(temp, "server status normal")

check_servers(temps)
