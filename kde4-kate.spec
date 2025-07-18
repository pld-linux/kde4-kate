# TODO:
#        /usr/lib64/python2.7/site-packages/PyKate4/__init__.py
#        /usr/lib64/python2.7/site-packages/PyKate4/kate.so
#        /usr/share/kde4/services/pate.desktop

%define		_state		stable
%define		orgname		kate
%define		qtver		4.8.3

Summary:	K Desktop Environment - Advanced Text Editor
Summary(pl.UTF-8):	K Desktop Environment -  Zaawansowany edytor tekstu
Name:		kde4-kate
Version:	4.14.3
Release:	4
License:	GPL
Group:		X11/Applications/Editors
Source0:	http://download.kde.org/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	14da162cc650075cfb364fd39e64924d
Patch0:		cxx.patch
URL:		http://www.kde.org/
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	python-PyKDE4-devel >= %{version}
BuildRequires:	sip-PyQt4
BuildRequires:	shared-mime-info
Obsoletes:	kate <= 4.8.0
Obsoletes:	kde4-kdebase-kwrite < 4.6.99
Obsoletes:	kde4-kdesdk-kate < 4.6.99
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KDE advanced text editor featuring among others:
- fast opening/editing of files even the big ones (opens a 50MB file
  in a few seconds)
- powerful syntaxhighlighting engine, extensible via XML files
- Code Folding capabilities for C++, C, PHP and more
- Dynamic Word Wrap - long lines are wrapped at the window border on
  the fly for better overview
- multiple views allows you to view more instances of the same
  document and/or more documents at one time
- support for different encodings globally and at write time
- built in dockable terminal emulation
- sidebars with a list of open documents, a directory viewer with a
  directory chooser, a filter chooser and more
- a plugin interface to allow third party plugins
- a "Filter" command allows you to run selected text through a shell
  command

KWrite is a simple texteditor, with syntaxhighlighting, codefolding,
dynamic word wrap and more, it's the lightweight version of Kate,
providing more speed for minor tasks.

%description -l pl.UTF-8
Kate (KDE advanced text editor) to zaawansowany edytor tekstu KDE o
możliwościach obejmujących m.in.:
- szybkie otwieranie i edycję nawet dużych plików (otwiera plik 50MB w
  parę sekund)
- potężny silnik podświetlania składni, rozszerzalny za pomocą plików
  XML
- możliwość zwijania kodu dla C++, C, PHP i innych języków
- dynamiczne zawijanie wierszy - długie linie są zawijane na granicy
  okna w locie dla lepszej widoczności
- wiele widoków pozwalających oglądać więcej instancji tego samego
  dokumentu i/lub więcej dokumentów w tym samym czasie
- obsługę różnych kodowań globalnie i w czasie zapisu
- wbudowaną emulację dokowalnego terminala
- paski z listą otwartych dokumentów, przeglądarkę katalogów z
  możliwością wybierania katalogu i filtrów
- interfejs wtyczek obsługujący zewnętrzne wtyczki
- polecenie "Filtr" pozwalające przepuszczać zaznaczony tekst przez
  polecenie powłoki

KWrite to prosty edytor tekstu z podświetlaniem składni, zwijaniem
kodu, dynamicznym zawijaniem wierszy itp. Jest lżejszą wersją Kate,
szybszą dla mniejszych zadań.

%package devel
Summary:	kate development files
Summary(pl.UTF-8):	Pliki dla programistów kate
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	kate-devel <= 4.8.0

%description devel
kate development files.

%description devel -l pl.UTF-8
Pliki dla programistów kate.

%prep
%setup -q -n %{orgname}-%{version}
%patch -P0 -p1

%build
install -d build
cd build
%cmake \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%find_lang      kate            --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{orgname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kate
#%attr(755,root,root) %{_bindir}/ktesnippets_editor
%attr(755,root,root) %{_bindir}/kwrite
%attr(755,root,root) %{_libdir}/kde4/*.so
%attr(755,root,root) %{_libdir}/libkateinterfaces.so
%attr(755,root,root) %{_libdir}/libkateinterfaces.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkateinterfaces.so.?
%attr(755,root,root) %{_libdir}/libkatepartinterfaces.so
%attr(755,root,root) %{_libdir}/libkatepartinterfaces.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkatepartinterfaces.so.?
%attr(755,root,root) %{_libdir}/libkdeinit4_kate.so
%attr(755,root,root) %{_libdir}/libkdeinit4_kwrite.so
%dir %{py_sitedir}/PyKate4
%{py_sitedir}/PyKate4/__init__.py
%attr(755,root,root) %{py_sitedir}/PyKate4/kate.so
%{_datadir}/apps/kate
%{_datadir}/apps/katepart
%{_datadir}/apps/katexmltools
%{_datadir}/apps/kconf_update/kate-2.4.upd
%{_datadir}/apps/ktexteditor_*
%{_datadir}/apps/kwrite
%{_datadir}/config/katemoderc
%{_datadir}/config/katerc
%{_datadir}/config/kateschemarc
%{_datadir}/config/katesyntaxhighlightingrc
%{_datadir}/config/ktexteditor_codesnippets_core.knsrc
%{_datadir}/kde4/services/kate*.desktop
%{_datadir}/kde4/services/ktexteditor_*.desktop
%{_datadir}/kde4/services/pate.desktop
%{_datadir}/kde4/services/plasma-applet-katesession.desktop
%{_datadir}/kde4/servicetypes/kateplugin.desktop
%{_datadir}/kde4/servicetypes/katepythonplugin.desktop
%{_desktopdir}/kde4/kate.desktop
%{_desktopdir}/kde4/kwrite.desktop
%{_iconsdir}/*/*/actions/debug-kategdb.png
%{_iconsdir}/*/*/apps/kate.*
%{_iconsdir}/*/*/apps/ktexteditorautobrace.*
%{_kdedocdir}/en/kwrite
%{_mandir}/man1/kate.1*

%files devel
%defattr(644,root,root,755)
%{_includedir}/kate
%{_includedir}/kate_export.h
