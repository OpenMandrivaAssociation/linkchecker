%define __noautoprov '_network.so|htmlsax.so'

Summary:	Check HTML documents for broken links
Name:		linkchecker
Version:	8.3
Release:	2
Url:		https://linkchecker.sourceforge.net
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


%changelog
* Tue Sep 04 2012 Alexander Khrukin <akhrukin@mandriva.org> 8.0-1
+ Revision: 816345
- version update 8.0

* Wed Jun 13 2012 Alexander Khrukin <akhrukin@mandriva.org> 7.9-1
+ Revision: 805446
- version update 7.9

* Tue May 15 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 7.8-1
+ Revision: 798987
- update to 7.8

* Wed Apr 25 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 7.7-1
+ Revision: 793341
- update to 7.7

* Wed Apr 04 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 7.6-1
+ Revision: 789157
- update to 7.6

* Tue Feb 14 2012 Alexander Khrukin <akhrukin@mandriva.org> 7.5-1
+ Revision: 773925
- version update 7.5

* Tue May 31 2011 Funda Wang <fwang@mandriva.org> 7.0-1
+ Revision: 682018
- update to new version 7.0

* Mon May 09 2011 Funda Wang <fwang@mandriva.org> 6.9-1
+ Revision: 672653
- update to new version 6.9

* Wed Mar 16 2011 Stéphane Téletchéa <steletch@mandriva.org> 6.5-1
+ Revision: 645283
- update to new version 6.5

* Fri Jan 07 2011 Funda Wang <fwang@mandriva.org> 6.2-1mdv2011.0
+ Revision: 629211
- update to new version 6.2

* Sat Dec 25 2010 Funda Wang <fwang@mandriva.org> 6.1-1mdv2011.0
+ Revision: 624726
- update to new version 6.1

* Sun Dec 19 2010 Funda Wang <fwang@mandriva.org> 6.0-1mdv2011.0
+ Revision: 623141
- new version 6.0

* Sun Nov 21 2010 Funda Wang <fwang@mandriva.org> 5.5-1mdv2011.0
+ Revision: 599351
- update to new version 5.5

* Sat Nov 13 2010 Bogdano Arendartchuk <bogdano@mandriva.com> 5.4-1mdv2011.0
+ Revision: 597037
- new version 5.4
- rebuild for python 2.7

* Fri Oct 01 2010 Funda Wang <fwang@mandriva.org> 5.3-1mdv2011.0
+ Revision: 582366
- requires pyqt4 for gui
- New version 5.3

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 4.7-4mdv2010.0
+ Revision: 439541
- rebuild

* Mon Jul 28 2008 Thierry Vignaud <tv@mandriva.org> 4.7-3mdv2009.0
+ Revision: 250802
- rebuild

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 4.7-1mdv2008.1
+ Revision: 136572
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Aug 10 2007 Pixel <pixel@mandriva.com> 4.7-1mdv2008.0
+ Revision: 61052
- new release

