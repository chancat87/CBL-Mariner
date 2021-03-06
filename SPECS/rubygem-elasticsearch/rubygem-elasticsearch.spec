%global debug_package %{nil}
%global gemdir %(IFS=: R=($(gem env gempath)); echo ${R[${#R[@]}-1]})
%global gem_name elasticsearch
Summary:        Ruby integrations for Elasticsearch
Name:           rubygem-elasticsearch
Version:        7.6.0
Release:        1%{?dist}
License:        Apache 2.0
Vendor:         Microsoft Corporation
Distribution:   Mariner
Group:          Development/Languages
URL:            https://rubygems.org/gems/%{gem_name}/versions/%{version}
Source0:        https://rubygems.org/downloads/%{gem_name}-%{version}.gem
BuildRequires:  ruby
Requires:       rubygem-elasticsearch-api
Requires:       rubygem-elasticsearch-transport

%description
Ruby integrations for Elasticsearch (client, API, etc.)

%prep
%setup -q -c -T

%build

%install
gem install -V --local --force --install-dir %{buildroot}/%{gemdir} %{SOURCE0}

%files
%defattr(-,root,root,-)
%license %{gemdir}/gems/%{gem_name}-%{version}/LICENSE
%{gemdir}

%changelog
* Tue Jan 04 2021 Henry Li <lihl@microsoft.com> - 7.6.0-1
- License verified
- Original version for CBL-Mariner