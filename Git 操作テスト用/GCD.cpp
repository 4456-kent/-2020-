#include <bits/stdc++.h>
using namespace std;

//公約数
void div(long long a, vector<long long> &n) {
  n.push_back(1);
  for (long long i = 2; i <= sqrt(a); i++)
    if (a % i == 0) n.push_back(i);
  if (n.at(n.size() - 1) == sqrt(a))
    for (long long i = n.size() - 2; i >= 0; i--)
      n.push_back(a / n.at(i));
  else
    for (long long i = n.size() - 1; i >= 0; i--)
      n.push_back(a / n.at(i));
  return;
}

void comdiv(long long a, long long b, vector<long long> &n) {
  if (a > b) swap(a, b);
  vector<long long> m(0);
  div(a, m);
  for (long long i = 0; i < m.size(); i++)
    if (b % m.at(i) == 0) n.push_back(m.at(i));
  return;
}

int main() {
  long long a, b;
  cin >> a >> b;
  vector<long long> n(0);
  comdiv(a, b, n);
  cout << n.at(n.size() - 1) << endl;
}
