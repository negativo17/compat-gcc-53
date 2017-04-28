%global DATE 20160406
%global SVNREV 234777
%global gcc_version 5.3.1
%global gcc_compat_version 5
# Note, gcc_release must be integer, if you want to add suffixes to
# %{release}, append them after %{gcc_release} on Release: line.
%global gcc_release 6
%global _unpackaged_files_terminate_build 0
%global _performance_build 1
# Hardening slows the compiler way too much.
%undefine _hardened_build

%global attr_ifunc 1
Summary: Various compilers (C, C++, Objective-C, Java, ...)
Name: compat-gcc-%{gcc_compat_version}
Version: %{gcc_version}
Release: %{gcc_release}%{?dist}
# libgcc, libgfortran, libgomp, libstdc++ and crtstuff have
# GCC Runtime Exception.
License: GPLv3+ and GPLv3+ with exceptions and GPLv2+ with exceptions and LGPLv2+ and BSD
Group: Development/Languages
# The source for this package was pulled from upstream's vcs.  Use the
# following commands to generate the tarball:
# svn export svn://gcc.gnu.org/svn/gcc/branches/redhat/gcc-5-branch@%{SVNREV} gcc-%{version}-%{DATE}
# tar cf - gcc-%{version}-%{DATE} | bzip2 -9 > gcc-%{version}-%{DATE}.tar.bz2
Source0: gcc-%{version}-%{DATE}.tar.bz2
Source1: dummylib.sh
%global isl_version 0.14
URL: http://gcc.gnu.org
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
# Need binutils with -pie support >= 2.14.90.0.4-4
# Need binutils which can omit dot symbols and overlap .opd on ppc64 >= 2.15.91.0.2-4
# Need binutils which handle -msecure-plt on ppc >= 2.16.91.0.2-2
# Need binutils which support .weakref >= 2.16.91.0.3-1
# Need binutils which support --hash-style=gnu >= 2.17.50.0.2-7
# Need binutils which support mffgpr and mftgpr >= 2.17.50.0.2-8
# Need binutils which support --build-id >= 2.17.50.0.17-3
# Need binutils which support %gnu_unique_object >= 2.19.51.0.14
# Need binutils which support .cfi_sections >= 2.19.51.0.14-33
# Need binutils which support --no-add-needed >= 2.20.51.0.2-12
# Need binutils which support -plugin
BuildRequires: binutils >= 2.24
# While gcc doesn't include statically linked binaries, during testing
# -static is used several times.
BuildRequires: glibc-static
BuildRequires: zlib-devel, gettext, dejagnu, bison, flex, sharutils
BuildRequires: texinfo, texinfo-tex, /usr/bin/pod2man
BuildRequires: gmp-devel >= 4.1.2-8, mpfr-devel >= 2.2.1, libmpc-devel >= 0.8.1
# For VTA guality testing
BuildRequires: gdb
# Make sure pthread.h doesn't contain __thread tokens
# Make sure glibc supports stack protector
# Make sure glibc supports DT_GNU_HASH
BuildRequires: glibc-devel >= 2.4.90-13
BuildRequires: elfutils-devel >= 0.147
BuildRequires: elfutils-libelf-devel >= 0.147
# Need .eh_frame ld optimizations
# Need proper visibility support
# Need -pie support
# Need --as-needed/--no-as-needed support
# On ppc64, need omit dot symbols support and --non-overlapping-opd
# Need binutils that owns /usr/bin/c++filt
# Need binutils that support .weakref
# Need binutils that supports --hash-style=gnu
# Need binutils that support mffgpr/mftgpr
# Need binutils that support --build-id
# Need binutils that support %gnu_unique_object
# Need binutils that support .cfi_sections
# Need binutils that support --no-add-needed
# Need binutils that support -plugin
Requires: binutils >= 2.24
# Make sure gdb will understand DW_FORM_strp
Conflicts: gdb < 5.1-2
Requires: glibc-devel >= 2.2.90-12
Requires: libgcc >= %{version}-%{release}
Requires: libgomp >= %{version}-%{release}
AutoReq: true
Autoprov: false
Obsoletes: compat-egcs
Obsoletes: compat-gcc
Obsoletes: compat-gcc-objc
Obsoletes: compat-egcs-objc
Obsoletes: compat-gcc-g77
Obsoletes: compat-egcs-g77
Obsoletes: compat-gcc-java
Obsoletes: compat-libgcj
Obsoletes: compat-libgcj-devel
Obsoletes: compat-gcc-32
Obsoletes: compat-gcc-34
Obsoletes: compat-gcc-44
Obsoletes: gcc%{gcc_compat_version}

