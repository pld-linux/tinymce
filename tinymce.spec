# TODO
# - separate plugins?
# - separate panguages?
# - is the language separation working at all?
Summary:	Web based Javascript HTML WYSIWYG editor control
Summary(pl):	Kontrolka edytora WYSIWYG HTML-a oparta na WWW z Javascriptem
Name:		tinymce
Version:	1.44
Release:	0.5
Epoch:		0
License:	LGPL
Group:		Applications/WWW
Source0:	http://dl.sourceforge.net/tinymce/%{name}_%(echo %{version} | tr . _).tgz
# Source0-md5:	171cb3ca0fd3232c7822bc06834c8f17
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
  Swedish, Italian, German, Czech, Hungarian, Dutch, Finnish, Danish
  and Arabic and much more.
- Multiple browser support, currently Mozilla, MSIE and FireFox.

%description -l pl
TinyMCE to niezale¿na od platformy kontrolka edytor aWYSIWYG HTML-a
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
  szwedzki, w³oski, niemiecki, czeski, wêgierski, holenderski,
  fiñski, duñski, arabski i inne
- obs³uga wielu przegl±darek, aktualnie Mozilla, MSIE i Firefox

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_examplesdir}/%{name}-%{version},%{_appdir}}

cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a jscripts/tiny_mce/* $RPM_BUILD_ROOT%{_appdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc changelog readme todo
%doc docs/*.htm docs/*.css
%lang(zh_CN) %doc docs/zh_cn

%dir %{_appdir}
%{_appdir}/*.*

%dir %{_appdir}/langs
%lang(ar) %{_appdir}/langs/ar.js
%lang(cs) %{_appdir}/langs/cs.js
%lang(da) %{_appdir}/langs/da.js
%lang(de) %{_appdir}/langs/de.js
%lang(el) %{_appdir}/langs/el.js
%lang(en) %{_appdir}/langs/en.js
%lang(es) %{_appdir}/langs/es.js
%lang(fa) %{_appdir}/langs/fa.js
%lang(fi) %{_appdir}/langs/fi.js
%lang(fr) %{_appdir}/langs/fr.js
%lang(fr_CA) %{_appdir}/langs/fr_ca.js
%lang(hu) %{_appdir}/langs/hu.js
%lang(it) %{_appdir}/langs/it.js
%lang(ja) %{_appdir}/langs/ja.js
%lang(ko) %{_appdir}/langs/ko.js
%lang(nl) %{_appdir}/langs/nl.js
%lang(nb) %{_appdir}/langs/no.js
%lang(pl) %{_appdir}/langs/pl.js
%lang(pt) %{_appdir}/langs/pt.js
%lang(ru) %{_appdir}/langs/ru.js
%lang(sv) %{_appdir}/langs/sv.js
%lang(th) %{_appdir}/langs/th.js
%lang(zh_CN) %{_appdir}/langs/zh_cn.js
%{_appdir}/langs/readme.txt

# TODO languages
%dir %{_appdir}/plugins
%{_appdir}/plugins/readme.txt

%dir %{_appdir}/plugins/advhr
%{_appdir}/plugins/advhr/*.*
%{_appdir}/plugins/advhr/images
%dir %{_appdir}/plugins/advhr/langs
%lang(cs) %{_appdir}/plugins/advhr/langs/cs.js
%lang(de) %{_appdir}/plugins/advhr/langs/de.js
%lang(en) %{_appdir}/plugins/advhr/langs/en.js
%lang(fa) %{_appdir}/plugins/advhr/langs/fa.js
%lang(fr) %{_appdir}/plugins/advhr/langs/fr.js
%lang(fr_CA) %{_appdir}/plugins/advhr/langs/fr_ca.js
%lang(pl) %{_appdir}/plugins/advhr/langs/pl.js
%lang(sv) %{_appdir}/plugins/advhr/langs/sv.js
%lang(zh_CN) %{_appdir}/plugins/advhr/langs/zh_cn.js

# TODO: .. continue after testing is language separation working at all...
%{_appdir}/plugins/advimage
%{_appdir}/plugins/advlink
%{_appdir}/plugins/contextmenu
%{_appdir}/plugins/emotions
%{_appdir}/plugins/flash
%{_appdir}/plugins/iespell
%{_appdir}/plugins/insertdatetime
%{_appdir}/plugins/preview
%{_appdir}/plugins/print
%{_appdir}/plugins/save
%{_appdir}/plugins/searchreplace
%{_appdir}/plugins/table
%{_appdir}/plugins/zoom

# TODO languages
%{_appdir}/themes

%dir %{_examplesdir}/%{name}-%{version}
%{_examplesdir}/%{name}-%{version}/*.*
%lang(zh_CN) %{_examplesdir}/%{name}-%{version}/zh_cn
