.MODEL SMALL
.STACK 100H

.DATA

.CODE
   MAIN PROC
   
   MOV AX, @DATA
   MOV DS, AX
   
   XOR CX, CX
   XOR BX, BX
   MOV AH, 1
   
TAKE_INPUT: 
    INT 21H
    CMP AL, 0DH
    JE NEW_LINE 
    
    INC CX 
    MOV BL,AL
    
    PUSH BX
    JMP TAKE_INPUT   
    
NEW_LINE: 
    MOV AH, 2
    MOV DL, 0DH
    INT 21H
    MOV DL, 0AH
    INT 21H
    JCXZ EXIT
    
    
OUTPUT:  
    POP DX 
    INT 21H
    LOOP OUTPUT
       
    
EXIT:
    MOV AH, 4CH
    INT 21H
    
    
    MAIN ENDP
END MAIN