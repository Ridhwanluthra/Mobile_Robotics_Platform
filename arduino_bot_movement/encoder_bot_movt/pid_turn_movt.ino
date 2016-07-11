#include "I2Cdev.h"

#include "MPU6050_6Axis_MotionApps20.h"

#if I2CDEV_IMPLEMENTATION == I2CDEV_ARDUINO_WIRE
    #include "Wire.h"
#endif

MPU6050 mpu;

#define OUTPUT_READABLE_EULER


//Defined for IMU

bool dmpReady = false;  // set true if DMP init was successful
uint8_t mpuIntStatus;   // holds actual interrupt status byte from MPU
uint8_t devStatus;      // return status after each device operation (0 = success, !0 = error)
uint16_t packetSize;    // expected DMP packet size (default is 42 bytes)
uint16_t fifoCount;     // count of all bytes currently in FIFO
uint8_t fifoBuffer[64]; // FIFO storage buffer


Quaternion q;           // [w, x, y, z]         quaternion container
VectorInt16 aa;         // [x, y, z]            accel sensor measurements
VectorInt16 aaReal;     // [x, y, z]            gravity-free accel sensor measurements
VectorInt16 aaWorld;    // [x, y, z]            world-frame accel sensor measurements
VectorFloat gravity;    // [x, y, z]            gravity vector
float euler[3];         // [psi, theta, phi]    Euler angle container
float ypr[3];           // [yaw, pitch, roll]   yaw/pitch/roll container and gravity vector

volatile bool mpuInterrupt = false;     // indicates whether MPU interrupt pin has gone high
float init_imu;


// for motor movement
int rf =9 ,rb =10,lf=5,lb=6;
int motor_speed =100; //(0-255)

// for PID
int power_difference, encoderleft, encoderright, proportional;
int base, next;
const int maximum = 100;


// for encoders
double unit_distance = .9507;
int deg_dis = 3;
int x;
int y;
int a, b;

int enc_rtcount = 0, enc_ltcount = 0;
int r_en = 7, l_en = 3;


int count = 0;


void dmpDataReady() {
    mpuInterrupt = true;
}
void setup() {
  // BEGIN IMU INIT
  #if I2CDEV_IMPLEMENTATION == I2CDEV_ARDUINO_WIRE
      Wire.begin();
      TWBR = 24; // 400kHz I2C clock (200kHz if CPU is 8MHz)
  #elif I2CDEV_IMPLEMENTATION == I2CDEV_BUILTIN_FASTWIRE
      Fastwire::setup(400, true);
  #endif
  Serial.begin(115200);

  while (!Serial); // wait for Leonardo enumeration, others continue immediately
  Serial.println(F("Initializing I2C devices..."));
  mpu.initialize();

  Serial.println(F("Testing device connections..."));
  Serial.println(mpu.testConnection() ? F("MPU6050 connection successful") : F("MPU6050 connection failed"));


  Serial.println(F("\nSend any character to begin DMP programming and demo: "));
  while (Serial.available() && Serial.read()); // empty buffer
  while (!Serial.available());                 // wait for data
  while (Serial.available() && Serial.read()); // empty buffer again

  Serial.println(F("Initializing DMP..."));
  devStatus = mpu.dmpInitialize();

  mpu.setXGyroOffset(220);
  mpu.setYGyroOffset(76);
  mpu.setZGyroOffset(-85);
  mpu.setZAccelOffset(1788); // 1688 factory default for my test chip

  if (devStatus == 0) {
      Serial.println(F("Enabling DMP..."));
      mpu.setDMPEnabled(true);

      Serial.println(F("Enabling interrupt detection (Arduino external interrupt 0)..."));
      attachInterrupt(0, dmpDataReady, RISING);
      mpuIntStatus = mpu.getIntStatus();

      Serial.println(F("DMP ready! Waiting for first interrupt..."));
      dmpReady = true;

      packetSize = mpu.dmpGetFIFOPacketSize();
  }
  else {
      Serial.print(F("DMP Initialization failed (code "));
      Serial.print(devStatus);
      Serial.println(F(")"));
  }
  // END IMU INIT
  
  // encoder pins
  pinMode(r_en, INPUT);
  pinMode(l_en, INPUT);
  // motor pins
  pinMode(lf, OUTPUT);
  pinMode(lb, OUTPUT);
  pinMode(rf, OUTPUT);
  pinMode(rb, OUTPUT);
  
  while(millis() < 20000) {
    init_imu = imu_read();
  }
  base = imu_read();
}


void loop() {
  if (count == 0) {
    imu_read();
    
//        base=imu_read();
//    forward_movt(110);


    // turn_right(20);
   //  base=imu_read();
    // forward_movt(30);
    
    
        //   turn_left(20);
    //  base=imu_read();
      forward_movt(30);
//      
//      
//      
//         base=imu_read();
//         forward_movt(30);
//             
//             
//             
//             turn_right(20);
        
    count =1;
  }
}



