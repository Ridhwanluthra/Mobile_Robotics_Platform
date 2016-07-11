int rf =5 ,rb =6,lf=9,lb=10;
int motor_speed =150; //(0-255)

//int arr[10][2]={
//  {10,10},{10,10},{10,10},{10,10},{10,10 },
//  {10,-10},{10,-10},{10,-10},{10,-10},{10,-10}
//};
int power_difference, encoderleft, encoderright, proportional;
const int maximum = 100;


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

  pinMode(lf, OUTPUT);
  pinMode(lb, OUTPUT);
  pinMode(rf, OUTPUT);
  pinMode(rb, OUTPUT);
//      delay(4000);
}

void loop() {
  //  for(int i=0;i<10;i++){
  //    for(int j=0;j<2;j++){
  //      if(j==0){
  //        forward_movt(arr[i][j]);
  //      }
  //      else{
  //        if(arr[i][j]>0){
  //          turn_right(3);
  //        }
  //        else{
  //          turn_left(5);
  //        }
  //      }
  //    }
  //  }
  //  
  /*
  Serial.print(call_rtenc());
  Serial.print("  ");
  Serial.println(call_ltenc());
  */
  
/*  proportional = enc_ltcount - enc_rtcount;
  power_difference = proportional/2;
  Serial.println(proportional);
  if (proportional > 10) {
    sstop();
    delay(500);
    left();
    delay(150);
  }
  if (proportional < -10) {
    sstop();
    delay(500);
    right();
    delay(150);
  }
  if (power_difference > maximum)
    power_difference = maximum;
  if (power_difference < -maximum)
    power_difference = -maximum;
  */
  forward_movt(600);
}


void forward_movt (int dist){
  int no_of_spokes = (int)(dist/unit_distance);
  //Serial.println(no_of_spokes);

  while(enc_rtcount <= no_of_spokes*2) {
    call_rtenc();
    call_ltenc();
    
    proportional = enc_ltcount - enc_rtcount;
    power_difference = proportional*10;
    
    Serial.print(proportional);
    Serial.print("  ");
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
    
  //encoder
  //enc_ltcount = 0;
  //enc_rtcount = 0;
  //sstop();
  //delay(3000);

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
  if (power_difference < 0)//moving left -----errooor 
  {
    analogWrite(rf, (maximum + power_difference));  ////////////right motor at less speed so that bot moves right
    analogWrite(rb,LOW);
    analogWrite(lf, maximum);
    analogWrite(lb,LOW);
    
    Serial.print("PW > 0");
    Serial.print("  ");
    Serial.print("right");
    Serial.print("  ");
    Serial.print(maximum + power_difference);
    Serial.print("  ");
    Serial.print("left");
    Serial.print("  ");
    Serial.print(maximum);
    Serial.println("  ");
  }
  else //moving right -------errror
  {
    analogWrite(rf,maximum);
    analogWrite(rb, LOW);
    analogWrite(lf, maximum - power_difference);/// left motor is at less speed so that bot moves left
    analogWrite(lb, LOW);
    
    Serial.print("PW > 0");
    Serial.print("  ");
    Serial.print("right");
    Serial.print("  ");
    Serial.print(maximum);
    Serial.print("  ");
    Serial.print("left");
    Serial.print("  ");
    Serial.print(maximum - power_difference);
    Serial.println("  ");
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
