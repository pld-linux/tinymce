# TODO
# - separate plugins?
%define	_ver %(echo %{version} | tr . _)
Summary:	Web based Javascript HTML WYSIWYG editor control
Summary(pl):	Kontrolka edytora WYSIWYG HTML-a oparta na WWW z Javascriptem
Name:		tinymce
Version:	2.0.8
Release:	0.1
License:	LGPL v2
Group:		Applications/WWW
Source0:	http://dl.sourceforge.net/tinymce/%{name}_%{_ver}.tgz
# Source0-md5:	1e830e21c329278d8665966b82af2dfe
URL:		http://tinymce.moxiecode.com/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/%{name}

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

%description -l pl
TinyMCE to niezale¿na od platformy kontrolka edytora WYSIWYG HTML-a
oparta na WWW z Javascriptem opublikowana z otwartymi ¼ród³ami na
warunkach licencji LGPL przez Moxiecode Systems AB. Ma mo¿liwo¶æ
przekszta³cenia pól HTML TEXTAREA i innych elementów HTML-a w
instancje edytora. TinyMCE jest bardzo ³atwy do integracji w innych
systemach CMS.

Mo¿liwo¶ci:
- ³atwa do zintegrowania przy u¿yciu tylko dwóch linijek kodu
- obs³uga motywów i szablonów
- obs³uga wtyczek
- ³atwa do rozszerzenia w³asnym kodem
- dostosowywalne wyj¶cie HTML/XHML 1.0; elementy block invalid i
  atrybuty force
- obs³uga wielu jêzyków (pakiety jêzykowe) - aktualnie angielski,
  szwedzki, w³oski, niemiecki, czeski, wêgierski, holenderski, fiñski,
  duñski, arabski i inne
- obs³uga wielu przegl±darek, aktualnie Mozilla, MSIE i Firefox

%prep
%setup -q -n %{name}
mv docs html

rm -f jscripts/tiny_mce/license.txt # LGPL v2

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_examplesdir}/%{name}-%{version},%{_appdir}}

cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a jscripts/tiny_mce/* $RPM_BUILD_ROOT%{_appdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc changelog readme
%doc html

%{_examplesdir}/%{name}-%{version}

%dir %{_appdir}
%{_appdir}/*.js
%{_appdir}/*.htm
%{_appdir}/utils

%dir %{_appdir}/langs
%{_appdir}/langs/readme.txt
%{_appdir}/langs/en.js

%dir %{_appdir}/plugins
%{_appdir}/plugins/readme.txt

%{_appdir}/plugins/advhr
%{_appdir}/plugins/advimage
%{_appdir}/plugins/advlink
%{_appdir}/plugins/autosave
%{_appdir}/plugins/cleanup
%{_appdir}/plugins/contextmenu
%{_appdir}/plugins/devkit
%{_appdir}/plugins/directionality
%{_appdir}/plugins/emotions
%{_appdir}/plugins/flash
%{_appdir}/plugins/fullpage
%{_appdir}/plugins/fullscreen
%{_appdir}/plugins/iespell
%{_appdir}/plugins/inlinepopups
%{_appdir}/plugins/insertdatetime
%{_appdir}/plugins/layer
%{_appdir}/plugins/media
%{_appdir}/plugins/nonbreaking
%{_appdir}/plugins/noneditable
%{_appdir}/plugins/paste
%{_appdir}/plugins/preview
%{_appdir}/plugins/print
%{_appdir}/plugins/save
%{_appdir}/plugins/searchreplace
%{_appdir}/plugins/style
%{_appdir}/plugins/table
%{_appdir}/plugins/visualchars
%{_appdir}/plugins/xhtmlxtras
%{_appdir}/plugins/zoom

%{_appdir}/themes/simple
%{_appdir}/themes/advanced
