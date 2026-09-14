# Dell Latitude 5420

| | |
|---|---|
| Regulatory model | P137G |
| Troubleshooting depth | **full** |
| Documents | 2 |

- **Latitude 5420 Service Manual** — January 2025 Rev. A04
  - Source: https://dl.dell.com/topicspdf/latitude-5420-laptop_owners-manual2_en-us.pdf
  - Answers: Diagnostic LED codes, built-in self-test for display faults, SupportAssist, swollen battery handling, network power cycle, flea-power drain, OS recovery, BIOS setup, clearing a forgotten BIOS password
- **Latitude 5420 Setup and Specifications** — May 2023 Rev. A04
  - Source: https://dl.dell.com/topicspdf/latitude-5420-laptop_owners-manual_en-us.pdf
  - Answers: Views of the machine, ports and slots, display options, memory limits, battery capacity, keyboard, camera, power adapter

Extracted from the vendor document. Teardown chapters are omitted — they answer nothing a user asks. See `../SOURCES.md`.

## Software

_Latitude 5420 Service Manual, pages 86–86_

Software
This chapter details the supported operating systems along with instructions on how to install the drivers.
Topics:
• Operating system
• Downloading the drivers
Operating system
Your Latitude 5420 supports the following operating systems:
● Windows 10 Pro, 64-bit
● Windows 10 Home, 64-bit
● Windows 10 Pro Education, 64-bit
● Windows 10 Enterprise N, 64-bit
● Ubuntu Linux 20.04 LTS, 64-bit
Downloading the drivers
Steps
1. Turn on your computer.
2. Go to Dell Support Site .
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
4
86 Software

## BIOS Setup

_Latitude 5420 Service Manual, pages 87–101_

