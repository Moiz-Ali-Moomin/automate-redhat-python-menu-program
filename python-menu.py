import os
while True:
        os.system("sudo clear")
        os.system("tput setaf 2")
        print("`````````````````````````````````````````````````````````````````Python Command Menu```````````````````````````````````````````````````````````")
        os.system("tput setaf 7")
        print()
        width = os.get_terminal_size().columns
        print("""
                                              Type "A" -> TO GET THE COMMANDS TO CREATE WEBSITE
                                              Type "B" -> TO GET THE COMMANDS FOR REDHAT
											  Type "C" -> TO GET THE COMMANDS FOR DOCKER
                                              Type "D" -> TO SETUP and INSTALL SOFTWARE WITH YUM
                                              Type "E" -> TO EXIT FORM THE PYTHON MENU PROGRAM\n\n""".center(width))			   
        a = input()

	
        if a == "A":
            while True:
                os.system("clear")
                os.system("tput setaf 2")
                print("`````````````````````````````````````````````````````````````````Welcome to the httpd configuration```````````````````````````````````````````````````````````")
                os.system("tput setaf 7")
                print()
                b = int(input("""
Press 1 : To download the httpd software
Press 2 : Start the httpd service
Press 3 : Disabled the firewall service
Press 4 : Create an website page
Press 5 : See the content of webpage
Press 6 : Deliver the content on browser
Press 7 : To Exit
\n\n"""))
                if b == 1:
                     os.system("sudo yum install httpd -y")
                elif b == 2:
                     os.system("sudo systemctl start httpd")
                     os.system("sudo systemctl enable httpd")
                elif b == 3:
                     os.system("sudo systemctl stop firewalld")
                elif b == 4:
                     html_file = input("Name of an html page file: ")
                     os.system("sudo vi /var/www/html/{}.html".format(html_file))
                elif b == 5:
                     html_file = input("Name of an html page file: ")
                     os.system("sudo cat /var/www/html/{}.html".format(html_file))
                elif b == 6:
                     ip_address = input("Enter your IP Address: ")
                     html_file = input("Enter the page name: ")
                     os.system("curl http://{}/{}.html".format(ip_address,html_file))
                elif b == 7:
                    break
                input("Please Enter to continue....")
        elif a == "E":
            os.system("clear")
            os.system("tput setaf 2")
            print("```````````````````````````````````````````````````````````'Thank You'```````````````````````````````````````````````````````````")
            os.system("tput setaf 7")
            print()
            exit()
        elif a == "D":
            while True:
                os.system("clear")
                os.system("tput setaf 2")
                print("```````````````````````````````````````````````````````````'Welcome to the yum configuration'```````````````````````````````````````````````````````````")
                os.system("tput setaf 7")
                print()
                b = int(input("""
Press 1 : Check the Software Name
Press 2 : See the yum configuration details
Press 3 : Check the software name
Press 4 : (Install/Uninstall) the software
Press 5 : List the software in yum
Press 6 : Exit the program
\n\n"""))
                if b == 1:
                    soft = input("Enter the software name: ")
                    os.system("sudo rpm -q {}".format(soft))
                elif b == 2:
                    os.system("sudo yum repolist")
                elif b == 3:
                    command = input("Enter the command name: ")
                    os.system("sudo yum whatprovides {}".format(command))
                elif b == 4:
                    yum_iu = input("Choose what do you want (install/uninstall): ")
                    if yum_iu == "install":
                        soft_name = input("Enter the software name: ")
                        os.system("sudo yum install {} -y".format(soft_name))
                    elif yum_iu == "uninstall":
                        soft_name = input("Enter the software name: ")
                        os.system("sudo yum remove {} -y".format(soft_name))
                elif b == 5:
                    list_item = input("Enter the software name to check: ")
                    os.system("sudo yum list {}".format(list_item))
                elif b == 6:
                    break
                else:
                    print("It is not exist")
                input("Please Enter to continue...")
        elif a == "C":
            while True:
                os.system("clear")
                os.system("tput setaf 2")
                print("```````````````````````````````````````````````````````````'Welcome to the Docker'```````````````````````````````````````````````````````````")
                os.system("tput setaf 7")
                print()
                b = int(input("""Press 1 : See the Version of the docker
Press 2 : List the Images Name of the docker
Press 3 : List all the containers
Press 4 : List the running containers
Press 5 : Download the new images
Press 6 : Search all the images
Press 7 : Start the container with its name or container ID
Press 8 : Stop the container with its name or container ID
Press 9 : Attach the container with itd name or container ID
Press 10 : See the information of the Docker
Press 11 : Remove an container or Image
Press 12 : Remove all the containers
Press 13 : Launch the new container
Press 14 : See the Log of an container
Press 15 : Start the docker services
Press 16 : Stop the docker services
Press 17 : Take Help of the Docker
Press 18 : Exit the Docker Menu 
\n\n"""))
                if b == 1:
                    os.system("sudo docker --version")
                elif b == 2:
                    os.system("sudo docker images")
                elif b == 3:
                    os.system("sudo docker ps -a")
                elif b == 4:
                    os.system("sudo docker ps")
                elif b == 5:
                    image = input("Enter the image name: ")
                    version = input("Enter the version/tag if need: ")
                    os.system("sudo docker pull {}:{}".format(image,version))
                elif b == 6:
                    image = input("Enter the image name: ")
                    os.system("sudo docker search {}".format(image))
                elif b == 7:
                    input_data = input("Enter the container id/name of the container: ")
                    os.system("sudo docker start {}".format(input_data))
                elif b == 8:
                    input_data = input("Enter the container id/name of the container: ")
                    os.system("sudo docker stop {}".format(input_data))
                elif b == 9:
                    input_data = input("Enter the container id/name of the container: ")
                    os.system("sudo docker attach {}".format(input_data))
                elif b == 10:
                    os.system("sudo docker info")
                elif b == 11:
                    input_data = input("What do you choose from delete (container/image): ")
                    if input_data == "container":
                        container = input("Enter the container id/name of the container: ")
                        os.system("sudo docker rm -f {}".format(container))
                    elif input_data == "image":
                        image = input("Enter the image name: ")
                        version = input("Enter the version if need: ")
                        os.system("sudo docker rmi -f {}:{}".format(image,version))
                    else:
                        print("not found in search")
                elif b == 12:
                    os.system("sudo docker rm -f `docker ps -a -q`")
                elif b == 13:
                    image = input("Enter the image name: ")
                    version = input("Enter the version if need: ")
                    name = input("Enter the name of the container if need: ")
                    bash_shell = input("Enter the particular command for use the image if need: ")
                    os.system("sudo docker run -it --name {} {}:{} '{}'".format(name,image,version,bash_shell))
                elif b == 14:
                    input_data = input("Enter the container id/name of an container: ")
                    os.system("sudo docker logs {}".format(input_data))
                elif b == 15:
                    os.system("sudo systemctl start docker")
                    os.system("sudo systemctl enable docker")
                elif b == 16:
                    os.system("sudo systemctl stop docker")
                    os.system("sudo systemctl disable docker")
                elif b == 17:
                    os.system("sudo docker --help")
                elif b == 18:
                    break
                else:
                    print("Not Found")
                input("Please Enter to Continue....")
        
        elif a == "B":
            while True:
                os.system("clear")
                os.system("tput setaf 2")
                print("```````````````````````````````````````````````````````````'Welcome to the RedHat Linux' ```````````````````````````````````````````````````````````")
                os.system("tput setaf 7")
                print()
                b = int(input('''Press 1 : See the date
Press 2 : See the current system calendar
Press 3 : See the calendar with user input
Press 4 : Check the internet connectivity of an IP
Press 5 : See the Stopped program status
Press 6 : For Continue the Stopped program
Press 7 : Make an Directory on system
Press 8 : List of the Files
Press 9 : Create an empty file
Press 10 : See the detailed List of the Files
Press 11 : Open the vim editor
Press 12 : Open the vi editor
Press 13 : Create an new user and its password
Press 14 : See the Current User Name
Press 15 : See the File System in Detail
Press 16 : See the memory/RAM Space of an system
Press 17 : See the live status of every command output
Press 18 : Read the every file
Press 19 : Run the command output using an file
Press 20 : Print the text/command output message
Press 21 : See the location of an command
Press 22 : Getting more information of an particular command
Press 23 : See the IP Address of an Network Card
Press 24 : Open the calculator
Press 25 : Setup the LVM
Press 26 : See the Status of every program
Press 27 : Remove the directory/folder
Press 28 : Exit this Menu\n\n'''))
                if b == 1:
                    os.system("sudo date")
                elif b == 2:
                    os.system("sudo cal")
                elif b == 3:
                    month = input("Enter the Month: ")
                    year = input("Enter the Year: ")
                    os.system("sudo `cal {} {}`".format(month,year))
                elif b == 4:
                    ip = input("Enter the IP Address: ")
                    os.system("ping {}".format(ip))
                elif b == 5:
                    os.system("jobs")
                elif b == 6:
                    os.system("fg")
                elif b == 7:
                    folder = input("Enter the folder name: ")
                    os.system("mkdir {}".format(folder))
                    print("{} Folder Created".format(folder))
                elif b == 8:
                    os.system("ls")
                elif b == 9:
                    file_name = input("Give the text file name")
                    os.system("touch {}.txt".format(file_name))
                    print("{}.txt Empty file Created".format(file_name))
                elif b == 10:
                    os.system("ls -lh")
                elif b == 11:
                    print("Opening the vim Text Editor....")
                    os.system("sudo vim")
                elif b == 12:
                    print("Opening the vi Text Editor....")
                    os.system("vi")
                elif b == 13:
                    user_name = input("Give a user_name: ")
                    os.system("sudo useradd {}".format(user_name))
                    os.system("sudo passwd {}".format(user_name))
                elif b == 14:
                    os.system("whoami")
                elif b == 15:
                    os.system("df -h")
                elif b == 16:
                    os.system("free -m")
                elif b == 17:
                    command = input("Give any command: ")
                    os.system("watch -n 1 {}".format(command))
                elif b == 18:
                    file_name = input("Give the file name: ")
                    os.system("cat {}".format(file_name))
                elif b == 19:
                    filename = input("Give the file name: ")
                    os.system("source {}".format(filename))
                elif b == 20:
                    sc = input("What to do want: (string/command) ")
                    if sc == "string":
                        text = input("Enter a string: ")
                        os.system("echo '{}'".format(text))
                    else:
                        command = input("Enter a command: ")
                        os.system("echo `sudo {}`".format(command))
                elif b == 21:
                    command = input("Enter a command: ")
                    os.system("which {}".format(command))
                elif b == 22:
                    command = input("Enter a command name: ")
                    os.system("man {}".format(command))
                elif b == 23:
                    os.system("ifconfig enp0s3")
                elif b == 24:
                    os.system("bc")
                elif b == 25:
                    while True:
                        os.system("clear")
                        os.system("tput setaf 2")
                        print("```````````````````````````````````````````````````````````'Welcome to the LVM Parititon'```````````````````````````````````````````````````````````")
                        os.system("tput setaf 7")
                        print()
                        print("""\t\t\t\tPress 1 for see the all disks
Press 2 (create/delete) a physical volume
Press 3 display the physical volume
Press 4 (create/delete) the volume group
Press 5 display the volume group
Press 6 (create/delete) the logical volume
Press 7 display the logical volume
Press 8 extend the logical volume
Press 9 (format/continue-format) the logical volume
Press 10 display the filesystem
Press 11 (mount/umount) the logical volume to that particular folder
Press 12 exit the program
\t\t\t\n\n""")
                        c = int(input("Enter your choice: "))
                        if c == 1:
                            os.system("sudo fdisk -l")
                        elif c == 2:
                            disk = input("What you want (create/delete): ")
                            if disk == "create":
                                physical = input("Enter your disk name: ")
                                os.system("sudo pvcreate {}".format(physical))
                            elif disk == "delete":
                                physical = input("Enter your disk name: ")
                                os.system("sudo pvremove {}".format(physical))
                            else:
                                print("Not Found")
                        elif c == 3:
                            physical = input("Enter your disk name: ")
                            os.system("sudo pvdisplay {}".format(physical))
                        elif c == 4:
                            disk = input("What you want (create/delete): ")
                            if disk == "create":
                                volume = input("Enter your volume group name: ")
                                physical1 = input("Enter your 1st physical disk name: ")
                                physical2 = input("Enter your 2nd physical disk name: ")
                                os.system("sudo vgcreate {} {} {}".format(volume,physical1,physical2))
                            elif disk == "delete":
                                volume = input("Enter your volume group name: ")
                                os.system("sudo vgchange -an {}".format(volume))
                                os.system("sudo vgremove {}".format(volume))
                            else:
                                print("Not Found")
                        elif c == 5:
                            volume = input("Enter your volume group name: ")
                            os.system("sudo vgdisplay {}".format(volume))
                        elif c == 6:
                            disk = input("What you want (create/delete): ")
                            if disk == "create":
                                logical = input("Enter your logical volume name: ")
                                volume = input("Enter your volume group name: ")
                                size = input("Enter the size of logical volume (in G): ")
                                os.system("sudo lvcreate --size {} --name {} {}".format(size,logical,volume))
                            elif disk == "delete":
                                logical = input("Enter your logical volume name: ")
                                volume = input("Enter your volume group name: ")
                                os.system("sudo lvchange -an /dev/{}/{}".format(volume,logical))
                            else:
                                print("Not Found")
                        elif c == 7:
                            logical = input("Enter your volume group name: ")
                            os.system("sudo lvdisplay {}".format(logical))
                        elif c == 8:
                            volume = input("Enter your volume group name: ")
                            logical = input("Enter your logical volume name: ")
                            size = input("Enter the size of logical volume (in G): ")
                            os.system("sudo lvextend --size +{} /dev/{}/{}".format(size,volume,logical))
                        elif c == 9:
                            disk = input("What do you want (format/continue-format): ")
                            if disk == "format":
                                volume = input("Enter your volume group name: ")
                                logical = input("Enter your logical volume name: ")
                                os.system("sudo mkfs.ext4 /dev/{}/{}".format(volume,logical))
                            elif disk == "continue-format":
                                volume = input("Enter your volume group name: ")
                                logical = input("Enter your logical volume name: ")
                                os.system("sudo resize2fs /dev/{}/{}".format(volume,logical))
                            else:
                                print("Not Found")
                        elif c == 10:
                            os.system("df -h")
                        elif c == 11:
                            disk = input("What do you want (mount/umount): ")
                            if disk == "mount":
                                volume = input("Enter your volume group name: ")
                                logical = input("Enter your logical volume name: ")
                                folder = input("Enter your folder name: ")
                                os.system("sudo mount /{}".format(folder))
                                os.system("sudo mount /dev/{}/{}  /{}".format(volume,logical,folder))
                                print("Mounted Successfully")
                            elif disk == "umount":
                                folder = input("Enter your folder name: ")
                                os.system("sudo umount /{}".format(folder))
                                print("Umounted Successfuly")
                            else:
                                print("Not Found")
                        elif c == 12:
                            break
                        else:
                            print("Choose different option")
                        input("Press Enter to Continue...")
                elif b == 26:
                    os.system("netstat -tnlp")
                elif b == 27:
                    ff = input("What to do want: (file/folder) ")
                    if ff == "file":
                        filename = input("Enter the file name: ")
                        os.system("rm -rf {}".format(filename))
                    elif ff == "folder":
                        foldername = input("Enter the folder/location name: ")
                        os.system("rmdir {}".format(foldername))
                    else:
                        print("Not Found")
                elif b == 28:
                    break
                else:
                    print("not supported")
                input("Please Enter to continue the Menu....")
        else:
            print("Not Supported any option....\n")
            input("Press Enter to Continue.....")