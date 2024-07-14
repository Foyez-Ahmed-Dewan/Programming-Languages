.MODEL SMALL            ; "small" represent file size
.STACK 100h             ; "stack" is used to hold temporary variable, 
.DATA
    A DW 2
    B DW 8 
    SUM DW ?
.CODE
    MAIN PROC
        MOV AX,@DATA    
        MOV DS,AX
    
        MOV AX, A
        ADD AX, B
        MOV SUM, AX 
        
        AAA       
        
        MOV BX, AX
        
        ;PRINTING 1 FIRST
        MOV DL, BH
        ADD DL, 48
        ;ADD DX, 30H  ; YOU CAN USE THIS ALSO
        
        MOV AH, 2
        INT 21H 
        
        ;PRINTING 0 SECOND
        MOV DL, BL
        ADD DL, 48
        
        MOV AH, 2
        INT 21H                                           
    
    MAIN ENDP
    
 END MAIN