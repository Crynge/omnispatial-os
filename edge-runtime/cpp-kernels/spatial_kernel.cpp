#include <cmath>
#include <iostream>

double signal_score(double traffic, double event_heat) {
    return traffic * 0.6 + event_heat * 40.0;
}

int main() {
    std::cout << signal_score(0.72, 0.61) << std::endl;
    return 0;
}

