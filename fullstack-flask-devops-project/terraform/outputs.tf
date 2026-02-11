output "public_ip" {
  value = aws_instance.hotstar_server.public_ip
}

output "website_url" {
  value = "http://${aws_instance.hotstar_server.public_ip}"
}

output "api_url" {
  value = "http://${aws_instance.hotstar_server.public_ip}:5000"
}
