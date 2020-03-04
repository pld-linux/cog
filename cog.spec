Summary:	Configurator for GNOME
Summary(pl.UTF-8):	Konfigurator dla GNOME
Name:		cog
Version:	0.8.0
Release:	3
License:	GPL v2+
Group:		X11/Applications
#Source0Download: http://www.krakoa.dk/old-linux-software.html#COG
Source0:	http://www.krakoa.dk/progs/cog/%{name}-%{version}.tar.gz
# Source0-md5:	fa6a42b2fa355cf736f661e6ed0589e5
Patch0:		%{name}-desktop.patch
URL:		http://www.krakoa.dk/old-linux-software.html#COG
BuildRequires:	GConf2-devel >= 2.6.0
BuildRequires:	gettext-tools
BuildRequires:	gtk+2-devel >= 2:2.4.0
BuildRequires:	libglade2-devel >= 1:2.4.0
BuildRequires:	libgnomeui-devel >= 2.6.0
BuildRequires:	pkgconfig
Requires:	gtk+2 >= 2:2.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Configurator for GNOME is a program for editing advanced GNOME
settings in an easy way.

%description -l pl.UTF-8
Konfigurator dla GNOME umożliwia edycję zaawansowanych ustawień GNOME
w prosty sposób.

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_bindir}/cog
%{_datadir}/%{name}
%{_desktopdir}/cog.desktop
%{_pixmapsdir}/cog-icon-2-48x48.png
