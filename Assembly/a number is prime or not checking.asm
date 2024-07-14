.MODEL SMALL 
.STACK 100H 

.DATA 
    S DB 'Enter a number: $' 
    ST DB 10,13,'The Number is: $'  
    PR DB 'Prime $' 
    NP DB 'Not Prime $' 
    A DW ? 
    
.CODE 
    MAIN PROC 
        MOV AX, @DATA 
        MOV DS, AX   
     
        LEA DX, S 
        MOV AH, 9 
        INT 21H 
     
    
        MOV A, 0  
        MOV BX, 10         
    INPUT:             
        MOV AH, 1 
        INT 21H  
             
        CMP AL, 13 
        JE NEXT        
        
        SUB AL, 30H 
        MOV AH, 0        
        MOV CX, AX 
        MOV AX, A 
        MUL BX 
         
        ADD AX, CX 
        MOV A, AX 
        JMP INPUT
         
     NEXT:
       
        LEA DX, ST 
        MOV AH, 9 
        INT 21H 
         
        MOV CX, A 
        SUB CX, 2 
        MOV BL, 2
         
     L1:    
        MOV AX, A 
        DIV BL  
        CMP AH, 0 
        JE ERROR 
        INC BL 
        LOOP L1
          
        LEA DX, PR 
        MOV AH, 9 
        INT 21H 
        JMP EXIT
              
     ERROR:  
     
        LEA DX, NP 
        MOV AH, 9 
        INT 21H 
             
     EXIT: 
        MOV AH, 4CH 
        INT 21H 
    MAIN ENDP 
END MAIN  
