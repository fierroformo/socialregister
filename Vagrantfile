Vagrant::Config.run do |config|

  config.vm.box = "precise32"

  config.vm.forward_port 8000, 8000

  config.vm.share_folder "app", "/home/vagrant/app", "./app"

  config.vm.provision :chef_solo do |chef|
    chef.cookbooks_path = "cookbooks"
    chef.run_list = ["recipe[socialregister]"]
  end

end
