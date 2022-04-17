#include <iostream>
#include <vector>

void test1();
int test2();
int test3(int param);

std::string test4(std::string param);
std::string test5(std::string param, int param2, float param3, double param4);
std::vector<std::string> test6(std::vector<std::string> paramList);
 
class ForwardDeclareType; 
ForwardDeclareType test7(ForwardDeclareType param);
