Summary:	Configurator for GNOME
Summary(pl):	Konfigurator dla GNOME
Name:		cog
Version:	0.7.2
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.krakoa.dk/progs/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	f60600d4f1885b10e42a9af8a0c34f3e
Patch0:		%{name}-desktop.patch
BuildRequires:	GConf2-devel >= 2.6.0
BuildRequires:	libglade2-devel >= 1:2.3.6
BuildRequires:	libgnomeui-devel >= 2.6.0
URL:		http://www.krakoa.dk/linux-software.html#COG
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Configurator for GNOME is a program for editing advanced GNOME
settings in an easy way.

%description -l pl
Konfigurator dla GNOME umo¿liwia edycjê zaawansowanych ustawieñ GNOME
w prosty sposób.

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_pixmapsdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install pixmaps/cog-icon-2-48x48.png $RPM_BUILD_ROOT%{_pixmapsdir}/cog.png

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/*
%{_pixmapsdir}/*
