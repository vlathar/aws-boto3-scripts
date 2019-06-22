import boto3
import sys
def CreateUser():
	iam= boto3.client('iam')
	iam.create_user( UserName="avengers")
	#iam.attach_user_policy(UserName = 'avengers', PolicyArn='arn:aws:iam::aws:policy/AmazonEC2FullAccess')
	print("SUCCESS ")
	#iam.detach_role_policy(PolicyArn='arn:aws:iam::aws:policy/AmazonEC2FullAccess',RoleName='AmazonEC2FullAccess')
	iam.delete_user(UserName="avengers")