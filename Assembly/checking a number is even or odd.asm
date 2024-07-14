.MODEL SMALL
.STACK 100H
.DATA

    S DB 'ENTER YOUR NUMBER : $'
    ST DB 10, 13, 'YOUR NUMBER IS : ODD $'
    STR DB 10, 13, 'YOUR NUMBER IS : EVEN $'
    
    A DB ?  
    B DB ?
  
 .CODE
    MAIN PROC
        MOV AX, @DATA
        MOV DS, AX
        
        LEA DX, S
        MOV AH, 9
        INT 21H  
        
        MOV AH, 1
        INT 21H
        SUB AL, 48
        
        AND AL, 1
        
        CMP AL, 0
        JE L1   
        
        LEA DX, ST
        MOV AH, 9
        INT 21H
         
        JMP EXIT
        
        L1: 
            LEA DX, STR
            MOV AH, 9
            INT 21H
               
               
    EXIT:    
        MOV AH, 4CH
        INT 21H 
            
   MAIN ENDP
    END MAIN