BIOS Setup
NOTE: Depending on the computer and the installed devices, the options that are listed in this section may or may not be 
displayed.
CAUTION: Certain changes can make your computer work incorrectly. Before you change the settings in BIOS 
Setup, it is recommended that you note down the original settings for future reference.
Use BIOS Setup for the following purposes:
● Get information about the hardware installed in your computer, such as the amount of RAM and the capacity of the storage 
device.
● Change the system configuration information.
● Set or change a user-selectable option, such as the user password, type of storage device installed, and enable or disable 
base devices.
Topics:
• BIOS overview
• Entering BIOS Setup
• Navigation keys
• F12 One Time Boot menu
• System setup options
• Updating the BIOS
• System and setup password
• Clearing system and setup passwords
BIOS overview
The BIOS manages data flow between the computer's operating system and attached devices such as hard disk, video adapter, 
keyboard, mouse, and printer.
Entering BIOS Setup
Steps
1. Turn on your computer.
2. Press F2 immediately to enter the BIOS Setup.
NOTE: If you wait too long and the operating system logo appears, continue to wait until you see the desktop. Then, 
turn off your computer and try again.
Navigation keys
NOTE: For most of the BIOS Setup options, changes that you make are recorded but do not take effect until you restart 
the computer.
Table 4. Navigation keys 
Keys Navigation
Up arrow Moves to the previous field.
5
BIOS Setup 87
Table 4. Navigation keys (continued)
Keys Navigation
Down arrow Moves to the next field.
Enter Selects a value in the selected field (if applicable) or follows 
the link in the field.
Spacebar Expands or collapses a drop-down list, if applicable.
Tab Moves to the next focus area.
Esc Moves to the previous page until you view the main screen. 
Pressing Esc in the main screen displays a message that 
prompts you to save any unsaved changes and restart the 
computer.
F12 One Time Boot menu
To enter the One Time Boot menu, turn on or restart your computer, and then press F12 immediately.
NOTE: If you are unable to enter the One Time Boot menu, repeat the above action.
The One Time Boot menu displays the devices that you can boot from and also display the options to start diagnostics. The boot 
menu options are:
● Removable Drive (if available)
● STXXXX Drive (if available)
NOTE: XXX denotes the SATA drive number.
● Optical Drive (if available)
● SATA Hard Drive (if available)
● Diagnostics
The One Time Boot menu screen also displays the option to access BIOS Setup.
System setup options
NOTE: Depending on your computer and its installed devices, the items listed in this section may or may not appear.
Table 5. System setup options—System information menu 
Overview
Latitude 5420
BIOS Version Displays the BIOS version number.
Service Tag Displays the Service Tag of the computer.
Asset Tag Displays the Asset Tag of the computer.
Manufacture Date Displays the manufacture date of the computer.
Ownership Date Displays the ownership date of the computer.
Express Service Code Displays the express service code of the computer.
Ownership Tag Displays the Ownership Tag of the computer.
Signed Firmware Update Displays whether the Signed Firmware Update is enabled on your computer.
Battery Information
Primary Displays that battery is primary.
Battery Level Displays the battery level of the computer.
88 BIOS Setup
Table 5. System setup options—System information menu (continued)
Overview
Battery State Displays the battery state of the computer.
Health Displays the battery health of the computer.
AC Adapter Displays whether the AC adapter is connected or not.
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
DIMM_SLOT B Displays the DIMM B memory size.
DIMM_SLOT A Displays the DIMM A memory size.
Devices Information
Panel Type Displays the Panel Type of the computer.
Video Controller Displays the video controller type of the computer.
Video Memory Displays the video memory information of the computer.
Wi-Fi Device Displays the wireless device information of the computer.
Native Resolution Displays the native resolution of the computer.
Video BIOS Version Displays the video BIOS version of the computer.
Audio Controller Displays the audio controller information of the computer.
Bluetooth Device Displays the Bluetooth device information of the computer.
LOM MAC Address Displays the LAN On Motherboard (LOM) MAC address of the computer.
Pass Through MAC Address Displays the pass through MAC address of the computer.
Cellular Device Displays the M.2 PCIe SSD information of the computer.
Table 6. System setup options—Boot Configuration menu 
Boot Configuration
Boot Sequence
Boot mode Displays the boot mode.
BIOS Setup 89
Table 6. System setup options—Boot Configuration menu (continued)
Boot Configuration
Boot Sequence Displays the boot sequence.
Secure Digital (SD) Card Boot Enable or disable the SD card read-only boot.
By default, the Secure Digital (SD) Card Boot option is not enabled.
Secure Boot
Enable Secure Boot Enable or disable the secure boot feature.
By default, the option is enabled.
Secure Boot Mode Enable or disable to change the secure boot mode options.
By default, the Deployed Mode is enabled.
Expert Key Management
Enable Custom Mode Enable or disable custom mode.
By default, the custom mode option is not enabled.
Custom Mode Key Management Select the custom values for expert key management.
Table 7. System setup options—Integrated Devices menu 
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
90 BIOS Setup
Table 7. System setup options—Integrated Devices menu (continued)
Integrated Devices
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
Table 8. System setup options—Storage menu 
Storage
SATA/NVMe Operation
SATA/NVMe Operation Set the operating mode of the integrated storage device controller. By default, 
the RAID On option is enabled.
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
Device Displays the M.2 PCIe SSD-2 device information of the computer.
Enable MediaCard
Secure Digital (SD) Card Enable or disable the SD card.
By default, the Secure Digital (SD) Card option is enabled.
Secure Digital (SD) Card Read-Only Mode Enable or disable the SD card read-only mode.
BIOS Setup 91
Table 8. System setup options—Storage menu (continued)
Storage
By default, the Secure Digital (SD) Card Read-Only Mode option is not 
enabled.
Table 9. System setup options—Display menu 
Display
Display Brightness
Brightness on battery power Enable to set screen brightness when the computer is running on battery 
power.
Brightness on AC power Enable to set screen brightness when the computer is running on AC power.
Full Screen Logo Enable or disable full screen logo.
By default, the option is not enabled.
Table 10. System setup options—Connection menu 
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
Control WLAN radio Sense the connection of the computer to a wired network and subsequently 
disable the selected wireless radios (WLAN).
By default, the option is disabled.
Control WWAN radio Sense the connection of the computer to a wired network and subsequently 
disable the selected wireless radios (WWAN).
By default, the option is disabled.
92 BIOS Setup
Table 10. System setup options—Connection menu (continued)
Connection
HTTPs Boot Feature
HTTPs Boot Enable or disable the HTTPs Boot feature.
By default, the HTTPs Boot option is enabled.
HTTPs Boot Mode With Auto Mode, the HTTPs Boot extracts Boot URL from the DHCP. With 
Manual Mode, the HTTPs Boot reads Boot URL from the user-provided data.
By default, the Auto Mode option is enabled.
Table 11. System setup options—Power menu 
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
By default, the Intel Speed Shift Technology option is enabled.
Long Life Cycle Primary Battery By default, the Normal Battery option is enabled.
Table 12. System setup options—Security menu 
Security
TPM 2.0 Security 
BIOS Setup 93
Table 12. System setup options—Security menu (continued)
Security
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
Table 13. System setup options—Passwords menu 
Passwords
Admin Password Set, change, or delete the administrator password.
System Password Set, change, or delete the computer password.
NVMe SSD0 Set, change, or delete the NVMe SSD0 password.
Password Configuration
Upper Case Letter Reinforces password must have at least one upper case letter.
94 BIOS Setup
Table 13. System setup options—Passwords menu (continued)
Passwords
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
Table 14. System setup options—Update, Recovery menu 
Update, Recovery
UEFI Capsule Firmware Updates Enable or disable BIOS updates through UEFI capsule update packages.
By default, the option is enabled.
BIOS Recovery from Hard Drive Enables the user to recover from certain corrupted BIOS conditions from a 
recovery file on the user primary hard drive or an external USB key.
By default, the option is enabled.
BIOS Downgrade
Allow BIOS Downgrade Enable or disable the flashing of the computer firmware to previous revision is 
blocked.
By default, the option is enabled.
SupportAssist OS Recovery Enable or disable the boot flow for SupportAssist OS Recovery tool in the 
event of certain computer errors.
BIOS Setup 95
Table 14. System setup options—Update, Recovery menu (continued)
Update, Recovery
By default, the option is enabled.
BIOSConnect Enable or disable cloud Service OS recovery if the main operating system fails 
to boot with the number of failures equal to or greater than the value specified 
by the Auto OS Recovery Threshold setup option and local Service OS does not 
boot or is not installed.
By default, the option is enabled.
Dell Auto OS Recovery Threshold Controls the automatic boot flow for SupportAssist System Resolution Console 
and for Dell OS Recovery Tool.
By default, the threshold value is set to 2.
Table 15. System setup options—System Management menu 
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
Table 16. System setup options—Keyboard menu 
Keyboard
Numlock Enable Enable or disable the Numlock function when the computer boots.
By default, the option is enabled.
Fn Lock Options By default, the Fn lock option is enabled.
Keyboard Illumination Enables to change the keyboard illumination settings.
By default, the Bright option is enabled.
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
96 BIOS Setup
Table 17. System setup options—Pre-boot Behavior menu 
Pre-boot Behavior
Adapter Warnings
Enable Adapter Warnings Enable or disable the warning messages during boot when the adapters with 
less power capacity are detected.
By default, the option is enabled.
Warning and Errors Enable or disable the action to be done when a warning or error is encountered.
By default, the Prompt on Warnings and Errors option is enabled.
USB-C Warnings
Enable Dock Warning Messages Enable or disable Dock Warning Messages.
By default, the option is enabled.
Fastboot Enable to set the speed of the boot process.
By default, the Minimal option is enabled.
Extend BIOS POST Time Set the BIOS POST time.
By default, the 0 seconds option is enabled.
MAC Address Pass-Through Replaces the external NIC MAC address with the selected MAC address from 
the computer.
By default, the System Unique MAC Address option is enabled.
Table 18. System setup options—Performance menu 
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
Intel Hyper-Threading Technology
Enable Intel Hyper-Threading Technology Enable or disable Hyper-Threading in the processor.
By default, the option is enabled.
Dynamic Tuning:Machine Learning
Enable Dynamic Tuning:Machine Learning Enables the operating system capability to enhance dynamic power tuning 
capabilities based on detected workloads.
By default, the option is disabled.
BIOS Setup 97
Table 19. System setup options—System Logs menu 
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
CAUTION: If BitLocker is not suspended before updating the BIOS, the BitLocker key is not recognized the 
next time you reboot the computer. You will then be prompted to enter the recovery key to proceed, and the 
computer displays a prompt for the recovery key on each reboot. Failure to provide the recovery key can result 
in data loss or an operating system reinstall. For more information, see the Knowledge Base Resource updating 
the BIOS on Dell systems with BitLocker enabled .
Steps
1. Go to Dell Support Site .
2. Go to Identify your product or search support . In the box, enter the product identifier, model, service request or 
describe what you are looking for, and then click Search .
NOTE: If you do not have the Service Tag, use the SupportAssist to automatically identify your computer. You can also 
use the product ID or manually browse for your computer model.
3. Click Drivers & Downloads . Expand Find drivers .
4. Select the operating system installed on your computer.
5. In the Category drop-down list, select BIOS .
6. Select the latest version of BIOS, and click Download to download the BIOS file for your computer.
7. After the download is complete, browse the folder where you saved the BIOS update file.
8. Double-click the BIOS update file icon and follow the on-screen instructions.
For more information, search in the Knowledge Base Resource at Dell Support Site .
Updating the BIOS in Linux and Ubuntu
To update the system BIOS on a computer that is installed with Linux or Ubuntu, see the knowledge base article 000131486 at 
Dell Support Site .
98 BIOS Setup
Updating the BIOS using the USB drive in Windows
About this task
CAUTION: If BitLocker is not suspended before updating the BIOS, the BitLocker key is not recognized the 
next time you reboot the computer. You will then be prompted to enter the recovery key to proceed, and the 
computer displays a prompt for the recovery key on each reboot. Failure to provide the recovery key can result 
in data loss or an operating system reinstall. For more information, see the Knowledge Base Resource updating 
the BIOS on Dell systems with BitLocker enabled .
Steps
1. Go to Dell Support Site .
2. Go to Identify your product or search support . In the box, enter the product identifier, model, service request or 
describe what you are looking for, and then click Search .
NOTE: If you do not have the Service Tag, use the SupportAssist to automatically identify your computer. You can also 
use the product ID or manually browse for your computer model.
3. Click Drivers & Downloads . Expand Find drivers .
4. Select the operating system installed on your computer.
5. In the Category drop-down list, select BIOS .
6. Select the latest version of BIOS, and click Download to download the BIOS file for your computer.
7. Create a bootable USB drive. For more information, search in the Knowledge Base Resource at Dell Support Site .
8. Copy the BIOS setup program file to the bootable USB drive.
9. Connect the bootable USB drive to the computer that needs the BIOS update.
10. Restart the computer and press F12.
11. Select the USB drive from the One Time Boot Menu .
12. Type the BIOS setup program filename and press Enter .
The BIOS Update Utility appears.
13. Follow the on-screen instructions to complete the BIOS update.
Updating the BIOS from the One-Time boot menu
You can run the BIOS flash update file from Windows using a bootable USB drive or you can also update the BIOS from 
the One-Time boot menu on the computer. To update your computers BIOS, copy the BIOS XXXX.exe file onto a USB drive 
formatted with the FAT32 file system. Then, restart your computer and boot from the USB drive using the One-Time Boot 
Menu.
About this task
CAUTION: If BitLocker is not suspended before updating the BIOS, the next time you reboot the computer it 
will not recognize the BitLocker key. You will then be prompted to enter the recovery key to progress, and the 
computer will ask for this on each reboot. If the recovery key is not known this can result in data loss or an 
unnecessary operating system reinstall. For more information about this subject, search in the Knowledge Base 
Resource at Dell Support Site .
BIOS Update
To confirm if the BIOS Flash Update is listed as a boot option you can boot your computer to the One Time Boot Menu. If the 
option is listed, then the BIOS can be updated using this method.
To update your BIOS from the One-Time boot menu, you need the following:
● USB drive formatted to the FAT32 file system (the drive does not have to be bootable)
● BIOS executable file that you downloaded from the Dell Support website and copied to the root of the USB drive
● AC power adapter must be connected to the computer
● A functional computer battery to flash the BIOS
Perform the following steps to update the BIOS from the One-Time boot menu:
BIOS Setup 99
CAUTION: Do not turn off the computer during the BIOS flash update process. The computer may not boot if 
you turn off your computer.
Steps
1. Turn off the computer, insert the USB drive that contains the BIOS flash update file.
2. Turn on the computer and press F12 to access the One Time Boot Menu. Select BIOS Update using the mouse or arrow 
keys then press Enter.
The flash BIOS menu is displayed.
3. Click Flash from file .
4. Select the external USB device.
5. Select the file and double-click the flash target file, and then click Submit .
6. Click Update BIOS . The computer restarts to flash the BIOS.
7. The computer will restart after the BIOS flash update is completed.
System and setup password
CAUTION: The password features provide a basic level of security for the data on your computer.
CAUTION: Ensure that your computer is locked when it is not in use. Anyone can access the data that is stored 
on your computer, when left unattended.
Table 20. System and setup password 
Password type Description
System password Password that you must enter to boot to your operating 
system.
Setup password Password that you must enter to access and change the BIOS 
settings of your computer.
You can create a system password and a setup password to secure your computer.
NOTE: The System and setup password feature is disabled by default.
Assigning a System Setup password
Prerequisites
You can assign a new System or Admin Password only when the status is set to Not Set . To enter BIOS System Setup, press 
F2 immediately after a power-on or reboot.
Steps
1. In the System BIOS or System Setup screen, select Security and press Enter.
The Security screen is displayed.
2. Select System/Admin Password and create a password in the Enter the new password field.
Use the following guidelines to create the system password:
● A password can have up to 32 characters.
● A password can at least have one special character: "( ! " # $ % & ' * + , - . / : ; < = > ? @ [ \ ] ^ _ ` { | } )"
● A password can have numbers 0 to 9.
● A password can have an upper case letters from A to Z.
● A password can have a lower case letters from a to z.
3. Type the system password that you entered earlier in the Confirm new password field and click OK.
4. Press Y to save the changes.
The computer restarts.
100 BIOS Setup
Deleting or changing an existing system password or setup 
password
Prerequisites
Ensure that the Password Status is Unlocked in the System Setup before attempting to delete or change the existing 
system password and/or setup password. You cannot delete or change an existing system password or setup password if the 
Password Status is Locked. To enter the System Setup, press F2 immediately after a power-on or reboot.
Steps
1. In the System BIOS or System Setup screen, select System Security and press Enter.
The System Security screen is displayed.
2. In the System Security screen, verify that the Password Status is Unlocked.
3. Select System Password . Update or delete the existing system password, and press Enter or Tab.
4. Select Setup Password . Update or delete the existing setup password, and press Enter or Tab.
NOTE: If you change the system password and/or setup password, reenter the new password when prompted. If you 
delete the system password and/or setup password, confirm the deletion when prompted.
5. Press Esc. A message prompts you to save the changes.
6. Press Y to save the changes and exit from System Setup .
The computer restarts.
Clearing system and setup passwords
About this task
To clear the system or setup passwords, contact Dell technical support as described at Contact Support .
NOTE: For information about how to reset Windows or application passwords, see the documentation accompanying 
Windows or your application.
BIOS Setup 101

