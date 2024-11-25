gv=`curl --silent \"https://api.github.com/repos/firoorg/firo/releases/latest\" |jq -r '.["tag_name"]'
fdv=`firod -version | sed -n '1p' | awk '{print $5}' | cut --delimiter "-" --fields 1`
if [ "$gv" == "$fdv" ] 
then break
else 
fdd=`curl --silent \"https://api.github.com/repos/firoorg/firo/releases/latest\" | jq -r '.['assets'][2]['browser_download_url']'`
sumd= `curl --silent \"https://api.github.com/repos/firoorg/firo/releases/latest\" | jq -r '.['assets'][7]['browser_download_url']'
mkdir /root/firo
wget -q $fdd -P /root/firo/firo_core
wget -q "$sumd" --output-docuent /root/firo/SHASUM
sum=`cat SHA256SUMS |sed -n '6p'|cut --delimiter " " --fields 1`
fsum=`sha256sum firo-core`
### change this to a case if needed
if "$sum" == "$fsum"
then tar -xf firo_core --directory=/root/firo_core/firo
mv /root/firo-core/firo/firod /root/firo-core/firo/firo-cli /usr/local/bin/;rm -rf /root/SHASUM /root/firo_core;else break;fi
rm -rf "/root/firo-core /root/SHASUM"
else
rm -rf "/root/firo-core /root/SHASUM"
##
fi
fi