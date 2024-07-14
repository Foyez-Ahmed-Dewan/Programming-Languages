.MODEL SMALL
.STACK 100H

.DATA

    STR DB "HELLO WORLD$" 
    ST  DB 10,13, "FOYEZ$"    ; 10,13, is used to print new line    
    STT DB 10,13, 41H,42H,'C', 24H
    
.CODE
    MAIN PROC
        MOV AX, @DATA
        MOV DS, AX
          
        LEA DX, STR
        MOV AH, 9
        INT 21H     
        
        ;MOV AH, 2
        ;MOV DL, 10         ; this box is also used to print new line
        ;INT 21H
        ;MOV DL, 13
        ;INT 21H
        
        LEA DX, ST
        MOV AH, 9
        INT 21H 
        
        LEA DX, STT
        MOV AH, 9
        INT 21H
        
        
    MAIN ENDP
END MAIN