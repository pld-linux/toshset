Summary:	Toshset - a command-line tool allowing access to much of the Toshiba hardware interface
Summary(pl.UTF-8):	Toshset - narzędzie pozwalające na dostęp do wielu interfejsów sprzętowych Toshiby
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

%description -l pl.UTF-8
Toshset to działające z linii poleceń narzędzie pozwalające na dostęp
do wielu interfejsów sprzętowych Toshiby. Potrafi m.in. sterować
jasnością wyświetlacza, ustawiać prędkość wiatraczków i włączać
opcjonalny interfejs Bluetooth.

%prep
%setup -q
%patch -P0 -p0

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
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