## Troubleshooting

_Latitude 5420 Service Manual, pages 102–108_

Troubleshooting
Topics:
• Handling swollen rechargeable Li-ion batteries
• Dell SupportAssist Pre-boot System Performance Check diagnostics
• Built-in self-test (BIST)
• System diagnostic lights
• Recovering the operating system
• Backup media and recovery options
• Network power cycle
• Drain flea power (perform hard reset)
Handling swollen rechargeable Li-ion batteries
Like most laptops, Dell laptops use Lithium-ion batteries. One type of Lithium-ion battery is the rechargeable Li-ion battery. 
Rechargeable Li-ion batteries have increased in popularity in recent years and have become a standard in the electronics 
industry due to customer preferences for a slim form factor (especially with newer ultra-thin laptops) and long battery life. 
Inherent to rechargeable Li-ion battery technology is the potential for swelling of the battery cells.
A swollen battery may impact the performance of the laptop. To prevent possible further damage to the device enclosure or 
internal components leading to malfunction, discontinue the use of the laptop and discharge it by disconnecting the AC adapter 
and letting the battery drain.
Swollen batteries should not be used and must be replaced and disposed of properly. We recommend contacting Dell Support 
for options to replace a swollen battery under the terms of the applicable warranty or service contract, including options for 
replacement by a Dell authorized service technician.
The guidelines for handling and replacing rechargeable Li-ion batteries are as follows:
● Exercise caution when handling rechargeable Li-ion batteries.
● Discharge the battery before removing it from the laptop. To discharge the battery, unplug the AC adapter from the 
computer and operate the computer only on battery power. The battery is fully discharged when the computer no longer 
turns on when the power button is pressed.
● Do not crush, drop, mutilate, or penetrate the battery with foreign objects.
● Do not expose the battery to high temperatures, or disassemble battery packs and cells.
● Do not apply pressure to the surface of the battery.
● Do not bend the battery.
● Do not use tools of any type to pry on or against the battery.
● If a battery gets stuck in a device as a result of swelling, do not try to free it as puncturing, bending, or crushing a battery 
can be dangerous.
● Do not attempt to reassemble a damaged or swollen battery into a laptop.
● Swollen batteries that are covered under warranty should be returned to Dell in an approved shipping container (provided 
by Dell)—this is to comply with transportation regulations. Swollen batteries that are not covered under warranty should 
be disposed of at an approved recycling center. Contact Dell Support at Dell Support Site for assistance and further 
instructions.
● Using a non-Dell or incompatible battery may increase the risk of fire or explosion. Replace the battery only with a 
compatible battery purchased from Dell that is designed to work with your Dell computer. Do not use a battery from other 
computers with your computer. Always purchase genuine batteries from Dell Site or otherwise directly from Dell.
Rechargeable Li-ion batteries can swell for various reasons such as age, number of charge cycles, or exposure to high heat. For 
more information about how to improve the performance and lifespan of the laptop battery and to minimize the possibility of 
occurrence of the issue, search Dell laptop battery in the Knowledge Base Resource at Dell Support Site .
6
102 Troubleshooting
Dell SupportAssist Pre-boot System Performance 
Check diagnostics
About this task
SupportAssist diagnostics (also known as system diagnostics) performs a complete check of your hardware. The Dell 
SupportAssist Pre-boot System Performance Check diagnostics is embedded within the BIOS and launched by the BIOS 
internally. The embedded system diagnostics provides options for particular devices or device groups allowing you to:
● Run tests automatically or in an interactive mode.
● Repeat the tests.
● Display or save test results.
● Run thorough tests to add more options and obtain details about any failed devices.
● View status messages that inform you when the tests are completed successfully.
● View error messages that inform you of problems encountered during testing.
NOTE: Some tests for specific devices require user interaction. Always ensure that you are present at the computer when 
the diagnostic tests are performed.
For more information, see the knowledge base article 000181163 .
Running the SupportAssist Pre-Boot System Performance Check
Steps
1. Turn on your computer.
2. As the computer boots, press the F12 key.
3. On the boot menu screen, select Diagnostics .
The diagnostic quick test begins.
NOTE: For more information about running the SupportAssist Pre-Boot System Performance Check on a specific 
device, see Dell Support Site .
4. If there are any issues, error codes are displayed.
Note the error code and validation number and contact Dell.
Built-in self-test (BIST)
(Motherboard Built-In Self-Test) M-BIST
M-BIST is the system board built-in self-test diagnostics tool that improves the diagnostics accuracy of system board 
Embedded Controller (EC) failures.
NOTE: M-BIST can be manually initiated before Power On Self-Test (POST).
How to run M-BIST
NOTE: Before initiating M-BIST, ensure that the computer is in a power-off state.
1. Press and hold both the M key and the power button to initiate M-BIST.
2. The battery indicator LED may exhibit two states:
● Off: No fault was detected.
● Amber and White: Indicates a problem with the system board.
3. If there is a failure with the system board, the battery status LED flashes one of the following error codes for 30 seconds:
Troubleshooting 103
Table 21. LED error codes 
Blinking Pattern Possible Problem
Amber White
2 1 CPU Failure
2 8 LCD Power Rail Failure
1 1 TPM Detection Failure
2 4 Memory/RAM failure
4. If there is no failure with the system board, the LCD cycles through the solid color screens (that are described in the 
LCD-BIST) for 30 seconds and then turn off.
Logical Built-in Self-test (L-BIST)
L-BIST is an enhancement to the single LED error code diagnostics and is automatically initiated during POST. L-BIST will check 
the LCD power rail. If there is no power being supplied to the LCD (that is if the L-BIST circuit fails), the battery status LED 
flashes either an error code [2,8] or an error code [2,7].
NOTE: If L-BIST fails, LCD-BIST cannot function as no power will be supplied to the LCD.
How to invoke the L-BIST
1. Turn on your computer.
2. If the computer does not start up normally, look at the battery status LED:
● If the battery status LED flashes an error code [2,7], the display cable may not be connected properly.
● If the battery status LED flashes an error code [2,8], there is a failure on the LCD power rail of the system board, hence 
there is no power that is supplied to the LCD.
3. For cases, when a [2,7] error code is shown, check to see if the display cable is properly connected.
4. For cases when a [2,8] error code is shown, replace the system board.
LCD Built-in Self-Test (LCD-BIST)
Dell laptops have a built-in diagnostic tool that helps you determine if the screen abnormality you are experiencing is an inherent 
problem with the LCD (screen) of the Dell laptop or with the video card (GPU) and computer settings.
When you notice screen abnormalities like flickering, distortion, clarity issues, fuzzy or blurry image, horizontal or vertical lines, 
color fade, it is always a good practice to isolate the LCD (screen) by running the LCD-BIST.
How to invoke the LCD-BIST
1. Turn off your computer.
2. Disconnect any peripherals that are connected to the computer. Connect only the AC adapter (charger) to the computer.
3. Ensure that the LCD (screen) is clean (no dust particles on the surface of the screen).
4. Press and hold the D key and press the power button to enter LCD-BIST mode. Continue to hold the D key until the 
computer boots up.
5. The screen displays solid colors and changes colors on the entire screen to white, black, red, green, and blue twice.
6. Then it displays the colors white, black, and red.
7. Carefully inspect the screen for abnormalities (any lines, fuzzy color, or distortion on the screen).
8. At the end of the last solid color (red), the computer shuts down.
NOTE: Dell SupportAssist Preboot diagnostics upon launch initiates an LCD-BIST first, expecting a user intervention to 
confirm functionality of the LCD.
104 Troubleshooting
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
Table 22. System diagnostic lights 
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
Troubleshooting 105
Table 22. System diagnostic lights (continued)
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
106 Troubleshooting
Recovering the operating system
When your computer is unable to boot to the operating system even after repeated attempts, it automatically starts Dell 
SupportAssist OS Recovery.
Dell SupportAssist OS Recovery is a stand-alone tool that is preinstalled in Dell computers running the Windows operating 
system. It consists of tools to diagnose and troubleshoot issues that may occur before your computer boots to the operating 
system. It enables you to diagnose hardware issues, repair your computer, back up your files, and restore your computer to its 
factory state.
You can also download it from the Dell Support website to troubleshoot and fix your computer when it fails to boot into the 
primary operating system due to software or hardware failures.
For more information about the Dell SupportAssist OS Recovery, see Dell SupportAssist OS Recovery User's Guide at 
Serviceability Tools at the Dell Support Site . Click SupportAssist and then click SupportAssist OS Recovery .
Backup media and recovery options
It is recommended to create a recovery drive to troubleshoot and fix problems that may occur with Windows. Dell provides 
multiple options for recovering the Windows operating system on your Dell computer. For more information, see Dell Windows 
Backup Media and Recovery Options .
Network power cycle
About this task
If your computer is unable to access the Internet due to network connectivity issues, reset your network devices by performing 
the following steps:
Steps
1. Turn off the computer.
2. Turn off the modem.
NOTE: Some Internet service providers (ISPs) provide a modem and router combo device.
3. Turn off the wireless router.
4. Wait for 30 seconds.
5. Turn on the wireless router.
6. Turn on the modem.
7. Turn on the computer.
Drain flea power (perform hard reset)
About this task
Flea power is the residual static electricity that remains in the computer even after it has been powered off and the battery is 
removed.
For your safety, and to protect the sensitive electronic components in your computer, you must drain residual flea power before 
removing or replacing any components in your computer.
Draining flea power, also known as a performing a "hard reset," is also a common troubleshooting step if your computer does not 
turn on or boot into the operating system.
Perform the following steps to drain the flea power:
Steps
1. Turn off the computer.
2. Disconnect the power adapter from the computer.
Troubleshooting 107
3. Remove the base cover.
4. Remove the battery.
CAUTION: The battery is a Field Replaceable Unit (FRU) and the removal and installation procedures are 
intended for authorized service technicians only.
5. Press and hold the power button for 20 seconds to drain the flea power.
6. Install the battery.
7. Install the base cover.
8. Connect the power adapter to the computer.
9. Turn on the computer.
NOTE: For more information about performing a hard reset, go to Dell Support Site . On the menu bar at the top of 
the Support page, select Support > Support Library. In the Search field on the Support Library page, type the keyword, 
topic, or model number, and then click or tap the search icon to view the related articles.
108 Troubleshooting

