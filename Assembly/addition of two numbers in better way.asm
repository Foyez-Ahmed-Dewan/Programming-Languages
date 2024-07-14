.MODEL SMALL
.STACK 100H

.DATA

    ST DB "Enter your first number : $"
    STR DB 10, 13, "Enter your second number : $" 
    STT DB 10, 13, "SUBTRACTION IS = $"
    
    A   DB ?
    B   DB ?
    SUBS DB ?
    
.CODE
    MAIN PROC 
        MOV AX, @DATA
        MOV DS, AX
        
        LEA DX, ST
        MOV AH, 9
        INT 21H
        
        MOV AH, 1
        INT 21H  
        
        MOV A, AL
                   
                   
        LEA DX, STR
        MOV AH, 9
        INT 21H
        
        MOV AH, 1
        INT 21H
        
        MOV B, AL
        
        MOV AL, A
        SUB AL, B
        MOV SUBS, AL 
        
        MOV AH, 0
        
        AAA
        
        MOV BX, AX
        
        LEA DX, STT
        MOV AH, 9
        INT 21H
        
        
        MOV DL, BH
        ADD DL, 48
        
        MOV AH, 2
        INT 21H
        
        MOV DL, BL
        ADD DL, 48
        
        MOV AH, 2
        INT 21H
        
    
    
    
    MAIN ENDP
    
END MAIN