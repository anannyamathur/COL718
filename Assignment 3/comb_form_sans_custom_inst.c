#include <stdio.h>

int main()
{
    int c, A, X, n;

    A=100;
    X=10;
    n=10;
    
    int term1, term2, term3;

    printf ("Printing the equation \n");
    printf("(%u + %u)^ %u = ", A, X, n);

    term1=1;

        for (int i=1; i<=n; i++)
        {
            term1=term1*i;
        }

    for (int x=0; x<=n; x++)
    {
        term2=1;

        for (int i=1; i<=x; i++)
        {
            term2=term2*i;
        }

        term3=1;

        for (int i=1; i<=(n-x); i++)
        {
            term3=term3*i;
        }

        c=term1/(term2*term3);

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