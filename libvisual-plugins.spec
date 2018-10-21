#
# Conditional build:
%bcond_with	gstreamer	# build gstreamer plugin (requires gst 0.8.x)
%bcond_with	esd		# build esd plugin
#
Summary:	libvisual plugins
Summary(pl.UTF-8):	Wtyczki dla libvisual
Name:		libvisual-plugins
Version:	0.4.0
Release:	6
License:	GPL v2+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/libvisual/%{name}-%{version}.tar.gz
# Source0-md5:	4330e9287f9d6fae02f482f428a1e77b
Patch0:		%{name}-ac.patch
URL:		http://libvisual.org/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	alsa-lib-devel >= 1.0.0
BuildRequires:	autoconf >= 2.59-9
BuildRequires:	automake >= 1:1.7
BuildRequires:	bison
%if %{with esd}
BuildRequires:	esound-devel >= 0.2.28
%endif
BuildRequires:	gettext-tools >= 0.14.1
%if %{with gstreamer}
BuildRequires:	gstreamer-devel >= 0.8
BuildRequires:	gstreamer-devel < 0.9
%endif
BuildRequires:	gtk+2-devel >= 2.0
BuildRequires:	jack-audio-connection-kit-devel >= 0.98.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	libvisual-devel >= 0.4.0
BuildRequires:	pkgconfig >= 1:0.14
BuildRequires:	xorg-lib-libXxf86vm-devel
Obsoletes:	libvisual-plugin-actor-lv_dna
Obsoletes:	libvisual-plugin-actor-plazma
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libvisual plugins.

%description -l pl.UTF-8
Wtyczki dla libvisual.

%package -n libvisual-plugin-actor-JESS
Summary:	JESS actor plugin for libvisual
Summary(pl.UTF-8):	Wtyczka aktora JESS dla libvisual
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description -n libvisual-plugin-actor-JESS
JESS actor plugin for libvisual.

%description -n libvisual-plugin-actor-JESS -l pl.UTF-8
Wtyczka aktora JESS dla libvisual.

%package -n libvisual-plugin-actor-bumpscope
Summary:	Bumpscope actor plugin for libvisual
Summary(pl.UTF-8):	Wtyczka aktora Bumpscope dla libvisual
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description -n libvisual-plugin-actor-bumpscope
Bumpscope actor plugin for libvisual - a port of Bumpscope plugin for
XMMS.

%description -n libvisual-plugin-actor-bumpscope -l pl.UTF-8
Wtyczka aktora Bumpscope dla libvisual - port wtyczki Bumpscope dla
XMMS-a.

%package -n libvisual-plugin-actor-corona
Summary:	corona actor plugin for libvisual
Summary(pl.UTF-8):	Wtyczka aktora corona dla libvisual
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description -n libvisual-plugin-actor-corona
corona actor plugin for libvisual.

%description -n libvisual-plugin-actor-corona -l pl.UTF-8
Wtyczka aktora corona dla libvisual.

%package -n libvisual-plugin-actor-flower
Summary:	Pseudotoad flower actor plugin for libvisual - Yellow Rose of Texas
Summary(pl.UTF-8):	Wtyczka aktora Pseudotoad flower dla libvisual - Yellow Rose of Texas
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description -n libvisual-plugin-actor-flower
Pseudotoad flower actor plugin for libvisual - Yellow Rose of Texas.
This plugin renders an awesome responsive flower.

%description -n libvisual-plugin-actor-flower -l pl.UTF-8
Wtyczka aktora Pseudotoad flower dla libvisual - Yellow Rose of Texas.
Ta wtyczka rysuje reagujący kwiatek.

%package -n libvisual-plugin-actor-gdkpixbuf
Summary:	GdkPixbuf actor plugin for libvisual - image loader
Summary(pl.UTF-8):	Wtyczka aktora GdkPixbuf dla libvisual - wczytująca obrazki
License:	LGPL v2.1+
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description -n libvisual-plugin-actor-gdkpixbuf
GdkPixbuf actor plugin for libvisual. It can be used to show images.

%description -n libvisual-plugin-actor-gdkpixbuf -l pl.UTF-8
Wtyczka aktora GdkPixbuf dla libvisual. Potrafi pokazywać obrazki.

%package -n libvisual-plugin-actor-gforce
Summary:	G-Force actor plugin for libvisual
Summary(pl.UTF-8):	Wtyczka aktora G-Force dla libvisual
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description -n libvisual-plugin-actor-gforce
G-Force actor plugin for libvisual - UNIX port of G-Force plugin for
Winamp.

