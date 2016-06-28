int HR =5 ,HL =6, R=9,F=10;
int motor_speed =250; //(0-255)
//double c=90;
double unit_distance = .9507;
int deg_dis = 3;
int x;
int y;
int a, b;

int enc_rtcount = 0, enc_ltcount = 0;
int r_en = 7, l_en = 3;

void setup() {
  Serial.begin(9600);
  
  pinMode(r_en, INPUT);
  pinMode(l_en, INPUT);

  pinMode(R, OUTPUT);
  pinMode(F, OUTPUT);
  pinMode(HR, OUTPUT);
  pinMode(HL, OUTPUT);
      delay(4000);
}

void loop() {
  


 // if (millis()==30000){
    //forward_movt(30);
   // delay (1000);
 forward_movt(30);
   
//  call_ltenc();
//  call_rtenc();
 // turn_left(90);
  //delay(2000);
  //turn_right(90);
  //delay(2000);

    //turn(90);
//    backward_movt(20);
//    turn_left


  //}
}


void forward_movt (int dist){
  int no_of_spokes = (int)(dist/unit_distance);
  //Serial.println(no_of_spokes);
 call_rtenc();
  while(enc_rtcount<no_of_spokes) {
  forward();
  delay(15);
  sstop();
  delay(15);
}  
    call_rtenc();
  
  //encoder
  call_rtenc();
  enc_rtcount=0;
  analogWrite(F, 0);

}
 
void call_rtenc() {
  b = a;
  a = digitalRead(l_en);
  
  if((a == 0 && b == 1) || (a == 1 && b == 0)) {
    enc_rtcount++;
  }
}

void call_ltenc() {
  y = x;
  x = digitalRead(l_en);
  
  if((y == 0 && x == 1) || (y == 1 && x == 0)) {
    enc_ltcount++;
  }
}





void turn_left(int deg1){
  int no_of_spokes = (int)(deg1/deg_dis);
  //Serial.println(no_of_spokes);
 call_rtenc();
  while(enc_rtcount<no_of_spokes) {
    analogWrite(R, 0);
    analogWrite(F, motor_speed);
    analogWrite(HR, motor_speed);
    analogWrite(HL, 0);
    call_rtenc();
  }
  //encoder
  call_rtenc();
  enc_rtcount=0;
  analogWrite(F, 0);
  analogWrite(HR, 0);

}  

void turn_right(int deg1){
  int no_of_spokes = (int)(deg1/deg_dis);
  //Serial.println(no_of_spokes);
 call_ltenc();
  while(enc_ltcount<no_of_spokes) {
    analogWrite(R, 0);
    analogWrite(F, motor_speed);
    analogWrite(HR, 0);
    analogWrite(HL, motor_speed);
    call_ltenc();
  }
  //encoder
  call_ltenc();
  enc_ltcount=0;
  analogWrite(F, 0);
  analogWrite(HL, 0);  
}  



void forward(){
    analogWrite(R,LOW);
  analogWrite(F,motor_speed);
  analogWrite(HL,LOW);
  analogWrite(HR,LOW);
}  
void sstop() {
  digitalWrite(R,LOW);
  digitalWrite(F,LOW);
  digitalWrite(HL,LOW);
  digitalWrite(HR,LOW);
}
void right(){
  digitalWrite(R,LOW);
  digitalWrite(F,motor_speed);
  digitalWrite(HL,motor_speed);
  digitalWrite(HR,LOW);  
  
  
}
void left(){
  digitalWrite(R,LOW);
  digitalWrite(F,motor_speed);
  digitalWrite(HR,motor_speed);
  digitalWrite(HL,LOW);  
  
  
}
