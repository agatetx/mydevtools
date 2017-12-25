export EC2_SERVER="ubuntu@some-ec2-server"

ssh -i "someami.pem" $EC2_SERVER
sshfs -o IdentityFile=~/someami.pem $EC2_SERVER:/home/ubuntu ~/remote
ssh -i "deepami.pem" -L 6006:localhost:6006 $EC2_SERVER
scp  -r -i "../deepami.pem" $EC2_SERVER:some_files .
rsync -arsync -azvv -e "ssh -i deepami.pem" $EC2_SERVER:/home/ubuntu/disk2/datasets/sd*
rsync -azvv --progress some-ec2-server:SRC_DIR DST_DIR




