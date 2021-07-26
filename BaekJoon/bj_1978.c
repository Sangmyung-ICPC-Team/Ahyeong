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
	int N, num, cnt;

	scanf("%d", &N);

	cnt = 0;

	for (int i = 0; i < N; i++) {
		scanf("%d", &num);
		if (is_prime(num))
			cnt++;
	}

	printf("%d", cnt);

	return 0;
}