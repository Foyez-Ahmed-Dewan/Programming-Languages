 ;;; Directives
    PRESERVE8
    THUMB       
 
; Vector Table Mapped to Address 0 at Reset
; Linker requires __Vectors to be exported

    AREA    RESET, DATA, READONLY
    EXPORT  __Vectors
 
__Vectors 
    DCD  0x20001000 
      ; stack pointer value when stack is empty
    DCD  Reset_Handler  ; reset vector
    ALIGN
 
; The program
; Linker requires Reset_Handler
    AREA    MYCODE, CODE, READONLY
 
    ENTRY
    EXPORT Reset_Handler
 
 


Reset_Handler
;;;;;;;;;;User Code Starts from the next line;;;;;;;;;;;;
	; X = 10

	MOV R0, #0x20000000
	MOV R9, #10
	
	STR R9, [R0, #1]
	
	MOV R4, #0		; Y = 0
	 
	
WHILE
	LDR R6, [R0, #1]
	
	CMP R6, #0
	BEQ TARGET
	
	LSL R4, R6, #2
	SUB R6, R6, #1
	
	STR R6, [R0, #1]
	
	B WHILE
	

TARGET

STOP  
   B  STOP    
   
   END	;End of the program
