%define __jar_repack 0

Summary: Kafka and distributed topic based producer consumer queue
Name: kafka_2.9.2
Version: 0.8.1.1
Release: 1
License: Apache (v2)
Group: Applications
Source0: %{name}-%{version}.tgz
Source1: kafka.init
Source2: kafka.sysconfig
URL: http://kafka.apache.org
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Packager: charlie.wyse@am.sony.com

%description
Kafka is a distributed, partitioned, replicated commit log service. It provides the functionality of a messaging system, but with a unique design.

%prep

%setup -q -n %{name}-%{version}

%build

%install
rm -rf %{buildroot}/*
mkdir -p $RPM_BUILD_ROOT/etc/rc.d/init.d
mkdir -p $RPM_BUILD_ROOT/etc/sysconfig
mkdir -p $RPM_BUILD_ROOT/opt/kafka/logs
mkdir -p $RPM_BUILD_ROOT/var/log/kafka
install -m 755 %{S:1} $RPM_BUILD_ROOT/etc/rc.d/init.d/kafka
install -m 755 %{S:2} $RPM_BUILD_ROOT/etc/sysconfig/kafka
cp -pr * $RPM_BUILD_ROOT/opt/kafka

%files
%defattr(644, kafka, kafka)
%attr(755, kafka, kafka) /opt/kafka/bin
%attr(755, kafka, kafka) /var/log/kafka
%attr(755, root, root) /etc/rc.d/init.d/kafka
%config(noreplace) /opt/kafka/config
%config(noreplace) /etc/sysconfig/kafka
%doc /opt/kafka/LICENSE
%doc /opt/kafka/NOTICE
/opt/kafka/libs
/opt/kafka/logs

%clean
rm -rf $RPM_BUILD_ROOT

%pre
getent passwd kafka || useradd -M -s /sbin/nologin -c "Franz Kafka" -u 1883 kafka > /dev/null

%post
chkconfig --add kafka

service kafka start

%preun
if [ "$1" -eq 0 ]; then
  service kafka stop
  chkconfig --del kafka
  sleep 2
fi

%postun
if [ "$1" -eq 0 ]; then
  getent passwd kafka && userdel kafka > /dev/null
fi

%changelog
* Tue Nov 18 2014 Charlie Wyse <charlie.wyse@am.sony.com>
- Added support for /etc/sysconfig and changed kill signal in init script
* Wed Aug 20 2014 Charlie Wyse <charlie.wyse@am.sony.com>
- Update to Kafka 0.8.1.1 with scala 2.9.2 binary build.
* Wed Apr 9 2014 Edward Capriolo <edlinuxguru@gmail.com>
- Update to Kafka 0.8.0 encorporate some changes from https://github.com/kosii/kafka-rpm/
* Wed Jul 11 2012 Edward Capriolo <edward@m6d.com>
- Rebuild against kafka trunk for mirror mode support
* Mon May 7 2012  Edward Capriolo <edward@m6d.com>
- Fix init scripts, clear conf dir, skip system test dir
* Thu May 3 2012  Edward Capriolo <edward@m6d.com>
- Taking care of business
* Wed May 2 2012  Edward Capriolo <edward@m6d.com>
- Oldest at the bottom
