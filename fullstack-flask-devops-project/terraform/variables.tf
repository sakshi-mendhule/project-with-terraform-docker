variable "aws_region" {
  default = "ap-south-1"
}

variable "instance_type" {
  default = "t2.micro"
}

variable "key_name" {
  description = "Your existing AWS Key Pair name"
}

variable "project_name" {
  default = "hotstar-devops-project"
}
