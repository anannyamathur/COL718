#include <stdio.h>

int main()
{
    int c, A, X, n;

    A=100;
    X=10;
    n=10;
    
    printf ("Printing the equation \n");
    printf("(%u + %u)^ %u = ", A, X, n);

    for (int x=0; x<=n; x++)
    {
        asm
        (
            "comb_form   %[z], %[x], %[y]\n\t" 
            : [z] "=r" (c)
            : [x] "r" (n), [y] "r" (x)

        );

        if (x == n)
        {
            printf("%u*%u^%u*%u^%u \n", c,A,(n-x),X,x);
        }
        else
        {
            printf("%u*%u^%u*%u^%u + ", c,A,(n-x),X,x);
        }
    }

   printf("___________________________________________________ \n");
}