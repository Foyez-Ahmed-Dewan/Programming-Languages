.MODEL SMALL 
.STACK 100H 

.DATA
 
.CODE 
MAIN PROC 
    MOV AX, @DATA 
    MOV DS, AX  
     
    XOR BX, BX 
    MOV AH, 1 
    INT 21H 
     
    INPUT: 
        CMP AL, 0DH 
        JE NEXT 
        AND AL, 0FH  
        SHL BX, 1 
        OR BL, AL 
        INT 21H 
        JMP INPUT
        
         
    NEXT: 
        MOV AH, 2
        MOV DL, 10
        INT 21H
        MOV DL, 13
        INT 21H         
         
        MOV CX, 16
         
    OUTPUT:   
        SHL BX, 1 
        JC ONE 
        MOV DL, 0 
        JMP PRINT 
    ONE: 
        MOV DL, 1 
    PRINT: 
        ADD DL, 48 
        INT 21H 
        LOOP OUTPUT 
             
    EXIT: 
        MOV AH, 4CH 
        INT 21H 
    MAIN ENDP 
END MAIN  
