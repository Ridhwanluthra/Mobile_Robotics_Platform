
#include "I2Cdev.h"

#include "MPU6050_6Axis_MotionApps20.h"
#if I2CDEV_IMPLEMENTATION == I2CDEV_ARDUINO_WIRE
    #include "Wire.h"
#endif
MPU6050 mpu;
#define OUTPUT_READABLE_EULER

bool dmpReady = false;  // set true if DMP init was successful
uint8_t mpuIntStatus;   // holds actual interrupt status byte from MPU
uint8_t devStatus;      // return status after each device operation (0 = success, !0 = error)
uint16_t packetSize;    // expected DMP packet size (default is 42 bytes)
uint16_t fifoCount;     // count of all bytes currently in FIFO
uint8_t fifoBuffer[128]; // FIFO storage buffer


Quaternion q;           // [w, x, y, z]         quaternion container
VectorInt16 aa;         // [x, y, z]            accel sensor measurements
VectorInt16 aaReal;     // [x, y, z]            gravity-free accel sensor measurements
VectorInt16 aaWorld;    // [x, y, z]            world-frame accel sensor measurements
VectorFloat gravity;    // [x, y, z]            gravity vector
float euler[3];         // [psi, theta, phi]    Euler angle container
float ypr[3];           // [yaw, pitch, roll]   yaw/pitch/roll container and gravity vector
int rf =5 ,rb =6,lf=9,lb=10;
int motor_speed =100; //(0-255)
int count =0;

int test;
volatile bool mpuInterrupt = false;     // indicates whether MPU interrupt pin has gone high

double unit_distance = .9507;
int deg_dis = 3;
int x;
int y;
int a, b;

int enc_rtcount = 0, enc_ltcount = 0;
int r_en = 7, l_en = 3;

float init_imu;

float curr_imu;



void dmpDataReady() {
    mpuInterrupt = true;
}
void setup() {

    #if I2CDEV_IMPLEMENTATION == I2CDEV_ARDUINO_WIRE
        Wire.begin();
        TWBR = 24; // 400kHz I2C clock (200kHz if CPU is 8MHz)
    #elif I2CDEV_IMPLEMENTATION == I2CDEV_BUILTIN_FASTWIRE
        Fastwire::setup(400, true);
    #endif
    Serial.begin(115200);
      pinMode(r_en, INPUT);
  pinMode(l_en, INPUT);

  pinMode(lf, OUTPUT);
  pinMode(lb, OUTPUT);
  pinMode(rf, OUTPUT);
  pinMode(rb, OUTPUT);

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
        
    } else {
        Serial.print(F("DMP Initialization failed (code "));
        Serial.print(devStatus);
        Serial.println(F(")"));
    }
   while(millis() < 20000) {
      init_imu = imu_read();
  }
}


void loop() {
    
  if (count==0){
      imu_read();
   // forward_movt(300);
//    delay(200);

  turn_rt_imu(350);
  count =1;
  }

   
}

/*
float imu_read_off() {
  int check = imu_read_later();
  check = check - init_imu;
  if (check < 0) {
    check += 360;
  }
  Serial.println(check);
  return check;
}
*/

float imu_read(){
 if (!dmpReady) return 0;
    while (!mpuInterrupt && fifoCount < packetSize) {
    }


    mpuInterrupt = false;
    mpuIntStatus = mpu.getIntStatus(); 
    fifoCount = mpu.getFIFOCount();
//Serial.println(     mpuIntStatus);
    if ((mpuIntStatus & 0x10) || fifoCount == 1024) {
      mpu.resetFIFO();
        Serial.println(F("FIFO overflow!"));
    } else if (mpuIntStatus & 0x02) {
        while (fifoCount < packetSize) fifoCount = mpu.getFIFOCount();
        mpu.getFIFOBytes(fifoBuffer, packetSize);
        fifoCount -= packetSize;
        mpu.resetFIFO();
        #ifdef OUTPUT_READABLE_EULER
            // display Euler angles in degrees
            mpu.dmpGetQuaternion(&q, fifoBuffer);
            mpu.dmpGetEuler(euler, &q);
            if (euler[0]*180/M_PI <0){
              float neg_deg = euler[0]*180/M_PI +360;
              Serial.print("euler\t");
              Serial.println(neg_deg);
              return neg_deg;
            }
            else{
              Serial.print("euler\t");
              Serial.println(euler[0] * 180/M_PI);
              return  euler[0]*180/M_PI;
            }
         #endif
    }
}


