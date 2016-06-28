int HR =5 ,HL =6, R=9,F=10;
int motor_speed =250; //(0-255)
//double c=90;
double a_init, a_deg;
double unit_distance = .9507;
int deg_dis = 3;
int x;
int y;

bool a = false, b = false, c = false;
int a1=9, a2=9, a3=9, enc_rtcount=0;
int r_en=7, l_en=3;


bool aa = false, bb = false, cc = false;
int aa1=9, aa2=9, aa3=9, enc_ltcount=0;


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
 
 void call_rtenc(){
    x = digitalRead(r_en);;
    
    Serial.print(x);
    Serial.print("\t\t");
    Serial.println (enc_rtcount);  
  if(!a){
    a=true;
    a1 = x;
  }
  else if (!b){
    a2 = x;
    if(a1!=a2){
      b = true;
    }
  }
  else if (!c){
  a3 = x;
  if(a3!=a2){
      b= false,c=false;
      enc_rtcount+=1;   
    }
  }
}

 void call_ltenc(){
    y=digitalRead(l_en);;
    
    Serial.print(y);
    Serial.print("\t\t");
    Serial.println (enc_ltcount);  
  if(!aa){
    aa=true;
    aa1 = y;
  }
  else if (!bb){
    aa2 = y;
    if(aa1!=aa2){
      bb = true;
    }
  }
  else if (!cc){
  aa3 = y;
  if(aa3!=aa2){
      bb= false,cc=false;
      enc_ltcount+=1;   
    }
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
