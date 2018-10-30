#include <string.h>
#include "stdio.h"

int getStringValue(char *x);
int getCharValue(char c);
void rotate(char *p);
char getValueChar(int x);
char rotateChar(char c,int amount);

int strlenc;

int main(int argc, char const *argv[]) {

  char c[15000];

  scanf("%s",c);

  strlenc=strlen(c)/2;

  char h1[strlenc];
  char h2[strlenc];
  int x;

  memcpy(h1, &c[0], strlenc*sizeof(*c));
  memcpy(h2, &c[strlenc], strlenc*sizeof(*c));


  h1[strlen(h1)]='\0';
  h2[strlen(h2)]='\0';

  rotate(h1);
  rotate(h2);


  char out[strlenc];
  int i=0;
  for(i=0;i<strlenc;i++){
    out[i]=rotateChar(h1[i],getCharValue(h2[i]));
  }
  out[strlenc]='\0';
  printf("%s\n", out);

  return 0;
}

char rotateChar(char c,int amount){
  int chaV=getCharValue(c);

  chaV+=amount;

  while(chaV>25){
    chaV-=26;
  }
  char newC=getValueChar(chaV);

  return newC;
}


void rotate(char *p){
  int amount=getStringValue(p);
  for(int c=0;c<strlenc;c++){
    int chaV=getCharValue(p[c]);

    chaV+=amount;

    while(chaV>25){
      chaV-=26;
    }
    p[c]=getValueChar(chaV);

  }
}


int getStringValue(char *x){
  int count=0;

  for(int i=0;i<strlenc;i++){
    count+=getCharValue(x[i]);
  }
  return count;

}


int getCharValue(char c){
  int x=c;

  x=x-65;
  return x;

}

char getValueChar(int x){
  char c=x;

  c=c+65;
  return c;

}
