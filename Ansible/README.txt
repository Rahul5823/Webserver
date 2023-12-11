Steps and Working of Ansible

1. To install Ansible on control node,
	
	sudo apt update
	sudo apt install ansible

2. Create an inventory file named 'hosts.ini' where we group IP addresses of different nodes involved.

	In this file of 'hosts.ini', I grouped IP addresses along with configuring the SSH access from control node
	to managed node.

3. Now configure the Playbooks of ansible which are in the format of YAML. 

	In our case,  we use it to install webserver, deploy python server etc.

4. Then, execute the playbook

	ansible-playbook -i hosts.ini myplaybook.yaml