## Latitude 5420 Setup and Specifications

_Latitude 5420 Setup and Specifications, pages 1–2_

Latitude 5420
Setup and Specifications
Regulatory Model: P137G
Regulatory Type: P137G001, P137G002
May 2023
Rev. A04
Notes, cautions, and warnings
NOTE: A NOTE indicates important information that helps you make better use of your product.
CAUTION: A CAUTION indicates either potential damage to hardware or loss of data and tells you how to avoid
the problem.
WARNING: A WARNING indicates a potential for property damage, personal injury, or death.
© 2021-2023 Dell Inc. or its subsidiaries. All rights reserved. Dell Technologies, Dell, and other trademarks are trademarks of Dell Inc. or its
subsidiaries. Other trademarks may be trademarks of their respective owners.

## Set up your Latitude 5420

_Latitude 5420 Setup and Specifications, pages 4–5_

Set up your Latitude 5420
NOTE: The images in this document may differ from your computer depending on the configuration you ordered.
1. Connect the power adapter and press the power button.
NOTE: The battery may go into power-saving mode during shipment to conserve charge on the battery. Ensure that the
power adapter is connected to your computer when it is turned on for the first time.
2. Finish Windows setup.
Follow the on-screen instructions to complete the setup. When setting up, Dell recommends that you:
● Connect to a network for Windows updates.
NOTE: If connecting to a secured wireless network, enter the password for the wireless network access when
prompted.
● If connected to the Internet, sign in with or create a Microsoft account. If not connected to the Internet, create an
offline account.
● On the Support and Protection screen, enter your contact details.
3. Locate and use Dell apps from the Windows Start menu—Recommended.
Table 1. Locate Dell apps 
Resources Description
SupportAssist
Proactively checks the health of your computer’s hardware and software. The SupportAssist OS
Recovery tool troubleshoots issues with the operating system. For more information, see the
SupportAssist documentation at www.dell.com/support .
NOTE: In SupportAssist, click the warranty expiry date to renew or upgrade your warranty.
1
4 Set up your Latitude 5420
Table 1. Locate Dell apps (continued)
Resources Description
Dell Update
Updates your computer with critical fixes and latest device drivers as they become available.
For more information about using Dell Update, see the knowledge base article SLN305843 at
www.dell.com/support .
Dell Digital Delivery
Download software applications, which are purchased but not pre-installed on your computer.
For more information about using Dell Digital Delivery, see the knowledge base article 153764 at
www.dell.com/support .
Set up your Latitude 5420 5

