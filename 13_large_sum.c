// Because this is trivial in languages like python and java.
// We're trying it in C

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
	char numbers[100][51];
	char sum[50];
	int rest=0;
	int i=0, x, firstNum=0, justNum;
	FILE *fp;
	
	fp=fopen("13_input.txt", "r");
	
	while(!feof(fp)){
		fgets(numbers[i], 52, fp);
		numbers[i][50]='\0';
		if(feof(fp)) break;
		i++;
	}
	
	fclose(fp);
	
	strcpy(sum, numbers[0]);
	
	for(i=1; i<100; i++){
		rest=0;
		for(x=49; x>=0; x--){
			justNum=sum[x]-48+numbers[i][x]-48+rest;
			if(justNum>9) {
				justNum-=10;
				rest=1;
			}
			else rest=0;
			sum[x]=justNum+48;
		}
		if(rest) firstNum++;
	}
	
	printf("%d %s\n", firstNum, sum);
		
	return 0;
}
