%define __noautoprov '_network.so|htmlsax.so'

Summary:	Check HTML documents for broken links
Name:		linkchecker
Version:	8.0
Release:	1
Url:		http://linkchecker.sourceforge.net
Source0:	http://downloads.sourceforge.net/project/linkchecker/%{version}/LinkChecker-%{version}.tar.xz
License:	GPLv2+
Group:		Networking/WWW
BuildRequires:	python-devel
BuildRequires:	qt4-assistant
Requires:	python-qt4

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
export PATH=$PATH:/usr/lib/qt4/bin/

pushd doc/html
 make
popd

python setup.py build

%install
PYTHONDONTWRITEBYTECODE= python setup.py install --root=%{buildroot}

install -d %{buildroot}/etc
mv %{buildroot}/usr/share/linkchecker/linkcheckerrc %{buildroot}/etc

%find_lang %{name}

%files -f %{name}.lang
%config(noreplace) /etc/*
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{py_platsitedir}/*
%{_mandir}/*/*
%_datadir/%name
