import boto3
ec2 = boto3.client("ec2",region_name='us-west-2')

#create vpc
vpc = ec2.create_vpc(CidrBlock='10.0.0.0/16',DryRun=False)
ec2.create_tags(Resources=[vpc["Vpc"]["VpcId"]],Tags=[{"Key":"Name","Value":"diyblockchianVPC"}])
#vpc.wait_until_available()
print(vpc["Vpc"]["VpcId"], " is available. ")
vpc_id=vpc["Vpc"]["VpcId"]

#create subnet
subnet1=ec2.create_subnet(CidrBlock='10.0.1.0/24',VpcId=vpc_id)
print(subnet1["Subnet"]["SubnetId"])

subnet2=ec2.create_subnet(CidrBlock='10.0.2.0/24',VpcId=vpc_id)
print(subnet2["Subnet"]["SubnetId"])

subnet3=ec2.create_subnet(CidrBlock='10.0.3.0/24',VpcId=vpc_id)
print(subnet3["Subnet"]["SubnetId"])

ec2.create_tags(Resources=[subnet1["Subnet"]["SubnetId"]],Tags=[{'Key':'Name','Value':'public_subnet_1'}])
ec2.create_tags(Resources=[subnet2["Subnet"]["SubnetId"]],Tags=[{'Key':'Name','Value':'private_subnet_1'}])
ec2.create_tags(Resources=[subnet3["Subnet"]["SubnetId"]],Tags=[{'Key':'Name','Value':'private_subnet_2'}])

#create internet Gateway
ig=ec2.create_internet_gateway()
ec2.attach_internet_gateway(VpcId=vpc_id,InternetGatewayId=ig["InternetGateway"]["InternetGatewayId"])
print("Internet gateway created and attached to vpc.")

#creating route table
rt=ec2.create_route_table(VpcId=vpc_id)
ec2.create_route(RouteTableId=rt["RouteTable"]["RouteTableId"],DestinationCidrBlock='0.0.0.0/0',GatewayId=ig["InternetGateway"]["InternetGatewayId"])
print("Route table created and route added.")

ec2.associate_route_table(RouteTableId=rt["RouteTable"]["RouteTableId"],SubnetId=subnet1["Subnet"]["SubnetId"])

#create securtiy group
sg=ec2.create_security_group(GroupName='public_sg',Description='public_security_group',VpcId=vpc_id)
ec2.authorize_security_group_ingress(GroupId=sg["GroupId"],IpProtocol="tcp",CidrIp="0.0.0.0/0",FromPort=443,ToPort=443)
ec2.authorize_security_group_ingress(GroupId=sg["GroupId"],IpProtocol="tcp",CidrIp="0.0.0.0/0",FromPort=22,ToPort=22)
ec2.authorize_security_group_ingress(GroupId=sg["GroupId"],IpProtocol="tcp",CidrIp="0.0.0.0/0",FromPort=80,ToPort=80)

