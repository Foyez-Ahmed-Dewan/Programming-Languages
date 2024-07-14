.MODEL SMALL
.STACK 100H
.DATA

.CODE
    S    DB         'DIVIDEND : $'
    ST   DB 10, 13, 'DIVISOR : $'
    STR  DB 10, 13, 'QUOTIENT : $'
    STRR DB 10, 13, 'REMAINDER : $' 
    A DB ?
    B DB ?
    R DB ?

MAIN PROC 
    MOV AX, @DATA
    MOV DS, AX

    LEA DX, S
    MOV AH, 9
    INT 21H
    MOV AH, 1
    INT 21H
    SUB AL, 48
    MOV A, AL   
    
    LEA DX, ST
    MOV AH, 9
    INT 21H
    MOV AH, 1
    INT 21H
    SUB AL, 48
    MOV B, AL
    
    LEA DX, STR
    MOV AH, 9
    INT 21H  
    
    MOV BX, 0
    MOV BL, A
    MOV AX, BX 
    
    DIV B      
    MOV R, AH
    MOV DL, AL
    ADD DL, 48
    MOV AH, 2
    INT 21H 
      
    LEA DX, STRR
    MOV AH, 9
    INT 21H  
    
    MOV DL, R
    ADD DL, 48
    MOV AH, 2
    INT 21H

    MAIN ENDP
END MAIN
        




