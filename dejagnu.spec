#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x67DADC3E3F743649 (bje@air.net.au)
#
Name     : dejagnu
Version  : 1.6.1
Release  : 18
URL      : https://mirrors.kernel.org/gnu/dejagnu/dejagnu-1.6.1.tar.gz
Source0  : https://mirrors.kernel.org/gnu/dejagnu/dejagnu-1.6.1.tar.gz
Source99 : https://mirrors.kernel.org/gnu/dejagnu/dejagnu-1.6.1.tar.gz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: dejagnu-bin
Requires: dejagnu-data
Requires: dejagnu-doc
BuildRequires : expect
BuildRequires : tcl

%description
Introduction
------------
Welcome to DejaGnu!
DejaGnu is a framework for testing other programs. Its purpose is to
provide a single front-end for all tests.  Beyond this, DejaGnu offers
several advantages for testing:

%package bin
Summary: bin components for the dejagnu package.
Group: Binaries
Requires: dejagnu-data

%description bin
bin components for the dejagnu package.


%package data
Summary: data components for the dejagnu package.
Group: Data

%description data
data components for the dejagnu package.


%package dev
Summary: dev components for the dejagnu package.
Group: Development
Requires: dejagnu-bin
Requires: dejagnu-data
Provides: dejagnu-devel

%description dev
dev components for the dejagnu package.


%package doc
Summary: doc components for the dejagnu package.
Group: Documentation

%description doc
doc components for the dejagnu package.


%prep
%setup -q -n dejagnu-1.6.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1521068845
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1521068845
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/runtest

%files data
%defattr(-,root,root,-)
/usr/share/dejagnu/baseboards/README
/usr/share/dejagnu/baseboards/aarch64-sim.exp
/usr/share/dejagnu/baseboards/am33_2.0-libremote.exp
/usr/share/dejagnu/baseboards/androideabi.exp
/usr/share/dejagnu/baseboards/arm-ice.exp
/usr/share/dejagnu/baseboards/arm-sid.exp
/usr/share/dejagnu/baseboards/arm-sim.exp
/usr/share/dejagnu/baseboards/basic-sid.exp
/usr/share/dejagnu/baseboards/basic-sim.exp
/usr/share/dejagnu/baseboards/cris-sim.exp
/usr/share/dejagnu/baseboards/d30v-sim.exp
/usr/share/dejagnu/baseboards/fr30-sim.exp
/usr/share/dejagnu/baseboards/frv-sim.exp
/usr/share/dejagnu/baseboards/gdbserver-sample.exp
/usr/share/dejagnu/baseboards/i386-sid.exp
/usr/share/dejagnu/baseboards/iq2000-sim.exp
/usr/share/dejagnu/baseboards/jmr3904-sim.exp
/usr/share/dejagnu/baseboards/linux-gdbserver.exp
/usr/share/dejagnu/baseboards/linux-libremote.exp
/usr/share/dejagnu/baseboards/m68k-sid.exp
/usr/share/dejagnu/baseboards/mcore-moto-sim.exp
/usr/share/dejagnu/baseboards/mcore-sim.exp
/usr/share/dejagnu/baseboards/mips-lnews-sim.exp
/usr/share/dejagnu/baseboards/mips-lsi-sim.exp
/usr/share/dejagnu/baseboards/mips-sim-idt32.exp
/usr/share/dejagnu/baseboards/mips-sim-idt64.exp
/usr/share/dejagnu/baseboards/mips-sim-mti32.exp
/usr/share/dejagnu/baseboards/mips-sim-mti64.exp
/usr/share/dejagnu/baseboards/mips-sim-mti64_64.exp
/usr/share/dejagnu/baseboards/mips-sim-mti64_n32.exp
/usr/share/dejagnu/baseboards/mips-sim-sde32.exp
/usr/share/dejagnu/baseboards/mips-sim-sde64.exp
/usr/share/dejagnu/baseboards/mips-sim.exp
/usr/share/dejagnu/baseboards/mmixware-sim.exp
/usr/share/dejagnu/baseboards/mn10200-sim.exp
/usr/share/dejagnu/baseboards/mn10300-sim.exp
/usr/share/dejagnu/baseboards/msp430-sim.exp
/usr/share/dejagnu/baseboards/mt-sid.exp
/usr/share/dejagnu/baseboards/multi-sim.exp
/usr/share/dejagnu/baseboards/powerpc-sim.exp
/usr/share/dejagnu/baseboards/powerpcle-sim.exp
/usr/share/dejagnu/baseboards/rx-sim.exp
/usr/share/dejagnu/baseboards/sh-sid.exp
/usr/share/dejagnu/baseboards/sh-sim.exp
/usr/share/dejagnu/baseboards/sparc-sim.exp
/usr/share/dejagnu/baseboards/sparc64-sim.exp
/usr/share/dejagnu/baseboards/sparclite-sim-le.exp
/usr/share/dejagnu/baseboards/sparclite-sim.exp
/usr/share/dejagnu/baseboards/tx39-sim.exp
/usr/share/dejagnu/baseboards/unix.exp
/usr/share/dejagnu/baseboards/v850-sim.exp
/usr/share/dejagnu/baseboards/visium-sim.exp
/usr/share/dejagnu/baseboards/vr4100-sim.exp
/usr/share/dejagnu/baseboards/vr4111-sim.exp
/usr/share/dejagnu/baseboards/vr4300-sim.exp
/usr/share/dejagnu/baseboards/xtensa-sim.exp
/usr/share/dejagnu/config/README
/usr/share/dejagnu/config/aarch64-fv8.exp
/usr/share/dejagnu/config/adb.exp
/usr/share/dejagnu/config/default.exp
/usr/share/dejagnu/config/gdb-comm.exp
/usr/share/dejagnu/config/gdb_stub.exp
/usr/share/dejagnu/config/sid.exp
/usr/share/dejagnu/config/sim.exp
/usr/share/dejagnu/config/unix.exp
/usr/share/dejagnu/config/vxworks.exp
/usr/share/dejagnu/debugger.exp
/usr/share/dejagnu/dejagnu.exp
/usr/share/dejagnu/dg.exp
/usr/share/dejagnu/dmucs.exp
/usr/share/dejagnu/framework.exp
/usr/share/dejagnu/ftp.exp
/usr/share/dejagnu/kermit.exp
/usr/share/dejagnu/libexec/config.guess
/usr/share/dejagnu/libgloss.exp
/usr/share/dejagnu/remote.exp
/usr/share/dejagnu/rlogin.exp
/usr/share/dejagnu/rsh.exp
/usr/share/dejagnu/runtest.exp
/usr/share/dejagnu/ssh.exp
/usr/share/dejagnu/standard.exp
/usr/share/dejagnu/stub-loader.c
/usr/share/dejagnu/target.exp
/usr/share/dejagnu/targetdb.exp
/usr/share/dejagnu/telnet.exp
/usr/share/dejagnu/testglue.c
/usr/share/dejagnu/tip.exp
/usr/share/dejagnu/utils.exp

%files dev
%defattr(-,root,root,-)
/usr/include/*.h

%files doc
%defattr(-,root,root,-)
%doc /usr/share/info/*
%doc /usr/share/man/man1/*
