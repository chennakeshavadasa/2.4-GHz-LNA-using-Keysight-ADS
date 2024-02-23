# Simulated Result
- Here I have tried to simulate every 64 RF Transistor devices(GaAs) to find which has min NF and good Gain.
 
 ## **Device chosen for the design**
 - After many consideration I chose the device **pf_mwt_MWT_170_19931015**	which offers a **nFmin of 0.123 dB** and **Gain	of 15.933 dB** **at 2.4GHz**,	**nFmin of 0.202 dB**	and **Gain	of 13.565 dB at 4GHz.**
 - The datasheet of the device: https://www.digchip.com/datasheets/parts/datasheet/3934/MWT-170-pdf.php
   
 - **FEATURES**
   10 dB GAIN AT 12 GHz, EXCELLENT FOR FEEDBACK AMPLIFIER APPLICATIONS, 100 MHz TO 12 GHz, 0.3 MICRON REFRACTORY METAL/GOLD GATE, 630 MICRON GATE WIDTH, CHOICE OF CHIP AND THREE PACKAGE TYPES.

 - **DESCRIPTION**
The MwT-1 is a GaAs MESFET device whose nominal quarter-micron gate length and 630 micron gate width make it ideally suited to
applications requiring high-gain in the 100 MHz to 12 GHz frequency range. The straight geometry of the MwT-1 makes it equally
effective for either wideband (e.g. 2 to 6 GHz) or narrow-band applications. The chip is produced using MwT’s reliable metal system and
devices from each wafer are screened to insure reliability. All chips are passivated using MwT’s patented “Diamond-Like Carbon” process
for increased durability, Designers can use MwT’s unique BIN selection feature to choose devices from narrow Idss ranges, insuring
consistent circuit operation.

## Simulated devices result
 -  Below table is to simplify the noted result. 

