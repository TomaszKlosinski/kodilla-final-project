Vagrant.configure("2") do |config|
    config.vm.box = "ubuntu/jammy64"
    config.vm.hostname = "blog"
    config.vm.synced_folder ".", "/opt/blog/"
    config.vm.network "forwarded_port", guest: 5000, host: 5001, host_ip: "127.0.0.1"
    config.vm.provision "shell", inline: <<-SHELL
       cd /opt/blog

       apt install software-properties-common
       add-apt-repository ppa:deadsnakes/ppa

       wget https://dl-ssl.google.com/linux/linux_signing_key.pub -O /tmp/google.pub
       gpg --no-default-keyring --keyring /etc/apt/keyrings/google-chrome.gpg --import /tmp/google.pub
       echo 'deb [arch=amd64 signed-by=/etc/apt/keyrings/google-chrome.gpg] http://dl.google.com/linux/chrome/deb/ stable main' | sudo tee /etc/apt/sources.list.d/google-chrome.list

       apt update -y

       apt install -y google-chrome-stable
       apt install -y python3.10 python3.11 python3
       apt install -y python3-pip

       /usr/bin/python3 -m pip install tox
       /usr/bin/python3 -m tox --recreate
    SHELL
  end
