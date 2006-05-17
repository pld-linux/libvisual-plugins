#
# Conditional build:
%bcond_with	gstreamer	# build gstreamer plugin (requires gst 0.8.x)
#
Summary:	libvisual plugins
Summary(pl):	Wtyczki dla libvisual
Name:		libvisual-plugins
Version:	0.4.0
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/libvisual/%{name}-%{version}.tar.gz
# Source0-md5:	4330e9287f9d6fae02f482f428a1e77b
Patch0:		%{name}-ac.patch
URL:		http://libvisual.sourceforge.net/
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	X11 >= 6.8.0
BuildRequires:	alsa-lib-devel >= 1.0.0
BuildRequires:	autoconf >= 2.59-9
BuildRequires:	automake >= 1:1.7
BuildRequires:	bison
BuildRequires:	esound-devel >= 0.2.28
%if %{with gstreamer}
BuildRequires:	gstreamer-devel >= 0.8
BuildRequires:	gstreamer-devel < 0.9
%endif
BuildRequires:	gtk+2-devel >= 2.0
BuildRequires:	jack-audio-connection-kit-devel >= 0.98.0
#BuildRequires:	libgoom2-devel not present in cvs yet
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	libvisual-devel >= 0.4.0
BuildRequires:	pkgconfig >= 1:0.14
Obsoletes:	libvisual-plugin-actor-lv_dna
Obsoletes:	libvisual-plugin-actor-plazma
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libvisual plugins.

%description -l pl
Wtyczki dla libvisual.

%package -n libvisual-plugin-actor-JESS
Summary:	actor-JESS plugin for libvisual
Summary(pl):	Wtyczka actor-JESS dla libvisual
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description -n libvisual-plugin-actor-JESS
actor-JESS plugin for libvisual.

%description -n libvisual-plugin-actor-JESS -l pl
Wtyczka actor-JESS dla libvisual.

%package -n libvisual-plugin-actor-bumpscope
Summary:	actor-bumpscope plugin for libvisual
Summary(pl):	Wtyczka actor-bumpscope dla libvisual
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description -n libvisual-plugin-actor-bumpscope
actor-bumpscope plugin for libvisual.

%description -n libvisual-plugin-actor-bumpscope -l pl
Wtyczka actor-bumpscope dla libvisual.

%package -n libvisual-plugin-actor-corona
Summary:	actor-corona plugin for libvisual
Summary(pl):	Wtyczka actor-corona dla libvisual
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description -n libvisual-plugin-actor-corona
actor-corona plugin for libvisual.

%description -n libvisual-plugin-actor-corona -l pl
Wtyczka actor-corona dla libvisual.

%package -n libvisual-plugin-actor-flower
Summary:	actor-flower plugin for libvisual
Summary(pl):	Wtyczka actor-flower dla libvisual
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description -n libvisual-plugin-actor-flower
actor-flower plugin for libvisual.

%description -n libvisual-plugin-actor-flower -l pl
Wtyczka actor-flower dla libvisual.

%package -n libvisual-plugin-actor-gdkpixbuf
Summary:	actor-gdkpixbuf plugin for libvisual
Summary(pl):	Wtyczka actor-gdkpixbuf dla libvisual
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description -n libvisual-plugin-actor-gdkpixbuf
actor-gdkpixbuf plugin for libvisual.

%description -n libvisual-plugin-actor-gdkpixbuf -l pl
Wtyczka actor-gdkpixbuf dla libvisual.

%package -n libvisual-plugin-actor-gforce
Summary:	actor-gforce plugin for libvisual
Summary(pl):	Wtyczka actor-gforce dla libvisual
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description -n libvisual-plugin-actor-gforce
actor-gforce plugin for libvisual.

%description -n libvisual-plugin-actor-gforce -l pl
Wtyczka actor-gforce dla libvisual.

%package -n libvisual-plugin-actor-gstreamer
Summary:	actor-gstreamer plugin for libvisual
Summary(pl):	Wtyczka actor-gstreamer dla libvisual
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description -n libvisual-plugin-actor-gstreamer
actor-gstreamer plugin for libvisual.

%description -n libvisual-plugin-actor-gstreamer -l pl
Wtyczka actor-gstreamer dla libvisual.

%package -n libvisual-plugin-actor-infinite
Summary:	actor-infinite plugin for libvisual
Summary(pl):	Wtyczka actor-infinite dla libvisual
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description -n libvisual-plugin-actor-infinite
actor-infinite plugin for libvisual.

%description -n libvisual-plugin-actor-infinite -l pl
Wtyczka actor-infinite dla libvisual.

%package -n libvisual-plugin-actor-jakdaw
Summary:	actor-jakdaw plugin for libvisual
Summary(pl):	Wtyczka actor-jakdaw dla libvisual
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description -n libvisual-plugin-actor-jakdaw
actor-jakdaw plugin for libvisual.

%description -n libvisual-plugin-actor-jakdaw -l pl
Wtyczka actor-jakdaw dla libvisual.

%package -n libvisual-plugin-actor-lv_analyzer
Summary:	actor-lv_analyzer plugin for libvisual
Summary(pl):	Wtyczka actor-lv_analyzer dla libvisual
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description -n libvisual-plugin-actor-lv_analyzer
actor-lv_analyzer plugin for libvisual.

