.global _start
_start:
	MOV r0,#4294967040
    MOV r1,#0xf
	ADD r2,r0,r1    
	
	SWI 0