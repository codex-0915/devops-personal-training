# Provider Block
provider "aws" {
    profile = "default"
    region = "us-east-1"
}

# VPC
resource "aws_vpc" "test_vpc" {
    cidr_block = var.vpc_cidr
    tags = {
        Name = var.vpc_name
    }
}

# Subnets
resource "aws_subnet" "test_subnet" {
    vpc_id = aws_vpc.test_vpc.id
    cidr_block = var.subnet_cidr
    tags = {
        Name = var.subnet_name
    }
}

# Creates a route to the internet
resource "aws_internet_gateway" "test_ig" {
    vpc_id = aws_vpc.test_vpc.id
    tags = {
        Name = var.igw_name
    }
}

# Creates new route table with IGW
resource "aws_route_table" "public_rt" {
    vpc_id = aws_vpc.test_vpc.id

    route {
        cidr_block = "0.0.0.0/0"
        gateway_id = aws_internet_gateway.test_ig.id
    }

    tags = {
        Name = var.igw_name
    }
}

# Associates route table with subnet
resource "aws_route_table_association" "public_1_rt_assoc" {
    subnet_id = aws_subnet.test_subnet.id
    route_table_id = aws_route_table.public_rt.id
}

# Creates new security group open to HTTP traffic
resource "aws_security_group" "test_sg" {
    name = "HTTP"
    vpc_id = aws_vpc.test_vpc.id

    ingress {
        from_port = 80
        to_port = 80
        protocol = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
    }

    egress {
        from_port = 0
        to_port = 0
        protocol = -1
        cidr_blocks = ["0.0.0.0/0"]
    }
}

# Creates EC2 instance
resource "aws_instance" "app_instance" {
    ami = var.ec2_ami
    instance_type = var.ec2_instance_type

    vpc_security_group_ids = [aws_security_group.test_sg.id]
    subnet_id = aws_subnet.test_subnet.id
    associate_public_ip_address = true

    user_data = <<-EOF
        #!/bin/bash

        amazon-linux-extras install nginx1 -y
        echo "<h1>Hello world from $(hostname -f)</h1>" > /usr/share/nginx/html/index.html
        systemctl enable nginx
        systemctl start nginx
        EOF

    tags = {
        Name = var.ec2_name
    }
}