/*
float imu_read_later(){
 if (!dmpReady) return 0;
    while (!mpuInterrupt && fifoCount < packetSize) {
    }


    mpuInterrupt = false;
    mpuIntStatus = mpu.getIntStatus();


    fifoCount = mpu.getFIFOCount();

    if ((mpuIntStatus & 0x10) || fifoCount == 1024) {

        mpu.resetFIFO();
        Serial.println("later");
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
              return neg_deg;
            }
            else{
              return  euler[0]*180/M_PI;
            }
         #endif
    }
}
*/

void forward_movt (int dist){
  int no_of_spokes = (int)(dist/unit_distance);
  //Serial.println(no_of_spokes);
  init_imu=imu_read();
  while(call_rtenc() <= no_of_spokes*2) {
  //Serial.println(call_rtenc());
    forward();
  }  
    
  //encoder
  
  enc_rtcount=0;
	
  sstop();

}
 
void turn_left (int dist){
  int no_of_spokes = (int)(dist/unit_distance);
  //Serial.println(no_of_spokes);
  init_imu=imu_read();
  while(call_rtenc() <= no_of_spokes*2) {
    Serial.println(call_rtenc());
    right();
  }

    
  //encoder
  
  enc_rtcount=0;
  sstop();

} 
 
 void backward_movt (int dist){
  int no_of_spokes = (int)(dist/unit_distance);
  //Serial.println(no_of_spokes);
  init_imu=imu_read();
  while(call_rtenc() <= no_of_spokes*2) {
    Serial.println(call_rtenc());
    backward();
    }  
    
  //encoder
  
  enc_rtcount=0;
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


void turn_right (int dist){
  int no_of_spokes = (int)(dist/unit_distance);
  //Serial.println(no_of_spokes);
  init_imu=imu_read();
  while(call_rtenc() <= no_of_spokes*2) {
    Serial.println(call_rtenc());
  left();
}  
    
  //encoder
  
  enc_rtcount=0;
  init_imu=imu_read();
  sstop();

}



void turn_rt_imu(float deg){
  float to_turn = init_imu +deg;
  if(to_turn >= 360){
    greater_rt(to_turn);
  }
  else{
    while(to_turn >=imu_read() ) {
      left();
      
    }
  }
  
 sstop();
    
    
  
  init_imu = imu_read();
}

void greater_rt(float to_turn){
  to_turn=to_turn-360;
  Serial.println("\t\t\t\t\t\tasdfgg");
  while(imu_read()<358 && imu_read()>3){
      Serial.println("\t\t\tasdfgg");
    left();
  }
  sstop();
  delay(200);
  while(imu_read()<to_turn){
    left();
  }
  sstop();
}



void turn_lt_imu(float deg){
  float to_turn =init_imu- deg;
  if(to_turn<0){
    lesser_lt(to_turn);
  }
  else{
    while (to_turn > imu_read()){
      right();
    }
  }
  sstop();
  init_imu=imu_read();
}

void lesser_lt(float to_turn){
  to_turn=to_turn+360;
  while(imu_read()>3 && imu_read<358){
    right();
  }
  while(imu_read()>to_turn){
    right();
  }
  sstop();
  
}










  
void forward(){
  analogWrite(rf,motor_speed);
  analogWrite(rb,LOW);
  analogWrite(lf,motor_speed);
  analogWrite(lb,LOW);
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

