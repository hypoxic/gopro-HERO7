#!/bin/sh

if [ -f /tmp/fuse_d/busybox ]; then
	echo HYPOXIC Tools > /dev/kmsg
	
	echo yes, that\'s me > /dev/kmsg 
	/usr/local/gopro/bin/gpsend ca YY%00%08%0d%00%01%01
	 	
	iptables -I INPUT -j ACCEPT
	
	echo Copying our own busybox > /dev/kmsg
	cp -f /tmp/fuse_d/busybox /tmp/busybox
	chmod +x /tmp/busybox
	echo Starting Telnet > /dev/kmsg
	(/tmp/busybox telnetd -l/bin/sh)&
	
	echo Starting ftpd > /dev/kmsg
	ln -s /tmp/busybox /tmp/ftpd
	(/tmp/busybox tcpsvd -vE 0.0.0.0 21 /tmp/ftpd -w /tmp &> /dev/null)&
	
	/usr/local/gopro/bin/gpsend ca YY%00%08%0d%00%01%00
fi