%description -n libvisual-plugin-actor-gforce -l pl.UTF-8
Wtyczka aktura G-Force dla libvisual - uniksowy port wtyczki G-Force
dla Winampa.

%package -n libvisual-plugin-actor-gstreamer
Summary:	GStreamer actor plugin for libvisual - play video or do effects
Summary(pl.UTF-8):	Wtyczka aktora GStreamer dla libvisual - odtwarzanie filmów lub pokazywanie efektów
License:	LGPL v2.1+
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description -n libvisual-plugin-actor-gstreamer
GStreamer actor plugin for libvisual. It's capable of using gstreamer
to play video or do effects using the gstreamer pipeline.

%description -n libvisual-plugin-actor-gstreamer -l pl.UTF-8
Wtyczka aktora GStreamer dla libvisual. Potrafi wykorzystywać
gstreamera do odtwarzania filmów lub pokazywania efektów przy użyciu
potoku gstreamera.

%package -n libvisual-plugin-actor-infinite
Summary:	Infinite actor plugin for libvisual
Summary(pl.UTF-8):	Wtyczka aktora Infinite dla libvisual
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description -n libvisual-plugin-actor-infinite
Infinite actor plugin for libvisual.

%description -n libvisual-plugin-actor-infinite -l pl.UTF-8
Wtyczka aktora Infinite dla libvisual.

%package -n libvisual-plugin-actor-jakdaw
Summary:	Jakdaw actor plugin for libvisual
Summary(pl.UTF-8):	Wtyczka aktora Jakdaw dla libvisual
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description -n libvisual-plugin-actor-jakdaw
Jakdaw actor plugin for libvisual - port of XMMS Jakdaw plugin.

%description -n libvisual-plugin-actor-jakdaw -l pl.UTF-8
Wtyczka aktora Jakdaw dla libvisual - port wtyczki Jakdaw dla XMMS-a.

%package -n libvisual-plugin-actor-lv_analyzer
Summary:	lv_analyzer actor plugin for libvisual - a nice simple spectrum analyzer
Summary(pl.UTF-8):	Wtyczka aktora lv_analyzer dla libvisual - przyjemny analizator widma
License:	LGPL v2.1+
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description -n libvisual-plugin-actor-lv_analyzer
lv_analyzer actor plugin for libvisual - a nice simple spectrum
analyzer.

%description -n libvisual-plugin-actor-lv_analyzer -l pl.UTF-8
Wtyczka aktora lv_analyzer dla libvisual - przyjemny, prosty
analizator widma.

%package -n libvisual-plugin-actor-lv_gltest
Summary:	lv_gltest actor plugin for libvisual - OpenGL analyzer
Summary(pl.UTF-8):	Wtyczka aktora lv_gltest dla libvisual - analizator OpenGL
License:	LGPL v2.1+
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description -n libvisual-plugin-actor-lv_gltest
lv_gltest actor plugin for libvisual. This plugin shows an OpenGL bar
analyzer like the XMMS one.

%description -n libvisual-plugin-actor-lv_gltest -l pl.UTF-8
Wtyczka aktora lv_gltest dla libvisual. Wyświetla w OpenGL-u pasek
analizatora podobny do tego w XMMS-ie.

%package -n libvisual-plugin-actor-lv_scope
Summary:	lv_scope actor plugin for libvisual - display simple scope
Summary(pl.UTF-8):	Wtyczka aktora lv_scope dla libvisual - wyświetlanie prostego zakresu
License:	LGPL v2.1+
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description -n libvisual-plugin-actor-lv_scope
lv_scope actor plugin for libvisual - a test plugin that displays a
simple scope.

%description -n libvisual-plugin-actor-lv_scope -l pl.UTF-8
Wtyczka aktora lv_scope dla libvisual - wtyczka testowa wyświetlająca
prosty zakres.

%package -n libvisual-plugin-actor-madspin
Summary:	madspin actor plugin for libvisual - a nifty visual effect using OpenGL
Summary(pl.UTF-8):	Wtyczka aktora madspin dla libvisual - efekt wizualny wykorzystujący OpenGL
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description -n libvisual-plugin-actor-madspin
madspin actor plugin for libvisual - a nifty visual effect using
OpenGL.

%description -n libvisual-plugin-actor-madspin -l pl.UTF-8
Wtyczka aktora madspin dla libvisual - efekt wizualny wykorzystujący
OpenGL.

