//#include <stdio.h>
#include <stdlib.h>

int main()
{
	int T = 0;
	int P2[4] = {6,2,4,8};
	int P3[4] = {1,3,9,7};
	int P7[4] = {1,7,9,3};
	int P8[4] = {6,8,4,2};

	scanf_s("%d", &T);

	int* a = (int*)malloc(sizeof(int) * T);
	int* b = (int*)malloc(sizeof(int) * T);

	int temp = 0;
	int ans = 0;
	int r = 0;

	for (int i = 0; i < T; i++)
	{
		scanf_s("%d %d", &a[i], &b[i]);
	}

	for (int i = 0; i < T; i++)
	{
		temp = a[i] % 10;
		r = b[i] % 4;

		if (temp == 0) ans = 10;
		else if (temp == 1 || temp == 5 || temp == 6)
		{
			ans = temp;
		}
		else if (temp == 4) ans = (b[i] % 2 == 1) ? 4 : 6;
		else if (temp == 9) ans = (b[i] % 2 == 1) ? 9 : 1;
		else
		{
			if (temp == 2) ans = P2[r];
			else if (temp == 3) ans = P3[r];
			else if (temp == 7) ans = P7[r];
			else ans = P8[r];
		}
		printf("%d \n", ans);
	}
	free(a);
	free(b);
}
