variable "vpc_cidr" {
    description = "Value of the CIDR range for the VPC"
    type = string
    default = "100.0.0.0/16"
}

variable "vpc_name" {
    description = "Value of the name for the VPC"
    type = string
    default = "TestVPC"
}

variable "subnet_cidr" {
    description = "Value of the subnet CIDR for the VPC"
    type = string
    default = "38.0.101.76/24"
}

variable "subnet_name" {
    description = "Value of the subnet name for the VPC"
    type = string
    default = "TestSubnet"
}

variable "igw_name" {
    description = "Value of the Internet Gateway for the VPC"
    type = string
    default = "TestIGW"
}

variable "ec2_ami" {
    description = "Value of the AMI ID for the EC2 instance"
    type = string
    default = "ami-0166fe664262f664c" # Amazon Linux 2 AMI (HVM) - Kernel 5.10, SSD Volume Type
}

variable "ec2_instance_type" {
    description = "Value of the instance type for the EC2 instance"
    type = string
    default = "t2.micro"
}

variable "ec2_name" {
    description = "Value of the name for the EC2 instance"
    type = string
    default = "TestEC2"
}

