%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppet-kafka
%global commit 4bbf44eb9fed06afced809a6bb8b8d94f04d87c3
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-kafka
Version:        2.1.0
Release:        2%{?alphatag}%{?dist}
Summary:        Module for managing apache kafka
License:        Apache 2.0

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
* Tue Nov 15 2016 Alfredo Moralejo <amoralej@redhat.com> 2.1.0-2.4bbf44e.git
- Newton update 2.1.0 (4bbf44eb9fed06afced809a6bb8b8d94f04d87c3)

* Wed Sep 21 2016 Haikel Guemar <hguemar@fedoraproject.org> - 2.1.0-1.061ef74.git
- Newton update 2.1.0 (061ef746e4a0534f652ead2098a03ff09b859461)


