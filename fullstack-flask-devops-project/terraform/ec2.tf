data "aws_ami" "amazon_linux" {
  most_recent = true
  owners      = ["amazon"]

  filter {
    name   = "name"
    values = ["amzn2-ami-hvm-*-x86_64-gp2"]
  }
}

resource "aws_instance" "hotstar_server" {
  ami                    = ami-0317b0f0a0144b137
  instance_type          = t3.micro
  key_name               = New-key
  vpc_security_group_ids = vpc-060d9dd67927b11f1

  user_data = <<-EOF
              #!/bin/bash
              yum update -y
              amazon-linux-extras install docker -y
              service docker start
              usermod -a -G docker ec2-user

              curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
              chmod +x /usr/local/bin/docker-compose

              yum install git -y

              cd /home/ec2-user
              git clone https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPO.git

              cd YOUR_REPO
              docker-compose up -d
              EOF

  tags = {
    Name = var.project_name
  }
}
