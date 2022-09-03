Name:		bolt
Version:	0.9.3
Release:	1
Summary:	Thunderbolt device manager
Group:		System/Kernel and hardware
License:	LGPLv2+
URL:		https://gitlab.freedesktop.org/bolt/bolt
Source0:	https://gitlab.freedesktop.org/bolt/bolt/-/archive/%{version}/%{name}-%{version}.tar.bz2

BuildRequires:	asciidoc
BuildRequires:	meson
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(libudev)
BuildRequires:	pkgconfig(libsystemd)
BuildRequires:	pkgconfig(polkit-agent-1)
BuildRequires:	systemd

# Optional.
BuildRequires:	pkgconfig(pygobject-3.0)
BuildRequires:	pkgconfig(umockdev-1.0)
BuildRequires:	python3dist(dbus-python)
BuildRequires:	python3dist(python-dbusmock)

Requires(post):		rpm-helper
Requires(preun):	rpm-helper

%description
Bolt is a aserspace system daemon to enable security levels for Thunderbolt on GNU/Linux.
Thunderbolt is the brand name of a hardware interface developed by Intel that allows the connection of external peripherals to a computer.
Devices connected via Thunderbolt can be DMA masters and thus read system memory without interference of the operating system (or even the CPU).
Version 3 of the interface introduced 5 different security levels, 
in order to mitigate the aforementioned security risk that connected devices pose to the system. The security level is set by the system firmware.

%prep
%autosetup -p1

%build
%meson -Ddb-name=boltd
%meson_build

%install
%meson_install

%post
%_post_service %{name}

%preun
%_preun_service %{name}

%files
%license COPYING
%doc README.md
%{_bindir}/boltctl
%{_libexecdir}/boltd
%{_unitdir}/%{name}.service
%{_udevrulesdir}/*-%{name}.rules
%{_datadir}/dbus-1/system.d/org.freedesktop.bolt.conf
%{_datadir}/dbus-1/interfaces/org.freedesktop.bolt.xml
%{_datadir}/polkit-1/actions/org.freedesktop.bolt.policy
%{_datadir}/polkit-1/rules.d/org.freedesktop.bolt.rules
%{_datadir}/dbus-1/system-services/org.freedesktop.bolt.service
#{_mandir}/man1/boltctl.1*
#{_mandir}/man8/boltd.8*
%ghost %dir %{_localstatedir}/lib/boltd
