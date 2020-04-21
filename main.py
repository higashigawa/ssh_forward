from sshtunnel import SSHTunnelForwarder
from time import sleep

with SSHTunnelForwarder(
    ('172.28.***.***', 22),
    ssh_username="username",
    ssh_password="password",
    remote_bind_address=('172.28.***.***', 3389),
    local_bind_address=('127.0.0.1', 13389)
) as server:

    print(server.local_bind_port)
    print("-------サーバーへ接続中です。-----")
    while True:
        # press Ctrl-C for stopping
        sleep(1)

print('FINISH!')
