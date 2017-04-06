# MaxRAM
Open Hardware BBC RAM/ROM Board

My current thoughts are a board that covers the BBCs 4 sideways ROM sockets and has the following features:
1 4 MBit (512KB) 32 Pin DIP Flash Chip (Socketed) [Microchip Technology SST39SF040-70-4C-PHE]
1 4 Mbit (512KB) SRAM Chip [Alliance Memory, Inc. AS6C4008-55PCN]
1 PLD to handle the logic [ATF1502ASL-25JU44-ND]
1 Simple diode battery backup circuit and battery connector or maybe an IC [DS1210S+TRL-ND] for Battery Backup.

Slot 15 will contain the ROM Manager.
8 Slots will be Write Protected RAM.
8 Slots will be Read Write RAM.
16 pages of Flash will be selected at power on with the ability to switch to 16 pages of RAM after boot.