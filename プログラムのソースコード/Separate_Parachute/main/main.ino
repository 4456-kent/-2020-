#include<Wire.h>

#define MPU6050_ADDR 0x68
#define SAMPLING_RATE 50
#define ACCEL_SCALE_MODIFIER 8192
#define ACCEL_RANGE 4

#define BME280_ADDR 0x76
#define STANDARD_PRESSURE 1013.0  //実際に測定して代入

//加速度データ
int16_t acc_x_mesure,acc_y_mesure,acc_z_mesure;
float acc_x,acc_y,acc_z,synthetic_acc;

//気温補正データ
uint16_t dig_T1;
int16_t  dig_T2;
int16_t  dig_T3;

//気圧補正データ
uint16_t dig_P1;
int16_t  dig_P2;
int16_t  dig_P3;
int16_t  dig_P4;
int16_t  dig_P5;
int16_t  dig_P6;
int16_t  dig_P7;
int16_t  dig_P8;
int16_t  dig_P9;

unsigned char dac[26];
unsigned int i;

int32_t t_fine;
int32_t adc_P, adc_T;

float get_value_acc();
float get_value_alt();

void setup() {
  Wire.begin();
  
  Wire.beginTransmission(MPU6050_ADDR);   /*MPU6050のセットアップ*/
  Wire.write(0x6B);
  Wire.write(0x80);
  Wire.endTransmission();
  delay(250);
  Wire.beginTransmission(MPU6050_ADDR);
  Wire.write(0x6B);
  Wire.write(0x00);
  Wire.endTransmission();
  delay(250);
  Wire.beginTransmission(MPU6050_ADDR);
  Wire.write(0x6A);
  Wire.write(0x07);
  Wire.endTransmission();
  delay(250);
  Wire.beginTransmission(MPU6050_ADDR);
  Wire.write(0x6A);
  Wire.write(0x00);
  Wire.endTransmission();
  delay(250);
  Wire.beginTransmission(MPU6050_ADDR);
  Wire.write(0x1C);
  Wire.write(0x08);
  Wire.endTransmission();
  Wire.beginTransmission(MPU6050_ADDR);
  Wire.write(0x1B);
  Wire.write(0x08);
  Wire.endTransmission();
  Wire.beginTransmission(MPU6050_ADDR);
  Wire.write(0x1A);
  Wire.write(0x00);
  Wire.endTransmission();

  Wire.beginTransmission(BME_280_ADDR);   /*BME280のセットアップ*/
  Wire.write(0xF2);
  Wire.write(0x01);
  Wire.endTransmission();
  Wire.beginTransmission(BME_280_ADDR);   
  Wire.write(0xF4);
  Wire.write(0x27);
  Wire.endTransmission();
  Wire.beginTransmission(BME_280_ADDR);   
  Wire.write(0xF5);
  Wire.write(0xA0);
  Wire.endTransmission();

   //BME280補正データ取得
  Wire.beginTransmission(BME280_ADDR);//I2Cスレーブ「Arduino Uno」のデータ送信開始
  Wire.write(0x88);//出力データバイトを「補正データ」のアドレスに指定
  Wire.endTransmission();//I2Cスレーブ「Arduino Uno」のデータ送信終了
  
  Wire.requestFrom(BME280_ADDR, 26);//I2Cデバイス「BME280」に26Byteのデータ要求
  for (i=0; i<26; i++){
    while (Wire.available() == 0 ){}
    dac[i] = Wire.read();//dacにI2Cデバイス「BME280」のデータ読み込み
  }
  
  dig_T1 = ((uint16_t)((dac[1] << 8) | dac[0]));
  dig_T2 = ((int16_t)((dac[3] << 8) | dac[2]));
  dig_T3 = ((int16_t)((dac[5] << 8) | dac[4]));

  dig_P1 = ((uint16_t)((dac[7] << 8) | dac[6]));
  dig_P2 = ((int16_t)((dac[9] << 8) | dac[8]));
  dig_P3 = ((int16_t)((dac[11] << 8) | dac[10]));
  dig_P4 = ((int16_t)((dac[13] << 8) | dac[12]));
  dig_P5 = ((int16_t)((dac[15] << 8) | dac[14]));
  dig_P6 = ((int16_t)((dac[17] << 8) | dac[16]));
  dig_P7 = ((int16_t)((dac[19] << 8) | dac[18]));
  dig_P8 = ((int16_t)((dac[21] << 8) | dac[20]));
  dig_P9 = ((int16_t)((dac[23] << 8) | dac[22]));

  dig_H1 = ((uint8_t)(dac[25]));

  Wire.beginTransmission(BME280_ADDR);//I2Cスレーブ「Arduino Uno」のデータ送信開始
  Wire.write(0xE1);//出力データバイトを「補正データ」のアドレスに指定
  Wire.endTransmission();//I2Cスレーブ「Arduino Uno」のデータ送信終了
  
  Wire.requestFrom(BME280_ADDR, 7);//I2Cデバイス「BME280」に7Byteのデータ要求
  for (i=0; i<7; i++){
    while (Wire.available() == 0 ){}
    dac[i] = Wire.read();//dacにI2Cデバイス「BME280」のデータ読み込み
  }
  
  dig_H2 = ((int16_t)((dac[1] << 8) | dac[0]));
  dig_H3 = ((uint8_t)(dac[2]));
  dig_H4 = ((int16_t)((dac[3] << 4) + (dac[4] & 0x0F)));
  dig_H5 = ((int16_t)((dac[5] << 4) + ((dac[4] >> 4) & 0x0F)));
  dig_H6 = ((int8_t)dac[6]);
  
  delay(1000);//1000msec待機(1秒待機)
}