Patch0: gcc5-hack.patch
Patch1: gcc5-java-nomulti.patch
Patch2: gcc5-ppc32-retaddr.patch
Patch3: gcc5-rh330771.patch
Patch4: gcc5-i386-libgomp.patch
Patch5: gcc5-sparc-config-detection.patch
Patch6: gcc5-libgomp-omp_h-multilib.patch
Patch7: gcc5-libtool-no-rpath.patch
Patch8: gcc5-isl-dl.patch
Patch10: gcc5-libstdc++-docs.patch
Patch11: gcc5-no-add-needed.patch
Patch12: gcc5-libgo-p224.patch
Patch13: gcc5-aarch64-async-unw-tables.patch
Patch14: gcc5-libsanitize-aarch64-va42.patch
Patch15: gcc5-rh1279639.patch

# On ARM EABI systems, we do want -gnueabi to be part of the
# target triple.
%global _gnu %{nil}
%global gcc_target_platform %{_target_platform}

%description
The gcc package contains the GNU Compiler Collection version 5.
You'll need this package in order to compile C code.

%package c++
Summary: C++ support for GCC
Group: Development/Languages
Requires: compat-gcc-%{gcc_compat_version} = %{version}-%{release}
Requires: libstdc++ >= %{version}-%{release}
BuildRequires: libstdc++
Autoreq: true
AutoProv: false
Obsoletes: compat-egcs-c++
Obsoletes: compat-gcc-c++
Obsoletes: compat-libstdc++
Obsoletes: compat-libstdc++-devel
Obsoletes: compat-gcc-32-c++
Obsoletes: compat-gcc-34-c++
Obsoletes: compat-gcc-44-c++
Obsoletes: gcc%{gcc_compat_version}-c++

%description c++
This package adds C++ support to the GNU Compiler Collection.
It includes support for most of the current C++ specification,
including templates and exception handling.

%package gfortran
Summary: Fortran support
Group: Development/Languages
Requires: compat-gcc-%{gcc_compat_version} = %{version}-%{release}
Requires: libgfortran >= %{version}-%{release}
BuildRequires: gmp-devel >= 4.1.2-8, mpfr-devel >= 2.2.1
BuildRequires: libgfortran
Autoreq: true
Autoprov: false
Obsoletes: gcc3-g77
Obsoletes: gcc-g77
Obsoletes: compat-gcc-32-g77
Obsoletes: compat-gcc-34-g77
Obsoletes: compat-gcc-44-gfortran
Obsoletes: gcc%{gcc_compat_version}-gfortran

%description gfortran
The gcc-gfortran package provides support for compiling Fortran
programs with the GNU Compiler Collection.

%prep
%setup -q -n gcc-%{version}-%{DATE}
%patch0 -p0 -b .hack~
%patch1 -p0 -b .java-nomulti~
%patch2 -p0 -b .ppc32-retaddr~
%patch3 -p0 -b .rh330771~
%patch4 -p0 -b .i386-libgomp~
%patch5 -p0 -b .sparc-config-detection~
%patch6 -p0 -b .libgomp-omp_h-multilib~
%patch7 -p0 -b .libtool-no-rpath~
%patch11 -p0 -b .no-add-needed~
%patch12 -p0 -b .libgo-p224~
rm -f libgo/go/crypto/elliptic/p224{,_test}.go
%patch13 -p0 -b .aarch64-async-unw-tables~
%patch14 -p0 -b .libsanitize-aarch64-va42~
%patch15 -p0 -b .rh1279639~
sed -i -e 's/ -Wl,-z,nodlopen//g' gcc/ada/gcc-interface/Makefile.in

echo 'Red Hat %{version}-%{gcc_release}' > gcc/DEV-PHASE

cp -a libstdc++-v3/config/cpu/i{4,3}86/atomicity.h

./contrib/gcc_update --touch

LC_ALL=C sed -i -e 's/\xa0/ /' gcc/doc/options.texi

