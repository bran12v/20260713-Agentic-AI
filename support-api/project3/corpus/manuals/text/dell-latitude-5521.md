# Dell Latitude 5521

| | |
|---|---|
| Regulatory model | P104F |
| Troubleshooting depth | **full** |
| Documents | 3 |

- **Latitude 5521 Service Manual** — June 2023 Rev. A03
  - Source: https://dl.dell.com/topicspdf/latitude-15-5521-laptop_owners-manual_en-us.pdf
  - Answers: Diagnostic LED codes, built-in self-test, SupportAssist, RTC reset, swollen battery handling, Wi-Fi power cycle, flea-power drain, OS recovery, BIOS setup and boot sequence, clearing passwords
- **Latitude 5521 Re-imaging guide for Windows 10** — no revision stated
  - Source: https://dl.dell.com/topicspdf/latitude-15-5521-laptop_reference-guide_en-us.pdf
  - Answers: Order of reinstallation, driver installation sequence, what to install after a clean Windows image
- **Latitude 5521 Setup and Specifications** — August 2021 Rev. A01
  - Source: https://dl.dell.com/topicspdf/latitude-15-5521-laptop_setup-guide_en-us.pdf (via the Internet Archive, snapshot 20221014185919)
  - Answers: Views of the machine, ports and slots, display options, memory limits, battery capacity, keyboard shortcuts, camera, power adapter

Extracted from the vendor document. Teardown chapters are omitted — they answer nothing a user asks. See `../SOURCES.md`.

## Drivers and downloads

_Latitude 5521 Service Manual, pages 102–102_

Drivers and downloads
This chapter details the supported operating systems along with instructions on how to install the drivers.
Topics:
• Downloading the drivers
Downloading the drivers
Steps
1. Turn on your computer.
2. Go to www.dell.com/support .
3. Enter the Service Tag of your computer, and then click Submit .
NOTE: If you do not have the Service Tag, use the auto-detect feature or manually browse for your computer model.
4. Click Drivers & downloads .
5. Click the Detect Drivers button.
6. Review and agree to the Terms and Conditions to use SupportAssist , then click Continue .
7. If necessary, your computer starts to download and install SupportAssist .
NOTE: Review on-screen instructions for browser-specific instructions.
8. Click View Drivers for My System .
9. Click Download and Install to download and install all driver updates detected for your computer.
10. Select a location to save the files.
11. If prompted, approve requests from User Account Control to make changes on the system.
12. The application installs all drivers and updates identified.
NOTE: Not all files can be installed automatically. Review the installation summary to identify if manual installation is 
necessary.
13. For manual download and installation, click Category .
14. From the drop-down list, select the preferred driver.
15. Click Download to download the driver for your computer.
16. After the download is complete, navigate to the folder where you saved the driver file.
17. Double-click the driver file icon and follow the instructions on the screen to install the driver.
3
102 Drivers and downloads

## System setup

_Latitude 5521 Service Manual, pages 103–117_

