#!/bin/bash
# echo "HOST ip: $(cat /etc/resolv.conf | grep nameserver | awk '{ print $2 }')"
# echo "WSL2 ip: $(hostname -I | awk '{print $1}')"
HOST=$(cat /etc/resolv.conf | grep nameserver | awk '{ print $2 }')
WSL2=$(hostname -I | awk '{print $1}')
PROXY_HTTP="http://${HOST}:7890"
# edit function
function Cat(){
	echo "HOST ip: ${HOST}"		
	echo "WSL2 ip: ${WSL2}"
	echo "PROXY_HTTP: ${PROXY_HTTP}"
}
function Set(){
	export http_proxy="${PROXY_HTTP}"
	export https_proxy="${PROXY_HTTP}"
	git config --system http.proxy "${PROXY_HTTP}"
	git config --system https.proxy "${PROXY_HTTP}"
	echo "The Proxy environment has been set!"
}
function Unset(){
	unset http_proxy
	unset https_proxy
	git config --system --unset http.proxy "${PROXY_HTTP}"
	git config --system --unset https.proxy "${PROXY_HTTP}"
	echo "The Proxy environment has not been set!"
}
if [ "$1" = "set" ]; then
	Set
elif [ "$1" = "unset" ]; then
	Unset				
elif [ "$1" = "cat" ]; then
	Cat		
else		
	echo "Incorrect arguments."
fi
