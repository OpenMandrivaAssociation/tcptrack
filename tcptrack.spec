Summary:	A packet sniffer which displays TCP information like the 'top' command
Name:		tcptrack
Version:	1.4.2
Release:	2
Group:		Monitoring
License:	GPLv2+
URL:		https://www.rhythm.cx/~steve/devel/tcptrack/
Source0:	http://www.rhythm.cx/~steve/devel/tcptrack/release/%{version}/source/%{name}-%{version}.tar.gz
BuildRequires:	ncurses-devel
BuildRequires:	pcap-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description 
tcptrack is a sniffer which displays information about TCP connections it sees
on a network interface. It passively watches for connections on the network
interface, keeps track of their state and displays a list of connections in a
manner similar to the unix 'top' command. It displays source and destination
addresses and ports, connection state, idle time, and bandwidth usage.

%prep

%setup -q -n %{name}-%{version}

%build
%serverbuild

%configure2_5x

%make

%install
rm -rf %{buildroot}

%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog README INSTALL NEWS
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*


%changelog
* Mon Sep 05 2011 Oden Eriksson <oeriksson@mandriva.com> 1.4.2-1mdv2012.0
+ Revision: 698282
- 1.4.2 (fixes CVE-2011-2903)

* Wed Dec 29 2010 Leonardo Coelho <leonardoc@mandriva.com> 1.4.0-1mdv2011.0
+ Revision: 626065
- New version 1.4.0

* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 1.3.0-7mdv2010.0
+ Revision: 445386
- rebuild

* Wed Oct 29 2008 Oden Eriksson <oeriksson@mandriva.com> 1.3.0-6mdv2009.1
+ Revision: 298436
- rebuilt against libpcap-1.0.0

* Sat Sep 20 2008 Oden Eriksson <oeriksson@mandriva.com> 1.3.0-5mdv2009.0
+ Revision: 286182
- added a gcc43 patch from fedora

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild

* Thu Feb 07 2008 Oden Eriksson <oeriksson@mandriva.com> 1.3.0-1mdv2008.1
+ Revision: 163367
- import tcptrack

