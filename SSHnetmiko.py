import netmiko
import time


def ssh_open_connect(ip, unit_ip):
    try:
        user_name = "your_username"
        pass_word = "your_password"
        # cmd_file = "config.txt"
        from netmiko import ConnectHandler
        session = ConnectHandler( device_type='cisco_ios', ip=ip , username=user_name , password=pass_word)

        output = session.find_prompt() # Showing Prompt current position
        session.config_mode() #Enter Config Terminal
        print output
        command_make = "line vty 0 25\n no access 1 in" #command to send to device
        print command_make
        output = session.send_command(command_make)
        print output
        output = session.send_command("do wr")
        print output



       # backups_file.close()

    except netmiko.NetMikoAuthenticationException:
        print "%s Not connected" % ip

    except netmiko.NetMikoTimeoutException

start_ip = input("PLEASE WRITE START IP: ")
end_ip = input("PLEASE WRITE END IP: ")
for i in xrange(start_ip, end_ip+1):
    ssh_open_connect("182.24."+str(i)+".1",i)



# Script By Mohsen Abedi ( Mohsenabedi.net )






