#include<stdio.h>
struct Fcfs
{
    int no,at,bt,wt,tt,st,ft;
};
struct Fcfs a[20],temp;
int tat,twt,i,j,t,k,n;
float average_tt,average_wt;
void details()
{
    printf("Enter the number of processes \t");
    scanf("%d",&n);
    printf("Enter the details \n");
    for(k=1;k<=n;k++)
    {
        printf("Enter process no \t");
        scanf("%d",&a[k].no);
        printf("Enter arrival time and burst time \t");
        scanf("%d%d",&a[k].at,&a[k].bt);
    }
}
void sort()
{
    for(i=1;i<=n-1;i++)
    {
        for(j=i+1;j<=n;j++)
        {
            if(a[i].at>a[j].at)
            {
                temp=a[i];
                a[i]=a[j];
                a[j]=temp;
            }
        }
    }
}
void process()
{

    int start=a[1].at,finish=0;
    for(i=1;i<=n;++i)
    {
        a[i].st=start;
        a[i].ft=a[i].st+a[i].bt;
        finish=a[i].ft;
        a[i].tt=finish-a[i].at;
        a[i].wt=a[i].tt-a[i].bt;
        start=finish;
    }
    printf("\n PgmnNo\t AT\t BT\t start\t WT\t CT\t TAT\n");
    for(i=1;i<=n;++i)
    {
        printf("%d \t%d \t%d \t%d \t%d \t%d \t%d \t\n",i,a[i].at,a[i].bt,a[i].st,a[i].wt,a[i].ft,a[i].tt);
        tat+=a[i].tt;
        twt+=a[i].wt;
    }
    average_tt=(float)tat/n;
    average_wt=(float)twt/n;
    printf("AVERAGE TURN AROUND TIME =%f\n",average_tt);
    printf("AVERAGE WAITING TIME =%f\n",average_wt);

}
void main()
{
    details();
    Sort();
    process();
}