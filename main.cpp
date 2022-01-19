#include <iostream>
#include <vector>

using namespace std;

int main()
{
  vector<int> a;
  a.push_back(5);
  a.push_back(50);

  for (int i = 0; i < a.size(); i++)
  {
    cout << a[i] << endl;
  }

  return 0;
}
