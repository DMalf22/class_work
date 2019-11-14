/*
Domenic Malfetano
CPE 555 HW 3
*/

#include <stdio.h>
#include <stdlib.h>

int main() {
  int latD, latM, lonD, lonM; //units for output
  float lon, lat, temp, latS, lonS; //input for latitude and longitude
  char ns, ew; //cardinal directions

  //Input
  printf("Input Latitude: ");
  scanf("%f", &lat);
  printf("Input Longitude: " );
  scanf("%f", &lon);

  if(lat < 0){
    ns = 'S';
    lat*= -1;
  }

  else if (lat > 0){
    ns = 'N';
  }

  else {
    ns = ' ';
  }
  if(lon < 0){
    ew = 'W';
    lon*= -1;
  }

  else if (lon > 0){
    ew = 'E';
  }

  else {
    ew = ' ';
  }

  latD = (int) lat;
  lat = lat - latD;
  temp = lat * 60;
  latM = (int) temp;
  lat = temp - latM;
  temp = lat * 60;
  latS = temp;

  lonD = (int) lon;
  lon = lon - lonD;
  temp = lon * 60;
  lonM = (int) temp;
  lon = temp - lonM;
  temp = lon * 60;
  lonS = temp;

  printf("Latitude: %d Degrees, %d Minutes, %f Seconds, %c\n", latD, latM, latS, ns);
  printf("Longitude: %d Degrees, %d Minutes, %f Seconds, %c\n", lonD, lonM, lonS, ew);

  return 0;
  
}
