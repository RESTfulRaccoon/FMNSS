# FIRO NODE AUTOMATION TOOLS
A set of tools designed to help users set up update and interact with their master node.

## Firo Masternode Start Script (INCOMPLETE)

Designed to make starting a masternode easier, required 

#### Depends
`python3`

#### How to use
Download Dependencies `list of depends`
Download **start_script.py** ***instructions***

Set up a VPS [Guide](https://firo.org/guide/masternode-setup.html#step-4-get-a-vps).

From your VPS you will get a Username (usually root), a password and an external ip address.

Use `python3 ./start_script.py SERVER_PASSWORD EXTERNAL_IP WALLET_PASSWORD` 

From there the script will take over and set up your masternode including an automated Firod updater.

#### Additional options
--superuser : Use this option if you have already created a superuser and will not be using $root to log into your server

--port : The port you would like to use to make ssh connections (Random over 10000 by default) 
**NOTE: You will be prompted to check your selected port is not in use if under 10000

--rpc-user : Username for Firod RPC (Random by default)

--rpc-pass : Password for Firod RPC (Random by default)

--no-firewall : Prevent script from changing firewall options (Only use this if you plan on setting up your own firewall) *NOTE: If this option is selected and you **DO NOT** configure your firewall to accept incoming traffic on port 8168 you masternode **WILL NOT** work*

--keep-port : Keep default ssh port (22)

-v, --verbose : If you would like to know what the script is doing.

### What it does

After recieving the required user input as well as any other user variables this script will automatically:

1. Unlock your wallet to gather required information for node set up then lock your wallet.
2. Generate an ssh-key for your masternode server.
3. Enter your server.
4. Download required dependancies.
5. Create a static LOCAL_IP address on server if required.
6. Configure server SSH to a non standard port
7. Set up IPTABLES firewall.
8. Removes any potentally insecure files.
9. Configures server SWAP file (if required).
10. Adds a new unprivladged user named "firo" to run the node.
11. Download Firod and check integrity of download.
12. Extracts Firod from tarball and moves to local binary folder.
13. Bootstraps blockchain from ***SHOUT OUT TO...*** .
14. Creates firod.config.
15. Ensures correct ownership of programs and files.
16. Set up automatic security updates for server.
17. Create Firod Service to automatically start Firod after reboot.
18. Create automated log rotation.
19. Download **updater.sh** and move to /usr/local/sbin.
20. Create cronjob to run **updater.sh** weekly.

Finally, when everything is complete on your server the script will unlock your wallet again to activate your masternode.

## Updater (UNTESTED)
Bash script for automatic updates of Firod

(Please note that if you have used the Firo start script to create your masternode this is completed automatically)

### How to use
1. SSH into the server containing your masternode
2. Download **firod_updater** `wget https://raw.githubusercontent.com/RESTfulRaccoon/firo-node-automation/refs/heads/main/updater/firod_automatic_update.sh`
3. Change **firod_updater** file permissions `chmod 744 firod_automatic_update.sh`
4. Change **firod_updater** owner to root `sudo chown root:root firod_automatic_update.sh`
5. Move the updater to your local admin binary folder `sudo mv firod_automatic_update.sh /usr/local/sbin/firod_automatic_update.sh`
6. Create an admin cronjob

   * `sudo crontab -e`

   * If this is your first time creating a cronjob you will be prompted to select an editor, use option 1 `nano` if you are unsure.

   * On the last line enter `5 2 * * 1 /bin/bash firod_automatic_updater.sh` where minute=5 hour=2 and day=1

   * This will set your masternode to check for an update every Sunday at 2:05AM ***please consider changing this***
8. When you are finished use the key commands `ctrl + s` to save and `ctrl + x` to exit.
9. You should recieve a message stating *"crontab: installing new crontab"*

Thats it! Once you are finished your masternode should now automaticlly update!