%description -n libvisual-plugin-actor-lv_analyzer -l pl
Wtyczka actor-lv_analyzer dla libvisual.

%package -n libvisual-plugin-actor-lv_gltest
Summary:	actor-lv_gltest plugin for libvisual
Summary(pl):	Wtyczka actor-lv_gltest dla libvisual
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description -n libvisual-plugin-actor-lv_gltest
actor-lv_gltest plugin for libvisual.

%description -n libvisual-plugin-actor-lv_gltest -l pl
Wtyczka actor-lv_gltest dla libvisual.

%package -n libvisual-plugin-actor-lv_scope
Summary:	actor-lv_scope plugin for libvisual
Summary(pl):	Wtyczka actor-lv_scope dla libvisual
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description -n libvisual-plugin-actor-lv_scope
actor-lv_scope plugin for libvisual.

%description -n libvisual-plugin-actor-lv_scope -l pl
Wtyczka actor-lv_scope dla libvisual

%package -n libvisual-plugin-actor-madspin
Summary:	actor-madspin plugin for libvisual
Summary(pl):	Wtyczka actor-madspin dla libvisual
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description -n libvisual-plugin-actor-madspin
actor-madspin plugin for libvisual.

%description -n libvisual-plugin-actor-madspin -l pl
Wtyczka actor-madspin dla libvisual.

%package -n libvisual-plugin-actor-nastyfft
Summary:	actor-nastyfft plugin for libvisual
Summary(pl):	Wtyczka actor-nastyfft dla libvisual
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description -n libvisual-plugin-actor-nastyfft
actor-nastyfft plugin for libvisual.

%description -n libvisual-plugin-actor-nastyfft -l pl
Wtyczka actor-nastyfft dla libvisual.

%package -n libvisual-plugin-actor-oinksie
Summary:	actor-oinksie plugin for libvisual
Summary(pl):	Wtyczka actor-oinksie dla libvisual
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description -n libvisual-plugin-actor-oinksie
actor-oinksie plugin for libvisual.

%description -n libvisual-plugin-actor-oinksie -l pl
Wtyczka actor-oinksie dla libvisual.

%package -n libvisual-plugin-input-alsa
Summary:	ALSA input plugin for libvisual
Summary(pl):	Wtyczka wej¶cia ALSA dla libvisual
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description -n libvisual-plugin-input-alsa
ALSA input plugin for libvisual.

%description -n libvisual-plugin-input-alsa -l pl
Wtyczka wej¶ciowa ALSA dla libvisual.

%package -n libvisual-plugin-input-esd
Summary:	ESD input plugin for libvisual
Summary(pl):	Wtyczka wej¶ciowa ESD dla libvisual
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description -n libvisual-plugin-input-esd
ESD input plugin for libvisual.

%description -n libvisual-plugin-input-esd -l pl
Wtyczka wej¶ciowa ESD dla libvisual.

%package -n libvisual-plugin-input-jack
Summary:	JACK input plugin for libvisual
Summary(pl):	Wtyczka wej¶ciowa JACK dla libvisual
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description -n libvisual-plugin-input-jack
JACK input plugin for libvisual.

%description -n libvisual-plugin-input-jack -l pl
Wtyczka wej¶ciowa JACK dla libvisual.

%package -n libvisual-plugin-input-mplayer
Summary:	Mplayer input plugin for libvisual
Summary(pl):	Wtyczka wej¶ciowa mplayera dla libvisual
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description -n libvisual-plugin-input-mplayer
Mplayer input plugin for libvisual.

%description -n libvisual-plugin-input-mplayer -l pl
Wtyczka wej¶ciowa mplayera dla libvisual.

%package -n libvisual-plugin-morph-alphablend
Summary:	morph-alphablend plugin for libvisual
Summary(pl):	Wtyczka morph-alphablend dla libvisual
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description -n libvisual-plugin-morph-alphablend
morph-alphablend plugin for libvisual.

%description -n libvisual-plugin-morph-alphablend -l pl
Wtyczka morph-alphablend dla libvisual.

%package -n libvisual-plugin-morph-flash
Summary:	morph-flash plugin for libvisual
Summary(pl):	Wtyczka morph-flash dla libvisual
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description -n libvisual-plugin-morph-flash
morph-flash plugin for libvisual.

%description -n libvisual-plugin-morph-flash -l pl
Wtyczka morph-flash dla libvisual.

%package -n libvisual-plugin-morph-slide
Summary:	morph-slide plugin for libvisual
Summary(pl):	Wtyczka morph-slide dla libvisual
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description -n libvisual-plugin-morph-slide
morph-slide plugin for libvisual.

%description -n libvisual-plugin-morph-slide -l pl
Wtyczka morph-slide dla libvisual.

%package -n libvisual-plugin-morph-tentacle
Summary:	morph-tentacle plugin for libvisual
Summary(pl):	Wtyczka morph-tentacle dla libvisual
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description -n libvisual-plugin-morph-tentacle
morph-tentacle plugin for libvisual.

%description -n libvisual-plugin-morph-tentacle -l pl
Wtyczka morph-tentacle dla libvisual.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
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

rm -f $RPM_BUILD_ROOT%{_libdir}/libvisual-*/*/*.la

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

%files -n libvisual-plugin-input-esd
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvisual-*/input/input_esd.so

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
