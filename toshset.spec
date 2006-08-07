#
Summary:	Toshset is a command-line tool allowing access to much of the Toshiba hardware interface
Name:		toshset
Version:	1.71
Release:	0.1
License:	- (enter GPL/GPL v2/LGPL/BSD/BSD-like/other license name here)
Group:		Applications
Source0:	http://www.schwieters.org/toshset/%{name}-%{version}.tgz
# Source0-md5:	1afca9a6607436e39911e26a46b3c1d1
URL:		http://www.schwieters.org/toshset/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Toshset is a command-line tool allowing access to much of the Toshiba
hardware interface. It can do things like control display brightness,
set the fan speed, and enable the optional Bluetooth interface.

%prep
%setup -q

%build
./configure \
	--prefix=/usr --exec-prefix=/usr \
	--bindir=/usr/bin --sbindir=/usr/sbin \
	--sysconfdir=/etc --datadir=/usr/share \
	--includedir=/usr/include --libdir=/usr/lib \
	--libexecdir=/usr/lib --localstatedir=/var \
	--sharedstatedir=/var/lib --mandir=/usr/share/man \
	 --infodir=/usr/share/info --x-libraries=/usr/X11R6/lib
make

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%pre

%post

%preun

%postun

%files
%defattr(644,root,root,755)
%doc ChangeLog README README.video 

#%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/*