sed -i -e 's/Common Driver Var(flag_report_bug)/& Init(1)/' gcc/common.opt

%build

# Undo the broken autoconf change in recent Fedora versions
export CONFIG_SITE=NONE

rm -fr obj-%{gcc_target_platform}
mkdir obj-%{gcc_target_platform}
cd obj-%{gcc_target_platform}

CC=gcc
CXX=g++
OPT_FLAGS=`echo %{optflags}|sed -e 's/\(-Wp,\)\?-D_FORTIFY_SOURCE=[12]//g'`
OPT_FLAGS=`echo $OPT_FLAGS|sed -e 's/-m64//g;s/-m32//g;s/-m31//g'`
OPT_FLAGS=`echo $OPT_FLAGS|sed -e 's/-mfpmath=sse/-mfpmath=sse -msse2/g'`
OPT_FLAGS=`echo $OPT_FLAGS|sed -e 's/ -pipe / /g'`
%ifarch %{ix86}
OPT_FLAGS=`echo $OPT_FLAGS|sed -e 's/-march=i.86//g'`
%endif
OPT_FLAGS=`echo "$OPT_FLAGS" | sed -e 's/[[:blank:]]\+/ /g'`
case "$OPT_FLAGS" in
  *-fasynchronous-unwind-tables*)
    sed -i -e 's/-fno-exceptions /-fno-exceptions -fno-asynchronous-unwind-tables /' \
      ../libgcc/Makefile.in
    ;;
esac
CC="$CC" CFLAGS="$OPT_FLAGS" CXXFLAGS="`echo $OPT_FLAGS | sed 's/ -Wall / /g'`" XCFLAGS="$OPT_FLAGS" TCFLAGS="$OPT_FLAGS" \
CONFIGURE_OPTS="\
	--prefix=%{_prefix} --mandir=%{_mandir} --infodir=%{_infodir} \
	--with-bugurl=http://bugzilla.redhat.com/bugzilla \
	--enable-shared --enable-threads=posix --enable-checking=release \
    --disable-multilib \
	--with-system-zlib --enable-__cxa_atexit --disable-libunwind-exceptions \
	--enable-gnu-unique-object --enable-linker-build-id --with-linker-hash-style=gnu \
	--enable-shared --enable-threads=posix --enable-checking=release \
	--enable-plugin --enable-initfini-array \
	--disable-libgcj \
	--without-cloog --without-ppl \
	--with-tune=generic \
%ifarch %{ix86}
	--with-arch=i686 \
%endif
%ifarch x86_64
	--with-arch_32=i686 \
%endif
	--build=%{gcc_target_platform}\
    "

CC="$CC" CXX="$CXX" CFLAGS="$OPT_FLAGS" \

	CXXFLAGS="`echo " $OPT_FLAGS " | sed 's/ -Wall / /g;s/ -fexceptions / /g' \
		  | sed 's/ -Werror=format-security / -Wformat -Werror=format-security /'`" \
	XCFLAGS="$OPT_FLAGS" TCFLAGS="$OPT_FLAGS" \
	../configure --enable-bootstrap \
	--enable-languages=c,c++,fortran \
	$CONFIGURE_OPTS

#GCJFLAGS="$OPT_FLAGS" make %{?_smp_mflags} BOOT_CFLAGS="$OPT_FLAGS" bootstrap
GCJFLAGS="$OPT_FLAGS" make %{?_smp_mflags} BOOT_CFLAGS="$OPT_FLAGS" profiledbootstrap

CC="`%{gcc_target_platform}/libstdc++-v3/scripts/testsuite_flags --build-cc`"
CXX="`%{gcc_target_platform}/libstdc++-v3/scripts/testsuite_flags --build-cxx` `%{gcc_target_platform}/libstdc++-v3/scripts/testsuite_flags --build-includes`"