## Views of Latitude 5420

_Latitude 5420 Setup and Specifications, pages 6–11_

Views of Latitude 5420
Topics:
• Right
• Left
• Palm rest
• Front
• Bottom
• Back
• System board layout
• Keyboard shortcuts
• Battery charge and status LED
Right
1. microSD-card slot 2. Universal audio port
3. USB 3.2 Gen 1 port 4. USB 3.2 Gen 1 port with PowerShare
5. HDMI 2.0 port 6. RJ45 Ethernet port
7. Wedge-shaped lock slot
2
6 Views of Latitude 5420
Left
1. Thunderbolt 4 port with DisplayPort Alt Mode/USB4/Power
Delivery
2. Thunderbolt 4 port with DisplayPort Alt Mode/USB4/Power
Delivery
3. Air vents 4. Smart card reader slot (optional)
Palm rest
Views of Latitude 5420 7
1. Privacy shutter 2. Power button (with optional fingerprint reader)
3. Keyboard 4. NFC/Contactless smart card reader—(optional)
5. Clickpad
Front
1. Dual-array microphones 2. IR emitter/Ambient Light Sensor (ALS)—(optional)
3. Camera (FHD RGB IR/HD RGB IR/HD RGB) 4. Camera status LED
5. Dual-array microphones 6. Display panel
7. Battery diagnostic LED
8 Views of Latitude 5420
Bottom
1. Speakers 2. Service tag label
3. MicroSim-card slot (optional) 4. Air vent
Back
1. SIM card tray
Views of Latitude 5420 9
System board layout
1. Fingerprint reader connector
2. WWAN connector
3. Camera/IR cable connector
4. eDP/display cable connector
5. Touch and sensor cable connector
6. System fan connector
7. Battery cable connector
8. Memory modules
9. Clickpad cable connector
10. USH board connector
11. WLAN connector
12. Solid-state drive slot
13. Coin-cell battery cable connector
14. Speaker cable connector
15. Battery LED cable connector
Keyboard shortcuts
NOTE: Keyboard characters may differ depending on the keyboard language configuration. Keys that are used for shortcuts
remain the same across all language configurations.
Table 2. List of keyboard shortcuts 
Keys Primary Behavior Secondary Behavior (Fn + Key)
Fn + Esc Escape Toggle Fn-key lock
Fn + F1 Mute audio F1 behavior
Fn + F2 Decrease volume F2 behavior
Fn + F3 Increase volume F3 behavior
10 Views of Latitude 5420
Table 2. List of keyboard shortcuts (continued)
Keys Primary Behavior Secondary Behavior (Fn + Key)
Fn + F4 Mic Mute F4 behavior
Fn + F5 Keyboard backlight
NOTE: Not applicable for nonbacklight keyboard.
F5 behavior
Fn + F6 Decrease screen brightness F6 behavior
Fn + F7 Increase screen brightness F7 behavior
Fn + F8 Switch to external display F8 behavior
Fn + F9 Disable camera F9 behavior
Fn + F10 Print Screen F10 behavior
Fn + F11 Home F11 behavior
Fn + F12 End F12 behavior
Fn + Left Arrow Left Arrow Home
Fn + Right Arrow Right Arrow End
Fn + Right Ctrl Emulates right click --
Fn + P SafeScreen (e-Privacy) --
Battery charge and status LED
Table 3. Battery charge and status LED Indicator 
Power Source LED Behavior computer Power State Battery Charge Level
AC Adapter Off S0 - S5 Fully Charged
AC Adapter Solid White S0 - S5 < Fully Charged
Battery Off S0 - S5 11-100%
Battery Solid Amber (590+/-3 nm) S0 - S5 < 10%
● S0 (ON) - Computer is turned on.
● S4 (Hibernate) - The computer consumes the least power compared to all other sleep states. The computer is almost at an
OFF state, expect for a trickle power. The context data is written to hard drive.
● S5 (OFF) - The computer is in a shutdown state.
Views of Latitude 5420 11

## Specifications of Latitude 5420

