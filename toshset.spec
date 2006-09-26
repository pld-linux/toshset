Summary:	Toshset - a command-line tool allowing access to much of the Toshiba hardware interface
Summary(pl):	Toshset - narzêdzie pozwalaj±ce na dostêp do wielu interfejsów sprzêtowych Toshiby
Name:		toshset
Version:	1.72
Release:	1
License:	GPL
Group:		Applications
Source0:	http://www.schwieters.org/toshset/%{name}-%{version}.tgz
# Source0-md5:	27730989b58353a4ecaac35d76dc530f
Patch0:		%{name}-Makefilein.patch
URL:		http://www.schwieters.org/toshset/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Toshset is a command-line tool allowing access to much of the Toshiba
hardware interface. It can do things like control display brightness,
set the fan speed, and enable the optional Bluetooth interface.

%description -l pl
Toshset to dzia³aj±ce z linii poleceñ narzêdzie pozwalaj±ce na dostêp
do wielu interfejsów sprzêtowych Toshiby. Potrafi m.in. sterowaæ
jasno¶ci± wy¶wietlacza, ustawiaæ prêdko¶æ wiatraczków i w³±czaæ
opcjonalny interfejs Bluetooth.

%prep
%setup -q
%patch0 -p0

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README README.video 
#%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