# Make generated man pages even if Pod::Man is not new enough
perl -pi -e 's/head3/head2/' ../contrib/texi2pod.pl
for i in ../gcc/doc/*.texi; do
  cp -a $i $i.orig; sed 's/ftable/table/' $i.orig > $i
done
make -C gcc generated-manpages
for i in ../gcc/doc/*.texi; do mv -f $i.orig $i; done

# Copy various doc files here and there
cd ..
mkdir -p rpm.doc/gfortran
mkdir -p rpm.doc/changelogs/{gcc/cp,libstdc++-v3,libgomp}

for i in {gcc,gcc/cp,libstdc++-v3,libgomp}/ChangeLog*; do
	cp -p $i rpm.doc/changelogs/$i
done

(cd gcc/fortran; for i in ChangeLog*; do
	cp -p $i ../../rpm.doc/gfortran/$i
done)
(cd libgfortran; for i in ChangeLog*; do
	cp -p $i ../rpm.doc/gfortran/$i.libgfortran
done)

rm -f rpm.doc/changelogs/gcc/ChangeLog.[1-9]
find rpm.doc -name \*ChangeLog\* | xargs bzip2 -9

cd -

# Fix up libstdc++.so's
d_first=yes
for d in `pwd`/%{gcc_target_platform}/libstdc++-v3 `pwd`/%{gcc_target_platform}/*/libstdc++-v3; do
  test -d $d || continue
  pushd $d/src
    sh %{SOURCE1} .libs/libstdc++.so .libs/ll.so libstdc++-symbols.ver
    rm .libs/libstdc++.so; cp .libs/ll.so .libs/libstdc++.so
    if [ x"$d_first" = xyes ]; then
      rm .libs/libstdc++.so.6
      libstdcxx_so=`basename %{_prefix}/%{_lib}/libstdc++.so.6.0.*`
      cp -a %{_prefix}/%{_lib}/$libstdcxx_so .libs/
      cd .libs; ln -sf $libstdcxx_so libstdc++.so.6; cd -
      d_first=no
    fi
  popd
done
# Fix up libgomp.so's
d_first=yes
for d in `pwd`/%{gcc_target_platform}/libgomp `pwd`/%{gcc_target_platform}/*/libgomp; do
  test -d $d || continue
  mapf=`pwd`/../libgomp/libgomp.map
  pushd $d
    sh %{SOURCE1} .libs/libgomp.so .libs/ll.so $mapf
    rm .libs/libgomp.so; cp .libs/ll.so .libs/libgomp.so
    if [ x"$d_first" = xyes ]; then
      rm .libs/libgomp.so.1
      libgomp_so=`basename %{_prefix}/%{_lib}/libgomp.so.1.0.*`
      cp -a %{_prefix}/%{_lib}/$libgomp_so .libs/
      cd .libs; ln -sf $libgomp_so libgomp.so.1; cd -
      d_first=no
    fi
  popd
done
# Fix up libgfortran.so's
d_first=yes
for d in `pwd`/%{gcc_target_platform}/libgfortran `pwd`/%{gcc_target_platform}/*/libgfortran; do
  test -d $d || continue
  mapf=`pwd`/../libgfortran/gfortran.map
  pushd $d
    sh %{SOURCE1} .libs/libgfortran.so .libs/ll.so $mapf
    rm .libs/libgfortran.so; cp .libs/ll.so .libs/libgfortran.so
    if [ x"$d_first" = xyes ]; then
      rm .libs/libgfortran.so.3
      libgfortran_so=`basename %{_prefix}/%{_lib}/libgfortran.so.3.0.*`
      cp -a %{_prefix}/%{_lib}/$libgfortran_so .libs/
      cd .libs; ln -sf $libgfortran_so libgfortran.so.3; cd -
      d_first=no
    fi
  popd
done
# Fix up libgcc_s.so's
d_first=yes
for d in `pwd`/%{gcc_target_platform}/libgcc `pwd`/%{gcc_target_platform}/*/libgcc/*/; do
  test -d $d || continue
  pushd $d
    mapf=libgcc.map
    if [ ! -f $mapf ]; then mapf=../libgcc.map; fi
    sh %{SOURCE1} libgcc_s.so ll.so $mapf
    rm libgcc_s.so; cp ll.so libgcc_s.so
    if [ x"$d_first" = xyes ]; then
      rm libgcc_s.so.1
      libgcc_s_so=`basename %{_prefix}/%{_lib}/libgcc_s-*.so.1`
      cp -a %{_prefix}/%{_lib}/$libgcc_s_so .
      ln -sf $libgcc_s_so libgcc_s.so.1
      d_first=no
    fi
  popd
done

%install
rm -fr %{buildroot}

cd obj-%{gcc_target_platform}