_Latitude 5420 Setup and Specifications, pages 12–23_

Specifications of Latitude 5420
Topics:
• Dimensions and weight
• Processors
• Chipset
• Operating system
• Memory
• Ports and connectors
• Communications
• Audio
• Storage
• Media-card reader
• Keyboard
• Camera
• Clickpad
• Power adapter
• Battery
• Display
• Fingerprint reader (optional)
• Video
• Multiple display support matrix
• Hardware security
• Operating and storage environment
• Sensor and control
Dimensions and weight
Table 4. Dimensions and weight 
Description Values
Height:
Front 0.76 in. (19.30 mm)
Rear 0.82 in. (20.90 mm)
Width 12.65 in. (321.35 mm)
Depth 8.35 in. (212.00 mm)
Weight (maximum) 3.03 lb (1.37 kg)
NOTE: The weight of your computer depends on the configuration
ordered and the manufacturing variability.
3
12 Specifications of Latitude 5420
Processors
NOTE: Processor numbers are not a measure of performance. Processor availability subject to change and may vary by
region/country.
Table 5. Processors 
Processors Wattage Core
count
Thread
count
Speed Cache Integrated graphics
10thGeneration Intel Core
i5-10310U
15 W 4 8 1.70 GHz to 4.40
GHz
6 MB Intel UHD Graphics
11th Generation Intel Core
i3-1125G4
17.50 W 4 8 2.00 GHz to 3.70
GHz
8 MB Intel UHD Graphics
11th Generation Intel Core
i5-1135G7
17.50 W 4 8 2.40 GHz to 4.20
GHz
8 MB Intel Iris X e Graphics
11th Generation Intel Core
i5-1145G7
17.50 W 4 8 2.60 GHz to 4.40
GHz
8 MB Intel Iris X e Graphics
11th Generation Intel Core
i7-1165G7
17.50 W 4 8 2.80 GHz to 4.70
GHz
12 MB Intel Iris X e Graphics
11th Generation Intel Core
i7-1185G7
17.50 W 4 8 3.00 GHz to 4.80
GHz
12 MB Intel Iris X e Graphics
Chipset
The following table lists the details of the chipset supported by your Latitude 5420
Table 6. Chipset 
Description Values
Chipset Intel PCH-LP
Processor ● 10th Generation Intel Core i5 processors
● 11th Generation Intel Core i3/i5/i7 processors
DRAM bus width 64-bit
Flash EPROM 32 MB
PCIe bus Up to Gen 3
Operating system
Your Latitude 5420 supports the following operating systems:
● Windows 11 Home, 64-bit
● Windows 11 Home National Academic, 64-bit
● Windows 11 Pro, 64-bit
● Windows 11 Pro National Academic, 64-bit
● Windows 10 Home, 64-bit
● Windows 10 Pro, 64-bit
● Windows 10 Pro Education, 64-bit
Specifications of Latitude 5420 13
● Windows 10 Enterprise, 64-bit
● Ubuntu 20.04 LTS, 64-bit
Memory
The following table lists the memory specifications of your Latitude 5420:
Table 7. Memory specifications 
Description Values
Slots Two SO-DIMM slots
Type DDR4, Dual-channel
Speed 3200 MHz
Maximum memory 64 GB
Minimum memory 4 GB
Memory size per slot 4 GB, 8 GB, 16 GB, 32 GB
Configurations supported ● 4 GB, 1 x 4 GB, DDR4, 3200 MHz
● 8 GB, 2 x 4 GB, DDR4, 3200 MHz
● 8 GB, 1 x 8 GB, DDR4, 3200 MHz
● 16 GB, 2 x 8 GB, DDR4, 3200 MHz
● 16 GB, 1 x 16 GB, DDR4, 3200 MHz
● 32 GB, 2 x 16 GB, DDR4, 3200 MHz
● 64 GB, 2 x 32 GB, DDR4, 3200 MHz
Ports and connectors
Table 8. External ports and connectors 
External:
USB ● One USB 3.2 Gen 1 port
● One USB 3.2 Gen 1 port with PowerShare
● Two Thunderbolt 4 ports with DisplayPort Alt Mode/
USB4/Power Delivery
Audio One universal audio port
Video One HDMI 2.0 port
Media card reader One micro SD-card slot
Docking port Supported through USB Type-C
Power adapter port Type-C power input
Security One wedge-shaped lock slot
Communication ● RJ45 port
● microSIM card (optional)
Card slot Smart card reader slot (optional)
14 Specifications of Latitude 5420
Table 9. Internal ports and connectors 
Internal:
M.2 ● M.2 2230 slot for Wi-Fi and Bluetooth combo card
● M.2 3042 for WWAN
● One M.2 2280/2230 slot for solid state drive
NOTE: To learn more about the features of different
types of M.2 cards, search in the Knowledge Base
Resource at www.dell.com/support .
Communications
Ethernet
Table 10. Ethernet specifications 
Description Values
Model number ● Intel I219-LM
● Intel I219-V
Transfer rate 10/100/1000 Mbps
Wireless module
Table 11. Wireless module specifications 
Description Option one Option two Option Three
Model number Intel Wi-Fi 6 AX201 Intel Wi-Fi 6 AX210 MediaTek MT792
Transfer rate Up to 2400 Mbps Up to 2400 Mbps Up to 1.2 Gbps
Frequency bands supported 2.4 GHz/5 GHz 2.4 GHz/5 GHz 2.4 GHz/5 GHz
Wireless standards ● Wi-Fi 802.11a/b/g
● Wi-Fi 4 (Wi-Fi 802.11n)
● Wi-Fi 5 (Wi-Fi 802.11ac)
● Wi-Fi 6 (Wi-Fi 802.11ax)
● Wi-Fi 802.11a/b/g
● Wi-Fi 4 (Wi-Fi 802.11n)
● Wi-Fi 5 (Wi-Fi 802.11ac)
● Wi-Fi 6 (Wi-Fi 802.11ax)
● Wi-Fi 802.11ax
● Wi-Fi 802.11ac
Encryption ● 64-bit/128-bit WEP
● AES-CCMP
● TKIP
● 64-bit/128-bit WEP
● AES-CCMP
● TKIP
● 64-bit/128-bit WEP
● AES-CCMP
● TKIP
Bluetooth Bluetooth 5.1 Bluetooth 5.2 Bluetooth 5.2
WWAN module
Table 12. Wireless module specifications 
Description Values
Model number Intel XMM 7360 Global LTE-Advanced, CAT9
Transfer rate Up to 450 Mbps DL/50 Mbps UL (Cat 9)
Specifications of Latitude 5420 15
Table 12. Wireless module specifications (continued)
Description Values
Frequency bands supported (1,2,3,4,5,7,8,11,12,13,17,18,19,20,21,26,28,29,30,38,39,40,41,66
), HSPA+ (1, 2, 4,5, 8)
Wireless standards Not Applicable
Encryption Not Applicable
Bluetooth Not Applicable
NOTE: For instructions on how to find your computer's IMEI (International Mobile Station Equipment Identity) number, see
the knowledge base article 000143678 at www.dell.com/support .
Audio
Table 13. Audio specifications 
Description Values
Controller REALTEK ALC3204
Stereo conversion Supported
Internal interface High definition audio interface
External interface Universal audio port
Speakers Two
Internal speaker amplifier Supported (audio codec integrated)
External volume controls Keyboard shortcut controls
Speaker output:
Average 2 W
Peak 2.5 W
Subwoofer output Not supported
Microphone Dual-array microphones
Storage
This section lists the storage options on your Latitude 5420.
Your computer supports one of the following configurations:
● One M.2 2230, Gen 3 PCIe x4 NVMe, Class 35 SSD (slot 1)
● One M.2 2280, Gen 3 PCIe x4 NVMe, Classs 40 SSD (slot 1)
● One M.2 2280, Gen 3 PCIe x4 NVMe, Class 40 SSD, Self-encrypting drive (slot 1)
The primary drive of your computer varies with the storage configuration.
16 Specifications of Latitude 5420
Table 14. Storage specifications 
Storage type Interface type Capacity
M.2 2230, Class 35 solid-state drive Gen 3 PCIe x4 NVMe Up to 512 GB
M.2 2280, Class 40 solid-state drive Gen 3 PCIe x4 NVMe Up to 1 TB
M.2 2280, Class 40 solid-state drive,
Self-encrypting drive
Gen 3 PCIe x4 NVMe Up to 512 GB
Media-card reader
Table 15. Media-card reader specifications 
Description Values
Type One microSD-card
Cards supported ● Micro Secure Digital (mSD)
● Micro Secure Digital High Capacity (mSDHC)
● Micro Secure Digital Extended Capacity (mSDXC)
Keyboard
Table 16. Keyboard specifications 
Description Values
Type ● Extended single-point non-backlit keyboard
● Extended single-point backlit keyboard
Layout QWERTY
Number of keys ● United States and Canada: 79 keys
● United Kingdom: 80 keys
● Japan: 83 keys
Size X=18.05 mm key pitch
Y=18.05 mm key pitch
Shortcut keys Some keys on your keyboard have two symbols on them.
These keys can be used to type alternate characters or to
perform secondary functions. To type the alternate character,
press Shift and the desired key. To perform secondary
functions, press Fn and the desired key.
NOTE: You can define the primary behavior of the
function keys (F1–F12) by changing the Function Key
Behavior in system setup program. Keyboard shortcuts
Specifications of Latitude 5420 17
Camera
The following table lists the camera specifications of your Latitude 5420.
Table 17. Camera specifications 
Description Option one Option two Option three
Number of cameras One One One
Camera type Integrated 6 mm HD RGB Webcam Integrated 6 mm HD RGB +
IR Webcam
Integrated 6 mm FHD RGB
+ IR Webcam with proximity
sensor and ALS (Optional)
Camera location Front camera Front camera Front camera
Camera sensor type CMOS sensor technology CMOS sensor technology CMOS sensor technology
Camera resolution:
Still image 0.92 megapixels 0.92 megapixels 0.92 megapixels
Video 1280 x 720 (HD) at 30 fps 1280 x 720 (HD) at 30 fps 1920 x 1080 (FHD) at 30
fps
Infrared camera resolution:
Still image NA 0.23 0.23
Video NA 640 x 360 640 x 360
Diagonal viewing angle:
Camera 78.60 degrees 87 degrees 87.60 degrees
Infrared camera NA 87 degrees 87.60 degrees
Clickpad
The following table lists the clickpad specifications of your Precision 3560.
Table 18. Clickpad specifications 
Description Values
Clickpad resolution >=300 dpi
Clickpad dimensions:
Horizontal 115 mm (4.53 inch)
Vertical 67 mm (2.64 inch)
Power adapter
Table 19. Power adapter specifications 
Description Values
Type 65 W 90 W
18 Specifications of Latitude 5420
Table 19. Power adapter specifications (continued)
Description Values
Diameter (connector) USB-C USB-C
Input voltage 100 VAC x 240 VAC 100 VAC x 240 VAC
Input frequency 50 Hz to 60 Hz 50 Hz to 60 Hz
Input current (maximum) 1.7 A 1.5 A
Output current (continuous) ● 20 V/3.25 A (Continuous)
● 15 V/3 A (Continuous)
● 9.0 V/3 A (Continuous
● 5.0 V/3 A (Continuous)
● 20 V/4.5 A (Continuous)
● 15 V/3 A (Continuous)
● 9.0 V/3 A (Continuous
● 5.0 V/3 A (Continuous)
Rated output voltage 20 VDC/15 VDC/9 VDC/5 VDC 20 VDC/15 VDC/9 VDC/5 VDC
Temperature range:
Operating 0°C to 40°C (32°F to 104°F) 0°C to 40°C (32°F to 104°F)
Storage -40°C to 70°C (-40°F to 158°F) -40°C to 70°C (-40°F to 158°F)
Battery
The following table lists the battery specifications of your Latitude 5420.
Table 20. Battery specifications 
Description Values
Battery type 3-cell rechargeable Liion battery, 42 WHr,
ExpressCharge Boost
4-cell rechargeable Liion battery, 63 WHr,
ExpressCharge Boost
3-cell rechargeable
Li-ion battery, 42
WHr LCL
4-cell rechargeable Liion battery, 63 WHr LCL
Battery voltage 11.40 VDC 15.20 VDC 11.40 VDC 15.20 VDC
Battery weight
(maximum)
0.18 kg ( 0.40 lb) 0.25 kg ( 0.55 lb) 0.18 kg ( 0.40 lb) 0.25 kg ( 0.55 lb)
Battery dimensions:
Height 5.70 mm (0.22 in.) 5.70 mm (0.22 in.) 5.70 mm (0.22 in.) 5.70 mm (0.22 in.)
Width 95.90 mm (3.78 in.) 95.90 mm (3.78 in.) 95.90 mm (3.78 in.) 95.90 mm (3.78 in.)
Depth 207.90 mm (8.19 in.) 238.00 mm (9.37 in.) 207.90 mm (8.19 in.) 238.00 mm (9.37 in.)
Temperature
range:
Operating ● Charge: 0 °C to 50 °C (32
°F to 122 °F)
● Discharge:0 °C to 70 °C
(32 °F to 158 °F)
● Charge: 0 °C to 50
°C (32 °F to 122
°F)
● Discharge:0 °C to
70 °C (32 °F to 158
°F)
● Charge: 0 °C to
50 °C (32 °F to
122 °F)
● Discharge:0 °C
to 70 °C (32 °F
to 158 °F)
● Charge: 0 °C to 50
°C (32 °F to 122 °F)
● Discharge:0 °C to 70
°C (32 °F to 158 °F)
Storage –20 °C to 60 °C (4 °F to 140
°F)
–20 °C to 60 °C (4 °F
to 140 °F)
–20 °C to 60 °C (4
°F to 140 °F)
–20 °C to 60 °C (4 °F
to 140 °F)
Specifications of Latitude 5420 19
Table 20. Battery specifications (continued)
Description Values
Battery operating
time
Varies depending on operating
conditions and can significantly
reduce under certain powerintensive conditions.
Varies depending on
operating conditions
and can significantly
reduce under
certain power-intensive
conditions.
Varies depending on
operating conditions
and can significantly
reduce under certain
power-intensive
conditions.
Varies depending on
operating conditions and
can significantly reduce
under certain powerintensive conditions.
Battery
charging time
(approximate)
From 0% up to 35% in
20 minutes (ExpressCharge
Boost), 2 hr ( Express charge ),
3 hr (Standard charge) (when
the computer is off)
NOTE: Control the
charging time, duration,
start and end time, and so
on using the Dell Power
Manager application. For
more information on the
Dell Power Manager see, on
www.dell.com/
From 0% up to
35% in 20 minutes
(ExpressCharge Boost),
2 hr ( Express charge ),
3 hr (Standard charge)
(when the computer is
off)
NOTE: Control
the charging time,
duration, start and
end time, and
so on using the
Dell Power Manager
application. For
more information
on the Dell Power
Manager see, on
www.dell.com/
2 hr ( Express
charge ), 3 hr
(Standard charge)
(when the computer
is off).
NOTE: Control
the charging
time, duration,
start and end
time, and so on
using the Dell
Power Manager
application. For
more
information on
the Dell Power
Manager see, on
www.dell.com/
2 hr ( Express charge ),
3 hr (Standard charge)
(when the computer is
off).
NOTE: Control
the charging time,
duration, start and
end time, and so on
using the Dell Power
Manager application.
For more information
on the Dell Power
Manager see, on
www.dell.com/
Life span
(approximate)
1 year 1 year 3 years 3 years
Coin-cell battery CR-2032 CR-2032 CR-2032 CR-2032
Display
The following table lists the display specifications of your Latitude 5420.
Table 21. Display specifications 
Description Option one Option two Option three Option four Option five
Display type High Definition (HD) Full High Definition
(FHD)
Full High Definition
(FHD)
Full High
Definition (FHD)
Full High
Definition (FHD
Display-panel
technology
Twisted Nematic
(TN)
Wide Viewing Angle
(WVA)
Wide Viewing Angle
(WVA),Low Blue
Light (LBL)
Wide Viewing
Angle (WVA)
Wide viewing
angle (WVA)
Display-panel
dimensions (active
area):
Height 173.95 mm 173.95 mm 173.95 mm 173.95 mm 173.95 mm
Width 309.4 mm 309.4 mm 309.4 mm 309.4 mm 309.4 mm
Diagonal 355.6 mm 355.6 mm 355.6 mm 355.6 mm 355.6 mm
Display-panel native
resolution
1366 x 768 1920 x 1080 1920 x 1080 1920 x 1080 1920 x 1080
20 Specifications of Latitude 5420
Table 21. Display specifications (continued)
Description Option one Option two Option three Option four Option five
Luminance (typical) 220 nits 250 nits 400 nits 300 nits 300 nits
Megapixels 1.049 2.07 2.07 2.07 2.07
Color gamut NTSC 45% NTSC 45% sRGB 100% NTSC 72% sRGB 100% typ
Pixels Per Inch
(PPI)
112 157 157 157 157
Contrast ratio (typ) 300:1 600:1 1000:1 600:1 600:1
Response time
(max)
25 ms 35 ms 35 ms 35 ms 35 ms
Refresh rate 60 Hz 60 Hz 60 Hz 60 Hz 60 Hz
Horizontal view
angle
40 +/-degrees 80 +/-degrees 80 +/-degrees 80 +/-degrees 80 +/- degrees
Vertical view angle ● Top: 10 +/-
degrees
● Bottom: 30 +/-
degrees
80 +/-degrees 80 +/-degrees 80 +/-degrees 80 +/- degrees
Pixel pitch 0.2265 mm x 0.2265
mm
0.161 mm x 0.161 mm 0.161 mm x 0.161
mm
0.161 mm x 0.161
mm
0.161 mm x 0.161
mm
Power consumption
(maximum)
2.4 W 3.2 W 2.5 W 4.51W 3.5 W
Anti-glare vs glossy
finish
Anti-glare Anti-glare Anti-glare Anti-glare Anti-glare
Touch options No No No Yes Yes
Fingerprint reader (optional)
Table 22. Fingerprint reader specifications 
Description Power button option FIPS option
Sensor technology Capacitative Capacitive
Sensor resolution 500 dpi 508 dpi
Sensor pixel size, X 108 256
Sensor pixel size, Y 88 360
Specifications of Latitude 5420 21
Video
Table 23. Integrated graphics specifications 
Integrated graphics
Controller External display support Memory size Processor
Intel Iris X e Graphics HDMI 2.0, DisplayPort over USB Type-C Shared system memory 11th Generation
Intel Core i5/i7
Processors
NOTE: System
with singlechannel memory
is shown as Intel
UHD Graphics
in Intel Graphics
Command
Center (IGCC).
Intel UHD Graphics HDMI 2.0, DisplayPort over USB Type-C Shared system memory 11th Generation Intel
Core i3 Processors
Intel UHD Graphics HDMI 1.4, DisplayPort over USB Type-C Shared system memory 10th Generation
Intel Core i5/i7
Processors
Multiple display support matrix
The following table lists the multiple display support matrix of your Latitude 5420.
Table 24. Multiple display support matrix for 11th Generation Intel Core 
Graphics Card Supported external displays with computer
internal display on
Supported external displays
with computer internal display
off
Integrated GPU Up to 3 Up to 4
Table 25. Multiple display support matrix for 10th Generation Intel Core 
Graphics Card Supported external displays with computer
internal display on
Supported external displays
with computer internal display
off
Integrated GPU Up to 2 Up to 3
Hardware security
The following table lists the hardware security options supported by your .
Table 26. Hardware security 
Hardware security options
Trusted Platform Module (TPM) 2.0 discrete
FIPS 140-2 certification for TPM
TCG (Trusted Computing Group) Certification for TPM
Fingerprint reader in power button tied to ControlVault 3
22 Specifications of Latitude 5420
Table 26. Hardware security (continued)
Hardware security options
ControlVault 3 Advanced Authentication with FIPS 140-2 Level 3 Certification
Contacted Smart Card and ControlVault 3
Contactless Smart Card, NFC, and ControlVault 3
SED SSD NVMe, SSD and HDD (Opal and non-Opal) per SDL
FIPS 201 Full Scan FPR and ControlVault 3
Operating and storage environment
This table lists the operating and storage specifications of your Latitude 5420.
Airborne contaminant level: G1 as defined by ISA-S71.04-1985
Table 27. Computer environment 
Description Operating Storage
Temperature range 0°C to 40°C (32°F to 104°F) -40°C to 65°C (-40°F to 149°F)
Relative humidity (maximum) 10% to 90% (non-condensing) 0% to 95% (non-condensing)
Vibration (maximum) * 0.66 GRMS 1.30 GRMS
Shock (maximum) 140 G † 160 G †
Altitude range -15.2 m to 3048 m (-50 ft to 10000 ft) -15.2 m to 10668 m (-50 ft to 35000 ft)
CAUTION: Operating and storage temperature ranges may differ among components, so operating or storing
the device outside these ranges may impact the performance of specific components.
* Measured using a random vibration spectrum that simulates user environment.
† Measured using a 2 ms half-sine pulse.
Sensor and control
The following table lists the location of the sensor and control available in your .
Table 28. Sensor and control 
Sensor support
Sensor Ambient Light Sensor on the hinge-up (optional)
P-sensor on the hinge-up (optional)
Accelerometer (G sensor): One on the base (system board) and another on the
hinge-up (optional)
Specifications of Latitude 5420 23
