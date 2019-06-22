import boto3
from botocore.exceptions import ClientError


def create_ec2_instance(image_id, instance_type):
    ec2_client = boto3.client('ec2')
    try:
        response = ec2_client.run_instances(ImageId=image_id,
                                            InstanceType=instance_type,
                                            MinCount=1,
                                            MaxCount=1)
    except ClientError as e:
        print("ERROR ",e)
    return response['Instances'][0]


def main():
    image_id = 'ami-0b3046001e1ba9a99'
    #Amazon Linux 2 AMI (HVM), SSD Volume Type 
    #image_id=input("Enter the AMI ")
    #instance_type=input("Enter the instance type- t2.micro ")
    instance_type = 't2.micro'

    instance_info = create_ec2_instance(image_id, instance_type)
    print(instance_info)

if __name__ == '__main__':
    main()