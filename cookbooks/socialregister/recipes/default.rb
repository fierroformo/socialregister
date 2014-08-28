include_recipe "apt"
include_recipe "build-essential"

%w{
   python python-dev zsh git-core vim-nox build-essential
   tree ipython python-setuptools python-psycopg2
}.each do |pkg|
  package pkg do
    action :install
  end
end

#
# Paquetes de Python
#

# Desde pip
bash "Instalar paquetes en requirements.txt" do
    code <<-EOH
    easy_install pip
    pip install -r /home/vagrant/app/requirements/development.txt
    EOH
end

# Configurar zsh
bash "Configurar zsh con oh-my-zsh!" do
    code <<-EOH
    git clone https://github.com/jairtrejo/oh-my-zsh.git /home/vagrant/.oh-my-zsh
    cp /home/vagrant/.oh-my-zsh/templates/zshrc.zsh-template /home/vagrant/.zshrc
    usermod -s /bin/zsh vagrant
    EOH
end
