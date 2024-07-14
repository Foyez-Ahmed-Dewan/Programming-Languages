.MODEL SMALL 
.STACK 100H 

.DATA 
    CR DB 'CORRECT $'
    NCR DB 'INCORRECT $' 
    
.CODE  

MAIN PROC 
    MOV AX, @DATA 
    MOV DS, AX  
      
    XOR CX, CX 
    
    L1: 
        XOR BX, BX 
        MOV AH, 1 
        INT 21H 
         
        CMP AL, 13 
        JE NEWLINE  
         
        CMP AL, '(' 
        JE INSERT 
         
        CMP AL, ')' 
        JE REMOVE 
         
        JMP L1 
            INSERT: 
                    MOV BL, AL 
                    PUSH BX 
                    INC CX 
                    JMP L1   
            REMOVE:    
                    JCXZ PROBLEM 
                    POP DX 
                    DEC CX 
             
                    CMP DX, '(' 
                    JNE PROBLEM
             
                    JMP L1 
             NEWLINE:        
                    MOV AH, 2
                    INT 21H
                    MOV DL, 10, 13
                    INT 21H
       
         
                    CMP CX, 0 
                    JNE PROBLEM 
           
                    JMP AC
             
            AC: 
                    LEA DX, CR 
                    MOV AH, 9 
                    INT 21H 
                    JMP EXIT
             
            PROBLEM: 
                    LEA DX, NCR 
                    MOV AH, 9 
                    INT 21H
                     
            EXIT: 
                    MOV AH, 4CH 
                    INT 21H 
    MAIN ENDP 
END MAIN  
