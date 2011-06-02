Summary:	Java based project manager
Summary(pl.UTF-8):	Napisany w Javie system zarządzania projektem
Name:		openproj
Version:	1.4
Release:	1
License:	Common Public Attribution License 1.0 (CPAL)
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/openproj/%{name}-%{version}-src.tar.gz
# Source0-md5:	bf5d96951959c9a280cb5e5400a1105a
Source1:	%{name}.sh
Source2:	%{name}.desktop
URL:		http://www.openproj.org/
BuildRequires:	ant
BuildRequires:	jdk
BuildRequires:	jpackage-utils
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	unzip
Requires(post,postun):	shared-mime-info
Requires:	jre >= 1.5.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A desktop replacement for Microsoft Project. It is capable of sharing
files with Microsoft Project and has very similar functionality
(Gantt, PERT diagram, histogram, charts, reports, detailed usage), as
well as tree views which aren't in MS Project.

%prep
%setup -q -n %{name}-%{version}-src

%build
cd openproj_build
%ant

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_datadir}/mime/packages
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/{lib,samples}
install -d $RPM_BUILD_ROOT%{_docdir}/%{name}
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}}

install openproj_build/dist/lib/*		$RPM_BUILD_ROOT%{_datadir}/%{name}/lib
install openproj_build/dist/%{name}.jar 	$RPM_BUILD_ROOT%{_datadir}/%{name}
install openproj_build/resources/%{name}.sh	$RPM_BUILD_ROOT%{_datadir}/%{name}
install openproj_build/resources/samples/* 	$RPM_BUILD_ROOT%{_datadir}/%{name}/samples
install openproj_build/license/index.html 	$RPM_BUILD_ROOT%{_docdir}/%{name}/license.html
install openproj_build/resources/%{name}.xml 	$RPM_BUILD_ROOT%{_datadir}/mime/packages/%{name}.xml
install openproj_build/resources/%{name}.png 	$RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE1} 				$RPM_BUILD_ROOT%{_bindir}/%{name}
install %{SOURCE2} 				$RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_mime_database

%postun
%update_mime_database

%files
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}/license.html
%attr(755,root,root) %{_bindir}/openproj
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/lib
%dir %{_datadir}/%{name}/samples
%{_datadir}/%{name}/%{name}.jar
%{_datadir}/%{name}/%{name}.sh
%{_datadir}/%{name}/lib/*
%{_datadir}/%{name}/samples/*
%{_pixmapsdir}/%{name}.png
%{_datadir}/mime/packages/%{name}.xml
%{_desktopdir}/*.desktop
