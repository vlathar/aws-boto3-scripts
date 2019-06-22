#print instances description of present instances
import boto3
from botocore.exceptions import ClientError
def descInstance(filter):
	session=boto3.client('ec2')
	try:
		ec2_instance=session.describe_instances(Filters=[{'Name' : filter,'Values' : ['running']}])	
		print(ec2_instance)
	except ClientError as e:
		print("ERROR",e)
	return None

def main():
	filter=input("Enter instance Id for filter ")
	descInstance(filter)

if __name__ == '__main__':
	main()