.MODEL SMALL 
.STACK 100H
.DATA 
.CODE
    ST  DB 'ENTER MULTIPLICAND : $'
    STR DB 10, 13, 'ENTER MULTIPLIER : $'
    STT DB 10, 13, 'PRODUCT : $'
    A DB ?
    B DB ?
MAIN PROC       
    MOV AX, @DATA
    MOV DS, AX

    MOV AH, 9
    LEA DX, ST
    INT 21H
    MOV AH, 1
    INT 21H
    SUB AL, 48
    MOV A, AL
    
    MOV AH, 9
    LEA DX, STR
    INT 21H
    MOV AH, 1
    INT 21H
    SUB AL, 48
    MOV B, AL
    
    MOV AH, 9
    LEA DX, STT
    INT 21H
    MOV AL, A
    MUL B

    AAM
    MOV BX, AX
    MOV DL, BH
    ADD DX, 48
    MOV AH, 2
    INT 21H

    MOV DL, BL
    ADD DL, 48
    MOV AH, 2
    INT 21H

    MAIN ENDP
END MAIN

         