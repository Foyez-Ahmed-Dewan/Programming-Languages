
;Suppose, a 2D array of size 5 X 6 is declared in row major 
;order. Write an assembly program to clear the 3rd row and 3rd column of the array.

.MODEL SMALL
 .STACK 100H
 
 .DATA
    A DW 1, 1, 1, 1, 1, 1
      DW 1, 1, 1, 1, 1, 1
      DW 1, 1, 1, 1, 1, 1
      DW 1, 1, 1, 1, 1, 1
      DW 1, 1, 1, 1, 1, 1
    
    CNT DW ?
         
         
 .CODE
    MAIN PROC
        MOV AX, @DATA
        MOV DS, AX
     
        
        MOV BX, 24
        XOR SI, SI
        MOV CX, 6
    
    TOP:
        MOV A[BX][SI], 0
        ADD SI, 2
        LOOP TOP 
        
                
        
        MOV SI, 4
        XOR BX, BX
        MOV CX, 5
        
     TOP2:
        MOV A[BX][SI], 0
        ADD SI, 12
        LOOP TOP2 
        
        
        ; SET COUNTER = 30 AS 5 * 6 = 30 
        MOV CX, 30
        LEA BX, A 
        ;INITIALIZING CNT = 0
        MOV AX, 0
        MOV CNT, AX
                  
     PRINT:
        MOV DX, [BX]
        ADD DX, 48
        MOV AH, 2
        INT 21H 
        
        MOV DL, ' '
        INT 21H
        
        INC CNT
        CMP CNT, 6
        JNE LEVEL
        
        MOV AH, 2
        MOV DL, 0DH
        INT 21H
        MOV DL, 0AH
        INT 21H
        
        MOV AX, 0
        MOV CNT, AX
        
    LEVEL:
        ADD BX, 2
        LOOP PRINT
     
    EXIT:
        MOV AH, 4CH
        INT 21H
        
         
     
        
        
         
        
        
        
    MAIN ENDP
END MAIN