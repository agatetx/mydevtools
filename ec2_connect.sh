export EC2_SERVER="ubuntu@ec2-34-215-198-232.us-west-2.compute.amazonaws.com"

ssh -i "deepami.pem" $EC2_SERVER
sshfs -o IdentityFile=~/deepami.pem $EC2_SERVER:/home/ubuntu ~/remote
ssh -i "deepami.pem" -L 6006:localhost:6006 $EC2_SERVER