%package -n libvisual-plugin-actor-nastyfft
Summary:	NastyFFT actor plugin for libvisual
Summary(pl.UTF-8):	Wtyczka aktora NastyFFT dla libvisual
License:	LGPL v2.1+
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description -n libvisual-plugin-actor-nastyfft
NastyFFT actor plugin for libvisual. It shows nasty FFT visualization
effect using OpenGL.

%description -n libvisual-plugin-actor-nastyfft -l pl.UTF-8
Wtyczka aktora NastyFFT dla libvisual - wyświetla paskudny efekt
wizualizacji FFT przy użyciu OpenGL.

%package -n libvisual-plugin-actor-oinksie
Summary:	Oinksie actor plugin for libvisual
Summary(pl.UTF-8):	Wtyczka aktora Oinksie dla libvisual
License:	LGPL v2.1+
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description -n libvisual-plugin-actor-oinksie
Oinksie actor plugin for libvisual.

%description -n libvisual-plugin-actor-oinksie -l pl.UTF-8
Wtyczka aktora Oinksie dla libvisual.

%package -n libvisual-plugin-input-alsa
Summary:	ALSA input plugin for libvisual
Summary(pl.UTF-8):	Wtyczka wejścia ALSA dla libvisual
License:	LGPL v2.1+
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description -n libvisual-plugin-input-alsa
ALSA input plugin for libvisual.

%description -n libvisual-plugin-input-alsa -l pl.UTF-8
Wtyczka wejściowa ALSA dla libvisual.

%package -n libvisual-plugin-input-esd
Summary:	ESD input plugin for libvisual
Summary(pl.UTF-8):	Wtyczka wejściowa ESD dla libvisual
License:	LGPL v2.1+
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	esound-libs >= 0.2.28

%description -n libvisual-plugin-input-esd
ESD input plugin for libvisual.

%description -n libvisual-plugin-input-esd -l pl.UTF-8
Wtyczka wejściowa ESD dla libvisual.

%package -n libvisual-plugin-input-jack
Summary:	JACK input plugin for libvisual
Summary(pl.UTF-8):	Wtyczka wejściowa JACK dla libvisual
License:	LGPL v2.1+
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
BuildRequires:	jack-audio-connection-kit-libs >= 0.98.0

%description -n libvisual-plugin-input-jack
JACK input plugin for libvisual.

%description -n libvisual-plugin-input-jack -l pl.UTF-8
Wtyczka wejściowa JACK dla libvisual.

%package -n libvisual-plugin-input-mplayer
Summary:	MPlayer input plugin for libvisual - use data exported from MPlayer
Summary(pl.UTF-8):	Wtyczka wejściowa MPlayer dla libvisual - odczyt danych wyeksportowanych z MPlayera
License:	LGPL v2.1+
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description -n libvisual-plugin-input-mplayer
MPlayer input plugin for libvisual. It uses data exported from
'mplayer -af export'.

%description -n libvisual-plugin-input-mplayer -l pl.UTF-8
Wtyczka wejściowa MPlayer dla libvisual. Wykorzystuje dane
wyeksportowane z polecenia "mplayer -af export".

%package -n libvisual-plugin-morph-alphablend
Summary:	alphablend morph plugin for libvisual
Summary(pl.UTF-8):	Wtyczka przejść alphablend dla libvisual
License:	LGPL v2.1+
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description -n libvisual-plugin-morph-alphablend
alphablend morph plugin for libvisual. It morphs between two video
sources using the alphablend method.

%description -n libvisual-plugin-morph-alphablend -l pl.UTF-8
Wtyczka przejść alphablend dla libvisual. Wykonuje przejście między
dwoma źródłami obrazu przy użyciu metody alphablend (blendingu z
kanałem alpha).

%package -n libvisual-plugin-morph-flash
Summary:	flash morph plugin for libvisual - an flash in and out morph
Summary(pl.UTF-8):	Wtyczka przejścia flash dla libvisual - przejscie przez jasny błysk
License:	LGPL v2.1+
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description -n libvisual-plugin-morph-flash
flash morph plugin for libvisual. It morphs between two video sources
using a bright flash.

%description -n libvisual-plugin-morph-flash -l pl.UTF-8
Wtyczka przejścia flash dla libvisual. Wykonuje przejście między dwoma
źródłami obrazu przy użyciu jasnego błysku.

