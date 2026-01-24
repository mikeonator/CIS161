.global _start
_start:
    @Step 1
	MOV r0,#4294967040

    @Step 2
    MOV r1,#0xf

    @Step 3
	ADD r2,r0,r1

    @Step 4
	ORR r3,r1,r0
	
    @Step 5
    MOV r4,#0x00000040
    STR r0,[r4]

    @Step 6
    MOV r5,#0x4D
    MOV r6,#0x41

	SWI 0