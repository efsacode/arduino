int array[10] = {1,5,52,3,15,7,4,17,2,10};

void setup() {
  Serial.begin(9600);
}

void loop() {
  for(int i = 0; i<10; i++){
    Serial.print(array[i]);
    if (i < 9) Serial.print(" ");
  }
  Serial.println(); // Satır sonu
  delay(3000); 
}