TARGET_PLATFORM=%{gcc_target_platform}

# There are some MP bugs in libstdc++ Makefiles
make -C %{gcc_target_platform}/libstdc++-v3

make prefix=%{buildroot}%{_prefix} mandir=%{buildroot}%{_mandir} \
  infodir=%{buildroot}%{_infodir} install

FULLPATH=%{buildroot}%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}
FULLEPATH=%{buildroot}%{_prefix}/libexec/gcc/%{gcc_target_platform}/%{gcc_version}

# fix some things
gzip -9 %{buildroot}%{_infodir}/*.info*

cxxconfig="`find %{gcc_target_platform}/libstdc++-v3/include -name c++config.h`"
for i in `find %{gcc_target_platform}/[36]*/libstdc++-v3/include -name c++config.h 2>/dev/null`; do
  if ! diff -up $cxxconfig $i; then
    cat > %{buildroot}%{_prefix}/include/c++/%{gcc_version}/%{gcc_target_platform}/bits/c++config.h <<EOF
#ifndef _CPP_CPPCONFIG_WRAPPER
#define _CPP_CPPCONFIG_WRAPPER 1
#include <bits/wordsize.h>
#if __WORDSIZE == 32
`cat $(find %{gcc_target_platform}/32/libstdc++-v3/include -name c++config.h)`
#else
`cat $(find %{gcc_target_platform}/libstdc++-v3/include -name c++config.h)`
#endif
#endif
EOF
    break
  fi
done

for f in `find %{buildroot}%{_prefix}/include/c++/%{gcc_version}/%{gcc_target_platform}/ -name c++config.h`; do
  for i in 1 2 4 8; do
    sed -i -e 's/#define _GLIBCXX_ATOMIC_BUILTINS_'$i' 1/#ifdef __GCC_HAVE_SYNC_COMPARE_AND_SWAP_'$i'\
&\
#endif/' $f
  done
done

# Nuke bits/*.h.gch dirs
# 1) there is no bits/*.h header installed, so when gch file can't be
#    used, compilation fails
# 2) sometimes it is hard to match the exact options used for building
#    libstdc++-v3 or they aren't desirable
# 3) there are multilib issues, conflicts etc. with this
# 4) it is huge
# People can always precompile on their own whatever they want, but
# shipping this for everybody is unnecessary.
rm -rf %{buildroot}%{_prefix}/include/c++/%{gcc_version}/%{gcc_target_platform}/bits/*.h.gch

if [ -n "$FULLLPATH" ]; then
  mkdir -p $FULLLPATH
else
  FULLLPATH=$FULLPATH
fi

find %{buildroot} -name \*.la | xargs rm -f

mv -f %{buildroot}%{_prefix}/%{_lib}/libgomp.spec $FULLPATH/

OBJDIR=`pwd`/%{gcc_target_platform}
pushd $FULLPATH
cp -a $OBJDIR/libstdc++-v3/src/.libs/libstdc++.so .
cp -a $OBJDIR/libgfortran/.libs/libgfortran.so .
cp -a $OBJDIR/libgcc/libgcc_s.so .
cp -a $OBJDIR/libgomp/.libs/libgomp.so .
mv -f %{buildroot}%{_prefix}/%{_lib}/libstdc++.*a $FULLPATH/
mv -f %{buildroot}%{_prefix}/%{_lib}/libsupc++.*a $FULLPATH/
mv -f %{buildroot}%{_prefix}/%{_lib}/libgfortran.*a $FULLPATH/
mv -f %{buildroot}%{_prefix}/%{_lib}/libgomp.*a $FULLPATH/

strip -g `find . \( -name libgfortran.a -o -name libgomp.a \
		    -o -name libgcc.a -o -name libgcov.a \
		    -o -name libstdc++.a -o -name libsupc++.a \
		    -o -name libgcc_eh.a \) -a -type f`
chmod 755 %{buildroot}%{_prefix}/%{_lib}/libgfortran.so.3.*
chmod 755 %{buildroot}%{_prefix}/%{_lib}/libgomp.so.1.*

mv $FULLPATH/include-fixed/syslimits.h $FULLPATH/include/syslimits.h
mv $FULLPATH/include-fixed/limits.h $FULLPATH/include/limits.h
for h in `find $FULLPATH/include -name \*.h`; do
  if grep -q 'It has been auto-edited by fixincludes from' $h; then
    rh=`grep -A2 'It has been auto-edited by fixincludes from' $h | tail -1 | sed 's|^.*"\(.*\)".*$|\1|'`
    diff -up $rh $h || :
    rm -f $h
  fi
done

cd ..

for i in %{buildroot}%{_prefix}/bin/{*gcc,*++,gcov,gfortran}; do
  mv -f $i ${i}%{gcc_compat_version}
done
for i in %{buildroot}%{_mandir}/man1/{gcc,g++,gcov,gfortran}; do
  mv -f $i.1 ${i}%{gcc_compat_version}.1
done
for i in %{buildroot}%{_infodir}/{gcc,gfortran}; do
  mv -f $i.info.gz ${i}%{gcc_compat_version}.info.gz
done

# Remove binaries we will not be including, so that they don't end up in
# gcc-debuginfo
rm -f %{buildroot}%{_prefix}/%{_lib}/{libffi*,libiberty.a}
rm -f $FULLEPATH/install-tools/{mkheaders,fixincl}
rm -f %{buildroot}%{_prefix}/lib/{32,64}/libiberty.a
rm -f %{buildroot}%{_prefix}/%{_lib}/libssp*
rm -f %{buildroot}%{_prefix}/bin/%{gcc_target_platform}-{gcc*,c++*,g++*gfortran*}
rm -f %{buildroot}%{_prefix}/bin/cpp

rm -f %{buildroot}%{_prefix}/%{_lib}/lib*.so*
rm -f %{buildroot}%{_prefix}/%{_lib}/lib*.a
# Remove libraries for the other arch on multilib arches
rm -f %{buildroot}%{_prefix}/lib/lib*.so*
rm -f %{buildroot}%{_prefix}/lib/lib*.a

%check
cd obj-%{gcc_target_platform}

# run the tests.
make %{?_smp_mflags} -k check ALT_CC_UNDER_TEST=gcc ALT_CXX_UNDER_TEST=g++ \
     RUNTESTFLAGS="--target_board=unix/'{,-fstack-protector-strong}'" || :
echo ====================TESTING=========================
( LC_ALL=C ../contrib/test_summary || : ) 2>&1 | sed -n '/^cat.*EOF/,/^EOF/{/^cat.*EOF/d;/^EOF/d;/^LAST_UPDATED:/d;p;}'
echo ====================TESTING END=====================
mkdir testlogs-%{_target_platform}-%{version}-%{release}
for i in `find . -name \*.log | grep -F testsuite/ | grep -v 'config.log\|acats.*/tests/'`; do
  ln $i testlogs-%{_target_platform}-%{version}-%{release}/ || :
done
tar cf - testlogs-%{_target_platform}-%{version}-%{release} | bzip2 -9c \
  | uuencode testlogs-%{_target_platform}.tar.bz2 || :
rm -rf testlogs-%{_target_platform}-%{version}-%{release}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_prefix}/bin/gcc%{gcc_compat_version}
%{_prefix}/bin/gcov%{gcc_compat_version}
%{_mandir}/man1/gcc%{gcc_compat_version}.1*
%{_mandir}/man1/gcov%{gcc_compat_version}.1*
%{_infodir}/gcc%{gcc_compat_version}*
%dir %{_prefix}/lib/gcc
%dir %{_prefix}/lib/gcc/%{gcc_target_platform}
%dir %{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}
%dir %{_prefix}/libexec/gcc
%dir %{_prefix}/libexec/gcc/%{gcc_target_platform}
%dir %{_prefix}/libexec/gcc/%{gcc_target_platform}/%{gcc_version}
%{_prefix}/libexec/gcc/%{gcc_target_platform}/%{gcc_version}/cc1
%dir %{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include
%{_prefix}/libexec/gcc/%{gcc_target_platform}/%{gcc_version}/lto1
%{_prefix}/libexec/gcc/%{gcc_target_platform}/%{gcc_version}/lto-wrapper
%{_prefix}/libexec/gcc/%{gcc_target_platform}/%{gcc_version}/liblto_plugin.so*
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/stddef.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/stdarg.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/stdfix.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/varargs.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/float.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/limits.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/stdbool.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/iso646.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/syslimits.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/unwind.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/omp.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/openacc.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/stdint.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/stdint-gcc.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/stdalign.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/stdnoreturn.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/stdatomic.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/mmintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/xmmintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/emmintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/pmmintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/tmmintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/ammintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/smmintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/nmmintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/bmmintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/wmmintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/immintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/avxintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/x86intrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/fma4intrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/xopintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/lwpintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/popcntintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/bmiintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/tbmintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/ia32intrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/avx2intrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/bmi2intrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/f16cintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/fmaintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/lzcntintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/rtmintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/xtestintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/adxintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/prfchwintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/rdseedintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/fxsrintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/xsaveintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/xsaveoptintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/avx512cdintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/avx512erintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/avx512fintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/avx512pfintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/shaintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/mm_malloc.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/mm3dnow.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/cpuid.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/cross-stdarg.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/avx512bwintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/avx512dqintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/avx512ifmaintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/avx512ifmavlintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/avx512vbmiintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/avx512vbmivlintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/avx512vlbwintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/avx512vldqintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/avx512vlintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/clflushoptintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/clwbintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/pcommitintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/mwaitxintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/xsavecintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/xsavesintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/sanitizer
%{_prefix}/libexec/gcc/%{gcc_target_platform}/%{gcc_version}/collect2
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/crt*.o
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/libgcc.a
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/libgcov.a
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/libgcc_eh.a
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/libgcc_s.so
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/libgomp.spec
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/libgomp.a
%doc gcc/README* rpm.doc/changelogs/gcc/ChangeLog* gcc/COPYING*

%files c++
%defattr(-,root,root,-)
%{_prefix}/bin/g++%{gcc_compat_version}
%{_mandir}/man1/g++%{gcc_compat_version}.1*
%dir %{_prefix}/include/c++
%dir %{_prefix}/include/c++/%{gcc_version}
%{_prefix}/include/c++/%{gcc_version}/[^gjos]*
%{_prefix}/include/c++/%{gcc_version}/os*
%{_prefix}/include/c++/%{gcc_version}/s[^u]*
%dir %{_prefix}/lib/gcc
%dir %{_prefix}/lib/gcc/%{gcc_target_platform}
%dir %{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}
%dir %{_prefix}/libexec/gcc
%dir %{_prefix}/libexec/gcc/%{gcc_target_platform}
%dir %{_prefix}/libexec/gcc/%{gcc_target_platform}/%{gcc_version}
%{_prefix}/libexec/gcc/%{gcc_target_platform}/%{gcc_version}/cc1plus
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/libstdc++.so
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/libstdc++.a
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/libsupc++.a
%doc rpm.doc/changelogs/gcc/cp/ChangeLog*
%doc rpm.doc/changelogs/libstdc++-v3/ChangeLog* libstdc++-v3/README*

%files gfortran
%defattr(-,root,root,-)
%{_prefix}/bin/gfortran%{gcc_compat_version}
%{_mandir}/man1/gfortran%{gcc_compat_version}.1*
%{_infodir}/gfortran%{gcc_compat_version}*
%dir %{_prefix}/lib/gcc
%dir %{_prefix}/lib/gcc/%{gcc_target_platform}
%dir %{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}
%dir %{_prefix}/libexec/gcc
%dir %{_prefix}/libexec/gcc/%{gcc_target_platform}
%dir %{_prefix}/libexec/gcc/%{gcc_target_platform}/%{gcc_version}
%dir %{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/finclude
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/finclude/omp_lib.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/finclude/omp_lib.f90
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/finclude/omp_lib.mod
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/finclude/omp_lib_kinds.mod
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/finclude/openacc.f90
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/finclude/openacc.mod
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/finclude/openacc_kinds.mod
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/finclude/openacc_lib.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/finclude/ieee_arithmetic.mod
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/finclude/ieee_exceptions.mod
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/finclude/ieee_features.mod
%{_prefix}/libexec/gcc/%{gcc_target_platform}/%{gcc_version}/f951
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/libgfortranbegin.a
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/libgfortran.a
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/libgfortran.so
%doc rpm.doc/gfortran/*

%changelog
* Tue Dec 20 2016 Byoungchan Lee <byoungchan.lee@gmx.com> 5.3.1-6
- new compat package (Fedora 23's GCC 5 + EL7 compat-gcc-44)


