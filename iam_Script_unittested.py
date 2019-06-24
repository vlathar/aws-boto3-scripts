import boto3,unittest
from botocore.exceptions import ClientError,ParamValidationError
class iaManagement():

	def __init__(self,username,pol_name,pol_arn):
		#policy_arn= the AMAZON RESOURCE NAME of the IAM policy
		#role_name= name of the role to attach
		self.username=username
		self.pol_name=pol_name
		self.pol_arn=pol_arn
	
	def createuser(self):
		try:
			res=iam.create_user(UserName=self.username)
			print("user created ",res)
			return "Success"
		except ParamValidationError as e:
			print("Parameters validation error. Retry.")
		except iam.exceptions.EntityAlreadyExistsException:
			print("User exists already.")
			pass
		except ClientError as e:
			print("UNEXPECTED ERROR OCCURED ",e)

	def deleteuser(self):
		try:
			res=iam.delete_user(UserName=self.username)
			print("Deleted SUCCESSFULLY ")
			return "Success"
		except ClientError:
			print("ERROR OCCURRED PLEASE CHECK PARAMs or detach policies first.")
			pass
		

	def attachPol(self):
		try:
			iam.attach_user_policy(UserName=self.username,PolicyArn=self.pol_arn)
			print("ATTACHED POLICY ")
			return "Success"
		except:
			print("ERROR occurred while attaching policy. PLease check.")
			pass
	
	def getPol(self):
		#returns info about the specified managed policy
		try:
			res=iam.get_policy(PolicyArn=self.policy_arn)
			print(res)
			return "Success"
		except ClientError as e:
			print("Couldn't fetch policy details. Details ",e)
			pass

	def detachPol(self):
		try:
			iam.detach_user_policy(UserName=self.username,PolicyArn=self.pol_arn)
			print("DETACHED POLICY ")
			return "Success"
		except ClientError:
			print("ERROR occurred while detaching policy. PLease check.")
			pass

obj = iaManagement("asus",'AmazonDynamoDBFullAccess','arn:aws:iam::aws:policy/AmazonDynamoDBFullAccess')

class iamTestClass(unittest.TestCase):
	
	def test_CUser(self):
		self.assertEqual(obj.createUser(),"Success")

	def test_APol(self):
		self.assertEqual(obj.attachPol(),"Success")

	def test_pol(self):
		self.assertEqual(obj.getPol(),"Success")

	def test_DPol(self):
		self.assertEqual(obj.detachPol(),"Success")

	def test_DUser(self):
		self.assertEqual(obj.deleteuser(),"Success")

if __name__=='__main__':
	iam=boto3.client('iam')
	unittest.main() 
  