float get_value_acc() {
  Wire.beginTransmission(MPU6050_ADDR);
  Wire.write(0x3B);
  Wire.endTransmission();
  Wire.requestFrom(MPU6050_ADDR,14);
  while(Wire.available()<14){
    acc_x_mesure=Wire.read()<<8|Wire.read();
    acc_y_mesure=Wire.read()<<8|Wire.read();
    acc_z_mesure=Wire.read()<<8|Wire.read();
  }
  if(acc_x_mesure<=ACCEL_SCALE_MODIFIER*ACCEL_RANGE){
    acc_x=acc_x_mesure/ACCEL_SCALE_MODIFIER;
  }else if(acc_x_mesure>ACCEL_SCALE_MODIFIER*ACCEL_RANGE){
    acc_x=acc_x_mesure/ACCEL_SCALE_MODIFIER-ACCEL_RANGE*2;
  }
  if(acc_y_mesure<=ACCEL_SCALE_MODIFIER*ACCEL_RANGE){
    acc_y=acc_y_mesure/ACCEL_SCALE_MODIFIER;
  }else if(acc_y_mesure>ACCEL_SCALE_MODIFIER*ACCEL_RANGE){
    acc_y=acc_y_mesure/ACCEL_SCALE_MODIFIER-ACCEL_RANGE*2;
  }
  if(acc_z_mesure<=ACCEL_SCALE_MODIFIER*ACCEL_RANGE){
    acc_z=acc_z_mesure/ACCEL_SCALE_MODIFIER;
  }else if(acc_z_mesure>ACCEL_SCALE_MODIFIER*ACCEL_RANGE){
    acc_z=acc_z_mesure/ACCEL_SCALE_MODIFIER-ACCEL_RANGE*2;
  }

  synthetic_acc=sqrt(pow(acc_x,2)+pow(acc_y,2)+pow(acc_z,2));
  return(synthetic_acc);
}

float get_value_alt(){
   int32_t  temp_cal;
   uint32_t pres_cal;
   float temp,pres;

   Wire.beginTransmission(BME280_ADDR);//I2Cスレーブ「Arduino Uno」のデータ送信開始
   Wire.write(0xF7);//出力データバイトを「気圧データ」のアドレスに指定
   Wire.endTransmission();//I2Cスレーブ「Arduino Uno」のデータ送信終了
  
  Wire.requestFrom(BME280_ADDR, 8);//I2Cデバイス「BME280」に6Byteのデータ要求
  for (i=0; i<6; i++){
    while (Wire.available() == 0 ){}
    dac[i] = Wire.read();//dacにI2Cデバイス「BME280」のデータ読み込み
  }

  adc_P = ((uint32_t)dac[0] << 12) | ((uint32_t)dac[1] << 4) | ((dac[2] >> 4) & 0x0F);
  adc_T = ((uint32_t)dac[3] << 12) | ((uint32_t)dac[4] << 4) | ((dac[5] >> 4) & 0x0F);

  pres_cal = BME280_compensate_P_int32(adc_P);//気圧データ補正計算
  temp_cal = BME280_compensate_T_int32(adc_T);//温度データ補正計算

  pres = (float)pres_cal / 100.0;//気圧データを実際の値に計算
  temp = (float)temp_cal / 100.0;//温度データを実際の値に計算

  alt=(pow(STANDARD_PRESSURE/pres,1/5.257)-1)*(temp+273.15)/0.0065;

    return(alt);
}

//温度補正 関数
int32_t BME280_compensate_T_int32(int32_t adc_T)
{
  int32_t var1, var2, T;
  var1  = ((((adc_T>>3) - ((int32_t)dig_T1<<1))) * ((int32_t)dig_T2)) >> 11;
  var2  = (((((adc_T>>4) - ((int32_t)dig_T1)) * ((adc_T>>4) - ((int32_t)dig_T1))) >> 12) * ((int32_t)dig_T3)) >> 14;
  t_fine = var1 + var2;
  T  = (t_fine * 5 + 128) >> 8;
  return T;
}
//気圧補正 関数
uint32_t BME280_compensate_P_int32(int32_t adc_P)
{
  int32_t var1, var2;
  uint32_t p;
  var1 = (((int32_t)t_fine)>>1) - (int32_t)64000;
  var2 = (((var1>>2) * (var1>>2)) >> 11 ) * ((int32_t)dig_P6);
  var2 = var2 + ((var1*((int32_t)dig_P5))<<1);
  var2 = (var2>>2)+(((int32_t)dig_P4)<<16);
  var1 = (((dig_P3 * (((var1>>2) * (var1>>2)) >> 13 )) >> 3) + ((((int32_t)dig_P2) * var1)>>1))>>18;
  var1 =((((32768+var1))*((int32_t)dig_P1))>>15);
  if (var1 == 0)
  {
    return 0; // avoid exception caused by division by zero
  }
  p = (((uint32_t)(((int32_t)1048576)-adc_P)-(var2>>12)))*3125;
  if (p < 0x80000000)
  {
    p = (p << 1) / ((uint32_t)var1);
  }
  else
  {
    p = (p / (uint32_t)var1) * 2;
  }
  var1 = (((int32_t)dig_P9) * ((int32_t)(((p>>3) * (p>>3))>>13)))>>12;
  var2 = (((int32_t)(p>>2)) * ((int32_t)dig_P8))>>13;
  p = (uint32_t)((int32_t)p + ((var1 + var2 + dig_P7) >> 4));
  return p;
}

void loop(){
  
}