void forward_movt (int dist){
  int no_of_spokes = (int)(dist/unit_distance);
  //Serial.println(no_of_spokes);

  while(enc_ltcount <= no_of_spokes/2) {
    //call_rtenc();
    Serial.println(enc_ltcount);
    call_ltenc();
    //imu_read();
    next = imu_read_off();
    /*Serial.print(base);
    Serial.print("\t");
    Serial.print(next);
    Serial.println("\t");*/
       if(next<180)
       {proportional = next ;
       }else if(next>=180)
       {
         proportional=next-360;
       }
   //prortional = next - base+offset;
 
//    Serial.println("proportional---");
//    Serial.println(proportional);
//    Serial.println("base---");
//    Serial.println(base);
//    Serial.println("next---");
//    Serial.println(next);
//    Serial.println("--------------");
    power_difference = proportional*25;
    
    //Serial.print(proportional);
    //Serial.print("  ");
/*    if (proportional > 10) {
      sstop();
      delay(1000);
      left();
      delay(300);
      proportional = 0;
    }
    if (proportional < -10) {
      sstop();
      delay(1000);
      right();
      delay(300);
      proportional = 0;
    }*/

    if (power_difference > maximum)
      power_difference = maximum;
    if (power_difference < -maximum)
      power_difference = -maximum;    
    //Serial.println(call_rtenc());
    forward();
  }
  enc_ltcount = 0;
  enc_rtcount = 0;
  sstop();
  delay(3000);
}

void turn_right(float deg){
  float to_turn = init_imu +deg;
  if(to_turn >= 360){
    greater_rt(to_turn);
  }
  else{
    while(to_turn >=imu_read() ) {
      right();
      
    }
  }
  
 sstop();    
  init_imu = imu_read();
}

void greater_rt(float to_turn){
  to_turn=to_turn-360;
  while(imu_read()<358 && imu_read()>3){
    right();
  }
  sstop();
  delay(200);
  while(imu_read()<to_turn){
    right();
  }
  sstop();
}



void turn_left(float deg){
  float to_turn =init_imu- deg;
  Serial.println(to_turn);
  if(to_turn<0){
    lesser_lt(to_turn);
  }
  else{
      Serial.println("\n");
    Serial.println(imu_read());
    while (to_turn < imu_read()){
      left();
    }
  }
  sstop();
  init_imu=imu_read();
}

void lesser_lt(float to_turn){
  to_turn=to_turn+360;
  while(imu_read() > 2 && imu_read() < 358){
    left();
  }
  while(imu_read()>to_turn){
    left();
  }
  sstop();
}


int call_rtenc() {
  b = a;
  a = digitalRead(r_en);
  
  if((a == 0 && b == 1) || (a == 1 && b == 0)) {
    enc_rtcount++;
  }
  return enc_rtcount;
}

int call_ltenc() {
  y = x;
  x = digitalRead(l_en);
  
  if((y == 0 && x == 1) || (y == 1 && x == 0)) {
    enc_ltcount++;

  }
  return enc_ltcount;
}

void forward(){
  if (power_difference < 0)//moving left -----errooor 
  {
    analogWrite(rf, (maximum + power_difference));  ////////////right motor at less speed so that bot moves right
    analogWrite(rb,LOW);
    analogWrite(lf, maximum);
    analogWrite(lb,LOW);
    
//    Serial.print("PW > 0");
//    Serial.print("  ");
//    Serial.print("right");
//    Serial.print("  ");
//    Serial.print(maximum + power_difference);
//    Serial.print("  ");
//    Serial.print("left");
//    Serial.print("  ");
//    Serial.print(maximum);
//    Serial.println("  ");
  }
  else //moving right -------errror
  {
    analogWrite(rf,maximum);
    analogWrite(rb, LOW);
    analogWrite(lf, maximum - power_difference);/// left motor is at less speed so that bot moves left
    analogWrite(lb, LOW);
    
//    Serial.print("PW > 0");
//    Serial.print("  ");
//    Serial.print("right");
//    Serial.print("  ");
//    Serial.print(maximum);
//    Serial.print("  ");
//    Serial.print("left");
//    Serial.print("  ");
//    Serial.print(maximum - power_difference);
//    Serial.println("  ");
  }
} 
void sstop() {
  digitalWrite(lf,LOW);
  digitalWrite(lb,LOW);
  digitalWrite(rb,LOW);
  digitalWrite(rf,LOW);
}
void backward(){
  analogWrite(rf,LOW);
  analogWrite(rb,motor_speed);
  analogWrite(lf,LOW);
  analogWrite(lb,motor_speed);
}

void left (){
  analogWrite(rf,motor_speed);
  analogWrite(rb,LOW);
  analogWrite(lf,LOW);
  analogWrite(lb,motor_speed);
}

void right (){
  analogWrite(rf,LOW);
  analogWrite(rb,motor_speed);
  analogWrite(lf,motor_speed);
  analogWrite(lb,LOW);  
}


float imu_read(){
 if (!dmpReady) return 0;
    while (!mpuInterrupt && fifoCount < packetSize) {
    }


    mpuInterrupt = false;
    mpuIntStatus = mpu.getIntStatus();


    fifoCount = mpu.getFIFOCount();

    if ((mpuIntStatus & 0x10) || fifoCount == 1024) {

        mpu.resetFIFO();
        Serial.println(F("FIFO overflow!"));


    } else if (mpuIntStatus & 0x02) {

        while (fifoCount < packetSize) fifoCount = mpu.getFIFOCount();


        mpu.getFIFOBytes(fifoBuffer, packetSize);
        fifoCount -= packetSize;

        #ifdef OUTPUT_READABLE_EULER
            // display Euler angles in degrees
            mpu.dmpGetQuaternion(&q, fifoBuffer);
            mpu.dmpGetEuler(euler, &q);
            if (euler[0]*180/M_PI <0){
              float neg_deg = euler[0]*180/M_PI +360;
              //Serial.print("euler\t");
              //Serial.println(neg_deg);
              return neg_deg;
            }
            else{
              //Serial.print("euler\t");
              //Serial.println(euler[0] * 180/M_PI);
              return  euler[0]*180/M_PI;
            }
         #endif
    }
}

float imu_read_off() {
  float check = imu_read();
  check = check - base;
  
  if (check < 0) {
    check += 360;
  }
 // Serial.println(check);
  return check;
}