%package -n libvisual-plugin-morph-slide
Summary:	Slide morph plugin for libvisual - slide in/out morph plugin
Summary(pl.UTF-8):	Wtyczka przejścia slide dla libvisual - zmiana slajdów
License:	LGPL v2.1+
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description -n libvisual-plugin-morph-slide
Slide morph plugin for libvisual. It morphs between two video sources
by sliding one in and the other out.

%description -n libvisual-plugin-morph-slide -l pl.UTF-8
Wtyczka przejścia slide dla libvisual. Wykonuje przejście między dwoma
źródłami obrazu poprzez wsunięcie jednego i wysunięcie drugiego.

%package -n libvisual-plugin-morph-tentacle
Summary:	tentacle morph plugin for libvisual - some sort of wave that grows in size
Summary(pl.UTF-8):	Wtyczka przejścia tentacle dla libvisual - powiększająca się fala
License:	LGPL v2.1+
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description -n libvisual-plugin-morph-tentacle
tentacle morph plugin for libvisual. It morphs between two video
sources using some sort of wave that grows in size.

%description -n libvisual-plugin-morph-tentacle -l pl.UTF-8
Wtyczka przejścia tentacle dla libvisual. Wykonuje przejście między
dwoma źródłami obrazu przy użyciu pewnego rodzaju powiększającej się
fali.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__gettextize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	%{!?with_gstreamer:--disable-gstreamer-plugin}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libvisual-*/*/*.la

mv -f $RPM_BUILD_ROOT%{_datadir}/locale/{es_ES,es}
# es_AR is a copy of es
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/es_AR

%find_lang %{name}-0.4

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-0.4.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%dir %{_libdir}/libvisual-*/actor
%dir %{_libdir}/libvisual-*/input
%dir %{_libdir}/libvisual-*/morph
%dir %{_datadir}/libvisual-plugins-*
%dir %{_datadir}/libvisual-plugins-*/actor

%files -n libvisual-plugin-actor-JESS
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvisual-*/actor/actor_JESS.so

%files -n libvisual-plugin-actor-bumpscope
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvisual-*/actor/actor_bumpscope.so

%files -n libvisual-plugin-actor-corona
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvisual-*/actor/actor_corona.so

%files -n libvisual-plugin-actor-flower
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvisual-*/actor/actor_flower.so

%files -n libvisual-plugin-actor-gdkpixbuf
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvisual-*/actor/actor_gdkpixbuf.so

%files -n libvisual-plugin-actor-gforce
%defattr(644,root,root,755)
%doc plugins/actor/G-Force/{AUTHORS,COPYING,NEWS,README,TODO,docs/G-Force.txt}
%attr(755,root,root) %{_libdir}/libvisual-*/actor/actor_gforce.so
%{_datadir}/libvisual-plugins-*/actor/actor_gforce

%if %{with gstreamer}
%files -n libvisual-plugin-actor-gstreamer
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvisual-*/actor/actor_gstreamer.so
%endif

%files -n libvisual-plugin-actor-infinite
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvisual-*/actor/actor_infinite.so

%files -n libvisual-plugin-actor-jakdaw
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvisual-*/actor/actor_jakdaw.so

%files -n libvisual-plugin-actor-lv_analyzer
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvisual-*/actor/actor_lv_analyzer.so

%files -n libvisual-plugin-actor-lv_gltest
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvisual-*/actor/actor_lv_gltest.so

%files -n libvisual-plugin-actor-lv_scope
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvisual-*/actor/actor_lv_scope.so

%files -n libvisual-plugin-actor-madspin
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvisual-*/actor/actor_madspin.so
%{_datadir}/libvisual-plugins-*/actor/actor_madspin

%files -n libvisual-plugin-actor-nastyfft
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvisual-*/actor/actor_nastyfft.so

%files -n libvisual-plugin-actor-oinksie
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvisual-*/actor/actor_oinksie.so

%files -n libvisual-plugin-input-alsa
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvisual-*/input/input_alsa.so

%if %{with esd}
%files -n libvisual-plugin-input-esd
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvisual-*/input/input_esd.so
%endif

%files -n libvisual-plugin-input-jack
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvisual-*/input/input_jack.so

%files -n libvisual-plugin-input-mplayer
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvisual-*/input/input_mplayer.so

%files -n libvisual-plugin-morph-alphablend
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvisual-*/morph/morph_alphablend.so

%files -n libvisual-plugin-morph-flash
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvisual-*/morph/morph_flash.so

%files -n libvisual-plugin-morph-slide
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvisual-*/morph/morph_slide.so

%files -n libvisual-plugin-morph-tentacle
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvisual-*/morph/morph_tentacle.so
