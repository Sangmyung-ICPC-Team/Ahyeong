#include <stdio.h>

int is_prime(int n) {
	if (n == 1)
		return 0;

	for (int i = 2; i <= n / 2; i++) {
		if ((n % i) == 0)
			return 0;
	}

	return 1;
}

int main()
{
	int M, N, flag, sum, min;

	scanf("%d", &M);
	scanf("%d", &N);

	flag = sum = 0;
	min = 10001;

	for (int i = M; i <= N; i++) {
		if (is_prime(i))
		{
			flag = 1;
			sum += i;

			if (min > i)
				min = i;
		}
	}

	if (flag == 0)
		printf("-1");

	else
		printf("%d\n%d", sum, min);

	return 0;
}