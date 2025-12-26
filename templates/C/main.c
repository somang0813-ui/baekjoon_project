#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int n;
    if (scanf("%d", &n) != 1)
        return 0;

    for (int i = 0; i < n; i++)
    {
        int x;
        scanf("%d", &x);
        // 처리
    }

    printf("done\n");
    return 0;
}
