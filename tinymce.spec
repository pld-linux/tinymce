# TODO
# - separate plugins?
%define		ver %(echo %{version} | tr . _)
Summary:	Web based Javascript HTML WYSIWYG editor control
Summary(pl.UTF-8):	Kontrolka edytora WYSIWYG HTML-a oparta na WWW z Javascriptem
Name:		tinymce
Version:	3.2.4.1
Release:	1
License:	LGPL v2
Group:		Applications/WWW
Source0:	http://dl.sourceforge.net/tinymce/%{name}_%{ver}.zip
# Source0-md5:	70bf7209515af5fccf1c33b6319f4cd7
URL:		http://tinymce.moxiecode.com/
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	sed >= 4.0
BuildRequires:	unzip
Requires:	webapps
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_webapps	/etc/webapps
%define		_webapp		%{name}
%define		_sysconfdir	%{_webapps}/%{_webapp}
%define		_appdir		%{_datadir}/%{name}

%description
TinyMCE is a platform independent web based Javascript HTML WYSIWYG
editor control released as Open Source under LGPL by Moxiecode Systems
AB. It has the ability to convert HTML TEXTAREA fields or other HTML
elements to editor instances. TinyMCE is very easy to integrate into
other CMS systems.

Features:
- Easy to integrate, takes only two lines of code.
- Theme and template support.
- Plugin support.
- Easy to extend with custom code.
- Customizable HTML/XHTML 1.0 output. Block invalid elements and force
  attributes.
- International language support (Language packs) currenly English,
  Swedish, Italian, German, Czech, Hungarian, Dutch, Finnish, Danish and
  Arabic and much more.
- Multiple browser support, currently Mozilla, MSIE and FireFox.

%description -l pl.UTF-8
TinyMCE to niezależna od platformy kontrolka edytora WYSIWYG HTML-a
oparta na WWW z Javascriptem opublikowana z otwartymi źródłami na
warunkach licencji LGPL przez Moxiecode Systems AB. Ma możliwość
przekształcenia pól HTML TEXTAREA i innych elementów HTML-a w
instancje edytora. TinyMCE jest bardzo łatwy do integracji w innych
systemach CMS.

Możliwości:
- łatwa do zintegrowania przy użyciu tylko dwóch linijek kodu
- obsługa motywów i szablonów
- obsługa wtyczek
- łatwa do rozszerzenia własnym kodem
- dostosowywalne wyjście HTML/XHML 1.0; elementy block invalid i
  atrybuty force
- obsługa wielu języków (pakiety językowe) - aktualnie angielski,
  szwedzki, włoski, niemiecki, czeski, węgierski, holenderski, fiński,
  duński, arabski i inne
- obsługa wielu przeglądarek, aktualnie Mozilla, MSIE i Firefox

%prep
%setup -qc

find '(' -name '*.js' -o -name '*.css' -o -name '*.html' -o -name '*.htm' ')' -print0 | xargs -0 sed -i -e 's,\r$,,'

rm jscripts/tiny_mce/license.txt # LGPL v2

find -name '*_src.js' | xargs rm

mv jscripts/tiny_mce/plugins/example .

# tinymce-spellchecker.spec packages this
rm -rf jscripts/tiny_mce/plugins/spellchecker

cat <<'EOF' > apache.conf
Alias /tiny_mce/ %{_appdir}/
<Directory %{_appdir}>
	Allow from all
</Directory>
EOF

cat > lighttpd.conf <<'EOF'
alias.url += (
    "/tiny_mce/" => "%{_appdir}/",
)
EOF

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_examplesdir}/%{name}-%{version},%{_appdir},%{_sysconfdir}}

cp -a example examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a jscripts/tiny_mce/* $RPM_BUILD_ROOT%{_appdir}

cp -a apache.conf $RPM_BUILD_ROOT%{_sysconfdir}/apache.conf
cp -a apache.conf $RPM_BUILD_ROOT%{_sysconfdir}/httpd.conf
cp -a lighttpd.conf $RPM_BUILD_ROOT%{_sysconfdir}/lighttpd.conf

%clean
rm -rf $RPM_BUILD_ROOT

%triggerin -- apache1 < 1.3.37-3, apache1-base
%webapp_register apache %{_webapp}

%triggerun -- apache1 < 1.3.37-3, apache1-base
%webapp_unregister apache %{_webapp}

%triggerin -- apache < 2.2.0, apache-base
%webapp_register httpd %{_webapp}

%triggerun -- apache < 2.2.0, apache-base
%webapp_unregister httpd %{_webapp}

%triggerin -- lighttpd
%webapp_register lighttpd %{_webapp}

%triggerun -- lighttpd
%webapp_unregister lighttpd %{_webapp}

%files
%defattr(644,root,root,755)
%doc changelog.txt
%dir %attr(750,root,http) %{_sysconfdir}
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/apache.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/httpd.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/lighttpd.conf

%dir %{_appdir}
%{_appdir}/*.js
%{_appdir}/utils

%dir %{_appdir}/langs
%{_appdir}/langs/en.js

%dir %{_appdir}/plugins

%{_appdir}/plugins/advhr
%{_appdir}/plugins/advimage
%{_appdir}/plugins/advlink
%{_appdir}/plugins/autosave
%{_appdir}/plugins/bbcode
%{_appdir}/plugins/compat2x
%{_appdir}/plugins/contextmenu
%{_appdir}/plugins/directionality
%{_appdir}/plugins/emotions
%{_appdir}/plugins/fullpage
%{_appdir}/plugins/fullscreen
%{_appdir}/plugins/iespell
%{_appdir}/plugins/inlinepopups
%{_appdir}/plugins/insertdatetime
%{_appdir}/plugins/layer
%{_appdir}/plugins/media
%{_appdir}/plugins/nonbreaking
%{_appdir}/plugins/noneditable
%{_appdir}/plugins/pagebreak
%{_appdir}/plugins/paste
%{_appdir}/plugins/preview
%{_appdir}/plugins/print
%{_appdir}/plugins/safari
%{_appdir}/plugins/save
%{_appdir}/plugins/searchreplace
%{_appdir}/plugins/style
%{_appdir}/plugins/tabfocus
%{_appdir}/plugins/table
%{_appdir}/plugins/template
%{_appdir}/plugins/visualchars
%{_appdir}/plugins/xhtmlxtras

%dir %{_appdir}/themes
%{_appdir}/themes/simple
%{_appdir}/themes/advanced

%{_examplesdir}/%{name}-%{version}
