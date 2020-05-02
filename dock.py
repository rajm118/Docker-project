# this is a program to present docker functionalities
import os

print('''1.Start docker
2.stop docker
3.show docker images installed
5.start wordpress and sql server with environment ready as well as volume created
6.steps to create apache server
7.to inspect the docker containers
8.to exit
''')
ch=int(input("ENTER THE CHOICE"))
while(ch):
	if(ch==1):
		print("plz check the docker is installed or not")
		os.system("systemctl start docker")
	elif(ch==7):
    print("first find the name of container")
    os.system("docker ps -a")
    cont_name=input("enter input name")
    os.system("docker inspect {0}".format(cont_name))
  elif(ch==2):
		print("plz check the docker is installed or not")
		os.system("systemctl stop docker")
	elif(ch==3):
    print("showing docker images")
    os.system("docker images")
  elif(ch==6):
    print('''install a container like centOS etc
    then install the httpd services via yum with command
    yum install httpd
    if this doesnt work just stop firwalld from outside the container by stsemctl stop firewalld
    and stop selinux by setenforce 0
    and do systemctl restart docker
    now again do yum install httpd -y
    and it will get installed and now we have to shift the webpages in cd/var/www/html location
    as apache looks for webpages at this location
    now come out of container by ctrl+p+q
    and do ifconfig and it will give the ip of docker and try using it in browser as http://(ip)
    and you should able to see the website
  elif(ch==8):
    break
  elif(ch==5):
		print("creating multitier architecture")
		
		print("checking for wordpress image")
		os.system("docker pull wordpress:5.1.1-php7.3-apache")
		print("cheking for mysql server's image")		
		os.system("docker pull mysql:5.7")
		print("after installaion of images creating a network ")
		
		print("Enter The Name of Your Network: ",end=" ")
		network_name=input()
		os.system("docker network create --driver bridge{0}".format(network_name))
		print("network created")
		os.system("docker network ls") 
		
		print("now as our db server has lot of data imp to us we will make it as a persistence storage") 
		docker_storage_name=input("enter storage name")
		os.system("docker volume create {0}".format(dock_storage_name))
		print("see volume created : ",end=" ")
		os.system("docker volume ls")
		
		print("now connecting db with wordpress so it can be deployed")
		print("Choose the Root Password and Enter Here: ",end=" ")
		rpass=input()
		print("Enter the name of the USER: ",end=" ")
		uname=input()
		print("Enter the Password for this USER: ",end=" ")
		upass=input()
		print("Give The name to your Database: ",end=" ")
		db_name=input()
		print(">>>If u don't know about your docker storage name (choose form here): ")  
		os.system("docker voulme ls")
		print("Enter the Name of Docker_storage: ",end=" ")
		db_stg_name=input()
		print("Give the name to your container(this name will be used to link): ",end=" ")  
		name_cont=input()
		os.system("docker run -dit -e MYSQL_ROOT_PASSWORD={0} -e MYSQL_USER={1} -e MYSQL_PASSWORD={2} 
    -e MYSQL_DATABASE={3} -v {4}:/var/lib/mysql --name {5} 
    mysql:5.7".format(rpass,uname,upass,db_name,db_stg_name,name_cont))
    print('''now the service is deployed and just get the ip address from ifconfig command which is 
    to be executed in terminal outside the container i.e base os of docker
    and port no and you can access the service''')
  ch=int(input("ENTER user choice"))




  
		
