Summary: Check HTML documents for broken links
Name: linkchecker
Version: 5.4
Release: %mkrel 1
Url: http://linkchecker.sourceforge.net
Source0: http://downloads.sourceforge.net/project/linkchecker/%{version}/LinkChecker-%{version}.tar.gz
License: GPL
Group: Networking/WWW
BuildRequires: python-devel
BuildRequires: qt4-assistant
Requires: python-qt4
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
 Features:
  o recursive checking
  o multithreaded
  o output can be colored or normal text, HTML, SQL, CSV or a sitemap
    graph in GML or XML
  o HTTP/1.1, FTP, mailto:, nntp:, news:, Gopher, Telnet and local 
    file links are supported
  o restrict link checking with regular expression filters for URLs
  o proxy support
  o give username/password for HTTP and FTP authorization
  o robots.txt exclusion protocol support 
  o i18n support
  o command line interface
  o (Fast)CGI web interface (requires HTTP server)

%prep
%setup -qn LinkChecker-%{version}

%build
pushd doc/html
make
popd
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --root=%{buildroot}

install -d %{buildroot}/etc
mv %{buildroot}/usr/share/linkchecker/linkcheckerrc %{buildroot}/etc

%find_lang LinkChecker

%clean
rm -rf $RPM_BUILD_ROOT

%files -f LinkChecker.lang
%defattr(-,root,root)
%doc readme.txt
%config(noreplace) /etc/*
%{_bindir}/*
%{py_platsitedir}/*
%{_mandir}/*/*
%_datadir/%name
