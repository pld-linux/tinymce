find $RPM_BUILD_ROOT -type f -name '*.js' | sed '
	s:'"$RPM_BUILD_ROOT"'::
	s:\(.*/langs/\)\([^/_]\+\)\(.*\.js$\):%lang(\2) \1\2\3:
	s:^\([^%].*\)::
	s:%lang(C) ::
	s:^\$::
' | egrep -v '^$'
