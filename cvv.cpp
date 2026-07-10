#include <iostream>
#include <opencv2/opencv.hpp>
using namespace std;
using namespace cv;
int main()
{
    Mat img = imread("img.jpg");
    //Mat img(500,500,CV_8UC3);
    if (img.empty())
    {
        cout << "Could not load image!" << endl;
        return -1;
    }

    imshow("Image", img);

    waitKey(0);

    return 0;
}