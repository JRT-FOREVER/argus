
install :
	mkdir -p /usr/lib/argus
	install -m755 argus.py /usr/lib/argus/argus.py
	install -m755 config-dist.py /usr/lib/argus/config.py
	install -m755 argus.tpl /usr/lib/argus/argus.tpl
	install -m755 argus.service /lib/systemd/system/argus.service
	cp -r lib scripts /usr/lib/argus/
	mkdir -p /etc/argus
	ln -sf /usr/lib/argus/config.py /etc/argus/
	ln -sf /usr/lib/argus/scripts/ /etc/argus/

