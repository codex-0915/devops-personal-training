# Provider Block
provider "aws" {
    profile = "default"
    region = "us-east-1"
}

# Resource Block
resource "aws_instance" "app_server" {

    ami = "ami-0166fe664262f664c"
    instance_type = var.ec2_instance_type

    tags = {
        Name = var.instance_name
    }
}