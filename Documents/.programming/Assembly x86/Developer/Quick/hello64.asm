section .data
    msg db "Hello, World!", 0xA  ; Define the string (newline at the end)
    len equ $ - msg              ; Calculate the length of the string

section .text
    global _start                ; Entry point for the program

_start:
    ; Write to stdout
    mov rax, 1                   ; syscall: write
    mov rdi, 1                   ; file descriptor: stdout
    mov rsi, msg                 ; address of the message
    mov rdx, len                 ; length of the message
    syscall                      ; make the system call

    ; Exit the program
    mov rax, 60                  ; syscall: exit
    xor rdi, rdi                 ; exit code: 0
    syscall                      ; make the system call