System setup
CAUTION: Unless you are an expert computer user, do not change the settings in the BIOS Setup program. 
Certain changes can make your computer work incorrectly.
NOTE: Before you change BIOS Setup program, it is recommended that you write down the BIOS Setup program screen 
information for future reference.
Use the BIOS Setup program for the following purposes:
● Get information about the hardware installed in your computer, such as the amount of RAM and the size of the hard drive.
● Change the system configuration information.
● Set or change a user-selectable option, such as the user password, type of hard drive installed, and enabling or disabling 
base devices.
Topics:
• BIOS overview
• Entering BIOS setup program
• Navigation keys
• One Time Boot menu
• Boot Sequence
• System setup options
• Updating the BIOS
• System and setup password
• Clearing BIOS (System Setup) and System passwords
BIOS overview
The BIOS manages data flow between the computer's operating system and attached devices such as hard disk, video adapter, 
keyboard, mouse, and printer.
Entering BIOS setup program
About this task
Turn on (or restart) your computer and press F2 immediately.
Navigation keys
NOTE: For most of the System Setup options, changes that you make are recorded but do not take effect until you restart 
the system.
Keys Navigation
Up arrow Moves to the previous field.
Down arrow Moves to the next field.
Enter Selects a value in the selected field (if applicable) or follow the link in the field.
Spacebar Expands or collapses a drop-down list, if applicable.
Tab Moves to the next focus area.
4
System setup 103
Keys Navigation
Esc Moves to the previous page until you view the main screen. Pressing Esc in the main screen displays a 
message that prompts you to save any unsaved changes and restarts the system.
One Time Boot menu
To enter One Time Boot menu , turn on your computer, and then press F12 immediately.
NOTE: It is recommended to shutdown the computer if it is on.
The one-time boot menu displays the devices that you can boot from including the diagnostic option. The boot menu options 
are:
● Removable Drive (if available)
● STXXXX Drive (if available)
NOTE: XXX denotes the SATA drive number.
● Optical Drive (if available)
● SATA Hard Drive (if available)
● Diagnostics
The boot sequence screen also displays the option to access the System Setup screen.
Boot Sequence
Boot sequence enables you to bypass the System Setup–defined boot device order and boot directly to a specific device (for 
example: optical drive or hard drive). During the Power-on Self-Test (POST), when the Dell logo appears, you can:
● Access System Setup by pressing F2 key
● Bring up the one-time boot menu by pressing F12 key.
The one-time boot menu displays the devices that you can boot from including the diagnostic option. The boot menu options 
are:
● Windows Boot Manager
● UEFI HTTPs Boot
● UEFI RST Micron 2300 NVMe 512 GB 20502C1A4567
● ONBOARD NIC (IPV4)
● ONBOARD NIC (IPV6)
The boot sequence screen also displays the option to access the System Setup screen.
System setup options
NOTE: Depending on your computer and its installed devices, the items listed in this section may or may not appear.
Table 4. System setup options—System information menu 
Overview
Latitude 5520
BIOS Version Displays the BIOS version number.
Service Tag Displays the Service Tag of the computer.
Asset Tag Displays the Asset Tag of the computer.
Manufacture Date Displays the manufacture date of the computer.
Ownership Date Displays the ownership date of the computer.
104 System setup
Table 4. System setup options—System information menu (continued)
Overview
Express Service Code Displays the express service code of the computer.
Ownership Tag Displays the Ownership Tag of the computer.
Signed Firmware Update Displays whether the Signed Firmware Update is enabled on your computer.
Battery Information
Primary Displays that battery is primary.
Battery Level Displays the battery level of the computer.
Battery State Displays the battery state of the computer.
Health Displays the battery health of the computer.
AC Adapter Displays whether the AC adapter is connected or not.
Battery Life Type Display the Battery Life type of the computer
Processor Information
Processor Type Displays the processor type.
Maximum Clock Speed Displays the maximum processor clock speed.
Minimum Clock Speed Displays the minimum processor clock speed.
Current Clock Speed Displays the current processor clock speed.
Core Count Displays the number of cores on the processor.
Processor ID Displays the processor identification code.
Processor L2 Cache Displays the processor L2 Cache size.
Processor L3 Cache Displays the processor L3 Cache size.
Microcode Version Displays the microcode version.
Intel Hyper-Threading Capable Displays whether the processor is Hyper-Threading (HT) capable.
64-Bit Technology Displays whether 64-bit technology is used.
Memory Information
Memory Installed Displays the total computer memory installed.
Memory Available Displays the total computer memory available.
Memory Speed Displays the memory speed.
Memory Channel Mode Displays single or dual channel mode.
Memory Technology Displays the technology used for the memory.
DIMM_SLOT 1 Displays the DIMM 1 memory size.
DIMM_SLOT 2 Displays the DIMM 2 memory size.
Devices Information
Panel Type Displays the Panel Type of the computer.
Video Controller Displays the video controller type of the computer.
Video Memory Displays the video memory information of the computer.
Wi-Fi Device Displays the wireless device information of the computer.
Native Resolution Displays the native resolution of the computer.
Video BIOS Version Displays the video BIOS version of the computer.
Audio Controller Displays the audio controller information of the computer.
Bluetooth Device Displays the Bluetooth device information of the computer.
System setup 105
Table 4. System setup options—System information menu (continued)
Overview
LOM MAC Address Displays the LAN On Motherboard (LOM) MAC address of the computer.
Pass Through MAC Address Displays the pass through MAC address of the computer.
Cellular Device Displays the M.2 PCIe SSD information of the computer.
dGPU Video Controller Displays the Discrete graphics card information on the computer.
Table 5. System setup options—Boot Configuration menu 
Boot Configuration
Boot Sequence
Boot mode Displays the boot mode.
Boot Sequence Displays the boot sequence.
Secure Digital (SD) Card Boot Enable or disable the SD card read-only boot.
By default, the Secure Digital (SD) Card Boot option is not enabled.
Secure Boot
Enable Secure Boot Enable or disable the secure boot feature.
By default, the option is not enabled.
Secure Boot Mode Enable or disable to change the secure boot mode options.
By default, the Deployed Mode is enabled.
Expert Key Management
Enable Custom Mode Enable or disable custom mode.
By default, the custom mode option is not enabled.
Custom Mode Key Management Select the custom values for expert key management.
Table 6. System setup options—Integrated Devices menu 
Integrated Devices
Date/Time Displays the current date in MM/DD/YYYY format and current time in 
HH:MM:SS AM/PM format.
Camera Enables or disable the camera.
By default, the Enable Camera option is selected
Audio
Enable Audio Enable or disable the integrated audio controller.
By default, all the options are enabled.
USB/Thunderbolt Configuration ● Enable or disable booting from USB mass storage devices connected to 
external USB ports.
By default, the Enable External USB Ports option is enabled.
● Enable or disable booting from USB mass storage devices such as external 
hard drive, optical drive, and USB drive.
By default, the Enable USB Boot Support option is enabled.
Enable Thunderbolt Technology 
Support
Enable or disable the associated ports and adapters.
By default, the Enable Thunderbolt Technology Support option is selected.
Enable Thunderbolt Boot Support Enable or disable the Thunderbolt adapter peripheral device and USB devices 
connected to the Thunderbolt adapter to be used during BIOS Pre-boot.
106 System setup
Table 6. System setup options—Integrated Devices menu (continued)
Integrated Devices
By default, the Enable Thunderbolt Boot Support option is disabled.
Enable Thunderbolt (and PCIe behind 
TBT) pre-boot modules
Enable or disable the PCIe devices that are connected through a Thunderbolt 
adapter to execute the PCIe devices UEFI Option ROM (if present) during 
pre-boot.
By default, the Enable Thunderbolt (and PCIe behind TBT) pre-boot 
modules option is disabled.
Disable USB4 PCIE Tunneling Disable the USB4 PCIE Tunneling option.
By default, the option is disabled.
Video/Power only on Type-C Ports Enable or disable the Type-C port functionality to video or only power.
By default, the Video/Power only on Type-C Ports option is disabled.
Type-C Dock Override Enables to use connected Type-C Dell Dock to provide data stream with 
external USB ports disabled. When Type-C Dock override is enabled, the 
Video/Audio/Lan submenu is activated.
By default, the Type-C Dock Override option is enabled.
Video Enable or disable the usage of video on Dell Dock external ports.
By default, the Video option is disabled.
Audio Enable or disable the usage of audio on Dell Dock external ports.
By default, the Audio option is enabled.
Lan Enable or disable the usage of LAN on Dell Dock external ports.
By default, the Lan option is enabled.
Miscellaneous Devices Enable or disable Fingerprint Reader device.
By default, the Enable Fingerprint Reader Device option is enabled.
Unobtrusive Mode
Enable Unobtrusive Mode Enable or disable all the computer light and sound.
By default, the Enable Unobtrusive Mode option is disabled.
Table 7. System setup options—Storage menu 
Storage
SMART Reporting
Enable SMART Reporting Enable or disable Self-Monitoring, Analysis, and Reporting Technology 
(SMART) during computer startup.
By default, the Enable SMART Reporting option is not enabled.
Drive Information
SATA-1
Type Displays the SATA-1 type information of the computer.
Device Displays the SATA-1 device information of the computer.
M.2 PCIe SSD-1
Type Displays the M.2 PCIe SSD-1 type information of the computer.
Device Displays the M.2 PCIe SSD-1 device information of the computer.
M.2 PCIe SSD-2
Type Displays the M.2 PCIe SSD-2 type information of the computer.
System setup 107
Table 7. System setup options—Storage menu (continued)
Storage
Device Displays the M.2 PCIe SSD-2 device information of the computer.
Enable MediaCard
Secure Digital (SD) Card Enable or disable the SD card.
By default, the Secure Digital (SD) Card option is enabled.
Secure Digital (SD) Card Read-Only Mode Enable or disable the SD card read-only mode.
By default, the Secure Digital (SD) Card Read-Only Mode option is not 
enabled.
Table 8. System setup options—Display menu 
Display
Display Brightness
Brightness on battery power Enable to set screen brightness when the computer is running on battery 
power.
Brightness on AC power Enable to set screen brightness when the computer is running on AC power.
Touchscreen Enable to activate the Touchscreen on operating system
Full Screen Logo Enable or disable full screen logo.
By default, the option is not enabled.
Table 9. System setup options—Connection menu 
Connection
Network Controller Configuration
Integrated NIC Controls the on-board LAN controller.
By default, the Enabled with PXE option is enabled.
Enable UEFI Network Stack Enable or disable UEFI Network Stack.
By default, the Enable UEFI Network Stack and Enabled w/PXE option are 
enabled.
Wireless Device Enable
WWAN/GPS Enable or disable the internal WWAN/GPS device
By default, the option enabled.
WWAN Bus Mode Set the interface type of the Wireless Wan (WWAN) card.
By default, the Bus Mode PCIe option is enabled.
WLAN Enable or disable the internal WLAN device
By default, the option enabled.
Bluetooth Enable or disable the internal Bluetooth device
By default, the option enabled.
Contactless smartcard/NFC Enable or disable the internal Contactless smartcard/NFC device
By default, the option enabled.
Enable UEFI Network Stack Enable or disable UEFI Network Stack and controls the on-board LAN 
Controller.
By default, the Enable UEFI Network Stack option are enabled.
Wireless Radio Control
108 System setup
Table 9. System setup options—Connection menu (continued)
Connection
Control WLAN radio Sense the connection of the computer to a wired network and subsequently 
disable the selected wireless radios (WLAN).
By default, the option is disabled.
Control WWAN radio Sense the connection of the computer to a wired network and subsequently 
disable the selected wireless radios (WWAN).
By default, the option is disabled.
HTTPs Boot Feature
HTTPs Boot Enable or disable the HTTPs Boot feature.
By default, the HTTPs Boot option is enabled.
HTTPs Boot Mode With Auto Mode, the HTTPs Boot extracts Boot URL from the DHCP. With 
Manual Mode, the HTTPs Boot reads Boot URL from the user-provided data.
By default, the Auto Mode option is enabled.
Table 10. System setup options—Power menu 
Power
Battery configuration Enables the computer to run on battery during peak power usage hours. Use 
the table Custom Charge Start and Custom Charge Stop , to prevent AC 
power usage between certain times of each day.
By default, the Adaptive option is enabled.
Advanced Configuration
Enable Advanced Battery Charge 
Configuration
Enable or disable the advanced battery charge configuration.
By default, the Enable Advanced Battery Charge Configuration option is 
disabled.
Peak Shift Enables the computer to run on battery during peak power usage hours.
By default, the Enable Peak Shift option is enabled.
Enable Peak Shift
USB PowerShare
Enable USB PowerShare Enable or disable the USB PowerShare.
By default, the Enable USB PowerShare option is disabled
Thermal Management Enables to cool the fan and processor heat management to adjust the 
computer performance, noise, and temperature.
By default, the Optimized option is enabled.
USB Wake Support
Wake on Dell USB-C Dock When enabled, connecting a Dell USB-C Dock will wake the computer from 
standby.
By default, the Wake on Dell USB-C Dock option is enabled.
Block Sleep Enables to block entering sleep (S3) mode in the operating system.
By default, the Block Sleep option is disabled.
Lid Switch Enable or disable the lid switch.
By default, the Lid Switch option is enabled.
Intel Speed Shift Technology Enable or disable the Intel speed shift technology support.
System setup 109
Table 10. System setup options—Power menu (continued)
Power
By default, the Intel Speed Shift Technology option is enabled.
Table 11. System setup options—Security menu 
Security
TPM 2.0 Security 
TPM 2.0 Security On Enable or disable TPM 2.0 security options.
By default, the TPM 2.0 Security On option is enabled.
Attestation Enable Enables to control whether the Trusted Platform Module (TPM) Endorsement 
Hierarchy is available to the operating system.
By default, the Attestation Enable option is enabled.
Key Storage Enable Enables to control whether the Trusted Platform Module (TPM) Storage 
Hierarchy is available to the operating system.
By default, the Key Storage Enable option is enabled.
SHA-256 BIOS and the TPM will use the SHA-256 hash algorithm to extend 
measurements into the TPM PCRs during BIOS boot.
By default, the SHA-256 option is enabled.
Clear Enables to clear the TPM owner information and returns the TPM to the 
default state.
By default, the Clear option is disabled.
PPI ByPass for Clear Commands Controls the TPM Physical Presence Interface (PPI).
By default, the PPI ByPass for clear Commands option is disabled.
Intel Total Memory Encryption
Total Memory Encryption Enable or disable you to protect memory from physical attacks including freeze 
spray, probing DDR to read the cycles, and others.
By default, the Total Memory Encryption option is disabled.
Chassis intrusion Controls the chassis intrusion feature.
By default, the On-Silent option is enabled.
SMM Security Mitigation Enable or disable SMM Security Mitigation.
By default, the option is enabled.
Data Wipe on Next Boot
Start Data Wipe Enable or disable the data wipe on next boot.
By default, the option is enabled.
Absolute Enable or disable or permanently disable the BIOS module interface of the 
optional Absolute Persistence Module service from Absolute software.
By default, the option is enabled.
UEFI Boot Path Security Controls whether or not the computer will prompt the user to enter the admin 
password (if set) when booting to a UEFI boot device from the F12 boot menu.
By default, the Always Except Internal HDD option is enabled.
110 System setup
Table 12. System setup options—Passwords menu 
Passwords
Admin Password Set, change, or delete the administrator password.
System Password Set, change, or delete the computer password.
NVMe SSD0 Set, change, or delete the NVMe SSD0 password.
Password Configuration
Upper Case Letter Reinforces password must have at least one upper case letter.
By default, the option is disabled.
Lower Case Letter Reinforces password must have at least one lower case letter.
By default, the option is disabled.
Digit Reinforces password must have at least one digit.
By default, the option is disabled.
Special Character Reinforces password must have at least one special character.
By default, the option is disabled.
Minimum Characters Set the minimum characters allowed for password.
Password Bypass When enabled, this always prompts for computer and internal hard drive 
passwords when powered on from the off state.
By default, the Disabled option is enabled.
Password Changes 
Enable Non-Admin Password Changes Enable or disable to change computer and hard drive password without the 
need for admin password.
By default, the option is enabled.
Admin Setup Lockout
Enable Admin Setup Lockout Enables administrators control over how their users can or cannot access BIOS 
setup.
By default, the option is disabled.
Master Password Lockout
Enable Master Password Lockout When enabled, this will disable the master password support.
By default, the option is disabled.
Allow Non-Admin PSID Revert
Enable Allow Non-Admin PSID Revert Controls access to the Physical Security ID (PSID) revert of NVMe hard-drives 
from the Dell Security Manager prompt.
By default, the option is disabled.
Table 13. System setup options—Update, Recovery menu 
Update, Recovery
UEFI Capsule Firmware Updates Enable or disable BIOS updates through UEFI capsule update packages.
By default, the option is enabled.
BIOS Recovery from Hard Drive Enables the user to recover from certain corrupted BIOS conditions from a 
recovery file on the user primary hard drive or an external USB key.
By default, the option is enabled.
BIOS Downgrade
System setup 111
Table 13. System setup options—Update, Recovery menu (continued)
Update, Recovery
Allow BIOS Downgrade Enable or disable the flashing of the computer firmware to previous revision is 
blocked.
By default, the option is enabled.
SupportAssist OS Recovery Enable or disable the boot flow for SupportAssist OS Recovery tool in the 
event of certain computer errors.
By default, the option is enabled.
BISOConnect Enable or disable cloud Service OS recovery if the main operating system fails 
to boot with the number of failures equal to or greater than the value specified 
by the Auto OS Recovery Threshold setup option and local Service OS does not 
boot or is not installed.
By default, the option is enabled.
Dell Auto OS Recovery Threshold Controls the automatic boot flow for SupportAssist System Resolution Console 
and for Dell OS Recovery Tool.
By default, the threshold value is set to 2.
Table 14. System setup options—System Management menu 
System Management
Service Tag Display the Service Tag of the computer.
Asset Tag Create a computer Asset Tag.
AC Behavior
Wake on AC Enable or disable the wake on AC option.
By default, the option is disabled.
Wake on LAN
Wake on LAN Enable or disable the computer to power on by special LAN signals when it 
receives a wakeup signal from the WLAN.
By default, the Disabled option is selected.
Auto on Time Enable to set the computer to turn on automatically every day or on a 
preselected date and time. This option can be configured only if the Auto On 
Time is set to Everyday, Weekdays, or Selected Days.
By default, the option is disabled.
Intel AMT Capability Enable Intel Active Management Technology
MEBx Hotkey Allows the user to use Ctrl+P hotkey to access MEBx
USB Provision When enabled, Intel AMT can be provisioned using the local provisioning file 
through a USB storage device
Table 15. System setup options—Keyboard menu 
Keyboard
Numlock Enable Enable or disable the Numlock function when the computer boots.
By default, the option is enabled.
Fn Lock Options By default, the Fn lock option is enabled.
Keyboard Illumination Enables to change the keyboard illumination settings.
By default, the Bright option is enabled.
112 System setup
Table 15. System setup options—Keyboard menu (continued)
Keyboard
Keyboard Backlight Timeout on AC Set the timeout value for the keyboard backlight when an AC adapter is 
connected to the computer.
By default, the 10 seconds option is enabled.
Keyboard Backlight Timeout on 
Battery
Set the timeout value for the keyboard backlight when the is running only on 
battery power.
By default, the 10 seconds option is enabled.
Device Configuration Hotkey Access Manages whether you can access device configuration screens through 
hotkeys during computer startup.
By default, the option is enabled.
Table 16. System setup options—Pre-boot Behavior menu 
Pre-boot Behavior
Adapter Warnings
Enable Adapter Warnings Enable or disable the warning messages during boot when the adapters with 
less power capacity are detected.
By default, the option is enabled.
Warning and Errors Enable or disable the action to be done when a warning or error is encountered.
By default, the Prompt on Warnings and Errors option is enabled.
Fastboot Enable to set the speed of the boot process.
By default, the Minimal option is enabled.
Extend BIOS POST Time Set the BIOS POST time.
By default, the 0 seconds option is enabled.
MAC Address Pass-Through Replaces the external NIC MAC address with the selected MAC address from 
the computer.
By default, the System Unique MAC Address option is enabled.
Table 17. System setup options—Performance menu 
Performance
Multi Core Support 
Active Cores Enables to change the number of CPU cores available to the operating system.
By default, the All Cores options is enabled.
Intel SpeedStep
Enable Intel SpeedStep Technology Enables the computer to dynamically adjust processor voltage and core 
frequency, decreasing average power consumption and heat production.
By default, the option is enabled.
C-States Control
Enable C-State Control Enable or disable additional processor sleep states.
By default, the option is enabled.
Intel TurbocBoost Technology
Enable Intel Turbo Boost Technology Enable or disable Intel TurboBoost mode of the processor.
By default, the option is enabled.
System setup 113
Table 17. System setup options—Performance menu (continued)
Performance
Intel Hyper-Threading Technology
Enable Intel Hyper-Threading Technology Enable or disable Hyper-Threading in the processor.
By default, the option is enabled.
Dynamic Tuning:Machine Learning
Enable Dynamic Tuning:Machine Learning Enables the operating system capability to enhance dynamic power tuning 
capabilities based on detected workloads.
By default, the option is disabled.
Table 18. System setup options—System Logs menu 
System Logs
BIOS Event Log
Clear Bios Event Log Display BIOS events.
By default, the Keep option is enabled.
Thermal Event Log
Clear Thermal Event Log Display Thermal events.
By default, the Keep option is enabled.
Power Event Log
Clear Power Event Log Display power events.
By default, the Keep option is enabled.
License Information Displays the license information of the computer.
Updating the BIOS
Updating the BIOS in Windows
About this task
CAUTION: If BitLocker is not suspended before updating the BIOS, the next time you reboot the system it 
will not recognize the BitLocker key. You will then be prompted to enter the recovery key to progress and the 
system will ask for this on each reboot. If the recovery key is not known this can result in data loss or an 
unnecessary operating system re-install. For more information on this subject, search in the Knowledge Base 
Resource at www.dell.com/support .
Steps
1. Go to www.dell.com/support .
2. Click Product support . In the Search support box, enter the Service Tag of your computer, and then click Search .
NOTE: If you do not have the Service Tag, use the SupportAssist feature to automatically identify your computer. You 
can also use the product ID or manually browse for your computer model.
3. Click Drivers & Downloads . Expand Find drivers .
4. Select the operating system installed on your computer.
5. In the Category drop-down list, select BIOS .
6. Select the latest version of BIOS, and click Download to download the BIOS file for your computer.
7. After the download is complete, browse the folder where you saved the BIOS update file.
114 System setup
8. Double-click the BIOS update file icon and follow the on-screen instructions.
For more information, search in the Knowledge Base Resource at www.dell.com/support .
Updating the BIOS in Linux and Ubuntu
To update the system BIOS on a computer that is installed with Linux or Ubuntu, see the knowledge base article 000131486 at 
www.dell.com/support .
Updating the BIOS using the USB drive in Windows
About this task
CAUTION: If BitLocker is not suspended before updating the BIOS, the next time you reboot the system it 
will not recognize the BitLocker key. You will then be prompted to enter the recovery key to progress and the 
system will ask for this on each reboot. If the recovery key is not known this can result in data loss or an 
unnecessary operating system re-install. For more information on this subject, search in the Knowledge Base 
Resource at www.dell.com/support .
Steps
1. Follow the procedure from step 1 to step 6 in Updating the BIOS in Windows to download the latest BIOS setup program file.
2. Create a bootable USB drive. For more information, search in the Knowledge Base Resource at www.dell.com/support .
3. Copy the BIOS setup program file to the bootable USB drive.
4. Connect the bootable USB drive to the computer that needs the BIOS update.
5. Restart the computer and press F12 .
6. Select the USB drive from the One Time Boot Menu .
7. Type the BIOS setup program filename and press Enter .
The BIOS Update Utility appears.
8. Follow the on-screen instructions to complete the BIOS update.
Updating the BIOS from the F12 One-Time boot menu
Update your computer BIOS using the BIOS update.exe file that is copied to a FAT32 USB drive and booting from the F12 
One-Time boot menu.
About this task
CAUTION: If BitLocker is not suspended before updating the BIOS, the next time you reboot the system it 
will not recognize the BitLocker key. You will then be prompted to enter the recovery key to progress and the 
system will ask for this on each reboot. If the recovery key is not known this can result in data loss or an 
unnecessary operating system re-install. For more information on this subject, search in the Knowledge Base 
Resource at www.dell.com/support .
BIOS Update
You can run the BIOS update file from Windows using a bootable USB drive or you can also update the BIOS from the F12 
One-Time boot menu on the computer.
Most of the Dell computers built after 2012 have this capability, and you can confirm by booting your computer to the F12 
One-Time Boot Menu to see if BIOS FLASH UPDATE is listed as a boot option for your computer. If the option is listed, then the 
BIOS supports this BIOS update option.
NOTE: Only computers with BIOS Flash Update option in the F12 One-Time boot menu can use this function.
Updating from the One-Time boot menu
To update your BIOS from the F12 One-Time boot menu, you need the following:
● USB drive formatted to the FAT32 file system (key does not have to be bootable)
System setup 115
● BIOS executable file that you downloaded from the Dell Support website and copied to the root of the USB drive
● AC power adapter that is connected to the computer
● Functional computer battery to flash the BIOS
Perform the following steps to perform the BIOS update flash process from the F12 menu:
CAUTION: Do not turn off the computer during the BIOS update process. The computer may not boot if you turn 
off your computer.
Steps
1. From a turn off state, insert the USB drive where you copied the flash into a USB port of the computer.
2. Turn on the computer and press F12 to access the One-Time Boot Menu, select BIOS Update using the mouse or arrow keys 
then press Enter.
The flash BIOS menu is displayed.
3. Click Flash from file .
4. Select external USB device.
5. Select the file and double-click the flash target file, and then click Submit .
6. Click Update BIOS . The computer restarts to flash the BIOS.
7. The computer will restart after the BIOS update is completed.
System and setup password
Table 19. System and setup password 
Password type Description
System password Password that you must enter to log on to your system.
Setup password Password that you must enter to access and make changes to 
the BIOS settings of your computer.
You can create a system password and a setup password to secure your computer.
CAUTION: The password features provide a basic level of security for the data on your computer.
CAUTION: Anyone can access the data stored on your computer if it is not locked and left unattended.
NOTE: System and setup password feature is disabled.
Assigning a system setup password
Prerequisites
You can assign a new System or Admin Password only when the status is in Not Set .
About this task
To enter the system setup, press F2 immediately after a power-on or reboot.
Steps
1. In the System BIOS or System Setup screen, select Security and press Enter .
The Security screen is displayed.
2. Select System/Admin Password and create a password in the Enter the new password field.
Use the following guidelines to assign the system password:
● A password can have up to 32 characters.
● The password can contain the numbers 0 through 9.
● Only lower case letters are valid, upper case letters are not allowed.
116 System setup
● Only the following special characters are allowed: space, (”), (+), (,), (-), (.), (/), (;), ([), (\), (]), (`).
3. Type the system password that you entered earlier in the Confirm new password field and click OK.
4. Press Esc and a message prompts you to save the changes.
5. Press Y to save the changes.
The computer reboots.
Deleting or changing an existing system setup password
Prerequisites
Ensure that the Password Status is Unlocked (in the System Setup) before attempting to delete or change the existing 
System and Setup password. You cannot delete or change an existing System or Setup password, if the Password Status is 
Locked.
About this task
To enter the System Setup, press F2 immediately after a power-on or reboot.
Steps
1. In the System BIOS or System Setup screen, select System Security and press Enter .
The System Security screen is displayed.
2. In the System Security screen, verify that Password Status is Unlocked .
3. Select System Password , alter or delete the existing system password and press Enter or Tab.
4. Select Setup Password , alter or delete the existing setup password and press Enter or Tab.
NOTE: If you change the System and/or Setup password, re enter the new password when prompted. If you delete the 
System and Setup password, confirm the deletion when prompted.
5. Press Esc and a message prompts you to save the changes.
6. Press Y to save the changes and exit from System Setup.
The computer restarts.
Clearing BIOS (System Setup) and System passwords
About this task
To clear the system or BIOS passwords, contact Dell technical support as described at www.dell.com/contactdell .
NOTE: For information on how to reset Windows or application passwords, refer to the documentation accompanying 
Windows or your application.
System setup 117

## Troubleshooting

_Latitude 5521 Service Manual, pages 118–124_

Troubleshooting
Topics:
• Handling swollen rechargeable Li-ion batteries
• Dell SupportAssist Pre-boot System Performance Check diagnostics
• Built-in self-test (BIST)
• System diagnostic lights
• Recovering the operating system
• Real-Time Clock (RTC Reset)
• Backup media and recovery options
• Wi-Fi power cycle
• Drain residual flea power (perform hard reset)
Handling swollen rechargeable Li-ion batteries
Like most laptops, Dell laptops use Lithium-ion batteries. One type of Lithium-ion battery is the rechargeable Li-ion battery. 
Rechargeable Li-ion batteries have increased in popularity in recent years and have become standard in the electronics industry 
due to customer preferences for a slim form factor (especially with newer ultra-thin laptops) and long battery life. Inherent to 
rechargeable Li-ion battery technology is the potential for swelling of the battery cells.
Swollen battery may impact the performance of the laptop. To prevent possible further damage to the device enclosure or 
internal components leading to malfunction, discontinue the use of the laptop and discharge it by disconnecting the AC adapter 
and letting the battery drain.
Swollen batteries should not be used and should be replaced and disposed of properly. We recommend contacting Dell product 
support for options to replace a swollen battery under the terms of the applicable warranty or service contract, including options 
for replacement by a Dell authorized service technician.
The guidelines for handling and replacing rechargeable Li-ion batteries are as follows:
● Exercise caution when handling rechargeable Li-ion batteries.
● Discharge the battery before removing it from the system. To discharge the battery, unplug the AC adapter from the system 
and operate the system only on battery power. When the system will no longer power on when the power button is pressed, 
the battery is fully discharged.
● Do not crush, drop, mutilate, or penetrate the battery with foreign objects.
● Do not expose the battery to high temperatures, or disassemble battery packs and cells.
● Do not apply pressure to the surface of the battery.
● Do not bend the battery.
● Do not use tools of any type to pry on or against the battery.
● If a battery gets stuck in a device as a result of swelling, do not try to free it as puncturing, bending, or crushing a battery 
can be dangerous.
● Do not attempt to reassemble a damaged or swollen battery into a laptop.
● Swollen batteries that are covered under warranty should be returned to Dell in an approved shipping container (provided 
by Dell)—this is to comply with transportation regulations. Swollen batteries that are not covered under warranty should be 
disposed of at an approved recycling center. Contact Dell product support at https://www.dell.com/support for assistance 
and further instructions.
● Using a non-Dell or incompatible battery may increase the risk of fire or explosion. Replace the battery only with a 
compatible battery purchased from Dell that is designed to work with your Dell computer. Do not use a battery from other 
computers with your computer. Always purchase genuine batteries from https://www.dell.com or otherwise directly from 
Dell.
Rechargeable Li-ion batteries can swell for various reasons such as age, number of charge cycles, or exposure to high heat. 
For more information on how to improve the performance and lifespan of the laptop battery and to minimize the possibility of 
occurrence of the issue, search Dell Laptop Battery in the Knowledge Base Resource at www.dell.com/support .
5
118 Troubleshooting
Dell SupportAssist Pre-boot System Performance 
Check diagnostics
About this task
SupportAssist diagnostics (also known as system diagnostics) performs a complete check of your hardware. The Dell 
SupportAssist Pre-boot System Performance Check diagnostics is embedded with the BIOS and is launched by the BIOS 
internally. The embedded system diagnostics provides a set of options for particular devices or device groups allowing you to:
● Run tests automatically or in an interactive mode
● Repeat tests
● Display or save test results
● Run thorough tests to introduce additional test options to provide extra information about the failed device(s)
● View status messages that inform you if tests are completed successfully
● View error messages that inform you of problems encountered during testing
NOTE: Some tests for specific devices require user interaction. Always ensure that you are present at the computer 
terminal when the diagnostic tests are performed.
For more information, see https://www.dell.com/support/kbdoc/000180971 .
Running the SupportAssist Pre-Boot System Performance Check
Steps
1. Turn on your computer.
2. As the computer boots, press the F12 key as the Dell logo appears.
3. On the boot menu screen, select the Diagnostics option.
4. Click the arrow at the bottom left corner.
Diagnostics front page is displayed.
5. Click the arrow in the lower-right corner to go to the page listing.
The items detected are listed.
6. To run a diagnostic test on a specific device, press Esc and click Yes to stop the diagnostic test.
7. Select the device from the left pane and click Run Tests .
8. If there are any issues, error codes are displayed.
Note the error code and validation number and contact Dell.
Built-in self-test (BIST)
M-BIST
M-BIST (Built In Self-Test) is the system board's built-in self-test diagnostics tool that improves the diagnostics accuracy of 
system board embedded controller (EC) failures.
NOTE: M-BIST can be manually initiated before POST (Power On Self Test).
How to run M-BIST
NOTE: M-BIST must be initiated on the system from a power-off state either connected to AC power or with battery only.
1. Press and hold both the M key on the keyboard and the power button to initiate M-BIST.
2. With both the M key and the power button held down, the battery indicator LED may exhibit two states:
a. OFF: No fault detected with the system board
b. AMBER: Indicates a problem with the system board
3. If there is a failure with the system board, the battery status LED will flash one of the following error codes for 30 seconds:
Troubleshooting 119
Table 20. LED error codes 
Blinking Pattern Possible Problem
Amber White
2 1 CPU Failure
2 8 LCD Power Rail Failure
1 1 TPM Detection Failure
2 4 Memory/RAM failure
4. If there is no failure with the system board, the LCD will cycle through the solid color screens described in the LCD-BIST 
section for 30 seconds and then power off.
LCD Power rail test (L-BIST)
L-BIST is an enhancement to the single LED error code diagnostics and is automatically initiated during POST. L-BIST will check 
the LCD power rail. If there is no power being supplied to the LCD (that is if the L-BIST circuit fails), the battery status LED will 
flash either an error code [2,8] or an error code [2,7].
NOTE: If L-BIST fails, LCD-BIST cannot function as no power will be supplied to the LCD.
How to invoke L-BIST Test:
1. Press the power button to start the system.
2. If the system does not start up normally, look at the battery status LED:
● If the battery status LED flashes an error code [2,7], the display cable may not be connected properly.
● If the battery status LED flashes an error code [2,8], there is a failure on the LCD power rail of the system board, hence 
there is no power supplied to the LCD.
3. For cases, when a [2,7] error code is shown, check to see if the display cable is properly connected.
4. For cases when a [2,8] error code is shown, replace the system board.
LCD Built-in Self Test (BIST)
Dell laptops have a built-in diagnostic tool that helps you determine if the screen abnormality you are experiencing is an inherent 
problem with the LCD (screen) of the Dell laptop or with the video card (GPU) and PC settings.
When you notice screen abnormalities like flickering, distortion, clarity issues, fuzzy or blurry image, horizontal or vertical lines, 
color fade etc., it is always a good practice to isolate the LCD (screen) by running the Built-In Self Test (BIST).
How to invoke LCD BIST Test
1. Power off the Dell laptop.
2. Disconnect any peripherals that are connected to the laptop. Connect only the AC adapter (charger) to the laptop.
3. Ensure that the LCD (screen) is clean (no dust particles on the surface of the screen).
4. Press and hold D key and Power on the laptop to enter LCD built-in self test (BIST) mode. Continue to hold the D key, until 
the system boots up.
5. The screen will display solid colors and change colors on the entire screen to white, black, red, green, and blue twice.
6. Then it will display the colors white, black and red.
7. Carefully inspect the screen for abnormalities (any lines, fuzzy color or distortion on the screen).
8. At the end of the last solid color (red), the system will shut down.
NOTE: Dell SupportAssist Pre-boot diagnostics upon launch, initiates an LCD BIST first, expecting a user intervention 
confirm functionality of the LCD.
120 Troubleshooting
System diagnostic lights
Battery-status light
Indicates the power and battery-charge status.
Solid white — Power adapter is connected and the battery has more than 5 percent charge.
Amber — Computer is running on battery and the battery has less than 5 percent charge.
Off
● Power adapter is connected, and the battery is fully charged.
● Computer is running on battery, and the battery has more than 5 percent charge.
● Computer is in a sleep state, hibernation, or turned off.
The power and battery-status light blinks amber along with beep codes indicating failures.
For example, the power and battery-status light blinks amber two times followed by a pause, and then blinks white three times 
followed by a pause. This 2,3 pattern continues until the computer is turned off indicating no memory or RAM is detected.
The following table shows different power and battery-status light patterns and associated problems.
Table 21. System diagnostic lights 
Blinking Pattern Problem description Suggested resolution
Amber White
1 1 TPM detection failure Replace the system board.
1 2 Unrecoverable SPI flash 
failure
Replace the system board.
1 5 EC unable to program i-Fuse Replace the system board.
1 6 Generic catch-all for 
ungraceful EC code flow 
errors
Disconnect all power source 
(AC, battery, coin cell) and 
drain flea power by pressing 
and holding down power 
button.
2 1 CPU failure Run the Intel CPU diagnostics 
tools. If problem persists, 
replace the system board.
2 2 System Board failure 
(included BIOS corruption or 
ROM error)
Flash latest BIOS version. If 
problem persists, replace the 
system board.
2 3 No Memory / RAM detected Confirm that the memory 
module is installed properly. If 
problem persists, replace the 
memory module.
2 4 Memory / RAM failure Reset and swap memory 
modules among the slots. If 
problem persists, replace the 
memory module.
2 5 Invalid memory installed Reset and swap memory 
modules among the slots. If 
problem persists, replace the 
memory module.
2 6 System board / Chipset Error Replace the system board.
2 7 Potential LCD Panel damage 
and/ or LCD cable failure 
(SBIOS message)
Run LCD BIST to check 
for physical LCD damage. 
If no sign of life on 
display (no backlight), reseat 
display cable (EDP) at the 
Troubleshooting 121
Table 21. System diagnostic lights (continued)
Blinking Pattern Problem description Suggested resolution
Amber White
Motherboard. If the colors are 
displayed without distortion 
(screen showing a solid color) 
or the 2,7 code persists, 
replace the LCD assembly and 
display cable (EDP).
2 8 Power rail failure at the 
system board side
If the display is black or 
dim (no backlight), replace 
the Motherboard and display 
cable (EDP). If no display 
issues (LCD panel functional), 
only replace the Motherboard.
3 1 CMOS battery failure Reset the CMOS battery 
connection. If problem 
persists, replace the RTC 
battery.
3 2 PCI or Video card/chip failure Replace the system board.
3 3 BIOS recovery image not 
found
Flash latest BIOS version. If 
problem persists, replace the 
system board.
3 4 BIOS recovery image found 
but invalid
Flash latest BIOS version. If 
problem persists, replace the 
system board.
3 5 Power rail failure Replace the system board.
3 6 Flash corruption detected by 
SBIOS.
Replace the system board.
3 7 Timeout waiting on ME to 
reply to HECI message.
Replace the system board.
4 3 LCD Panel Failure Replace the LCD Assembly
4 4 Power rail failure at system 
board side
If the display is dim 
(no backlight), replace the 
Motherboard and display 
cable (EDP). If the display 
is black/no image on panel, 
replace the Motherboard and 
LCD Assembly.
4 5 LCD Panel Failure and Power 
rail failure at system board 
side.
Replace the Motherboard, 
LCD Assembly and Display 
Cable (EDP).
4 6 Display Cable (EDP) Failure Reseat the display cable 
(EDP) at the Motherboard. If 
the 4,6 code persists, replace 
the display cable (EDP).
Camera status light: Indicates whether the camera is in use.
● Solid white — Camera is in use.
● Off — Camera is not in use.
Caps Lock status light: Indicates whether Caps Lock is enabled or disabled.
● Solid white — Caps Lock enabled.
● Off — Caps Lock disabled.
122 Troubleshooting
Recovering the operating system
When your computer is unable to boot to the operating system even after repeated attempts, it automatically starts Dell 
SupportAssist OS Recovery.
Dell SupportAssist OS Recovery is a standalone tool that is preinstalled in all Dell computers installed with Windows operating 
system. It consists of tools to diagnose and troubleshoot issues that may occur before your computer boots to the operating 
system. It enables you to diagnose hardware issues, repair your computer, back up your files, or restore your computer to its 
factory state.
You can also download it from the Dell Support website to troubleshoot and fix your computer when it fails to boot into their 
primary operating system due to software or hardware failures.
For more information about the Dell SupportAssist OS Recovery, see Dell SupportAssist OS Recovery User's Guide at 
www.dell.com/serviceabilitytools . Click SupportAssist and then, click SupportAssist OS Recovery .
Real-Time Clock (RTC Reset)
The Real Time Clock (RTC) reset function allows you to recover Dell computer from No POST, No Power or, No Boot like 
situations. There is no coin-cell battery on this computer, the main battery reserves 2% of its capacity for RTC function.
How to Reset the Real-Time Clock (RTC)
● Start the RTC reset with the computer powered off and connected to AC power.
● Press and hold the power button for thirty (30-35) seconds.
● The computer RTC Reset occurs after you release the power button.
NOTE: For more information, see the knowledge base article 000125880 at https://www.dell.com/support/ .
Backup media and recovery options
It is recommended to create a recovery drive to troubleshoot and fix problems that may occur with Windows. Dell proposes 
multiple options for recovering Windows operating system on your Dell PC. For more information. see Dell Windows Backup 
Media and Recovery Options .
Wi-Fi power cycle
About this task
If your computer is unable to access the Internet due to Wi-Fi connectivity issues a Wi-Fi power cycle procedure may be 
performed. The following procedure provides the instructions on how to conduct a Wi-Fi power cycle:
NOTE: Some ISPs (Internet Service Providers) provide a modem/router combo device.
Steps
1. Turn off your computer.
2. Turn off the modem.
3. Turn off the wireless router.
4. Wait for 30 seconds.
5. Turn on the wireless router.
6. Turn on the modem.
7. Turn on your computer.
Troubleshooting 123
Drain residual flea power (perform hard reset)
About this task
Flea power is the residual static electricity that remains in the computer even after it has been powered off and the battery is 
removed.
For your safety, and to protect the sensitive electronic components in your computer, you are requested to drain residual flea 
power before removing or replacing any components in your computer.
Draining residual flea power, also known as a performing a "hard reset", is also a common troubleshooting step if your computer 
does not power on or boot into the operating system.
To drain residual flea power (perform a hard reset)
Steps
1. Turn off your computer.
2. Disconnect the power adapter from your computer.
3. Remove the base cover.
4. Remove the battery.
5. Press and hold the power button for 20 seconds to drain the flea power.
6. Install the battery.
7. Install the base cover.
8. Connect the power adapter to your computer.
9. Turn on your computer.
NOTE: For more information about performing a hard reset, search in the Knowledge Base Resource at www.dell.com/
support .
124 Troubleshooting

## Latitude 5521 Re-imaging guide for Windows 10

_Complete document, 16 pages_

Latitude 5521
Re-imaging guide for Windows 10
Regulatory Model: P104F
Regulatory Type: P104F003/P104F004
June 2021
Rev. A00
Notes, cautions, and warnings
NOTE: A NOTE indicates important information that helps you make better use of your product.
CAUTION: A CAUTION indicates either potential damage to hardware or loss of data and tells you how to avoid
the problem.
WARNING: A WARNING indicates a potential for property damage, personal injury, or death.
© 2021 Dell Inc. or its subsidiaries. All rights reserved. Dell, EMC, and other trademarks are trademarks of Dell Inc. or its subsidiaries. Other
trademarks may be trademarks of their respective owners.
Chapter 1: Installation overview.................................................................................................... 4
Chapter 2: Introduction.................................................................................................................5
Chapter 3: Order of reinstallation..................................................................................................6
Chapter 4: Updating or resetting the BIOS.................................................................................... 7
Flashing the BIOS................................................................................................................................................................ 7
Clearing CMOS settings.....................................................................................................................................................7
Trusted Platform Module (TPM) security..................................................................................................................... 7
Chapter 5: Reinstalling the operating system................................................................................ 8
Chapter 6: Reinstalling drivers and applications............................................................................ 9
Displaying drivers and applications on your computer................................................................................................9
Chapter 7: Reinstallation sequence for drivers and applications...................................................10
Intel chipset device software..........................................................................................................................................10
Downloading and installing the chipset driver.......................................................................................................10
Critical Microsoft Quick Fix Engineering (QFE) updates......................................................................................... 10
Intel Rapid Storage Technology (IRST)........................................................................................................................10
Downloading and installing the IRST driver............................................................................................................ 11
Graphics................................................................................................................................................................................ 11
Downloading and installing the Dell graphics driver............................................................................................. 11
Audio...................................................................................................................................................................................... 11
Downloading and installing the Dell audio driver................................................................................................... 11
Dell ControlVault3 Driver Firmware............................................................................................................................... 12
Downloading and installing the Dell ControlVault3 driver and firmware.........................................................12
IR Camera Driver................................................................................................................................................................ 12
Downloading and installing the IR camera driver..................................................................................................12
Dell Power Manager Service........................................................................................................................................... 12
Downloading and installing the DPM....................................................................................................................... 13
Wireless Local Network (WLAN) drivers and applications...................................................................................... 13
Downloading and installing the Wi-Fi driver...........................................................................................................13
Dell Docking Station WD19/WD19DC .......................................................................................................................... 13
Dell Thunderbolt Dock WD19TB..................................................................................................................................... 14
Chapter 8: .NET Framework.........................................................................................................15
Chapter 9: Getting help and contacting Dell.................................................................................16
Contents
Contents 3
Installation overview
CAUTION: This re-imaging guide is designed for system administrators. Do not attempt to re-image the system
if you are not an administrator or if you are unsure of the procedures. Failure to follow instructions may result in
permanent data loss.
NOTE: Information provided in this guide is applicable to computers with Windows 10 only.
NOTE: With the introduction of Windows 10, Microsoft has prioritized driver installations via Universal Windows Platform
(UWP) from the Microsoft Store. UWP applications replace Windows executable drivers and are a more secure method of
driver installation. Some domain administrators may place limits of Microsoft Store accessibility. If you have questions about
accessing the Microsoft Store for driver updates, contact your administrator.
NOTE: Dell recommends that you download and install the device drivers from the Dell Drivers & Downloads website.
Installing device drivers from a non-Dell website can cause system performance issues, corrupt operating system files, blue
screen errors, unexpected shutdowns, or infect your computer with malicious software.
Device drivers must be updated when you reinstall the operating system using either a CD, DVD, USB key, or when you are
facing networking, graphics, sound or other hardware-related problems. Dell recommends that you install or update device
drivers if you have performed a factory reset of your Dell computer using the Dell Backup and Recovery application or other
factory-reset methods. This ensures that you have the latest device drivers installed on your computer and that the devices
function optimally.
Installing or updating device drivers may lead to the following improvements:
● Increases in system performance
● Patched security risks
● Expanded compatibility
● Fixed device issues
● Support for new features
However, if your computer is operating normally and there are no driver issues or updates being prompted by Windows, driver
updates may be unnecessary. Updating drivers unnecessarily may create new problems.
Review the importance of each driver update on the Dell Drivers & Downloads page before assessing the need to continue with
an update.
1
4 Installation overview
Introduction
CAUTION: This re-imaging guide is designed for system administrators. Do not attempt to re-image the system
if you are not an administrator or are unsure of the procedures. Failure to follow instructions may result in
permanent data loss.
NOTE: Information that is provided in this guide is applicable to computers with Windows 10 only.
Re-imaging is the process of removing all software on the computer and reinstalling the removed software. Re-imaging is
required when software in the computer is corrupted or damaged and it can also be used as a means of removing harmful and
malicious software in your computer. This re-imaging guide provides the steps that are required for re-imaging your computer.
This guide assists you in installing Dell-recommended software stack and settings, drivers, and applications, which are tested
and validated on your computer. The installation of the listed drivers and applications as described in the guide enhances the
optimal performance of your computer.
Dell also provides drivers and applications that are not included with the Windows operating system. These drivers are required
to enable the following solid-state drives (SSDs):
● 128 GB PCIe SSD
● 256 GB PCIe SSD
● 512 GB PCIe SSD
● 1024 GB PCIe SSD
● 2048 GB PCIe SSD and larger capacity size PCIe SSDs
It is always recommended to re-image on a newly-installed operating system and not from any previous image-build. Ensure
BIOS settings, including SATA configurations and modes, are appropriately set and the latest drivers and applications are used
when re-imaging the computer.
2
Introduction 5
Order of reinstallation
NOTE: Some drivers and application installation steps may not be applicable, depending on the configuration of the
computer you have ordered.
To achieve optimal performance, install the drivers and applications in the following sequence:
1. BIOS : Enables the operating system to be loaded into the memory and enables the initial setup process on your computer.
2. Windows 10 operating system : The operating system controls the system's hardware to be a base on which other
software can operate on.
3. Intel chipset driver : Allows Windows to communicate and adjust settings on components on the system board which
includes:
● Intel Chipset Device Software Driver
● Intel Management Engine Components Installer
● Intel Serial IO Driver
● Intel HID Event Filter Driver
● Intel Thunderbolt Controller Driver
● Intel Dynamic Tuning Driver
● Intel Integrated Sensor Solution Driver
4. Critical Microsoft Quick Fix Engineering (QFE) updates : Microsoft updates that fix and optimize the operating system.
5. Intel Rapid Storage Technology (IRST) : Enables and enhances data storage virtualization for the storage drives installed
in the computer.
6. Graphics driver :
● Enhances and optimizes video performance.
● Enables and provides additional functionality not included in the native Microsoft VGA driver, including:
○ User-customizable power management features
○ Portability and behavioral profiles
○ Multiple-monitor support
7. Audio driver : Enables and enhances the audio controller.
8. Security drivers , which include:
● Dell ControlVault3 driver and firmware
● IR camera
.
9. Dell applications , which include:
● Dell Update application
● Dell Power Manager (DPM)
10. Networking and communication drivers , which include:
● Wireless Local Area Network (WLAN) adapter driver: Enables and enhances the wireless adapter.
● Bluetooth driver: Enables and enhances the Bluetooth adapter.
11. Dell Client Command Suite
NOTE: Dell Client Command Suite is the new name of our industry leading Client Systems Management tools. These
tools make Dell commercial client systems the world's most manageable client devices. Click Dell Client Command Suite
for more details
3
6 Order of reinstallation
Updating or resetting the BIOS
Flashing the BIOS
It is recommended to flash the BIOS when an update is available or when you replace the system board. To flash the BIOS:
1. Turn on your computer.
2. Go to www.dell.com/support .
3. Click Product support , enter the Service Tag of your computer, and then click Search .
NOTE: If you do not have the Service Tag, use the product ID or manually browse for your computer model.
4. Click Drivers & downloads > Find drivers .
5. Select the operating system installed on your computer.
6. Scroll down the page and expand BIOS .
7. Click Download to download the latest version of the BIOS for your computer.
8. After the download is complete, navigate to the folder where you saved the BIOS update file.
9. Double-click the BIOS update file icon and follow the instructions on the screen.
Clearing CMOS settings
In the event that flashing your computer with the latest BIOS update results in your computer being unable to boot, a BIOS
reset is necessary. Clearing the CMOS settings will reset the BIOS to factory settings. For more information about clearing the
CMOS settings, see your computer's Service Manual .
Trusted Platform Module (TPM) security
TPM must be enabled in the BIOS setup program for it to be deployed on the computer. Follow these steps to enable and
configure the TPM:
1. Turn on or restart your computer.
2. Press F2 when the Dell logo is displayed on the screen to enter the BIOS setup program.
The BIOS setup program is displayed.
3. On the left pane, select Security .
4. Select or clear any of the following options to enable or disable it, respectively:
● TPM state (Enabled or Disabled) :
Enabled: The BIOS will enable the TPM during POST and it can be accessed by the operating system.
Disabled: The BIOS will not enable the TPM during POST and it cannot be accessed by the operating system.
● TPM 2.0 security On : The TPM is enabled and activated.
● Clear : The BIOS clears the information stored in the TPM.
5. Save the settings and exit.
4
Updating or resetting the BIOS 7
Reinstalling the operating system
The Windows 10 (64-bit) operating system is validated for use on this computer. You can reset or reinstall the operating
system under different scenarios. For more information about reinstalling the operating system, see the knowledge base article
SLN297920 at www.dell.com/support .
Before attempting a reinstall of your operating system, Dell recommends that you backup all data as described in the Microsoft
knowledge base article .
5
8 Reinstalling the operating system
Reinstalling drivers and applications
Drivers and applications are software that enables Windows 10 to communicate with the hardware devices and software in your
computer. Devices such as video and sound cards require drivers to function correctly within Windows, and enable users to
adjust hardware settings.
Windows 10 includes drivers for most devices, but device-specific drivers may have to be downloaded and installed separately.
Dell recommends that you download the device drivers for your Dell computer from Drivers & Downloads .
Applications must be downloaded and installed separately. Dell recommends that you download the required applications for your
Dell computer from the Dell Download Center .
Displaying drivers and applications on your computer
1. Turn on your computer.
2. Go to www.dell.com/support .
3. Click Product support , enter the Service Tag of your computer, and then click Search .
NOTE: If you do not have the Service Tag, use the product ID or manually browse for your computer model.
4. Click Drivers & downloads > Find drivers .
5. Select the Windows operating system installed on your computer to get a list of the drivers and applications available on your
computer.
6
Reinstalling drivers and applications 9
Reinstallation sequence for drivers and
applications
Driver installation is critical after reinstalling the Windows operating system on your Dell computer. Install the drivers in the
correct sequence for your computer to function correctly. In some scenarios, you may have to reinstall or update the device
driver if you are encountering issues with a specific device.
For more information, see the Dell knowledge-base article SLN148687 at www.dell.com/support .
NOTE: The Windows 10 operating system includes touchpad drivers; no other touchpad-driver installation is required.
NOTE: The Windows 10 operating system includes the webcam drivers; no additional webcam-driver installation is required.
For video capture or streaming, users can install webcam software available from third-party providers.
Dell recommends installing drivers or applications in the following sequence.
Intel chipset device software
The Windows operating system may not include the updated Intel chipset device software for Dell computers. The Intel chipset
device software is available on Dell’s support site www.dell.com/support .
Downloading and installing the chipset driver
1. Turn on your computer.
2. Go to www.dell.com/support .
3. Click Product support , enter the Service Tag of your computer, and then click Search .
NOTE: If you do not have the Service Tag, use the product ID or manually browse for your computer model.
4. Click Drivers & downloads > Find drivers .
5. Scroll down the page and expand Chipset .
6. Click Download to download the chipset driver for your computer.
7. After the download is complete, navigate to the folder where you saved the chipset driver file.
8. Double-click the chipset driver file icon and follow the instructions on the screen.
Critical Microsoft Quick Fix Engineering (QFE)
updates
Dell recommends installing all the latest available QFE updates from the latest Windows Service Pack. Service packs are
automatically downloaded and installed when Windows Updates are enabled and can also be manually-downloaded and installed
from the Microsoft support site.
Intel Rapid Storage Technology (IRST)
The IRST software package enables and enhances high-performance Serial ATA (SATA) and SATA RAID capabilities for
supported operating systems. The IRST software package provides an added protection against data loss in the event of a
hard-drive failure.
7
10 Reinstallation sequence for drivers and applications
NOTE: The following conditions must be met before you can install IRST on your computer.
● Your computer has a RAID I/O controller hub (ICH). If your computer does not have a RAID ICH, you cannot install IRST
unless a third-party RAID controller card is installed.
● Your RAID controller is enabled by default.
CAUTION: If a SATA hard drive is already installed, enabling the RAID controller might cause your
computer to display a blue screen and an error code followed by a system reboot. To enable RAID,
reinstall the operating system.
Downloading and installing the IRST driver
1. Turn on your computer.
2. Go to www.dell.com/support .
3. Click Product support , enter the Service Tag of your computer, and then click Search .
NOTE: If you do not have the Service Tag, use the product ID or manually browse for your computer model.
4. Click Drivers & downloads > Find drivers .
5. Scroll down the page and expand Serial ATA .
6. Click Download to download the IRST driver for your computer.
7. After the download is complete, navigate to the folder where you saved the IRST driver file.
8. Double-click the driver file icon and follow the instructions on the screen.
Graphics
The Windows operating system includes the VGA-graphics driver only. For optimal-graphics performance, install the Dellgraphics driver applicable to your computer from www.dell.com/support .
Downloading and installing the Dell graphics driver
1. Turn on your computer.
2. Go to www.dell.com/support .
3. Click Product support , enter the Service Tag of your computer, and then click Search .
NOTE: If you do not have the Service Tag, use the product ID or manually browse for your computer model.
4. Click Drivers & downloads > Find drivers .
5. Scroll down the page and expand Video .
6. Click Download to download the graphics driver for your computer.
7. After the download is complete, navigate to the folder where you saved the graphics driver file.
8. Double-click the graphics driver file icon and follow the instructions on the screen.
Audio
The Windows operating system does not include the audio driver recommended by Dell. Install the HD audio driver available for
download from www.dell.com/support .
Downloading and installing the Dell audio driver
1. Turn on your computer.
2. Go to www.dell.com/support .
3. Click Product support , enter the Service Tag of your computer, and then click Search .
Reinstallation sequence for drivers and applications 11
NOTE: If you do not have the Service Tag, use the product ID or manually browse for your computer model.
4. Click Drivers & downloads > Find drivers .
5. Scroll down the page and expand Audio .
6. Click Download to download the audio driver for your computer.
7. After the download is complete, navigate to the folder where you saved the audio driver file.
8. Double-click the audio driver file icon and follow the instructions on the screen.
Dell ControlVault3 Driver Firmware
Dell ControlVault3 contains software that protects data in your computer from disclosure or modification. The software package
is available on Dell's support site www.dell.com/support .
Downloading and installing the Dell ControlVault3 driver and
firmware
1. Turn on your computer.
2. Go to www.dell.com/support .
3. Click Product support , enter the Service Tag of your computer, and then click Search .
NOTE: If you do not have the Service Tag, use the product ID or manually browse for your computer model.
4. Click Drivers & downloads > Find drivers .
5. Scroll down the page and select Security in the category.
6. Click Download to download the software package for your computer.
7. After the download is complete, navigate to the folder where you saved the Dell ControlVault3 driver and firmware.
8. Double-click the Dell ControlVault3 driver file icon and follow the instructions on the screen.
IR Camera Driver
IR Camera driver enables all the advanced camera features in your computer. The software package is available on the
www.dell.com/support .
Downloading and installing the IR camera driver
1. Turn on your computer.
2. Go to www.dell.com/support .
3. Click Product support , enter the Service Tag of your computer, and then click Submit .
NOTE: If you do not have the Service Tag, use the auto-detect feature or manually browse for your computer model.
4. Click Drivers & downloads > Find it myself .
5. Scroll down the page and expand Mouse, keyboard & Input Devices .
6. Click Download to download the audio driver for your computer.
7. After the download is complete, navigate to the folder where you saved the IR camera driver file.
8. Double-click the audio driver file icon and follow the instructions on the screen.
Dell Power Manager Service
Dell Power Manager (DPM) service is a Dell-developed application that provides simplified and efficient power management
capabilities for Dell computers. Following are the key features of DPM:
12 Reinstallation sequence for drivers and applications
● Battery information —Provides battery health information, adjust battery settings or create a custom-battery setting.
● Advanced charge mode —Allows you to control battery charging to prolong battery life.
● Peak shift —Allows you to reduce power consumption by automatically switching the computer to battery power during
certain times of the day, even when the computer is plugged into a direct power source.
● Thermal management —Allows you to control processor and cooling fan settings to manage performance, system surface
temperature, and fan noise.
● Battery extender —Conserves battery charge by affecting CPU power level, screen brightness and keyboard illumination
levels, and by muting audio.
● Alerts management —Enable or disable adapter, battery, docking station, thermal, and other types of alerts.
● Group policies —You can easily apply default settings and/or prevent users from changing power alerts system events,
power management, thermal management, battery extender, and battery settings.
● Product feedback —You can provide feedback about the software.
Downloading and installing the DPM
1. Turn on your computer.
2. Go to www.dell.com/support .
3. Click Product support , enter the Service Tag of your computer, and then click Search .
NOTE: If you do not have the Service Tag, use the product ID or manually browse for your computer model.
4. Click Drivers & downloads > Find drivers .
5. Scroll down the page and select System Management in the category.
6. Click Download to download the DPM application for your computer.
7. After the download is complete, navigate the folder where you saved the DPM file.
8. Double-click the DPM file icon and follow the instructions on the screen.
Wireless Local Network (WLAN) drivers and
applications
The Windows 10 operating system does not provide native-device driver support for WLAN controllers on Dell computers. To
obtain wireless network functionality, install the relevant WLAN drivers from the Dell support site. WLAN applications, which
provide additional features including enterprise authentication enhancements, can also be installed from the Dell support site.
Downloading and installing the Wi-Fi driver
1. Turn on the computer.
2. Go to www.dell.com/support .
3. Click Product support , enter the Service Tag of your computer, and then click Search .
NOTE: If you do not have the Service Tag, use the auto-detect feature or manually browse for your computer model.
4. Click Drivers & downloads > Find drivers .
5. Scroll down the page and expand Network .
6. Click Download to download the Wi-Fi driver for your computer.
7. After the download is complete, navigate to the folder where you saved the Wi-Fi driver file.
8. Double-click the Wi-Fi driver file icon and follow the instructions on the screen.
Dell Docking Station WD19/WD19DC
The Dell Docking Station WD19/WD19DC is a device that links all your electronic devices to your computer using a Thunderbolt
3 (Type-C) cable interface. Connecting the computer to the docking station enables you to access to all peripherals such as
Reinstallation sequence for drivers and applications 13
mouse, keyboard, stereo speakers, external hard drive, and large-screen displays, without having to plug each device directly to
the computer.
CAUTION: You must update your computer’s BIOS and the Dell Docking Station drivers to the latest versions
available on Dell support site before using the docking station. Older BIOS versions and drivers could result in
the docking station not being recognized by your computer or not functioning optimally.
For more information about the drivers required for the Dell Docking Station WD19/WD19DC , see www.dell.com/support .
Dell Thunderbolt Dock WD19TB
The Dell Thunderbolt Dock WD19TB is a device that links all your electronic devices to your computer using a Thunderbolt 3
(Type-C) cable interface. Connecting the computer to the docking station enables you to access to all peripherals such (mouse,
keyboard, stereo speakers, external hard drive, and large-screen displays) without having to plug each device into the computer.
CAUTION: You must update your computer’s BIOS and the Dell Docking Station drivers to the latest versions
available on Dell support site before using the docking station. Older BIOS versions and drivers could result in
the docking station not being recognized by your computer or not functioning optimally.
For more information about the drivers required for the Dell Thunderbolt Dock WD19TB, see www.dell.com/support .
14 Reinstallation sequence for drivers and applications
.NET Framework
The .NET Framework is a software framework from Microsoft, which is bundled with Windows operating systems. The .NET
Framework is intended to be used by applications created for the Windows 10 platform.
8
.NET Framework 15
Getting help and contacting Dell
Self-help resources
You can get information and help on Dell products and services using these self-help resources:
Table 1. Self-help resources 
Self-help resources Resource location
Information about Dell products and services www.dell.com
My Dell app
Tips
Contact Support In Windows search, type Contact Support , and press
Enter.
Online help for operating system www.dell.com/support/windows
Access top solutions, diagnostics, drivers and downloads, and
learn more about your computer through videos, manuals and
documents.
Your Dell computer is uniquely identified by a Service Tag or
Express Service Code. To view relevant support resources for
your Dell computer, enter the Service Tag or Express Service
Code at www.dell.com/support .
For more information on how to find the Service Tag for your
computer, see Locate the Service Tag on your computer .
Dell knowledge base articles for a variety of computer
concerns
1. Go to www.dell.com/support .
2. On the menu bar at the top of the Support page, select
Support > Knowledge Base .
3. In the Search field on the Knowledge Base page, type the
keyword, topic, or model number, and then click or tap the
search icon to view the related articles.
Contacting Dell
To contact Dell for sales, technical support, or customer service issues, see www.dell.com/contactdell .
NOTE: Availability varies by country/region and product, and some services may not be available in your country/region.
NOTE: If you do not have an active Internet connection, you can find contact information about your purchase invoice,
packing slip, bill, or Dell product catalog.
9
16 Getting help and contacting Dell

## Latitude 5521 Setup and Specifications

_Latitude 5521 Setup and Specifications, pages 1–2_

Latitude 5521
Setup and Specifications
Regulatory Model: P104F
Regulatory Type: P104F003/P104F004
August 2021
Rev. A01
Notes, cautions, and warnings
NOTE: A NOTE indicates important information that helps you make better use of your product.
CAUTION: A CAUTION indicates either potential damage to hardware or loss of data and tells you how to avoid
the problem.
WARNING: A WARNING indicates a potential for property damage, personal injury, or death.
© 2021 Dell Inc. or its subsidiaries. All rights reserved. Dell, EMC, and other trademarks are trademarks of Dell Inc. or its subsidiaries. Other
trademarks may be trademarks of their respective owners.

## Set up your Latitude 5521

_Latitude 5521 Setup and Specifications, pages 5–6_

Set up your Latitude 5521
NOTE: The images in this document may differ from your computer depending on the configuration you ordered.
1. Connect the power adapter and press the power button.
NOTE: To conserve battery power, the battery might enter power saving mode. Connect the power adapter and press
the power button to turn on the computer.
2. Finish operating system setup.
For Ubuntu:
Follow the on-screen instructions to complete the setup. For more information about installing and configuring Ubuntu, see
the knowledge base articles SLN151664 and SLN151748 at www.dell.com/support .
For Windows:
Follow the on-screen instructions to complete the setup. When setting up, Dell recommends that you:
● Connect to a network for Windows updates.
NOTE: If connecting to a secured wireless network, enter the password for the wireless network access when
prompted.
● If connected to the internet, sign-in with or create a Microsoft account. If not connected to the internet, create an
offline account.
● On the Support and Protection screen, enter your contact details.
3. Locate and use Dell apps from the Windows Start menu—Recommended.
Table 1. Locate Dell apps 
Resources Description
Dell Product Registration
Register your computer with Dell.
1
Set up your Latitude 5521 5
Table 1. Locate Dell apps (continued)
Resources Description
Dell Help & Support
Access help and support for your computer.
SupportAssist
SupportAssist is the smart technology that keeps your computer running at its best by optimizing
settings, detecting issues, removing viruses and notifies when you need to make system
updates. SupportAssist proactively checks the health of your system's hardware and software.
When an issue is detected, the necessary system state information is sent to Dell to begin
troubleshooting. SupportAssist is preinstalled on most of the Dell devices running Windows
operating system. For more information, see SupportAssist for Home PCs User's Guide on
www.dell.com/serviceabilitytools .
NOTE: In SupportAssist, click the warranty expiry date to renew or upgrade your warranty.
Dell Update
Updates your computer with critical fixes and latest device drivers as they become available.
For more information about using Dell Update, see the knowledge base article SLN305843 at
www.dell.com/support .
Dell Digital Delivery
Download software applications, which are purchased but not pre-installed on your computer.
For more information about using Dell Digital Delivery, see the knowledge base article 153764 at
www.dell.com/support .
6 Set up your Latitude 5521

## Views of Latitude 5521

_Latitude 5521 Setup and Specifications, pages 7–11_

Views of Latitude 5521
Topics:
• Right view
• Left
• Display
• Bottom view
• Palmrest
• Battery charge and status LED
Right view
1. microSD card reader
2. Universal audio port
3. USB 3.2 Gen 1 port
4. USB 3.2 Gen 1 port with PowerShare
5. HDMI 2.0 port
6. RJ-45 Ethernet port
7. Wedge-shaped lock slot
2
Views of Latitude 5521 7
Left
1. USB4.0 Type-C port with DisplayPort 2.0 port/Power Delivery/Thunderbolt
2. USB4.0 Type-C port with DisplayPort 2.0 port/Power Delivery/Thunderbolt
3. Fan vents
4. Smart card reader (optional)
8 Views of Latitude 5521
Display
1. Proximity sensor (optional)
2. Microphone
3. IR LED (optional)
4. RGB camera/ RGB IR camera (optional)
5. Camera indicator LED (optional)
6. Microphone
7. LCD panel
8. LED activity light
Views of Latitude 5521 9
Bottom view
1. Speakers
2. Service tag label
3. Fan vents
10 Views of Latitude 5521
Palmrest
1. Camera shutter
2. Power button with fingerprint reader (optional)
3. Keyboard
4. Contactless smart card reader (Optional)
5. Clickpad
Battery charge and status LED
Table 2. Battery charge and status LED Indicator 
Power Source LED Behavior computer Power State Battery Charge Level
AC Adapter Off S0 - S5 Fully Charged
AC Adapter Solid White S0 - S5 < Fully Charged
Battery Off S0 - S5 11-100%
Battery Solid Amber (590+/-3 nm) S0 - S5 < 10%
● S0 (ON) - Computer is turned on.
● S4 (Hibernate) - The computer consumes the least power compared to all other sleep states. The computer is almost at an
OFF state, expect for a trickle power. The context data is written to hard drive.
● S5 (OFF) - The computer is in a shutdown state.
Views of Latitude 5521 11

## Specifications of Latitude 5521

_Latitude 5521 Setup and Specifications, pages 12–27_

Specifications of Latitude 5521
Topics:
• Dimensions and weight
• Processor
• Chipset
• Operating system
• Memory
• External ports
• Internal slots
• Wireless module
• WWAN module
• Audio
• Storage
• Intel Optane memory
• Media-card reader
• Keyboard
• Clickpad
• Camera
• Power adapter
• Battery
• Display
• Fingerprint reader (optional)
• GPU—Integrated
• GPU—Discrete
• Sensor and control specifications
• Security options—Contacted smartcard reader
• Security options—Contactless smartcard reader
• Security
• Security Software
• Computer environment
Dimensions and weight
The following table lists the height, width, depth, and weight of your Latitude 5521.
Table 3. Dimensions and weight 
Description Values
Height:
Front height 22.67 mm (0.89 in.)
Rear height 24.05 mm (0.95 in.)
Width 357.80 mm (14.09 in.)
Depth 233.30 mm (9.19 in.)
Weight (minimum) 1.79 kg (3.95 lb)
3
12 Specifications of Latitude 5521
Table 3. Dimensions and weight (continued)
Description Values
NOTE: The weight of your computer depends on the
configuration ordered and manufacturing variability.
Processor
The following table lists the details of the processors supported by your Latitude 5521.
Table 4. Processor 
Description Option one Option two Option three
Processor type 11th Generation Intel Core
i5-11400H
11th Generation Intel Core
i5-11500H
11th Generation Intel Core
i7-11850H
Processor wattage 45 W 45 W 45 W
Processor core count 6 6 8
Processor thread count 12 12 16
Processor speed 2.70 GHz to 4.50 GHz 2.90 GHz to 4.60 GHz 2.50 GHz to 4.80 GHz
Processor cache 12 MB 12 MB 24 MB
Integrated graphics Intel UHD Graphics Intel UHD Graphics Intel UHD Graphics
Chipset
The following table lists the details of the chipset supported by your Latitude 5521.
Table 5. Chipset 
Description Values
Chipset Intel WM590
Processor 11th Generation Intel Core i5/i7
DRAM bus width Two channels, 64-bit
Flash EPROM 32 MB
PCIe bus Up to Gen 3.0
Operating system
Your Latitude 5521 supports the following operating systems:
● Windows 11 Home, 64-bit
● Windows 11 Pro, 64-bit
● Windows 11 Pro National Academic, 64-bit
● Windows 10 Home, 64-bit
● Windows 10 Pro, 64-bit
● Ubuntu 20.04 LTS, 64-bit
Specifications of Latitude 5521 13
Memory
The following table lists the memory specifications of your Latitude 5521.
Table 6. Memory specifications 
Description Values
Memory slots Dual-channel
Memory type DDR4
Memory speed 3200 MHz
Maximum memory configuration 64 GB
Minimum memory configuration 8 GB
Memory size per slot 8 GB, 16 GB, 32 GB
Memory configurations supported ● 8 GB, 1 x 8 GB, DDR4, 3200 MHz
● 16 GB, 1 x 16 GB, DDR4, 3200 MHz
● 16 GB, 2 x 8 GB, DDR4, 3200 MHz
● 32 GB, 1 x 32 GB, DDR4, 3200 MHz
● 32 GB, 2 x 16 GB, DDR4, 3200 MHz
● 64 GB, 2 x 32 GB, DDR4, 3200 MHz
External ports
The following table lists the external ports of your Latitude 5521.
Table 7. External ports 
Description Values
Network port One RJ-45 port
USB ports ● One USB 3.2 Gen 1 (Type-A) port
● One USB 3.2 Gen 1 (Type-A) port with PowerShare
● Two USB4 Type-C® port with Power Delivery/
DisplayPort/Thunderbolt™4
Audio port One Universal Audio Jack
Video port One HDMI 2.0 port
Media-card reader One microSD card slot
Power-adapter port DC-in USB Type-C
Security-cable slot One Wedge-shaped lock slot
14 Specifications of Latitude 5521
Internal slots
The following table lists the internal slots of your Latitude 5521.
Table 8. Internal slots 
Description Values
M.2 ● Two M.2 2230 slots for solid-state drive 128 GB/256
GB/512 GB
● Two M.2 2280 slots for solid-state drive 256 GB/512 GB/1
TB/2 TB
● Two M.2 2280 slots for Self-Encrypting solid-state drive
256 GB/512 GB
● One M.2 2280 slots for 32 GB Intel® Optane™ Memory +
512 GB QLC 3D NAND
NOTE: Intel® Optane™ Memory requires Gen 3
storage through Platform Controller Hub
● One SATA slot for 7 mm HDD 500 GB/1 TB/2 TB
NOTE: To learn more about the features of different
types of M.2 cards, see the knowledge base article
000144170 at www.dell.com/support .
Wireless module
The following table lists the Wireless Local Area Network (WLAN) module specifications of your Latitude 5521.
Table 9. Wireless module specifications 
Description Option one Option two Option three
Model number Qualcomm QCA61x4A Intel AX201 Intel AX210
Transfer rate Up to 867 Mbps Up to 2400 Mbps Up to 2400 Mbps
Frequency bands supported 2.4 GHz/5 GHz 2.4 GHz/5 GHz 2.4 GHz/5 GHz/6 GHz
Wireless standards ● Wi-Fi 802.11a/b/g
● WiFi 802.11n
● WiFi 802.11ac
● Wi-Fi 802.11a/b/g
● Wi-Fi 4 (WiFi 802.11n)
● Wi-Fi 5 (WiFi 802.11ac)
● Wi-Fi 6 (WiFi 802.11ax)
● Wi-Fi 802.11a/b/g
● Wi-Fi 4 (WiFi 802.11n)
● Wi-Fi 5 (WiFi 802.11ac)
● Wi-Fi 6E (WiFi 802.11ax)
Encryption ● 64-bit and 128-bit WEP
● 128-bit AES-CCMP
● TKIP
● 64-bit and 128-bit WEP
● 128-bit AES-CCMP
● TKIP
● 64-bit and 128-bit WEP
● 128-bit AES-CCMP
● TKIP
Bluetooth 5.0 5.2 5.2
Specifications of Latitude 5521 15
WWAN module
The following table lists the Wireless Wide Area Network (WWAN) module supported on your Latitude 5521.
Table 10. WWAN module specifications 
Description Values
Model number Intel 7360 (DW5820e)
Transfer rate Up to 450 Mbps DL/50 Mbps UL (Cat 9)
Frequency bands supported (1, 2, 3, 4, 5, 7, 8, 11, 12, 13, 17, 18, 19, 20, 21, 26, 28, 29, 30,
38, 39, 40, 41, 66), HSPA+ (1, 2, 4, 5, 8)
Wireless standards ● LTE Category 16
● UMTS/HSPA+
Encryption Not supported
Global Navigation Satellite System (GNSS) Supports GPS, BDS, and GLONASS
NOTE: For instructions on how to find your computer's IMEI (International Mobile Station Equipment Identity) number,
see the knowledge base article 000143678 at www.dell.com/support .
Audio
The following table lists the audio specifications of your Latitude 5521.
Table 11. Audio specifications 
Description Values
Audio controller Realtek ALC3204 with Waves MaxxAudio Pro
Stereo conversion 24-bit DAC (Digital-to-Analog) and ADC (Analog-to-Digital)
Internal audio interface Intel HDA (high-definition audio)
External audio interface Universal audio jack
Number of speakers 2
Internal-speaker amplifier Supported (audio codec integrated)
External volume controls Keyboard shortcut controls
Speaker output:
Average speaker output 2 W
Peak speaker output 2.5 W
Subwoofer output Not supported
Microphone Dual-array microphones
16 Specifications of Latitude 5521
Storage
This section lists the storage options on your Latitude 5521.
Your computer supports one of the following configurations:
● One 2.5-inch hard drive
● Two M.2 2230/2280 solid state drive
The primary drive of your computer varies with the storage configuration. For computers:
● with a M.2 drive, the M.2 drive is the primary drive
● without a M.2 drive, the 2.5-inch hard drive is the primary drive
Table 12. Storage specifications 
Storage type Interface type Capacity
2.5-inch 5400 rpm SATA hard-disk drive SATA up to 6 Gbps up to 2 TB
2.5-inch 7200 rpm SATA hard-disk drive SATA up to 6 Gbps up to 1 TB
2.5-inch 7200 rpm SED SATA hard-disk
drive
SATA AHCI, up to 6 Gbps 500 GB
M.2 2230 solid-state drive PCIe NVMe PCIe Gen3x4 NVMe, up to 32 Gbps up to 512 GB
M.2 2280 solid-state drive PCIe NVMe PCIe Gen3x4/Gen4x4 NVMe, up to 32
Gbps
up to 2 TB
M.2 2280 Opal Self Encrypting solidstate drive PCIe NVMe
PCIe Gen3x4 NVMe, up to 32 Gbps 1 TB
Intel Optane memory
Intel Optane memory functions only as a storage accelerator. It neither replaces nor adds to the memory (RAM) installed on
your computer.
NOTE: Intel Optane memory is supported on computers that meet the following requirements:
● 7th Generation or higher Intel Core i3/i5/i7 processor
● Windows 10 64-bit version or higher
● Latest version of Intel Rapid Storage Technology driver
Table 13. Intel Optane memory 
Description Values
Type Memory/Storage/Storage accelerator
Interface PCIe Gen3.0x4
Connector M.2 2280
Configurations supported 32 GB, 512 GB
Capacity Up to 512 GB
Specifications of Latitude 5521 17
Media-card reader
The following table lists the media cards supported by your Latitude 5521.
Table 14. Media-card reader specifications 
Description Values
Media-card type microSD card slot
Media-cards supported ● Micro Secure Digital (mSD)
● Micro Secure Digital High Capacity (mSDHC)
● Micro Secure Digital Extended Capacity (mSDXC)
NOTE: The maximum capacity supported by the media-card reader varies depending on the standard of the media card
installed in your computer.
Keyboard
The following table lists the keyboard specifications of your Latitude 5521.
Table 15. Keyboard specifications 
Description Values
Keyboard type ● Standard keyboard
● RGB backlit keyboard
Keyboard layout QWERTY
Number of keys ● United States and Canada: 102 keys
● United Kingdom: 103 keys
● Japan: 106 keys
Keyboard size X=18.6 mm key pitch
Y=19.05 mm key pitch
Keyboard shortcuts Some keys on your keyboard have two symbols on them.
These keys can be used to type alternate characters or to
perform secondary functions. To type the alternate character,
press Shift and the desired key. To perform secondary
functions, press Fn and the desired key.
NOTE: You can define the primary behavior of the
function keys (F1–F12) changing Function Key Behavior
in BIOS setup program.
Keyboard shortcuts
Clickpad
The following table lists the Clickpad specifications of your Latitude 5521.
Table 16. Clickpad specifications 
Description Values
Clickpad resolution: >300 dpi
18 Specifications of Latitude 5521
Table 16. Clickpad specifications (continued)
Description Values
Clickpad dimensions:
Horizontal 115 mm (4.53 in.)
Vertical 67 mm (2.64 in.)
Clickpad gestures For more information about Clickpad gestures available on
Windows, see the Microsoft knowledge base article 4027871
at support.microsoft.com .
Camera
The following table lists the camera specifications of your Latitude 5521.
Table 17. Camera specifications 
Description Option 1 Option 2 Option 3
Number of cameras One One One
Camera type ● RGB HD camera HD RGB + Ir
camera
FHD RGB + Ir camera, proximity
sensor/express sign-in
Camera location Front camera Front camera Front camera
Camera sensor type CMOS sensor technology CMOS sensor
technology
CMOS sensor technology
Camera resolution:
Still image 5 megapixel 0.92 megapixel 2.07 megapixels
Video 1280 x 720 (VGA/HD) at 30 fps 1280 x 720 (HD) at
30 fps
1920 x 1080 (FHD) at 30 fps
Infrared camera
resolution:
Still image N/A 0.23 0.23
Video N/A 640 x 360 at 15 fps 640 x 360 at 15 fps
Diagonal viewing
angle:
Camera 78.6 degrees 87 degrees 87.60 degrees
Infrared camera 87 degrees 87 degrees 87.60 degrees
Power adapter
The following table lists the power adapter specifications of your Latitude 5521.
Table 18. Power adapter specifications 
Description Option one Option two
Type 90 W AC adapter, USB-C 130 W AC adapter, USB-C
Specifications of Latitude 5521 19
Table 18. Power adapter specifications (continued)
Description Option one Option two
NOTE: 90 W is supported only in
UMA configuration.
Input voltage 100 VAC x 240 VAC 100 VAC x 240 VAC
Input frequency 50 Hz x 60 Hz 50 Hz x 60 Hz
Input current (maximum) 1.50 A 1.80 A
Output current (continuous) ● 20 V/4.50 A
● 15 V/3 A
● 9 V/3 A
● 5 V/ 3 A
● 20 V/6.50 A
● 5 V/1 A
Rated output voltage 20 VDC/15 VDC/9 VDC/5 VDC 20 VDC/5 VDC
Weight 0.64 lbs (0.29 kg) 0.77 lbs (0.35 kg)
Dimensions (inches) 0.87 x 2.60 x 5.12 0.87 x 2.60 x 5.63
Dimensions (mm) 22 x 66 x 130 22 x 66 x 143
Temperature range:
Operating 0°C to 40°C (32°F to 104°F) 0°C to 40°C (32°F to 104°F)
Storage -40°C to 70°C (-40°F to 158°F) -40°C to 70°C (-40°F to 158°F)
CAUTION: Operating and storage temperature ranges may differ among
components, so operating or storing the device outside these ranges may
impact the performance of specific components.
Battery
The following table lists the battery specifications of your Latitude 5521.
Table 19. Battery specifications 
Description Option one Option two Option three
Battery type 4-cell 64 WHr, Polymer, Long Cycle Life,
ExpressCharge capable
4-cell 64 WHr,
Polymer, nonLong Cycle Life,
ExpressCharge
capable
6 Cell 97
WHr ExpressCharge
capable
Battery voltage 15.20 V 15.20 V 11.40 VDC
Battery weight (maximum) 0.283 kg (0.62 lb) 0.283 kg (0.62
lb)
0.429 kg (0.95 lb)
Battery dimensions:
Height 7.60 mm 7.60 mm 7.70 mm (0.30 in.)
Width 226.60 mm 226.60 mm 332 mm (13.1 in.)
Depth 81.40 mm 81.40 mm 82.00 mm (3.22 in.)
20 Specifications of Latitude 5521
Table 19. Battery specifications (continued)
Description Option one Option two Option three
Temperature range:
Operating ● Charge: 0 °C to 45 °C, 32 °F to 113 °F
● Discharge: 0 °C to 70 °C, 32 °F to 158 °F
● Charge: 0
°C to 45 °C,
32 °F to 113
°F
● Discharge: 0
°C to 70 °C,
32 °F to 158
°F
0°C to 50°C (32°F
to 122°F)
Storage -20°C (-4°F ) to 65°C (149°F) -20°C (-4°F )
to 65°C
(149°F)
-20°C to 60°C
(-4°F to 140°F)
Battery operating time Varies depending on operating conditions and can
significantly reduce under certain power-intensive
conditions.
Varies
depending on
operating
conditions and
can significantly
reduce under
certain powerintensive
conditions.
Varies depending
on operating
conditions and can
significantly reduce
under certain powerintensive conditions.
Battery charging time
(approximate)
4Hrs hours (when the computer is off)
NOTE: Control the charging time, duration,
start and end time, and so on using the
Dell Power Manager application. For more
information on the Dell Power Manager see,
Me and My Dell on www.dell.com/
4Hrs hours
(when the
computer is off)
NOTE:
Control the
charging
time,
duration,
start and
end time,
and so on
using the
Dell Power
Manager
application.
For more
information
on the Dell
Power
Manager
see, Me and
My Dell on
www.dell.co
m/
4 Hrs hours (when
the computer is off)
NOTE: Control
the charging
time, duration,
start and end
time, and so on
using the Dell
Power Manager
application. For
more information
on the Dell
Power Manager
see, Me and My
Dell on
www.dell.com/
Approximate life span
(discharge/charge cycles)
● 3 years warranty ● 1 year
warranty
● 1 year warranty
Coin-cell battery CR2032 CR2032 CR2032
Specifications of Latitude 5521 21
Display
The following table lists the display specifications of your Latitude 5521.
Table 20. Display specifications 
Description Option one Option two Option three Option four Option five
Display type High Definition (HD) Full High Definition
(FHD)
Full High Definition
(FHD) Touch
Full High
Definition (FHD),
Super Low
Power (SLP),
Low Blue Light
Ultra High
Definition (UHD),
Super Low
Power (SLP),
Low Blue Light
Display-panel
technology
Twisted Nematic
(TN)
Wide Viewing Angle
(WVA)
Wide Viewing Angle
(WVA)
Wide Viewing
Angle (WVA)
Wide-Viewing
Angle ( WVA)
Display-panel
dimensions (active
area):
Height 193.60 mm (7.62 in.) 193.60 mm (7.62 in.) 193.60 mm (7.62
in.)
193.60 mm (7.62
in.)
193.60 mm (7.62
in.)
Width 344.20 mm (13.55
in.)
344.20 mm (13.55
in.)
344.20 mm (13.55
in.)
344.20 mm
(13.55 in.)
344.20 mm
(13.55 in.)
Diagonal 394.91 mm (15.55
in.)
394.91 mm (15.55
in.)
394.91 mm (15.55
in.)
394.91 mm
(15.55 in.)
394.91 mm
(15.55 in.)
Display-panel native
resolution
1366x768 1920 x 1080 1920 x 1080 1920 x 1080 3840 x 2160
Luminance (typical) 220 nits 250 nits 250 nits 400 nits 400 nits
Megapixels 1049088 2073600 2073600 2073600 8.3
Color gamut NTSC 45% NTSC 45% NTSC 45% sRGB 100% sRGB 100%
Pixels Per Inch
(PPI)
100 141 141 141 140
Contrast ratio (typ) 500:1 700:1 700:1 700:1 800:1
Response time
(min)
25 ms 25 ms 35 ms 35 ms 35 ms
Refresh rate 60 Hz 60 Hz 60 Hz 60 Hz 60 Hz
Horizontal view
angle
40/40 +/- degrees 80/80 +/- degrees 80/80 +/- degrees 80/80 +/-
degrees
80 minimum
Vertical view angle 10(U)/30(D) +/-
degrees
80(U)/80(D) +/-
degrees
80(U)/80(D) +/-
degrees
80(U)/80(D) +/-
degrees
80 minimum
Pixel pitch 0.252X0.252 mm 0.179X0.179 mm 0.179X0.179 mm 0.179X0.179 mm 0.161 x 0.161
Power consumption
(maximum)
4.20 W 4.2 W 4.2 W 4.6 W 3.50 W
Anti-glare vs glossy
finish
Anti-glare Anti-glare Anti-glare Anti-glare Anti-glare
Touch options No No Yes No No
22 Specifications of Latitude 5521
Fingerprint reader (optional)
The following table lists the specifications of the optional fingerprint-reader of your Latitude 5521.
Table 21. Fingerprint reader specifications 
Description Values
Fingerprint-reader sensor technology Capacitive
Fingerprint-reader sensor resolution 508 dpi
Fingerprint-reader sensor pixel size 256 x 360
GPU—Integrated
The following table lists the specifications of the integrated Graphics Processing Unit (GPU) supported by your Latitude 5521.
Table 22. GPU—Integrated 
Controller External display support Memory size Processor
Intel UHD Graphics HDMI 2.0 port/ USB Type-C
with DisplayPort 2.0 port
Shared system memory 11th Generation Intel core
i5/i7
GPU—Discrete
The following table lists the specifications of the discrete Graphics Processing Unit (GPU) supported by your Latitude 5521.
Table 23. GPU—Discrete 
Controller External display support Memory size Memory type
NVIDIA GeForce MX450 HDMI 2.0 port/ USB Type-C
with DisplayPort 2.0 port
2 GB GDDR6
Sensor and control specifications
Table 24. Sensor and control specifications 
Specifications
1. Accelerometer: One on the system board 
2. Accelerometer with Gyro: On the hinge-up (optional)
3. GPS (via WWAN Card only) (optional)
4. Proximity sensor (optional)
Security options—Contacted smartcard reader
Table 25. Contacted smartcard reader 
Title Description Dell ControlVault 3 Smartcard reader
ISO 7816 -3 Class A Card Support Reader capable of reading 5V powered
smartcard
Yes
Specifications of Latitude 5521 23
Table 25. Contacted smartcard reader (continued)
Title Description Dell ControlVault 3 Smartcard reader
ISO 7816 -3 Class B Card Support Reader capable of reading 3V powered
smartcard
Yes
ISO 7816 -3 Class C Card support Reader capable of reading 1.8V powered
smartcard
Yes
ISO 7816-1 Compliant Specification for the reader Yes
ISO 7816 -2 Compliant Specification for smartcard device
physical characteristics (size, location of
connection points, etc.)
Yes
T=0 support Cards support character level
transmission
Yes
T=1 support Cards support block level transmission Yes
EMVCo Compliant Compliant with EMVCo (for electronic
payment standards) smartcard
standards as posted to www.emvco.com
Yes
EMVCo Certified Formally certified based on EMVCO
smartcard standards
Yes
PC/SC OS interface Personal Computer/Smart Card
specification for integration of hardware
readers into personal computer
environments
Yes
CCID driver compliance Common driver support for Integrated
Circuit Card Interface Device for OS
level drivers.
Yes
Windows Certified Device certified by WHCK Yes
FIPS 201 (PIV/HSPD-12) Compliant via
GSA
Device compliant with FIPS 201/PIV/
HSPD-12 requirements
Yes
Security options—Contactless smartcard reader
Table 26. Contactless smartcard reader 
Title Description Dell ControlVault 3 Contactless
Smartcard reader with NFC
Felica Card Support Reader and software capable of
supporting Felica contactless cards
Yes
ISO 14443 Type A Card Support Reader and software capable of
supporting ISO 14443 Type A contactless
cards
Yes
ISO 14443 Type B Card Support Reader and software capable of
supporting ISO 14443 Type B contactless
cards
Yes
ISO/IEC 21481 Reader and software capable of
supporting ISO/IEC 21481 compliant
contactless cards and tokens
Yes
ISO/IEC 18092 Reader and software capable of
supporting ISO/IEC 21481 compliant
contactless cards and tokens
Yes
24 Specifications of Latitude 5521
Table 26. Contactless smartcard reader (continued)
Title Description Dell ControlVault 3 Contactless
Smartcard reader with NFC
ISO 15693 Card Support Reader and software capable of
supporting ISO15693 contactless cards
Yes
NFC Tag Support Supports reading and processing of NFC
compliant tag information
Yes
NFC Reader Mode Support for NFC Forum Defined Reader
mode
Yes
NFC Writer Mode Support for NFC Forum Defined Writer
mode
Yes
NFC Peer-to-Peer Mode Support for NFC Forum Defined Peer to
Peer mode
Yes
EMVCo Compliant Compliant with EMVCO smartcard
standards as posted to www.emvco.com
Yes
EMVCo Certified Formally certified based on EMVCO
smartcard standards
Yes
NFC Proximity OS Interface Enumerates NFP (Near Field Proximity)
device for OS to utilize
Yes
PC/SC OS interface Personal Computer/Smart Card
specification for integration of hardware
readers into personal computer
environments
Yes
CCID driver compliance Common driver support for Integrated
Circuit Card Interface Device for OS
level drivers
Yes
Windows Certified Device certified by Microsoft WHCK Yes
Dell ControlVault support Device connects to Dell ControlVault for
usage and processing
Yes
NOTE: 125 Khz proximity cards are not supported.
Table 27. Supported cards 
Manufacturer Card Supported
HID jCOP readertest3 A card (14443a) Yes
1430 1L
DESFire D8H
iClass (Legacy)
iClass SEOS
NXP/Mifare Mifare DESFire 8K White PVC Cards Yes
Mifare Classic 1K White PVC Cards
NXP Mifare Classic S50 ISO Card
G&D idOnDemand - SCE3.2 144K Yes
SCE6.0 FIPS 80K Dual+ 1 K Mifare
SCE6.0 nonFIPS 80K Dual+ 1 K Mifare
SCE6.0 FIPS 144K Dual + 1K Mifare
Specifications of Latitude 5521 25
Table 27. Supported cards (continued)
Manufacturer Card Supported
SCE6.0 nonFIPS 144K Dual + 1 K Mifare
SCE7.0 FIPS 144K
Oberthur idOnDemand - OCS5.2 80K Yes
ID-One Cosmo 64 RSA D V5.4 T=0 card
Security
Table 28. Security specifications 
Features Specifications
Trusted Platform Module (TPM) 2.0 Integrated on system board
Fingerprint reader Optional
Wedge-shaped lock slot Standard
Security Software
Table 29. Security Software specifications 
Specifications
Dell Client Command Suite
Optional Dell Data Security and Management Software
● Dell Client Command Suite
● Dell BIOS Verification
● Optional Dell Endpoint Security and Management Software
● VMware Carbon Black Endpoint Standard
● VMware Carbon Black Endpoint Standard + Secureworks Threat Detection and Response
● Dell Encryption Enterprise
● Dell Encryption Personal
● Carbonite
● VMware Workspace ONE
● Absolute Endpoint Visibility and Control
● Netskope
● Dell Supply Chain Defense
Computer environment
Airborne contaminant level: G1 as defined by ISA-S71.04-1985
Table 30. Computer environment 
Description Operating Storage
Temperature range 0°C to 35°C (32°F to 95°F) -40°C to 65°C (-40°F to 149°F)
Relative humidity (maximum) 10% to 80% (non-condensing) 0% to 95% (non-condensing)
Vibration (maximum) *
0.66 GRMS 1.30 GRMS
26 Specifications of Latitude 5521
Table 30. Computer environment (continued)
Description Operating Storage
Shock (maximum) 140 G † 160 G †
Altitude (maximum) 0 m to 3048 m (4.64 ft to 5518.4 ft) 0 m to 10668 m (4.64 ft to 19234.4 ft)
* Measured using a random vibration spectrum that simulates user environment.
† Measured using a 2 ms half-sine pulse when the hard drive is in use.
Specifications of Latitude 5521 27
