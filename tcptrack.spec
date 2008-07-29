Summary:	A packet sniffer which displays TCP information like the 'top' command
Name:		tcptrack
Version:	1.3.0
Release:	%mkrel 3
Group:		Monitoring
License:	GPLv2+
URL:		http://www.rhythm.cx/~steve/devel/tcptrack/
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

