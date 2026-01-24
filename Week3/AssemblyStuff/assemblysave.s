.global _start
_start:
	MOV r0,#4294967040
    MOV r1,#0xf
	ADD r2,r0,r1
	ORR r3,r1,r0
	
	SWI 0