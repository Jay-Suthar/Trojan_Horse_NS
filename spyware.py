import socket

def trojan():
    HOST = '192.168.233.217'  # ip
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
                print('\n')
                print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n')
                print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n')
                print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n')
                print('@@@@@@@@@@@@@@@@@@@@@@@@B&@@###&@&###&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n')
                print('@@@@@@@@@@@@@@@@@@@@@@@@GG#&BBB&@#BBB&@@##&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n')
                print('@@@@@@@@@@@@@@@@@@@@@@@@GPPGPPPGGGPGGB#BBB#&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n')
                print('@@@@@@@@@@@@@@@@@@@@@@@@GPPPPPPPPPPPPPPPGB&@&##&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n')
                print('@@@@@@@@@@@@@@@@@@@@@@@@GPPPPPPPPPPPPPPPPPGGBBB#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n')
                print('@@@@@@@@@@@@@@@@@@@@@@@@GPPPPPPPPPPPPPPPPPPPP#@@&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n')
                print('@@@@@@@@@@@@@@@@@@@@@@@@GPPPPPPPPGPPPPPPPPPPPGBBBB#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n')
                print('@@@@@@@@@@@@@@@@@@@@@@@@GPPPPPPPB&GPPPPPPPPPPPPB&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n')
                print('@@@@@@@@@@@@@@@@@@@@@@@@GPPPPPPB@@GPPPPPPPPPPPPG&&#&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n')
                print('@@@@@@@@@@@@@@@@@@@@@@@@GPPPPPB@@&GPPPPPPPPPPPPPGBBB&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n')
                print('@@@@@@@@@@@@@@@@@@@@@@@@BGGGG#@@@&GPPPPPPPPPY5PPB@&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n')
                print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&GPPPPPPPPPPPPPGGGGGGGGGGGGGGGGGB#&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n')
                print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&GPBBBBBBBBBBBBGPBBGGBBBBBBBBBBBGPG#BB###&@@@@@@@@@@@@@@@@@@@@@@@@@\n')
                print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&GGBBBBBBBBBBBBBBYJGGBBBBBBBBBBBBPG@@&#BBB#&@@@@@@@@@@@@@@@@@@@@@@@\n')
                print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&GGBBBBBBBBBBBBPJ!7!5BBBBBBBBBBBBPG@@@@#BBB#@@@@@@@@@@@@@@@@@@@@@@@\n')
                print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&GGBBBBBBBBBBBBG57??PBBBBBBBBBBBBPG@@@@&BBBB&@@@@@@@@@@@@@@@@@@@@@@\n')
                print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&GGBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBPG@@@@@BBBB&@@@@@@@@@@@@@@@@@@@@@@\n')
                print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&GGBBBBBBPGGGGGGGGGGGGGGGGGBBBBBBPG@@@@@BBBB&@@@@@@@@@@@@@@@@@@@@@@\n')
                print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&GGBBBBGPG&@@@@@@@@@@@@@@&GPBBBBBPG@@@@@BBBB&@@@@@@@@@@@@@@@@@@@@@@\n')
                print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&GGBBBGPB@@@@@@@@@@@@@@@@@&GPBBBBPG@@@@@BBBB&@@@@@@@@@@@@@@@@@@@@@@\n')
                print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&GPBBGPB@@@@@@@@@@@@@@@@@@@&GPGBBPG@@@@@BBBB&@@@@@@@@@@@@@@@@@@@@@@\n')
                print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&BBGPPPPP#@@@@@@@@@@@@@@@@@@@@@@BPPPPPBB#&@&&&&@@@@@@@@@@@@@@@@@@@@@@@\n')
                print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@&GPPPPPPPPG&@@@@@@@@@@@@@@@@@@@@@@#PPPPPPPPPB&@@@@@@@@@@@@@@@@@@@@@@@@@@\n')
                print('@@@@@@@@@@@@@@@@@@@@@@@@@@@&GPPGBBBBPPPG#&&&&&&&&&&&&&&&&&&&&#PPPGBBBBPPPG@@@@@@@@@@@@@@@@@@@@@@@@@@\n')
                print('@@@@@@@@@@@@@@@@@@@@@@@@@@@&PPPGBBBBPPPG#####################BPPPGBBBBGPPG@@@@@@@@@@@@@@@@@@@@@@@@@@\n')
                print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@#GPPPGGPPPG&@@@@@@@@@@@@@@@@@@@@@@#GPPPGGPPPG&@@@@@@@@@@@@@@@@@@@@@@@@@@\n')
                print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&#BGGGGB#@@@@@@@@@@@@@@@@@@@@@@@@@&#BGGGGB#@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n')
                print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n')
                print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n')
                print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n')
                
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

        
