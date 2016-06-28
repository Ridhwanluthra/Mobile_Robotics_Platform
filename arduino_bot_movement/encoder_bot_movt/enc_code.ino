int rf =5 ,rb =6,lf=9,lb=10;
int motor_speed =100; //(0-255)


//double c=90;
double unit_distance = .9507;
int deg_dis = 1;
int x;
int y;
int a, b;

int enc_rtcount = 0, enc_ltcount = 0;
int r_en = 7, l_en = 3;

void setup() {
  Serial.begin(9600);
  
  pinMode(r_en, INPUT);
  pinMode(l_en, INPUT);

  pinMode(lf, OUTPUT);
  pinMode(lb, OUTPUT);
  pinMode(rf, OUTPUT);
  pinMode(rb, OUTPUT);
      delay(2000);
}

void loop() {
  

     
 // if (millis()==30000){
    //forward_movt(30);
   // delay (1000);
 forward_movt(110);
 // /  delay(3000);
  //turn_right(90);
    //delay(3000);
delay(1000);
  //  delay(3000);
  turn_right(26);
 delay(1000); 
  backward_movt(50);
   delay(10000);
//  call_ltenc();
//  call_rtenc();
 // turn_left(90);
  //delay(2000);

  //delay(2000);

    //turn(90);
//    backward_movt(20);
//    turn_left


  //}
}


void forward_movt (int dist){
  int no_of_spokes = (int)(dist/unit_distance);
  //Serial.println(no_of_spokes);

  while(call_rtenc() <= no_of_spokes*2) {
    Serial.println(call_rtenc());
  forward();
}  
    
  //encoder
  
  enc_rtcount=0;
  sstop();

}
 
void turn_left (int dist){
  int no_of_spokes = (int)(dist/unit_distance);
  //Serial.println(no_of_spokes);

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

  while(call_rtenc() <= no_of_spokes*2) {
    Serial.println(call_rtenc());
  left();
}  
    
  //encoder
  
  enc_rtcount=0;
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