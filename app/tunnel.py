from sshtunnel import open_tunnel
from time import sleep
from dotenv import load_dotenv
import os

load_dotenv()
with open_tunnel(
    (os.getenv('SSH_HOST'), int(os.getenv('SSH_PORT'))),
    ssh_username=os.getenv('SSH_USER'),
    ssh_password=os.getenv('SSH_PASS'),
    remote_bind_address=(os.getenv('MARIADB_HOST'), int(os.getenv('MARIADB_PORT'))),
    local_bind_address=('', int(os.getenv('LOCAL_PORT')))
) as server:

    db_port = server.local_bind_port
    print("SSH tunnel started. Local bind port:", db_port)
    while True:
        # press Ctrl-C for stopping
        sleep(1)

print('FINISH!')