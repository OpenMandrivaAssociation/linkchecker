%define name linkchecker
%define version 4.6
%define release %mkrel 3

Summary: Check HTML documents for broken links
Name: %{name}
Version: %{version}
Release: %{release}
Url: http://linkchecker.sourceforge.net
Source0: http://prdownloads.sourceforge.net/%name/%name-%version.tar.bz2
License: GPL
Group: Networking/WWW
BuildRequires: python-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Conflicts: man-pages-fr < 1.58.0-17mdk

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
%setup -q

find -type f | xargs chmod a+r 
find -type f | xargs perl -pi -e 's|python2\.4|python|g'

%build
python setup.py config #-lcrypto
python setup.py build
make locale PYTHON=python

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --root=%{buildroot}

install -d %{buildroot}/etc
mv %{buildroot}/usr/share/linkchecker/linkcheckerrc %{buildroot}/etc

# as in debian/rules, why??
rm -rf %{buildroot}%{_libdir}/python*/site-packages/linkcheckssl

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-,root,root)
%doc README TODO
%config(noreplace) /etc/*
%{_bindir}/*
%{_libdir}/python*/site-packages/*
%{_mandir}/*/*
%_datadir/%name


