export EC2_SERVER="ubuntu@some-ec2-server"

ssh -i "someami.pem" $EC2_SERVER
sshfs -o IdentityFile=~/someami.pem $EC2_SERVER:/home/ubuntu ~/remote
ssh -i "deepami.pem" -L 6006:localhost:6006 $EC2_SERVER
scp  -r -i "../deepami.pem" $EC2_SERVER:some_files .
rsync -arsync -azvv -e "ssh -i deepami.pem" $EC2_SERVER:/home/ubuntu/disk2/datasets/sd*
rsync -azvv --progress some-ec2-server:SRC_DIR DST_DIR

# make volume:
sudo mkfs -t ext4 /dev/xvdf
mkdir data
sudo mount /dev/xvdf data
sudo chmod 777 data/

# make EFS
sudo apt-get -y install nfs-common
sudo mkdir efs