| No  | Device name                | NFmin at 2.4GHz | Gain at 2.4GHz | NFmin at  4GHz | Gain at 4GHz |
|-----|----------------------------|-----------------|----------------|----------------|--------------|
|  1  | pf_hp_ATF13786_19931015    | 0.090 dB        | 11.614 dB      | 0.147 dB       | 10.395 dB    |
|  2  | pf_hp_ATF13136_19931014    | 0.205 dB        | 10.570 dB      | 0.336 dB       | 9.691 dB     |
|  3  | pf_hp_ATF13284_19931014    | 0.198 dB        | 7.506 dB       | 0.326 dB       | 7.233 dB     |
|  4  | pf_hp_ATF13786_19931015    | 0.090 dB        | 11.614 dB      | 0.147 dB       | 10.395 dB    |
|  5  | pf_hp_ATF21170_19931015    | 0.209 dB        | 14.109 dB      | 0.341 dB       | 11.665 dB    |
|  6  | pf_hp_ATF26884_19931015    | 0.370 dB        | 9.357 dB       | 0.607 dB       | 8.776 dB     |
|  7  | pf_mit_MGF0904A_19931015   | 1.573 dB        | 6.942 dB       | 3.236 dB       | 2.571 dB     |
|  8  | pf_mit_MGF0905A_19931019   | 2.771 dB        | -0.061 dB      | 3.362 dB       | -3.338 dB    |
|  9  | pf_mit_MGF0906A_19931019   | 0.973 dB        | 8.164 dB       | 1.595 dB       | 4.571 dB     |
|  10 | pf_mit_MGF1302_19921216    | 0.589 dB        | 12.031 dB      | 0.973 dB       | 11.655 dB    |
|  11 | pf_mit_MGF1303B_19921216   | 0.387 dB        | 11.583 dB      | 0.638 dB       | 11.235 dB    |
|  12 | pf_mit_MGF1304A_19921216   | 0.526 dB        | 5.006 dB       | 0.871 dB       | 5.016 dB     |
|  13 | pf_mit_MGF1305_19921216    | 0.285 dB        | 9.702 dB       | 0.470 dB       | 9.598 dB     |
|  14 | pf_mit_MGF1402_19921216    | 0.683 dB        | 12.990 dB      | 1.131 dB       | 12.222 dB    |
|  15 | pf_mit_MGF1403_19921216    | 0.383 dB        | 11.598 dB      | 0.630 dB       | 11.105 dB    |
|  16 | pf_mit_MGF1412_19931022    | 1.114 dB        | 14.151 dB      | 1.369 dB       | 13.127 dB    |
|  17 | pf_mit_MGF1423_19931015    | 0.630 dB        | 9.543 dB       | 1.025 dB       | 7.750 dB     |
|  18 | pf_mit_MGF1425_19921216    | 0.369 dB        | 11.679 dB      | 0.608 dB       | 11.337 dB    |
|  19 | pf_mit_MGF1801_19931015    | 0.361 dB        | 13.274 dB      | 0.593 dB       | 10.258 dB    |
|  20 | pf_mit_MGF1902B_19921216   | 0.604 dB        | 12.471 dB      | 0.998 dB       | 11.726 dB    |
|  21 | pf_mit_MGF1903B_19931018   | 0.509 dB        | 10.425 dB      | 0.838 dB       | 9.257 dB     |
|  22 | pf_mit_MGF2148_19931019    | 0.923 dB        | 7.694 dB       | 1.514 dB       | 3.857 dB     |
|  23 | pf_mit_MGF2407A_19931018   | 1.594 dB        | 10.884 dB      | 2.740 dB       | 7.147 dB     |
|  24 | pf_mit_MGF2415A_19931015   | 1.787 dB        | 10.907 dB      | 2.904 dB       | 5.879 dB     |
|  25 | pf_mit_MGF2430A_19931015   | 1.480 dB        | 9.756 dB       | 2.413 dB       | 5.108 dB     |
|  26 | pf_mwt_MWT_170_19931015    | 0.123 dB        | 15.933 dB      | 0.202 dB       | 13.565 dB    |
|  27 | pf_mwt_MWT_270_19931015    | 0.812 dB        | 14.129 dB      | 0.931 dB       | 12.344 dB    |
|  28 | pf_mwt_MWT_370HP_19931015  | 0.361 dB        | 11.010 dB      | 0.596 dB       | 9.761 dB     |
|  29 | pf_mwt_MWT_370HP_19931015  | 0.361 dB        | 10.940 dB      | 0.596 dB       | 9.761 dB     |
|  30 | pf_mwt_MWT_470LN_19931015  | 0.870 dB        | 9.019 dB       | 1.423 dB       | 7.476 dB     |
|  31 | pf_mwt_MWT_671HP_19931015  | 0.866 dB        | 12.890 dB      | 1.396 dB       | 9.086 dB     |
|  32 | pf_mwt_MWT_770HP_19931015  | 0.315 dB        | 10.165 dB      | 0.522 dB       | 9.470 dB     |
|  33 | pf_mwt_MWT_770LN_19931020  | 0.809 dB        | 11.982 dB      | 1.330 dB       | 10.992 dB    |
|  34 | pf_mwt_MWT_773HP_19931015  | 0.709 dB        | 10.784 dB      | 1.172 dB       | 9.609 dB     |
|  35 | pf_mwt_MWT_871HP_19931015  | 0.359 dB        | 12.472 dB      | 0.594 dB       | 8.715 dB     |
|  36 | pf_mwt_MWT_971_19931020    | 0.256 dB        | 14.463dB       | 0.424 dB       | 11.38.3 dB   |
|  37 | pf_mwt_MWT_1171HP_19931020 | 0.927 dB        | 9.323 dB       | 1.517 dB       | 4.947 dB     |
|  38 | pf_nec_2SK354A_19921216    | 0.865 dB        | 10.685 dB      | 1.417 dB       | 9.575 dB     |
|  39 | pf_nec_2SK406_199310220    | 0.614 dB        | 11.802 dB      | 1.013 dB       | 11.264 dB    |
|  40 | pf_nec_2SK407_19921216     | 0.649 dB        | 5.658 dB       | 1.066 dB       | 5.504 dB     |
|  41 | pf_nec_2SK571_19921216     | 0.495 dB        | 11.363 dB      | 0.812dB        | 10.165 dB    |
|  42 | pf_nec_2SK609_19921216     | 0.304 dB        | 10.889 dB      | 0.500 dB       | 10.473 dB    |
|  43 | pf_nec_NE67383_19921216    | 0.649 dB        | 5.658 dB       | 1.066 dB       | 5.504 dB     |
|  44 | pf_nec_NE71083_19931022    | 0.614 dB        | 11.802 dB      | 1.013 dB       | 11.264 dB    |
|  45 | pf_nec_NE71084_19921216    | 1.494 dB        | 10.889 dB      | 1.382 dB       | 10.473 dB    |
|  46 | pf_nec_NE71084_19921216    | 1.442 dB        | 11.363 dB      | 1.468 dB       | 10.265 dB    |
|  47 | pf_nec_NE72089A_19921216   | 0.865 dB        | 10.685 dB      | 1.417 dB       | 9.575 dB     |
|  48 | pf_nec_NE76038_19921216    | 0.341 dB        | 9.057 dB       | 0.562 dB       | 9.024 dB     |
|  49 | pf_nec_NE76084_19921216    | 0.247 dB        | 7.966 dB       | 0.411 dB       | 7.979 dB     |
|  50 | pf_nec_NE76184A_19921216   | 0.755 dB        | 13.161 dB      | 1.219 dB       | 11.865 dB    |
|  51 | pf_nec_NE900075_19931018   | 0.723 dB        | 8.272 dB       | 1.182 dB       | 5.937 dB     |
|  52 | pf_nec_NE900175_19931018   | 0.737 dB        | 11.002 dB      | 1.209 dB       | 7.746 dB     |
|  53 | pf_nec_NE900275_19931018   | 1.203 dB        | 12.563 dB      | 1.921 dB       | 9.370 dB     |
|  54 | pf_oki_KGF1305_19931020    | 2.092 dB        | 7.997 dB       | 3.072 dB       | 2.426 dB     |
|  55 | pf_sms_CFY19_18_19921216   | 0.967 dB        | 9.125 dB       | 1.555 dB       | 8.612 dB     |
|  56 | pf_sms_CFY25_17_19921216   | 0.240 dB        | 10.139 dB      | 0.395 dB       | 10.055 dB    |
|  57 | pf_sms_CFY30_19931018      | 1.744 dB        | 8.071 dB       | 1.665 dB       | 7.301 dB     |
|  58 | pf_sms_CFY35_20_19931018   | 0.574 dB        | 4.813 dB       | 0.944 dB       | 4.951 dB     |
|  59 | pf_sms_CFY35_23_19931018   | 0.454 dB        | 7.557 dB       | 0.742 dB       | 7.032 dB     |
|  60 | pf_tsb_S8834_19931018      | 0.985 dB        | 7.052 dB       | 1.623 dB       | 5.169 dB     |
|  61 | pf_tsb_S8835_19931018      | 1.2662 dB       | 1.136 dB       | 2.038 dB       | 8.854 dB     |
|  62 | pf_tsb_S8835B_19931018     | 1.306 dB        | 8.142 dB       | 2.123 dB       | 4.123 dB     |
|  63 | pf_tsb_S8836A_19931018     | 1.982 dB        | 5.336 dB       | 3.206 dB       | 0.553 dB     |
|  64 | pf_tsb_S8837A_19931021     | 1.416 dB        | 2.501 dB       | 2.309 dB       | -2.452 dB    |



