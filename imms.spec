Summary:	Intelligent Multimedia Management System
Name:		imms
Version:	3.0.2
Release:	%mkrel 1
Source0:	http://prdownloads.sourceforge.net/imms/%{name}-%{version}.tar.bz2
Patch: http://www.luminal.org/files/imms/imms-audacious.patch
Patch2: imms-3.0.2-configure.patch
Patch3: imms-3.0.2-build.patch
License:	GPL
Group:		Sound
Url:		http://www.luminal.org/wiki/index.php/IMMS/IMMS
BuildRoot:	%{_tmppath}/%{name}-buildroot
Requires:	sox
Requires:	imms-plugin
BuildRequires:	autoconf2.5
BuildRequires:	fftw-devel >= 3.0
BuildRequires:	torch-devel >= 3
BuildRequires:	oggvorbis-devel >= 1.0
BuildRequires:	pcre-devel >= 4.3
BuildRequires:	readline-devel
BuildRequires:	libglade2.0-devel
BuildRequires:	sox
BuildRequires:	sqlite3-devel >= 3.0
BuildRequires:	taglib-devel
BuildRequires:	xmms-devel >= 1.2.7
BuildRequires:	audacious-devel

%description
IMMS is an adaptive playlist framework that tracks your listening patterns and
dynamically adapts to your taste.

It's major features include:

 * IMMS is easy to use. Song rating is done completely transparently to the
   user. It does not get in your way.

 * IMMS does a much better job of shuffling than most players. It keeps track
   of when a song was last played, and makes sure same songs are not repeated
   too often. It is even able to recognise different versions of the same song
   (eg. remixes) and treat them as one song!

 * IMMS uses a variety of techniques to figure out which songs should be
   played together, and which should not. It studies your listening habits, as
   well as using acoustic properties of the songs themselves, such as BPM and
   frequency spectrum.

 * IMMS is fair. Even unfavoured songs have a (small) chance of being played. 

Currently plugins for the following music players plug are available:

 * XMMS              - package xmms-imms
 * Audacious Media Player - package audacious-imms


%package -n xmms-%{name}
Group:		Sound
Summary:	IMMS plugin for XMMS
Provides:	imms-plugin
Requires:	xmms
Requires:	imms

%description -n xmms-%{name}
This is the Intelligent Multimedia Management System plugin for XMMS.


%package -n audacious-%{name}
Group:		Sound
Summary:	IMMS plugin for the Beep Media Player
Provides:	imms-plugin
Requires:	audacious
Requires:	imms
Provides: beep-media-player-imms
Obsoletes: beep-media-player-imms

%description -n audacious-%{name}
This is the Intelligent Multimedia Management System plugin for the Beep Media
Player.


%prep
%setup -q
%patch -p1 -b .audacious
%patch2 -p1
%patch3 -p1

%build
%configure2_5x
%make all

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%__install -d %{buildroot}/%{_libdir}/xmms/General/
%__install build/libxmmsimms.so %{buildroot}/%{_libdir}/xmms/General/

%__install -d %{buildroot}/%{_libdir}/audacious/General/
%__install build/libaudaciousimms2.so %{buildroot}/%{_libdir}/audacious/General/

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(0755,root,root,0755)
%{_bindir}/immsd
%{_bindir}/immsremote
%{_bindir}/immstool
%{_bindir}/analyzer
%defattr(0644,root,root,0755)
%doc LICENSE INSTALL README
%_datadir/imms


%files -n xmms-%{name}
%defattr(0755,root,root,0755)
%{_libdir}/xmms/General/*


%files -n audacious-%{name}
%defattr(0755,root,root,0755)
%{_libdir}/audacious/General/*


