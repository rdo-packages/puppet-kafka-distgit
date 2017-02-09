%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppet-kafka
%global commit 066d7a5bb630a41296428d81d3c1a1232574d008
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-kafka
Version:        2.2.0
Release:        1%{?alphatag}%{?dist}
Summary:        Module for managing apache kafka
License:        ASL 2.0

URL:            https://github.com/puppet-community/puppet-kafka

Source0:        https://github.com/puppet-community/%{upstream_name}/archive/%{commit}.tar.gz#/%{upstream_name}-%{shortcommit}.tar.gz

BuildArch:      noarch

Requires:       puppet-stdlib
Requires:       puppet-java
Requires:       puppet >= 2.7.0

%description
Module for managing apache kafka

%prep
%setup -q -n %{name}-%{upstream_version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/kafka/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/kafka/



%files
%{_datadir}/openstack-puppet/modules/kafka/


%changelog
* Thu Feb 09 2017 Alfredo Moralejo <amoralej@redhat.com> 2.2.0-1.066d7a5git
- Ocata update 2.2.0 (066d7a5bb630a41296428d81d3c1a1232574d008)

