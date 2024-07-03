Name: pantum
Version: 1.1.99
Release: alt4
License: see /usr/share/doc/pantum/copyright
BuildArch: x86_64
Group: Other
Summary: CUPS and SANE drivers for Pantum series printer and scanner.
Source: %name-%version.tar.gz


AutoReqProv: no

%description
Nothing.

%prep
%setup

%build

%install

mkdir -p %buildroot/etc
install -c -m0644 etc/pantumwrap %buildroot/etc/
mkdir -p %buildroot/etc/sane.d
mkdir -p %buildroot/etc/sane.d/dll.d
install -c -m0644 etc/sane.d/dll.d/pantum6500 %buildroot/etc/sane.d/dll.d/
install -c -m0644 etc/sane.d/dll.d/pantum_mfp %buildroot/etc/sane.d/dll.d/
install -c -m0644 etc/sane.d/pantum6500.conf %buildroot/etc/sane.d/
install -c -m0644 etc/sane.d/pantum_mfp.conf %buildroot/etc/sane.d/
mkdir -p %buildroot/etc/udev
mkdir -p %buildroot/etc/udev/rules.d
install -c -m0644 etc/udev/rules.d/60-pantum_mfp.rules %buildroot/etc/udev/rules.d/
mkdir -p %buildroot/opt
mkdir -p %buildroot/opt/pantum
mkdir -p %buildroot/opt/pantum/bin
install -c -m0755 opt/pantum/bin/ptqpdf %buildroot/opt/pantum/bin/
mkdir -p %buildroot/opt/pantum/ippfilter
install -c -m0644 opt/pantum/ippfilter/55-ippusbxd.rules %buildroot/opt/pantum/ippfilter/
install -c -m0644 opt/pantum/ippfilter/71-ipp-usb.rules %buildroot/opt/pantum/ippfilter/
install -c -m0644 opt/pantum/ippfilter/ipp-usb %buildroot/opt/pantum/ippfilter/
install -c -m0644 opt/pantum/ippfilter/pt-ipp-usb.service %buildroot/opt/pantum/ippfilter/
mkdir -p %buildroot/usr
mkdir -p %buildroot/usr/lib
mkdir -p %buildroot/usr/lib/cups
mkdir -p %buildroot/usr/lib/cups/filter
install -c -m0755 usr/lib/cups/filter/pt1700Filter %buildroot/usr/lib/cups/filter/
install -c -m0755 usr/lib/cups/filter/pt2013upgradeFilter %buildroot/usr/lib/cups/filter/
install -c -m0755 usr/lib/cups/filter/pt2500Filter %buildroot/usr/lib/cups/filter/
install -c -m0755 usr/lib/cups/filter/pt2510Filter %buildroot/usr/lib/cups/filter/
install -c -m0755 usr/lib/cups/filter/pt2550Filter %buildroot/usr/lib/cups/filter/
install -c -m0755 usr/lib/cups/filter/pt2800Filter %buildroot/usr/lib/cups/filter/
install -c -m0755 usr/lib/cups/filter/pt3100Filter %buildroot/usr/lib/cups/filter/
install -c -m0755 usr/lib/cups/filter/ptm5300Filter %buildroot/usr/lib/cups/filter/
install -c -m0755 usr/lib/cups/filter/ptm6500Filter %buildroot/usr/lib/cups/filter/
install -c -m0755 usr/lib/cups/filter/ptm6700Filter %buildroot/usr/lib/cups/filter/
install -c -m0755 usr/lib/cups/filter/ptps %buildroot/usr/lib/cups/filter/
install -c -m0755 usr/lib/cups/filter/rastertoPantum %buildroot/usr/lib/cups/filter/
install -c -m0755 usr/lib/cups/filter/rastertoPantumPCL %buildroot/usr/lib/cups/filter/
mkdir -p %buildroot/usr/lib64
mkdir -p %buildroot/usr/lib64/sane
install -c -m0644 usr/lib64/sane/libsane-pantum6500.so %buildroot/usr/lib64/sane/
install -c -m0644 usr/lib64/sane/libsane-pantum6500.so.1 %buildroot/usr/lib64/sane/
install -c -m0644 usr/lib64/sane/libsane-pantum6500.so.1.0.24 %buildroot/usr/lib64/sane/
install -c -m0644 usr/lib64/sane/libsane-pantum_mfp.so %buildroot/usr/lib64/sane/
install -c -m0644 usr/lib64/sane/libsane-pantum_mfp.so.1 %buildroot/usr/lib64/sane/
install -c -m0644 usr/lib64/sane/libsane-pantum_mfp.so.1.0.24 %buildroot/usr/lib64/sane/
mkdir -p %buildroot/usr/share
mkdir -p %buildroot/usr/share/cups
mkdir -p %buildroot/usr/share/cups/model
mkdir -p %buildroot/usr/share/cups/model/Pantum
install -c -m0644 usr/share/cups/model/Pantum/Pantum_BM2100ANW_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_BM2100A_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_BM2100NW_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_BM2100_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_BM2200AN_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_BM2200ANW_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_BM2200A_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_BM2200AW_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_BM2200FN_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_BM2200FNW_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_BM2200F_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_BM2200FW_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_BM2200N_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_BM2200NW_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_BM2200_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_BM2200W_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_BM4000ADN_Series_PS.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_BM4000ADW_Series_PS.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_BM4000FDN_Series_PS.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_BM4000FDW_Series_PS.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_BM4005ADN_Series_PS.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_BM4005FDN_Series_PS.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_BM4100FDN_Series_PS.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_BM4100FDW_Series_PS.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_BM5100ADN_Series_PS.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_BM5100ADW_Series_PS.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_BM5100FDN_Series_PS.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_BM5100FDW_Series_PS.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_BM5105ADN_Series_PS.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_BM5105FDN_Series_PS.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_BM5106ADN_Series_PS.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_BM5106ADW_Series_PS.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_BM5106FDN_Series_PS.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_BM5106FDW_Series_PS.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_BP2100N_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_BP2100NW_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_BP2100_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_BP2100W_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_BP2200N_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_BP2200NW_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_BP2200_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_BP2200W_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_BP4000DN_Series_PS.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_BP4000DW_Series_PS.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_BP4005DN_Series_PS.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_BP5100DN_Series_PS.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_BP5100DW_Series_PS.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_BP5101DN_Series_PS.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_BP5105DN_Series_PS.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_BP5106DN_Series_PS.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_BP5106DW_Series_PS.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_BP5126DN_Series_PS.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_CM1100ADN_Series_PS.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_CM1100ADW_Series_PS.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_CM1100DN_Series_PS.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_CM1100DW_Series_PS.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_CM1100FDW_Series_PS_.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_CP1100DN_Series_PS.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_CP1100DW_Series_PS.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_CP1100_Series_PS.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_L2300DW_Series_PS.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_L2350DW_Series_PS.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_L2710FDW_Series_PS.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_M118DW_Series_PS.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_M15DW_Series_PS.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_M29DW_Series_PS.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_M5100_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_M5200_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_M5300_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_M6503NW_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_M6503_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_M6535NW_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_M6700DN_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_M6700D_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_M6700DW_Plus_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_M6700DW_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_M6760D_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_M6760DW_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_M6800FDW_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_M6860FDN_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_M6860FDW_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_M7100DN_Series_PS.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_M7100D_Series_PS.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_M7100DW_Series_PS.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_M7108DW_Series_PS.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_M7160DW_Series_PS.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_M7170DW_Series_PS.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_M7200FDN_Series_PS.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_M7200FD_Series_PS.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_M7200FDW_Series_PS.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_M7300FDN_Series_PS.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_M7300FDW_Series_PS.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_P1000_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_P2000_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_P2210_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_P2210W_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_P2300_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_P2300W_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_P2503_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_P2503W_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_P2510_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_P2510W_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_P2517_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_P2535NW_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_P2550N_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_P2550_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_P2600N_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_P2600NW_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_P2600_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_P2650N_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_P2650_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_P3000_Series_PCL.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_P3000_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_P3000_Series_PS.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_P3007D_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_P3007DW_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_P3010D_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_P3010DW_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_P3020D_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_P3020DWS_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_P3060D_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_P3060DW_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_P3100_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_P3300DN_Series_PS.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_P3300DW_Series_PS.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_P3300_Series_PS.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_P3307DN_Series_PS.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_P3308DW_Series_PS.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_P3320D_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_P3320DWS_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_P3500DN_Series_PS.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_P3500DNT_Series_PS.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_P3500D_Series_PS.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_P3500DW_Series_PS.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_P3508DN_Series_PS.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_M6200N_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_M6200NW_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_M6200_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_M6200W_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_M6500N_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_M6500NW_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_M6500_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_M6500W_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_M6518NW_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_M6550N_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_M6550NW_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_M6550_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_M6550W_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_M6568NW_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_M6600N_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_M6600NW_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_M6600_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_M6600W_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_M6602W_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_MS6000NW_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_MS6000_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_MS6550NW_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_MS6550_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_MS6600NW_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_MS6600_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_P2200NW_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_P2200_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_P2200W_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_P2500N_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_P2500NW_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_P2500_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_P2500W_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_P2518NW_Series.ppd %buildroot/usr/share/cups/model/Pantum/
install -c -m0644 usr/share/cups/model/Pantum/Pantum_S2000_Series.ppd %buildroot/usr/share/cups/model/Pantum/
mkdir -p %buildroot/usr/share/doc
mkdir -p %buildroot/usr/share/doc/pantum
install -c -m0644 usr/share/doc/pantum/changelog.gz %buildroot/usr/share/doc/pantum/
install -c -m0644 usr/share/doc/pantum/copyright %buildroot/usr/share/doc/pantum/

%set_verify_elf_method no

%files
/opt/*
%_sysconfdir/*
%_prefix/*


%changelog
* Thu Jul 02 2024 Marat Faizov <faizov@cg.ru> 1.1.99-alt4
- Add working .ppd for printers 6500.

* Thu Jun 06 2024 Marat Faizov <faizov@cg.ru> 1.1.99-alt3
- Add additional *ModelName to all .ppd for different printers.

* Mon Apr 21 2024 Marat Faizov <faizov@cg.ru> 1.1.99-alt2
- repack for alt p8.
