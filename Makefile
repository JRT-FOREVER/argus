#PREFIX=/usr

install :
	install -Dm755 argus.py ${PREFIX}/usr/lib/argus/argus.py
	install -Dm755 config-dist.py ${PREFIX}/usr/lib/argus/config.py
	install -Dm755 argus.service ${PREFIX}/lib/systemd/system/argus.service
	cp -r lib public scripts ${PREFIX}/usr/lib/argus/
	mkdir -p ${PREFIX}/etc/argus
	ln -sf /usr/lib/argus/config.py ${PREFIX}/etc/argus/
	ln -sf /usr/lib/argus/scripts/ ${PREFIX}/etc/argus/

