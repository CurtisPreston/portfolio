
// https://open.kattis.com/problems/lastfactorialdigit
// Last Factorial Digit
#include <stdio.h>
#include <stdlib.h>
#include <cstring>

int Factorial(int x);

int main(int argc, char const *argv[]) {
  char Nu[10];


  scanf("%s",&Nu );



  int n;
  n=atoi(Nu);


  while (n>0) {
    int x;
    char in[10];
    scanf("%s",&in );
    x=atoi(in);

    sprintf(in, "%d", Factorial(x));

    printf("%c\n",in[strlen(in)-1]);
    n--;
  }


  return 0;
}


int Factorial(int x){
  int out=1;

  for(int i=1; i<=x; ++i)
        {
            out *= i;              // factorial = factorial*i;
        }

  return out;
}
