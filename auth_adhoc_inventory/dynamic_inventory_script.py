#json format

import json
import boto3

def get_aws_ec2_inventory():
    ec2 = boto3.client('ec2')
    instances = ec2.describe_instances()
    inventory = {
        'all': {
            'hosts': [],
            # 'vars': {
            #     'ansible_user': 'ec2-user',
            #     'ansible_ssh_private_key_file': '/path/to/key'
            # }
        },
        '_meta': {
            'hostvars': {}
        }
    }

    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            if instance['State']['Name'] == 'running':
                public_ip = instance['PublicIpAddress']
                inventory['all']['hosts'].append(public_ip)
                inventory['_meta']['hostvars'][public_ip] = {
                    'ansible_host': public_ip
                }

    print(json.dumps(inventory, indent=2))

if __name__ == '__main__':
    get_aws_ec2_inventory()


#ini format
import boto3

def get_aws_ec2_inventory_ini():
    ec2 = boto3.client('ec2')
    instances = ec2.describe_instances()
    ini_inventory = "[all]\n"

    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            if instance['State']['Name'] == 'running':
                public_ip = instance.get('PublicIpAddress')
                if public_ip:
                    ini_inventory += public_ip

    with open("dynamic_inventory.ini", "w") as f:
        f.write(ini_inventory.strip())

    print("Inventory written to dynamic_inventory.ini")

if __name__ == '__main__':
    get_aws_ec2_inventory_ini()

