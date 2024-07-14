.MODEL SMALL
.STACK 100H

.DATA
    A   DW 3
    B   DW 5
    DIF DW ?
    
.CODE
    MAIN PROC
        MOV AX, @DATA
        MOV DS, AX
        
        MOV AX, A
        SUB AX, B 
        NEG AX       
        MOV DIF, AX
       
        
        MOV BX, AX                          
        MOV DX, '-'
        MOV AH, 2
        INT 21H
      
        
        MOV DL, BL
        ADD DL, 48
        MOV AH, 2
        INT 21H
        
    
    MAIN ENDP
END MAIN    
