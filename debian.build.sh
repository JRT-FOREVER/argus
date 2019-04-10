
#checkinstall --install=no \
#--nodoc \
#--pkgname=argus \
#--pkggroup=python3 \
#--pkgversion=3.0 \
#--pkgarch=all \
#--pkgrelease=1 \
#--pkglicense=MIT \
#--requires="python3, python3-bottle"

mkdir -p debian

cat > debian/rules << EOF
#!/usr/bin/make -f
%:
	dh \$@

override_dh_auto_build:

override_dh_auto_install:
	PREFIX=`pwd`/debian/argus dh_auto_install
EOF


cat > debian/control << EOF
Source: argus
Maintainer: a-wing <1@233.email>
Build-Depends: debhelper (>= 8.0.0)
Standards-Version: 3.9.3
Section: utils

Package: argus
Priority: extra
Architecture: all
Depends: python3, python3-bottle
Description: Auxiliary reliable guardian undertaking system
EOF

cat > debian/changelog << EOF
argus (3.1) unstable; urgency=low

  * Initial release.

 -- a-wing <1@233.email>  Sun, 07 Apr 2019 22:07:56 +0800
EOF

echo 9 > debian/compat

debuild -us -uc

rm -r debian

