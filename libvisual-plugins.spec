Summary:	libvisual plugins
Summary(pl):	Wtyczki dla libvisual
Name:		libvisual-plugins
Version:	0.2.0
Release:	0.1
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/libvisual/%{name}-%{version}.tar.gz
# Source0-md5:	b7c7dcae33a510af36c6bb9cdb7133dd
URL:		http://libvisual.sourceforge.net/
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	alsa-lib-devel >= 1.0.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	esound-devel >= 0.2.28
BuildRequires:	gtk+2-devel
BuildRequires:	jack-audio-connection-kit-devel >= 0.98
#BuildRequires:	libgoom2-devel not present in cvs yet
BuildRequires:	libtool
BuildRequires:	libvisual-devel >= 0.2.0
BuildRequires:	pkgconfig >= 1:0.14
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libvisual plugins.

%description -l pl
Wtyczki dla libvisual.

%package -n libvisual-plugin-actor-bumpscope
Summary:	actor-bumpscope plugin for libvisual
Summary(pl):	Wtyczka actor-bumpscope dla libvisual
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description -n libvisual-plugin-actor-bumpscope
actor-bumpscope plugin for libvisual.

%description -n libvisual-plugin-actor-bumpscope -l pl
Wtyczka actor-bumpscope dla libvisual.

%package -n libvisual-plugin-actor-gdkpixbuf
Summary:	actor-gdkpixbuf plugin for libvisual
Summary(pl):	Wtyczka actor-gdkpixbuf dla libvisual
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description -n libvisual-plugin-actor-gdkpixbuf
actor-gdkpixbuf plugin for libvisual.

%description -n libvisual-plugin-actor-gdkpixbuf -l pl
Wtyczka actor-gdkpixbuf dla libvisual.

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

%package -n libvisual-plugin-actor-JESS
Summary:	actor-JESS plugin for libvisual
Summary(pl):	Wtyczka actor-JESS dla libvisual
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description -n libvisual-plugin-actor-JESS
actor-JESS plugin for libvisual.

%description -n libvisual-plugin-actor-JESS -l pl
Wtyczka actor-JESS dla libvisual.

%package -n libvisual-plugin-actor-lv_analyzer
Summary:	actor-lv_analyzer plugin for libvisual
Summary(pl):	Wtyczka actor-lv_analyzer dla libvisual
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description -n libvisual-plugin-actor-lv_analyzer
actor-lv_analyzer plugin for libvisual.

%description -n libvisual-plugin-actor-lv_analyzer -l pl
Wtyczka actor-lv_analyzer dla libvisual.

%package -n libvisual-plugin-actor-lv_dna
Summary: actor-lv_dna plugin for libvisual 
Summary(pl): Wtyczka actor-lv_dna dla libvisual
Group: Libraries 
Requires: %{name} = %{version}-%{release}

%description -n libvisual-plugin-actor-lv_dna
actor-lv_dna plugin for libvisual.

%description -n libvisual-plugin-actor-lv_dna -l pl 
Wtyczka actor-lv_dna dla libvisual.

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

%package -n libvisual-plugin-actor-oinksie
Summary:	actor-oinksie plugin for libvisual
Summary(pl):	Wtyczka actor-oinksie dla libvisual
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description -n libvisual-plugin-actor-oinksie
actor-oinksie plugin for libvisual.

%description -n libvisual-plugin-actor-oinksie -l pl
Wtyczka actor-oinksie dla libvisual.

%package -n libvisual-plugin-actor-plazma
Summary:	actor-plazma plugin for libvisual
Summary(pl):	Wtyczka actor-plazma dla libvisual
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description -n libvisual-plugin-actor-plazma
actor-plazma plugin for libvisual.

%description -n libvisual-plugin-actor-plazma -l pl
Wtyczka actor-plazma dla libvisual.

%package -n libvisual-plugin-input-alsa
Summary:	Alsa plugin for libvisual
Summary(pl):	Wtyczka alsy dla libvisual
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description -n libvisual-plugin-input-alsa
Alsa plugin for libvisual.

%description -n libvisual-plugin-input-alsa -l pl
Wtyczka alsy dla libvisual.

%package -n libvisual-plugin-input-esd
Summary:	ESD plugin for libvisual
Summary(pl):	Wtyczka ESD dla libvisual
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description -n libvisual-plugin-input-esd
ESD plugin for libvisual.

%description -n libvisual-plugin-input-esd -l pl
Wtyczka ESD dla libvisual.

%package -n libvisual-plugin-input-mplayer
Summary:	Mplayer plugin for libvisual
Summary(pl):	Wtyczka mplayera dla libvisual
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description -n libvisual-plugin-input-mplayer
Mplayer plugin for libvisual.

%description -n libvisual-plugin-input-mplayer -l pl
Wtyczka mplayera dla libvisual.

%package -n libvisual-plugin-input-jack
Summary:	jack plugin for libvisual
Summary(pl):	Wtyczka jack dla libvisual
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description -n libvisual-plugin-input-jack
jack plugin for libvisual.

%description -n libvisual-plugin-input-jack -l pl
Wtyczka jack dla libvisual.

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

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--enable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/libvisual/*/*.{a,la}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%dir %{_libdir}/libvisual/actor
%dir %{_libdir}/libvisual/input
%dir %{_libdir}/libvisual/morph

%files -n libvisual-plugin-actor-bumpscope
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvisual/actor/actor_bumpscope.so

%files -n libvisual-plugin-actor-gdkpixbuf
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvisual/actor/actor_gdkpixbuf.so

%files -n libvisual-plugin-actor-infinite
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvisual/actor/actor_infinite.so

%files -n libvisual-plugin-actor-jakdaw
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvisual/actor/actor_jakdaw.so

%files -n libvisual-plugin-actor-JESS
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvisual/actor/actor_JESS.so

%files -n libvisual-plugin-actor-lv_analyzer
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvisual/actor/actor_lv_analyzer.so

#%files -n libvisual-plugin-actor-lv_dna
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/libvisual/actor/actor_lv_dna.so

%files -n libvisual-plugin-actor-lv_gltest
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvisual/actor/actor_lv_gltest.so

%files -n libvisual-plugin-actor-lv_scope
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvisual/actor/actor_lv_scope.so

%files -n libvisual-plugin-actor-madspin
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvisual/actor/actor_madspin.so
%dir %{_datadir}/libvisual/actor/actor_madspin
%attr(755,root,root) %{_datadir}/libvisual/actor/actor_madspin/*

%files -n libvisual-plugin-actor-oinksie
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvisual/actor/actor_oinksie.so

%files -n libvisual-plugin-actor-plazma
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvisual/actor/actor_plazma.so

%files -n libvisual-plugin-input-alsa
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvisual/input/input_alsa.so

%files -n libvisual-plugin-input-esd
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvisual/input/input_esd.so

%files -n libvisual-plugin-input-mplayer
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvisual/input/input_mplayer.so

%files -n libvisual-plugin-input-jack
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvisual/input/input_jack.so

%files -n libvisual-plugin-morph-alphablend
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvisual/morph/morph_alphablend.so

%files -n libvisual-plugin-morph-flash
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvisual/morph/morph_flash.so

%files -n libvisual-plugin-morph-slide
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvisual/morph/morph_slide.so

%files -n libvisual-plugin-morph-tentacle
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvisual/morph/morph_tentacle.so
