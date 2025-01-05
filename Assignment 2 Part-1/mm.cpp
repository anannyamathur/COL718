# include <stdarg.h>
#include <stdlib.h>
# include <time.h>
#include <stdio.h>

# include <math.h>
# include <limits.h> 

# include <string.h>

#include <string>


#ifndef _WIN32
#define set_random drand48()*100
#else
#define set_random (double(rand())/RAND_MAX)
#endif

void print_to_file(double** values, const char* filename, int n)
{
    FILE *f=fopen(filename,"w");

    for (int i=0; i<n; i++)
    {
        for(int j=0; j<n; j++)
        {
            fprintf(f,"%f",values[i][j]);
            fprintf(f," ");
        }
        fprintf(f,"\n");
    }
    fclose(f);
}

double** initialise(int n) // to allocate space to n by n matrix of double precision
{
double **M= (double **)calloc(n,sizeof(double*));

for (int i=0; i<n; i++)
{
 M[i]=(double *)calloc(n,sizeof(double));
 
 
    for( int j=0; j<n; j++)
        {                        // initialise M
            M[i][j]=set_random;
            
        }
 
 
}
return M;
}

double** allocate_space(int n)
{
    double** A= (double **)calloc(n,sizeof(double*));
    
for (int i=0; i<n; i++)
{
 A[i]=(double *)calloc(n,sizeof(double));
 
}

return A;

}

void multiply(double** A, double** B, double**C, int n)
{
    
    double norm=0.0;

    for (int i=0; i<n; i++)
    {
        for (int j=0; j<n; j++)
        {
            norm=0.0;
            for (int k=0; k<n; k++)
            {
                norm=norm + A[i][k]*B[k][j];
            }

            C[i][j]=norm;
        }
    }
    
    print_to_file(A,"Input Matrix-1",n);
    print_to_file(B,"Input Matrix-2",n);
    print_to_file(C,"Matrix Multiplication Product",n);
    

}


int main(int argc, char* argv[])
{
    
    //int N=atoi(argv[1]);
    int N=100;

    double **c=allocate_space(N);
    double **a=initialise(N);
    double **b=initialise(N);
    
    multiply(a,b,c,N);

    return 0;

}