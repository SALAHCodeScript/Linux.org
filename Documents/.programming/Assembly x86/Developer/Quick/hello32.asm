section .data
    msg db "Hello, World!", 0xA  ; String with a newline
    len equ $ - msg              ; Calculate length of string

section .text
    global _start                ; Entry point for program

_start:
    ; Write to stdout
    mov eax, 4                   ; syscall: write
    mov ebx, 1                   ; file descriptor: stdout
    mov ecx, msg                 ; address of string to write
    mov edx, len                 ; length of string
    int 0x80                     ; interrupt for syscall

    ; Exit program
    mov eax, 1                   ; syscall: exit
    xor ebx, ebx                 ; exit code: 0
    int 0x80                     ; interrupt for syscall
