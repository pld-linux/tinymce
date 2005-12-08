# TODO
# - separate plugins?
# - separate languages?
# - is the language separation working at all?
%define	_ver %(echo %{version} | tr . _)
Summary:	Web based Javascript HTML WYSIWYG editor control
Summary(pl):	Kontrolka edytora WYSIWYG HTML-a oparta na WWW z Javascriptem
Name:		tinymce
Version:	2.0.1
Release:	0.3
License:	LGPL v2
Group:		Applications/WWW
Source0:	http://dl.sourceforge.net/tinymce/%{name}_%{_ver}.tgz
# Source0-md5:	c6ee73d135a5b677dacd3feaf3b9c223
Source1:	tinymce-find_lang.sh
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
install %{SOURCE1} find_lang.sh
mv docs html

rm -f jscripts/tiny_mce/license.txt # LGPL v2

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_examplesdir}/%{name}-%{version},%{_appdir}}

cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a jscripts/tiny_mce/* $RPM_BUILD_ROOT%{_appdir}

./find_lang.sh > %{name}.lang

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
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

%dir %{_appdir}/plugins
%{_appdir}/plugins/readme.txt

%dir %{_appdir}/plugins/_template
%{_appdir}/plugins/_template/*.*
%{_appdir}/plugins/_template/images
%dir %{_appdir}/plugins/_template/langs

%dir %{_appdir}/plugins/advhr
%{_appdir}/plugins/advhr/*.*
%{_appdir}/plugins/advhr/images
%{_appdir}/plugins/advhr/jscripts
%dir %{_appdir}/plugins/advhr/langs

%dir %{_appdir}/plugins/advimage
%{_appdir}/plugins/advimage/*.*
%{_appdir}/plugins/advimage/css
%{_appdir}/plugins/advimage/images
%{_appdir}/plugins/advimage/jscripts
%dir %{_appdir}/plugins/advimage/langs

%dir %{_appdir}/plugins/advlink
%{_appdir}/plugins/advlink/*.*
%{_appdir}/plugins/advlink/css
%{_appdir}/plugins/advlink/jscripts
%dir %{_appdir}/plugins/advlink/langs

%dir %{_appdir}/plugins/autosave
%{_appdir}/plugins/autosave/*.*
%dir %{_appdir}/plugins/autosave/langs

%{_appdir}/plugins/contextmenu

%dir %{_appdir}/plugins/directionality
%{_appdir}/plugins/directionality/*.*
%{_appdir}/plugins/directionality/images
%dir %{_appdir}/plugins/directionality/langs

%dir %{_appdir}/plugins/emotions
%{_appdir}/plugins/emotions/*.*
%{_appdir}/plugins/emotions/images
%{_appdir}/plugins/emotions/jscripts
%dir %{_appdir}/plugins/emotions/langs

%dir %{_appdir}/plugins/flash
%{_appdir}/plugins/flash/*.*
%{_appdir}/plugins/flash/css
%{_appdir}/plugins/flash/images
%{_appdir}/plugins/flash/jscripts
%dir %{_appdir}/plugins/flash/langs

%dir %{_appdir}/plugins/fullscreen
%{_appdir}/plugins/fullscreen/*.*
%{_appdir}/plugins/fullscreen/images
%dir %{_appdir}/plugins/fullscreen/langs

%dir %{_appdir}/plugins/iespell
%{_appdir}/plugins/iespell/*.*
%{_appdir}/plugins/iespell/images
%dir %{_appdir}/plugins/iespell/langs

%dir %{_appdir}/plugins/inlinepopups
%{_appdir}/plugins/inlinepopups/*.*
%{_appdir}/plugins/inlinepopups/images
%{_appdir}/plugins/inlinepopups/css
%{_appdir}/plugins/inlinepopups/jscripts

%dir %{_appdir}/plugins/insertdatetime
%{_appdir}/plugins/insertdatetime/*.*
%{_appdir}/plugins/insertdatetime/images
%dir %{_appdir}/plugins/insertdatetime/langs

%{_appdir}/plugins/noneditable

%dir %{_appdir}/plugins/paste
%{_appdir}/plugins/paste/*.*
%{_appdir}/plugins/paste/css
%{_appdir}/plugins/paste/images
%{_appdir}/plugins/paste/jscripts
%dir %{_appdir}/plugins/paste/langs

%dir %{_appdir}/plugins/preview
%{_appdir}/plugins/preview/*.*
%{_appdir}/plugins/preview/images
%dir %{_appdir}/plugins/preview/langs

%dir %{_appdir}/plugins/print
%{_appdir}/plugins/print/*.*
%{_appdir}/plugins/print/images
%dir %{_appdir}/plugins/print/langs

%dir %{_appdir}/plugins/save
%{_appdir}/plugins/save/*.*
%{_appdir}/plugins/save/images
%dir %{_appdir}/plugins/save/langs

%dir %{_appdir}/plugins/searchreplace
%{_appdir}/plugins/searchreplace/*.*
%{_appdir}/plugins/searchreplace/images
%{_appdir}/plugins/searchreplace/jscripts
%dir %{_appdir}/plugins/searchreplace/langs

%dir %{_appdir}/plugins/table
%{_appdir}/plugins/table/*.*
%{_appdir}/plugins/table/css
%{_appdir}/plugins/table/images
%{_appdir}/plugins/table/jscripts
%dir %{_appdir}/plugins/table/langs
%{_appdir}/plugins/table/langs/readme.txt

%dir %{_appdir}/plugins/zoom
%{_appdir}/plugins/zoom/*.*

%dir %{_appdir}/themes
%{_appdir}/themes/simple

%dir %{_appdir}/themes/advanced
%{_appdir}/themes/advanced/*.*
%{_appdir}/themes/advanced/css
%{_appdir}/themes/advanced/docs
%{_appdir}/themes/advanced/images
%{_appdir}/themes/advanced/jscripts
%dir %{_appdir}/themes/advanced/langs
%{_appdir}/themes/advanced/langs/*.txt
